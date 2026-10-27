"""Tests für wetter_bericht.py (Stand nach Lektion 3).

Nur reine Funktionen, keine Dateien, kein Live-Abruf.
"""

import pytest
from wetter_bericht import (
    berechne_kennzahlen,
    bereite_live_wetter_auf,
    beschreibe_wetter,
    vergleiche_staedte,
)


def tag(stadt, datum, tmin, tmax, niederschlag):
    return {"stadt": stadt, "datum": datum, "tmin": tmin, "tmax": tmax, "niederschlag_mm": niederschlag}


ZUERICH = [
    tag("Zürich", "2026-09-20", 10.0, 20.0, 0.0),
    tag("Zürich", "2026-09-21", 12.0, 24.0, 5.0),
]
BERN = [
    tag("Bern", "2026-09-20", 8.0, 18.0, 0.0),
    tag("Bern", "2026-09-21", 10.0, 20.0, 1.0),
]


# --- berechne_kennzahlen: Ist-Verhalten ---


def test_kennzahlen_durchschnitte():
    kennzahlen = berechne_kennzahlen(ZUERICH)
    assert kennzahlen["tmin_durchschnitt"] == 11.0
    assert kennzahlen["tmax_durchschnitt"] == 22.0


def test_kennzahlen_heissester_tag():
    kennzahlen = berechne_kennzahlen(ZUERICH)
    assert kennzahlen["tmax_hoechste"] == 24.0
    assert kennzahlen["tmax_hoechste_datum"] == "2026-09-21"


def test_kennzahlen_regen():
    kennzahlen = berechne_kennzahlen(ZUERICH)
    assert kennzahlen["regentage"] == 1
    assert kennzahlen["niederschlag_gesamt_mm"] == 5.0


# --- beschreibe_wetter: Ist-Verhalten ---


def test_beschreibe_wetter_bekannter_code():
    assert beschreibe_wetter(0) == "klar"


def test_beschreibe_wetter_frueher_unbekannte_codes_haben_jetzt_klartext():
    assert beschreibe_wetter(1) == "überwiegend klar"
    assert beschreibe_wetter(2) == "teilweise bewölkt"
    assert beschreibe_wetter(63) == "mässiger Regen"
    assert beschreibe_wetter(96) == "Gewitter mit Hagel"


def test_beschreibe_wetter_wirklich_unbekannter_code():
    assert beschreibe_wetter(999) == "unbekannt"


# --- vergleiche_staedte: test-first nach plan.md ---


def test_vergleich_temperaturdifferenz():
    ergebnis = vergleiche_staedte(ZUERICH, BERN)
    assert ergebnis["tmax_differenz"] == 3.0


def test_vergleich_rundet_erst_am_ende():
    # Ø tmax A = 20.04, Ø tmax B = 19.96: exakt 0.08 (gerundet 0.1), aus gerundeten Mitteln wäre es 0.0
    a = [tag("A", f"2026-09-{i + 1:02d}", 10.0, tmax, 0.0) for i, tmax in enumerate([20.0, 20.0, 20.0, 20.0, 20.2])]
    b = [tag("B", f"2026-09-{i + 1:02d}", 10.0, tmax, 0.0) for i, tmax in enumerate([19.9, 19.9, 20.0, 20.0, 20.0])]
    assert vergleiche_staedte(a, b)["tmax_differenz"] == 0.1


def test_vergleich_leere_liste_b_wirft_value_error():
    with pytest.raises(ValueError):
        vergleiche_staedte(BERN, [])


def test_vergleich_namen():
    ergebnis = vergleiche_staedte(ZUERICH, BERN)
    assert ergebnis["stadt_a"] == "Zürich"
    assert ergebnis["stadt_b"] == "Bern"


def test_vergleich_naessere_stadt():
    assert vergleiche_staedte(ZUERICH, BERN)["naessere_stadt"] == "Zürich"
    assert vergleiche_staedte(BERN, ZUERICH)["naessere_stadt"] == "Zürich"


def test_vergleich_gleicher_niederschlag_ist_none():
    assert vergleiche_staedte(ZUERICH, ZUERICH)["naessere_stadt"] is None


def test_vergleich_leere_liste_wirft_value_error():
    with pytest.raises(ValueError):
        vergleiche_staedte([], BERN)


# --- Kür: Randfall des Startpunkts ---


def test_kennzahlen_leere_liste_wirft_value_error():
    with pytest.raises(ValueError):
        berechne_kennzahlen([])


# --- Diagnose: leere Stadt ---


def test_kennzahlen_leere_liste_hat_klare_meldung():
    with pytest.raises(ValueError, match="Keine Wetterdaten"):
        berechne_kennzahlen([])


# --- Refactoring: reine Aufbereitung der API-Antwort ---


def test_live_wetter_aufbereiten():
    antwort = {"current": {"temperature_2m": 14.2, "weather_code": 61}}
    assert bereite_live_wetter_auf(antwort) == {"temperatur": 14.2, "beschreibung": "leichter Regen"}


def test_live_wetter_aufbereiten_unbekannter_code():
    antwort = {"current": {"temperature_2m": 3.0, "weather_code": 999}}
    assert bereite_live_wetter_auf(antwort)["beschreibung"] == "unbekannt"
