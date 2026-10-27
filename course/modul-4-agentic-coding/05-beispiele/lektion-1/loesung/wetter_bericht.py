"""Wetterbericht für eine Schweizer Stadt: CSV auswerten, Live-Wetter abrufen, Bericht als JSON speichern.

Musterlösung Lektion 1 (Modul 4).
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
    """Liest die CSV-Datei und gibt die Zeilen einer Stadt zurück (Zahlen als float)."""
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
    """Berechnet Durchschnitte, heissesten Tag, Regentage und Gesamtniederschlag."""
    heissester = max(zeilen, key=lambda zeile: zeile["tmax"])
    return {
        "tmin_durchschnitt": round(sum(z["tmin"] for z in zeilen) / len(zeilen), 1),
        "tmax_durchschnitt": round(sum(z["tmax"] for z in zeilen) / len(zeilen), 1),
        "tmax_hoechste": heissester["tmax"],
        "tmax_hoechste_datum": heissester["datum"],
        "regentage": sum(1 for z in zeilen if z["niederschlag_mm"] > 0),
        "niederschlag_gesamt_mm": round(sum(z["niederschlag_mm"] for z in zeilen), 1),
    }


def beschreibe_wetter(code: int) -> str:
    """Übersetzt einen Wettercode in Klartext ('unbekannt', falls der Code fehlt)."""
    return WETTERCODES.get(code, "unbekannt")


def hole_live_wetter(stadt: str) -> dict | None:
    """Ruft aktuelle Temperatur und Wettercode ab. Gibt None zurück, wenn der Abruf scheitert."""
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
    """Speichert den Bericht als lesbare JSON-Datei."""
    with open(pfad, "w", encoding="utf-8") as datei:
        json.dump(bericht, datei, indent=2, ensure_ascii=False)


def zeige_bericht(bericht: dict) -> None:
    """Gibt eine lesbare Zusammenfassung auf dem Bildschirm aus."""
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
    """Fragt nach einer Stadt, erstellt den Bericht und speichert ihn."""
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
