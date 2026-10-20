"""Lektion 4 – Übung: Defekte Daten und API-Fehler robust behandeln.

Ergänze die Stellen mit TODO. Starte das Programm mit:  uv run python start.py

Teil 2 braucht Netz. Ohne Netz setzt du OFFLINE = True: Dann liest das Programm die
gespeicherte Fehlerantwort `beispiel_fehler.json`.
"""

# ruff: noqa: F401, F841  (Gerüst: Importe und Variablen brauchst du erst in der Übung)
import csv
import json
from pathlib import Path

OFFLINE = False  # True = gespeicherte Fehlerantwort statt Live-Abruf

ORDNER = Path(__file__).parent
DATEI = ORDNER / "wetter_defekt.csv"
FEHLERANTWORT = ORDNER / "beispiel_fehler.json"
API_URL = "https://api.open-meteo.com/v1/forecast"


def lese_robust(pfad: Path) -> tuple[list[dict], int]:
    """Liest die CSV und überspringt kaputte Zeilen.

    Args:
        pfad: Pfad zur CSV-Datei mit Kopfzeile.

    Returns:
        Ein Tupel (gültige Zeilen, Anzahl übersprungener Zeilen).
    """
    gueltig = []
    uebersprungen = 0
    with open(pfad, newline="", encoding="utf-8") as datei:
        for zeile in csv.DictReader(datei):
            # TODO (Teil 1): try-Block: tmin, tmax, niederschlag_mm mit float(),
            #                wettercode mit int() umwandeln; Zeile an `gueltig` anhängen
            # TODO (Teil 1): except ValueError: `uebersprungen` um 1 erhöhen
            pass
    return gueltig, uebersprungen


def hole_temperatur(latitude: float, longitude: float, url: str = API_URL) -> float | None:
    """Ruft die aktuelle Temperatur ab und meldet Fehler verständlich.

    Returns:
        Die Temperatur in °C oder None, wenn etwas schiefging.
    """
    import requests  # erst hier importieren, damit OFFLINE ohne requests läuft

    parameter = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m"}
    # TODO (Teil 2): try:
    #     antwort = requests.get(url, params=parameter, timeout=5)
    #     antwort.raise_for_status()
    #     return antwort.json()["current"]["temperature_2m"]
    # TODO (Teil 2): except requests.exceptions.HTTPError: Grund aus
    #     fehler.response.json()["reason"] ausgeben
    # TODO (Teil 2): except requests.exceptions.RequestException: "Keine Verbindung" ausgeben
    # Achtung: Die Reihenfolge der except-Blöcke zählt – spezifisch zuerst, allgemein zuletzt!
    return None


def lies_fehlergrund(antwort: dict) -> str:
    """Gibt den Grund aus einer Fehlerantwort der API zurück."""
    # TODO (Teil 2, offline): antwort.get("reason", "unbekannter Fehler")
    return ""


def main() -> None:
    """Führt beide Teile aus und gibt die Kontrollwerte aus."""
    gueltig, uebersprungen = lese_robust(DATEI)
    print(f"Gültige Zeilen: {len(gueltig)}, übersprungen: {uebersprungen}")

    if OFFLINE:
        antwort = json.loads(FEHLERANTWORT.read_text(encoding="utf-8"))
        print("Grund aus Datei:", lies_fehlergrund(antwort))
    else:
        print("Ungültiger Breitengrad:", hole_temperatur(999, 7.45))


if __name__ == "__main__":
    main()
