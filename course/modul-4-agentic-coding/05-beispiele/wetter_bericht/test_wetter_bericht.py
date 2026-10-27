"""Tests für wetter_bericht: `vergleiche_staedte` (test-first, Lektion 2) und die Bestandsfunktionen."""

import json

import pytest
import requests
import wetter_bericht
from wetter_bericht import (
    CSV_DATEI,
    berechne_kennzahlen,
    beschreibe_wetter,
    hole_live_wetter,
    lese_stadt,
    main,
    speichere_bericht,
    vergleiche_staedte,
    zeige_bericht,
)


def tage(stadt: str, tmax_werte: list[float], niederschlag_werte: list[float] | None = None) -> list[dict]:
    """Baut Zeilen im Format von lese_stadt() (je Tag eine Zeile)."""
    if niederschlag_werte is None:
        niederschlag_werte = [0.0] * len(tmax_werte)
    return [
        {"stadt": stadt, "datum": f"2026-09-{tag:02d}", "tmin": tmax - 8.0, "tmax": tmax, "niederschlag_mm": mm}
        for tag, (tmax, mm) in enumerate(zip(tmax_werte, niederschlag_werte), start=1)
    ]


def test_a_waermer_als_b_gibt_positive_differenz():
    zeilen_a = tage("Zürich", [20.0, 22.0])  # Ø 21.0
    zeilen_b = tage("Bern", [18.0, 19.0])  # Ø 18.5

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["tmax_differenz"] == 2.5


def test_a_kaelter_als_b_gibt_negative_differenz():
    zeilen_a = tage("Bern", [10.0, 12.0])  # Ø 11.0
    zeilen_b = tage("Zürich", [14.0, 15.0])  # Ø 14.5

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["tmax_differenz"] == -3.5


def test_a_naesser_als_b_nennt_a():
    zeilen_a = tage("Zürich", [20.0, 20.0], [5.0, 3.0])  # 8.0 mm
    zeilen_b = tage("Lugano", [20.0, 20.0], [1.0, 2.0])  # 3.0 mm

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["naessere_stadt"] == "Zürich"


def test_b_naesser_als_a_nennt_b():
    zeilen_a = tage("Zürich", [20.0, 20.0], [1.0, 2.0])  # 3.0 mm
    zeilen_b = tage("Lugano", [20.0, 20.0], [5.0, 3.0])  # 8.0 mm

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["naessere_stadt"] == "Lugano"


def test_gleicher_niederschlag_gibt_none():
    zeilen_a = tage("Zürich", [20.0, 20.0], [4.0, 1.0])  # 5.0 mm
    zeilen_b = tage("Lugano", [20.0, 20.0], [2.0, 3.0])  # 5.0 mm

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["naessere_stadt"] is None


def test_naesser_entscheidet_der_gesamtniederschlag_nicht_die_zahl_der_regentage():
    zeilen_a = tage("Zürich", [20.0, 20.0], [10.0, 0.0])  # 1 Regentag, 10.0 mm
    zeilen_b = tage("Lugano", [20.0, 20.0, 20.0], [1.0, 1.0, 2.0])  # 3 Regentage, 4.0 mm

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["naessere_stadt"] == "Zürich"


def test_gleichstand_wird_auf_gerundeten_gesamtniederschlaegen_geprueft():
    zeilen_a = tage("Zürich", [20.0, 20.0], [5.04, 0.0])  # 5.04 mm, gerundet 5.0 mm
    zeilen_b = tage("Lugano", [20.0, 20.0], [2.0, 3.0])  # 5.0 mm

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["naessere_stadt"] is None


def test_leere_liste_a_wirft_value_error():
    zeilen_b = tage("Lugano", [20.0, 20.0])

    with pytest.raises(ValueError, match="Keine Wetterdaten vorhanden."):
        vergleiche_staedte([], zeilen_b)


def test_leere_liste_b_wirft_value_error():
    zeilen_a = tage("Zürich", [20.0, 20.0])

    with pytest.raises(ValueError, match="Keine Wetterdaten vorhanden."):
        vergleiche_staedte(zeilen_a, [])


def test_differenz_ist_auf_eine_dezimale_gerundet():
    zeilen_a = tage("Zürich", [20.6, 20.8])  # Ø 20.7
    zeilen_b = tage("Lugano", [21.8, 21.8])  # Ø 21.8

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis["tmax_differenz"] == -1.1


def test_ergebnis_hat_genau_die_vier_schluessel_mit_staedtenamen():
    zeilen_a = tage("Zürich", [20.0, 22.0], [5.0, 3.0])
    zeilen_b = tage("Lugano", [18.0, 19.0], [1.0, 2.0])

    ergebnis = vergleiche_staedte(zeilen_a, zeilen_b)

    assert ergebnis == {
        "stadt_a": "Zürich",
        "stadt_b": "Lugano",
        "tmax_differenz": 2.5,
        "naessere_stadt": "Zürich",
    }


def test_plan_beispiel_zuerich_gegen_lugano_aus_csv():
    zuerich = lese_stadt(CSV_DATEI, "Zürich")
    lugano = lese_stadt(CSV_DATEI, "Lugano")

    ergebnis = vergleiche_staedte(zuerich, lugano)

    assert ergebnis == {
        "stadt_a": "Zürich",
        "stadt_b": "Lugano",
        "tmax_differenz": -1.1,
        "naessere_stadt": "Zürich",
    }


# --- bestehende Funktionen -------------------------------------------------


CSV_INHALT = (
    "stadt,datum,tmin,tmax,niederschlag_mm,wettercode\n"
    "Zürich,2026-09-20,10.0,20.0,0.0,0\n"
    "Bern,2026-09-20,9.0,19.0,1.5,61\n"
    "Zürich,2026-09-21,12.0,24.0,2.5,61\n"
)


@pytest.fixture
def csv_datei(tmp_path):
    pfad = tmp_path / "wetter.csv"
    pfad.write_text(CSV_INHALT, encoding="utf-8")
    return pfad


def test_lese_stadt_filtert_zeilen_und_wandelt_zahlen_in_float():
    zeilen = lese_stadt(CSV_DATEI, "Zürich")

    assert len(zeilen) == 30
    assert all(z["stadt"] == "Zürich" for z in zeilen)
    assert isinstance(zeilen[0]["tmax"], float)


def test_lese_stadt_kleine_datei(csv_datei):
    zeilen = lese_stadt(csv_datei, "Zürich")

    assert [z["tmax"] for z in zeilen] == [20.0, 24.0]
    assert [z["niederschlag_mm"] for z in zeilen] == [0.0, 2.5]


def test_berechne_kennzahlen():
    zeilen = tage("Zürich", [20.0, 24.0], [0.0, 2.5])

    kennzahlen = berechne_kennzahlen(zeilen)

    assert kennzahlen == {
        "tmin_durchschnitt": 14.0,
        "tmax_durchschnitt": 22.0,
        "tmax_hoechste": 24.0,
        "tmax_hoechste_datum": "2026-09-02",
        "regentage": 1,
        "niederschlag_gesamt_mm": 2.5,
    }


def test_beschreibe_wetter_bekannter_und_unbekannter_code():
    assert beschreibe_wetter(95) == "Gewitter"
    assert beschreibe_wetter(999) == "unbekannt"


class FakeAntwort:
    def __init__(self, daten):
        self._daten = daten

    def raise_for_status(self):
        pass

    def json(self):
        return self._daten


def test_hole_live_wetter_erfolg(monkeypatch):
    antwort = FakeAntwort({"current": {"temperature_2m": 17.3, "weather_code": 3}})
    monkeypatch.setattr(wetter_bericht.requests, "get", lambda *a, **k: antwort)

    assert hole_live_wetter("Zürich") == {"temperatur": 17.3, "beschreibung": "bedeckt"}


def test_hole_live_wetter_netzwerkfehler_gibt_none(monkeypatch):
    def wirft(*args, **kwargs):
        raise requests.ConnectionError("offline")

    monkeypatch.setattr(wetter_bericht.requests, "get", wirft)

    assert hole_live_wetter("Zürich") is None


def test_hole_live_wetter_unerwartete_antwort_gibt_none(monkeypatch):
    monkeypatch.setattr(wetter_bericht.requests, "get", lambda *a, **k: FakeAntwort({"unerwartet": 1}))

    assert hole_live_wetter("Zürich") is None


def test_speichere_bericht_schreibt_lesbares_json_mit_umlauten(tmp_path):
    pfad = tmp_path / "bericht.json"

    speichere_bericht({"stadt": "Zürich"}, pfad)

    assert "Zürich" in pfad.read_text(encoding="utf-8")
    assert json.loads(pfad.read_text(encoding="utf-8")) == {"stadt": "Zürich"}


BERICHT = {
    "stadt": "Zürich",
    "kennzahlen": {
        "tmin_durchschnitt": 14.0,
        "tmax_durchschnitt": 22.0,
        "tmax_hoechste": 24.0,
        "tmax_hoechste_datum": "2026-09-02",
        "regentage": 1,
        "niederschlag_gesamt_mm": 2.5,
    },
    "live": {"temperatur": 17.3, "beschreibung": "bedeckt"},
}


def test_zeige_bericht_mit_live_wetter(capsys):
    zeige_bericht(BERICHT)

    ausgabe = capsys.readouterr().out
    assert "Wetterbericht Zürich" in ausgabe
    assert "Jetzt: 17.3 °C, bedeckt" in ausgabe


def test_zeige_bericht_ohne_live_wetter(capsys):
    zeige_bericht({**BERICHT, "live": None})

    assert "Live-Wetter nicht verfügbar" in capsys.readouterr().out


@pytest.fixture
def main_umgebung(tmp_path, csv_datei, monkeypatch):
    monkeypatch.setattr(wetter_bericht, "ORDNER", tmp_path)
    monkeypatch.setattr(wetter_bericht, "CSV_DATEI", csv_datei)

    def offline(*args, **kwargs):
        raise requests.ConnectionError("offline")

    monkeypatch.setattr(wetter_bericht.requests, "get", offline)  # nur die Systemgrenze ersetzen
    return tmp_path


def test_main_erstellt_bericht_und_datei(main_umgebung, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Zürich")

    main()

    bericht = json.loads((main_umgebung / "bericht_zürich.json").read_text(encoding="utf-8"))
    assert bericht["stadt"] == "Zürich"
    assert bericht["kennzahlen"]["tmax_durchschnitt"] == 22.0
    assert "Wetterbericht Zürich" in capsys.readouterr().out


def test_main_unbekannte_stadt(main_umgebung, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "Atlantis")

    main()

    assert "kenne ich nicht" in capsys.readouterr().out
    assert not list(main_umgebung.glob("bericht_*.json"))


def test_main_fehlende_csv(main_umgebung, monkeypatch, capsys):
    monkeypatch.setattr(wetter_bericht, "CSV_DATEI", main_umgebung / "gibt_es_nicht.csv")
    monkeypatch.setattr("builtins.input", lambda _: "Zürich")

    main()

    assert "fehlt" in capsys.readouterr().out
