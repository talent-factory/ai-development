"""Wetterbericht für eine Schweizer Stadt: CSV auswerten, Live-Wetter abrufen, Bericht als JSON speichern.

Startpunkt für Modul 4 (Stand der Nachbearbeitung von Modul 3).
Weather data by Open-Meteo.com (CC BY 4.0).
"""

import csv
import json
from pathlib import Path

import requests

ORDNER = Path(__file__).parent
CSV_DATEI = ORDNER / "wetter_30tage.csv"
API_URL = "https://api.open-meteo.com/v1/forecast"
QUELLE = "Weather data by Open-Meteo.com"

STAEDTE = {
    "Zürich": (47.3769, 8.5417),
    "Bern": (46.948, 7.4474),
    "Genf": (46.2044, 6.1432),
    "Basel": (47.5596, 7.5886),
    "Lugano": (46.0037, 8.9511),
}

WETTERCODES = {
    0: "klar",
    3: "bedeckt",
    45: "Nebel",
    61: "leichter Regen",
    80: "leichte Regenschauer",
    95: "Gewitter",
}


def lese_stadt(pfad: Path, stadt: str) -> list[dict]:
    """Liest die Zeilen einer Stadt aus der CSV-Datei.

    Args:
        pfad: Pfad zur UTF-8-kodierten CSV-Datei mit Spaltenkopf.
        stadt: Name der Stadt, wie in der Spalte `stadt` geschrieben.

    Returns:
        Die passenden Zeilen als Dictionaries in Dateireihenfolge. Die Felder `tmin`, `tmax`
        und `niederschlag_mm` sind in float umgewandelt, alle anderen bleiben Text. Leer,
        wenn die Stadt nicht vorkommt.
    """
    zeilen = []
    with open(pfad, newline="", encoding="utf-8") as datei:
        for zeile in csv.DictReader(datei):
            if zeile["stadt"] != stadt:
                continue
            for feld in ("tmin", "tmax", "niederschlag_mm"):
                zeile[feld] = float(zeile[feld])
            zeilen.append(zeile)
    return zeilen


def berechne_kennzahlen(zeilen: list[dict]) -> dict:
    """Berechnet Durchschnitte, heissesten Tag, Regentage und Gesamtniederschlag.

    Args:
        zeilen: Tageswerte einer Stadt mit den Feldern `tmin`, `tmax`, `niederschlag_mm`
            (als Zahlen) und `datum`. Sollte nicht leer sein, bei einer leeren Liste
            scheitert die Berechnung (nicht eigens abgefangen).

    Returns:
        Kennzahlen mit den Schlüsseln `tmin_durchschnitt`, `tmax_durchschnitt`,
        `tmax_hoechste`, `tmax_hoechste_datum`, `regentage` (Tage mit Niederschlag über 0 mm)
        und `niederschlag_gesamt_mm`. Durchschnitte und Gesamtniederschlag sind auf eine
        Nachkommastelle gerundet.
    """
    heissester = max(zeilen, key=lambda zeile: zeile["tmax"])
    return {
        "tmin_durchschnitt": round(sum(z["tmin"] for z in zeilen) / len(zeilen), 1),
        "tmax_durchschnitt": round(sum(z["tmax"] for z in zeilen) / len(zeilen), 1),
        "tmax_hoechste": heissester["tmax"],
        "tmax_hoechste_datum": heissester["datum"],
        "regentage": sum(1 for z in zeilen if z["niederschlag_mm"] > 0),
        "niederschlag_gesamt_mm": round(sum(z["niederschlag_mm"] for z in zeilen), 1),
    }


def vergleiche_staedte(zeilen_a: list[dict], zeilen_b: list[dict]) -> dict:
    """Vergleicht zwei Städte: Differenz der Ø tmax (A minus B) und die nässere Stadt.

    Args:
        zeilen_a: Tageswerte der ersten Stadt. Der Name stammt aus dem Feld `stadt` der ersten Zeile.
        zeilen_b: Tageswerte der zweiten Stadt, aufgebaut wie `zeilen_a`.

    Returns:
        Ein Dictionary mit `stadt_a`, `stadt_b`, `tmax_differenz` (Differenz der gerundeten
        Ø tmax, A minus B, auf 0.1 gerundet) und `naessere_stadt`. Das ist die Stadt mit dem
        grösseren Gesamtniederschlag (auf 0.1 mm gerundet), bei Gleichstand None.

    Raises:
        ValueError: Wenn eine der beiden Listen leer ist.
    """
    if not zeilen_a or not zeilen_b:
        raise ValueError("Keine Wetterdaten vorhanden.")
    stadt_a = zeilen_a[0]["stadt"]
    stadt_b = zeilen_b[0]["stadt"]
    kennzahlen_a = berechne_kennzahlen(zeilen_a)
    kennzahlen_b = berechne_kennzahlen(zeilen_b)
    niederschlag_a = kennzahlen_a["niederschlag_gesamt_mm"]
    niederschlag_b = kennzahlen_b["niederschlag_gesamt_mm"]
    if niederschlag_a > niederschlag_b:
        naessere_stadt = stadt_a
    elif niederschlag_b > niederschlag_a:
        naessere_stadt = stadt_b
    else:
        naessere_stadt = None
    return {
        "stadt_a": stadt_a,
        "stadt_b": stadt_b,
        "tmax_differenz": round(kennzahlen_a["tmax_durchschnitt"] - kennzahlen_b["tmax_durchschnitt"], 1),
        "naessere_stadt": naessere_stadt,
    }


def beschreibe_wetter(code: int) -> str:
    """Übersetzt einen Wettercode in Klartext.

    Args:
        code: Wettercode, wie ihn die Open-Meteo-API liefert.

    Returns:
        Die Beschreibung aus `WETTERCODES`, oder "unbekannt", wenn der Code dort nicht
        enthalten ist (die Tabelle deckt nur einen Teil der Codes ab).
    """
    return WETTERCODES.get(code, "unbekannt")


def hole_live_wetter(stadt: str) -> dict | None:
    """Ruft aktuelle Temperatur und Wetterlage einer Stadt bei Open-Meteo ab.

    Args:
        stadt: Name der Stadt. Muss in `STAEDTE` vorkommen, sonst entsteht ein KeyError
            (dieser wird nicht abgefangen).

    Returns:
        Ein Dictionary mit `temperatur` und `beschreibung` (Klartext zum Wettercode).
        None, wenn der Abruf scheitert: Netzwerk- oder HTTP-Fehler, ungültige Antwort
        oder fehlende Felder in der Antwort.
    """
    breite, laenge = STAEDTE[stadt]
    parameter = {
        "latitude": breite,
        "longitude": laenge,
        "current": "temperature_2m,weather_code",
        "timezone": "Europe/Zurich",
    }
    try:
        antwort = requests.get(API_URL, params=parameter, timeout=10)
        antwort.raise_for_status()
        aktuell = antwort.json()["current"]
        return {
            "temperatur": aktuell["temperature_2m"],
            "beschreibung": beschreibe_wetter(aktuell["weather_code"]),
        }
    except (requests.RequestException, KeyError, ValueError):
        return None


def speichere_bericht(bericht: dict, pfad: Path) -> None:
    """Speichert den Bericht als lesbare JSON-Datei (UTF-8, eingerückt, Umlaute unmaskiert).

    Args:
        bericht: Der zu speichernde Bericht. Muss JSON-serialisierbar sein.
        pfad: Zieldatei. Eine bestehende Datei wird überschrieben.
    """
    with open(pfad, "w", encoding="utf-8") as datei:
        json.dump(bericht, datei, indent=2, ensure_ascii=False)


def zeige_bericht(bericht: dict) -> None:
    """Gibt eine lesbare Zusammenfassung auf dem Bildschirm aus.

    Args:
        bericht: Bericht mit den Schlüsseln `stadt`, `kennzahlen` (wie von
            `berechne_kennzahlen`) und `live` (wie von `hole_live_wetter`, auch None).
    """
    kennzahlen = bericht["kennzahlen"]
    live = bericht["live"]
    print(f"Wetterbericht {bericht['stadt']}")
    print(f"  Ø tmin: {kennzahlen['tmin_durchschnitt']} °C, Ø tmax: {kennzahlen['tmax_durchschnitt']} °C")
    print(f"  Heissester Tag: {kennzahlen['tmax_hoechste_datum']} mit {kennzahlen['tmax_hoechste']} °C")
    print(f"  Regentage: {kennzahlen['regentage']}, Niederschlag: {kennzahlen['niederschlag_gesamt_mm']} mm")
    if live is None:
        print("  Live-Wetter nicht verfügbar")
    else:
        print(f"  Jetzt: {live['temperatur']} °C, {live['beschreibung']}")
    print(f"  Quelle: {QUELLE}")


def main() -> None:
    """Fragt nach einer Stadt, erstellt den Bericht, speichert ihn und zeigt ihn an.

    Der Bericht landet als `bericht_<stadt in Kleinbuchstaben>.json` neben diesem Skript.
    Bei unbekannter Stadt oder fehlender CSV-Datei gibt die Funktion eine Meldung aus
    und kehrt ohne Bericht zurück.
    """
    stadt = input(f"Stadt ({', '.join(STAEDTE)}): ").strip()
    if stadt not in STAEDTE:
        print(f"Die Stadt «{stadt}» kenne ich nicht. Bitte wähle eine aus: {', '.join(STAEDTE)}")
        return
    try:
        zeilen = lese_stadt(CSV_DATEI, stadt)
    except FileNotFoundError:
        print(f"Die Datei {CSV_DATEI.name} fehlt.")
        return
    bericht = {
        "stadt": stadt,
        "kennzahlen": berechne_kennzahlen(zeilen),
        "live": hole_live_wetter(stadt),
        "quelle": QUELLE,
    }
    speichere_bericht(bericht, ORDNER / f"bericht_{stadt.lower()}.json")
    zeige_bericht(bericht)


if __name__ == "__main__":
    main()
