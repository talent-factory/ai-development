"""Lektion 1 – Übung: Wetter Zürich aus einer Textdatei auswerten.

Ergänze die Stellen mit TODO. Starte das Programm mit:  uv run python start.py
"""

from pathlib import Path

DATEI = Path(__file__).parent / "wetter_zuerich.txt"
AUSGABE = Path(__file__).parent / "zusammenfassung.txt"


def lese_tage(pfad: Path) -> list[dict]:
    """Liest die Textdatei und gibt pro Zeile ein Dictionary zurück.

    Args:
        pfad: Pfad zur Textdatei (Format: datum;stadt;tmin;tmax;niederschlag).

    Returns:
        Liste von Dictionaries mit den Schlüsseln datum, tmin, tmax, niederschlag.
    """
    tage = []
    # TODO: Datei mit `with open(...)` öffnen (encoding="utf-8")
    # TODO: jede Zeile mit .strip() von \n befreien und mit .split(";") zerlegen
    # TODO: tmin, tmax und niederschlag mit float() umwandeln
    # TODO: ein Dictionary pro Tag an `tage` anhängen
    return tage


def finde_heissesten_tag(tage: list[dict]) -> dict:
    """Gibt den Tag mit der höchsten Maximaltemperatur zurück."""
    # TODO: Schleife über alle Tage, den grössten tmax-Wert merken
    return {}


def schreibe_zusammenfassung(tage: list[dict], pfad: Path) -> None:
    """Schreibt eine kurze Zusammenfassung in eine Textdatei."""
    heissester = finde_heissesten_tag(tage)
    # TODO: Datei mit `with open(pfad, "w", ...)` öffnen und drei Zeilen schreiben:
    #       Anzahl Tage, heissester Tag mit Datum und tmax, Anzahl Regentage
    print(heissester)


def main() -> None:
    """Liest, wertet aus und gibt die Kontrollwerte aus."""
    tage = lese_tage(DATEI)
    print(f"Anzahl Tage: {len(tage)}")
    schreibe_zusammenfassung(tage, AUSGABE)


if __name__ == "__main__":
    main()
