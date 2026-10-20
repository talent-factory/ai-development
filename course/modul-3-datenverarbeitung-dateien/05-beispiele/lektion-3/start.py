"""Lektion 3 – Übung: JSON speichern und laden, Wettercodes übersetzen, API abrufen.

Ergänze die Stellen mit TODO. Starte das Programm mit:  uv run python start.py

Fällt die API aus oder ist das Netz langsam, setze OFFLINE = True. Dann liest das
Programm die gespeicherte Antwort `beispiel_antwort.json` statt live abzurufen.
"""

# ruff: noqa: F401, F841  (Gerüst: Importe und Variablen brauchst du erst in der Übung)
import json
from pathlib import Path
from typing import Any

OFFLINE = False  # True = gespeicherte Antwort statt Live-Abruf

ORDNER = Path(__file__).parent
ZUSAMMENFASSUNG = ORDNER / "zusammenfassung.json"
BEISPIELANTWORT = ORDNER / "beispiel_antwort.json"
API_URL = "https://api.open-meteo.com/v1/forecast"

# Ergebnis aus Lektion 2 (Durchschnitt tmax je Stadt) – damit du hier direkt einsteigen kannst
DURCHSCHNITT_TMAX = {"Zürich": 20.7, "Bern": 19.9, "Genf": 21.4, "Basel": 21.6, "Lugano": 21.8}

# Fallback: vollständige Übersetzung (WMO-Codes). Nutze sie nur, wenn du mit Teil 2 nicht fertig wirst.
WETTERCODES_VOLL = {
    0: "klar",
    1: "überwiegend klar",
    2: "teilweise bewölkt",
    3: "bedeckt",
    45: "Nebel",
    61: "leichter Regen",
    63: "mässiger Regen",
    80: "leichte Regenschauer",
    95: "Gewitter",
    96: "Gewitter mit Hagel",
}

# TODO (Teil 2): Baue ein eigenes Dict mit nur diesen Codes: 0, 3, 45, 61, 80, 95
WETTERCODES: dict[int, str] = {}


def speichere_json(daten: dict, pfad: Path) -> None:
    """Speichert ein Dictionary als lesbare JSON-Datei."""
    # TODO (Teil 1): `with open(pfad, "w", encoding="utf-8")` und `json.dump(...)`
    # Tipp: indent=2 und ensure_ascii=False, damit "Zürich" lesbar bleibt
    pass


def lade_json(pfad: Path) -> Any:
    """Lädt eine JSON-Datei und gibt den Inhalt zurück."""
    # TODO (Teil 1): `json.load(datei)`
    return {}


def beschreibe_wetter(code: int) -> str:
    """Übersetzt einen Wettercode in Klartext ('unbekannt', falls der Code fehlt)."""
    # TODO (Teil 2): Dict-Zugriff mit .get(code, "unbekannt")
    return ""


def hole_wetter() -> dict:
    """Gibt die Wetterdaten für Bern zurück (live oder aus der Beispielantwort)."""
    if OFFLINE:
        # TODO (Teil 3): lade_json(BEISPIELANTWORT) zurückgeben
        return {}
    import requests  # erst hier importieren, damit OFFLINE ohne requests läuft

    parameter = {
        "latitude": 46.948,
        "longitude": 7.4474,
        "current": "temperature_2m,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code",
        "forecast_days": 3,
        "timezone": "Europe/Zurich",
    }
    # TODO (Teil 3): requests.get(API_URL, params=parameter, timeout=10)
    # TODO (Teil 3): mit .raise_for_status() Fehler melden, dann .json() zurückgeben
    return {}


def main() -> None:
    """Führt die drei Teile der Übung aus."""
    # Teil 1
    speichere_json(DURCHSCHNITT_TMAX, ZUSAMMENFASSUNG)
    print("Geladen:", lade_json(ZUSAMMENFASSUNG))

    # Teil 2 + 3
    antwort = hole_wetter()
    if not antwort:
        print("Teil 3 ist noch offen: hole_wetter() gibt noch keine Daten zurück.")
        return
    tage = antwort["daily"]["time"]
    print(f"Tage in der Antwort: {len(tage)}")
    # TODO (Teil 3): gib "heute: <Klartext>, <tmax> °C" aus
    # (tmax: antwort["daily"]["temperature_2m_max"][0], Code: antwort["daily"]["weather_code"][0])


if __name__ == "__main__":
    main()
