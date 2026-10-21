"""Lektion 3 – Musterlösung: JSON speichern und laden, Wettercodes übersetzen, API abrufen.

Mit OFFLINE = True läuft das Programm ohne Netz und liefert immer dieselbe Ausgabe.
"""

import json
from pathlib import Path
from typing import Any

OFFLINE = True  # True = gespeicherte Antwort statt Live-Abruf

ORDNER = Path(__file__).parent
ZUSAMMENFASSUNG = ORDNER / "zusammenfassung.json"
BEISPIELANTWORT = ORDNER / "beispiel_antwort.json"
BEISPIELANTWORT_5 = ORDNER / "beispiel_antwort_5_staedte.json"
API_URL = "https://api.open-meteo.com/v1/forecast"
STAEDTE = {
    "Zürich": (47.3769, 8.5417),
    "Bern": (46.948, 7.4474),
    "Genf": (46.2044, 6.1432),
    "Basel": (47.5596, 7.5886),
    "Lugano": (46.0037, 8.9511),
}
TAGES_VARIABLEN = "temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code"

DURCHSCHNITT_TMAX = {"Zürich": 20.7, "Bern": 19.9, "Genf": 21.4, "Basel": 21.6, "Lugano": 21.8}

WETTERCODES = {
    0: "klar",
    3: "bedeckt",
    45: "Nebel",
    61: "leichter Regen",
    80: "leichte Regenschauer",
    95: "Gewitter",
}


def speichere_json(daten: dict, pfad: Path) -> None:
    """Speichert ein Dictionary als lesbare JSON-Datei."""
    with open(pfad, "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=2, ensure_ascii=False)


def lade_json(pfad: Path) -> Any:
    """Lädt eine JSON-Datei und gibt den Inhalt zurück."""
    with open(pfad, encoding="utf-8") as datei:
        return json.load(datei)


def beschreibe_wetter(code: int) -> str:
    """Übersetzt einen Wettercode in Klartext ('unbekannt', falls der Code fehlt)."""
    return WETTERCODES.get(code, "unbekannt")


def hole_wetter() -> dict:
    """Gibt die Wetterdaten für Bern zurück (live oder aus der Beispielantwort)."""
    if OFFLINE:
        return lade_json(BEISPIELANTWORT)
    import requests  # erst hier importieren, damit OFFLINE ohne requests läuft

    parameter = {
        "latitude": 46.948,
        "longitude": 7.4474,
        "current": "temperature_2m,weather_code,wind_speed_10m",
        "daily": TAGES_VARIABLEN,
        "forecast_days": 3,
        "timezone": "Europe/Zurich",
    }
    antwort = requests.get(API_URL, params=parameter, timeout=10)
    antwort.raise_for_status()
    return antwort.json()


def hole_wetter_alle_staedte() -> list[dict]:
    """Gibt die Wetterdaten aller fünf Städte in einem Request zurück (Kür).

    Bei mehreren Orten liefert die API eine Liste statt eines Dictionaries.
    """
    if OFFLINE:
        return lade_json(BEISPIELANTWORT_5)
    import requests  # erst hier importieren, damit OFFLINE ohne requests läuft

    parameter = {
        "latitude": ",".join(str(lage[0]) for lage in STAEDTE.values()),
        "longitude": ",".join(str(lage[1]) for lage in STAEDTE.values()),
        "daily": TAGES_VARIABLEN,
        "forecast_days": 3,
        "timezone": "Europe/Zurich",
    }
    antwort = requests.get(API_URL, params=parameter, timeout=10)
    antwort.raise_for_status()
    return antwort.json()


def main() -> None:
    """Führt die drei Teile der Übung aus und gibt die Kontrollwerte aus."""
    # Teil 1: JSON speichern und laden
    speichere_json(DURCHSCHNITT_TMAX, ZUSAMMENFASSUNG)
    geladen = lade_json(ZUSAMMENFASSUNG)
    assert geladen == DURCHSCHNITT_TMAX
    print("Geladen:", geladen)

    # Teil 2 + 3: Wetter Bern
    antwort = hole_wetter()
    tage = antwort["daily"]["time"]
    print(f"Tage in der Antwort: {len(tage)}")
    code = antwort["daily"]["weather_code"][0]
    tmax = antwort["daily"]["temperature_2m_max"][0]
    print(f"heute: {beschreibe_wetter(code)}, {tmax} °C")

    # Kür: alle Städte
    for stadt, ort in zip(STAEDTE, hole_wetter_alle_staedte()):
        print(f"{stadt}: {ort['daily']['temperature_2m_max'][0]} °C")


if __name__ == "__main__":
    main()
