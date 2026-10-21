"""Lektion 4 – Musterlösung: Defekte Daten und API-Fehler robust behandeln.

Mit OFFLINE = True läuft das Programm ohne Netz und liefert immer dieselbe Ausgabe.
"""

import csv
import json
from pathlib import Path

OFFLINE = True  # True = gespeicherte Fehlerantwort statt Live-Abruf

ORDNER = Path(__file__).parent
DATEI = ORDNER / "wetter_defekt.csv"
FEHLERANTWORT = ORDNER / "beispiel_fehler.json"
LOGDATEI = ORDNER / "uebersprungen.log"
API_URL = "https://api.open-meteo.com/v1/forecast"


def lese_robust(pfad: Path, logdatei: Path | None = None) -> tuple[list[dict], int]:
    """Liest die CSV und überspringt kaputte Zeilen.

    Args:
        pfad: Pfad zur CSV-Datei mit Kopfzeile.
        logdatei: Optional (Kür): Datei, in die übersprungene Zeilen mit Grund geschrieben werden.

    Returns:
        Ein Tupel (gültige Zeilen, Anzahl übersprungener Zeilen).
    """
    gueltig = []
    meldungen = []
    with open(pfad, newline="", encoding="utf-8") as datei:
        leser = csv.DictReader(datei)
        for zeile in leser:
            try:
                for feld in ("tmin", "tmax", "niederschlag_mm"):
                    zeile[feld] = float(zeile[feld])
                zeile["wettercode"] = int(zeile["wettercode"])
            except ValueError as fehler:
                meldungen.append(f"Zeile {leser.line_num}: {fehler}")
            else:
                gueltig.append(zeile)
    if logdatei is not None:
        logdatei.write_text("\n".join(meldungen) + "\n", encoding="utf-8")
    return gueltig, len(meldungen)


def hole_temperatur(latitude: float, longitude: float, url: str = API_URL) -> float | None:
    """Ruft die aktuelle Temperatur ab und meldet Fehler verständlich.

    Returns:
        Die Temperatur in °C oder None, wenn etwas schiefging.
    """
    import requests  # erst hier importieren, damit OFFLINE ohne requests läuft

    parameter = {"latitude": latitude, "longitude": longitude, "current": "temperature_2m"}
    try:
        antwort = requests.get(url, params=parameter, timeout=5)
        antwort.raise_for_status()
        return antwort.json()["current"]["temperature_2m"]
    except requests.exceptions.HTTPError as fehler:
        print(f"Die API lehnt die Anfrage ab: {fehler.response.json()['reason']}")
    except requests.exceptions.JSONDecodeError:
        print("Die API hat eine leere oder ungültige Antwort geliefert.")
    except requests.exceptions.RequestException:
        print("Keine Verbindung zur API (Netz, Timeout oder falsche Adresse).")
    return None


def lies_fehlergrund(antwort: dict) -> str:
    """Gibt den Grund aus einer Fehlerantwort der API zurück."""
    return antwort.get("reason", "unbekannter Fehler")


def main() -> None:
    """Führt beide Teile aus und gibt die Kontrollwerte aus."""
    gueltig, uebersprungen = lese_robust(DATEI, LOGDATEI)
    print(f"Gültige Zeilen: {len(gueltig)}, übersprungen: {uebersprungen}")

    if OFFLINE:
        antwort = json.loads(FEHLERANTWORT.read_text(encoding="utf-8"))
        print("Grund aus Datei:", lies_fehlergrund(antwort))
    else:
        print("Ungültiger Breitengrad:", hole_temperatur(999, 7.45))


if __name__ == "__main__":
    main()
