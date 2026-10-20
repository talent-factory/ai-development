"""Lektion 2 – Übung: Wetterdaten aus einer CSV-Datei auswerten.

Ergänze die Stellen mit TODO. Starte das Programm mit:  uv run python start.py
"""

import csv  # noqa: F401  (wird in der Übung gebraucht)
from pathlib import Path

DATEI = Path(__file__).parent / "wetter_30tage.csv"
AUSGABE = Path(__file__).parent / "warme_tage.csv"
GRENZE = 20.0


def lese_csv(pfad: Path) -> list[dict]:
    """Liest die CSV-Datei und gibt pro Zeile ein Dictionary zurück.

    Args:
        pfad: Pfad zur CSV-Datei (mit Kopfzeile).

    Returns:
        Liste von Dictionaries. tmin, tmax und niederschlag_mm sind float.
    """
    zeilen = []
    # TODO: Datei mit `open(pfad, newline="", encoding="utf-8")` öffnen
    # TODO: mit `csv.DictReader(datei)` zeilenweise lesen
    # TODO: tmin, tmax und niederschlag_mm in float umwandeln und die Zeile anhängen
    return zeilen


def durchschnitt_tmax_je_stadt(zeilen: list[dict]) -> dict[str, float]:
    """Berechnet den Durchschnitt von tmax pro Stadt (auf 1 Stelle gerundet)."""
    # TODO: pro Stadt alle tmax-Werte sammeln (Dict mit Listen), dann den Schnitt bilden
    return {}


def filtere_warme_tage(zeilen: list[dict], grenze: float) -> list[dict]:
    """Gibt alle Zeilen zurück, deren tmax über der Grenze liegt."""
    # TODO: Schleife mit if tmax > grenze
    return []


def schreibe_csv(zeilen: list[dict], pfad: Path) -> None:
    """Schreibt Zeilen mit Kopfzeile in eine CSV-Datei."""
    # TODO: `csv.DictWriter` mit fieldnames=zeilen[0].keys(), writeheader(), writerows()
    # Tipp: `newline=""` und `encoding="utf-8"` beim Öffnen nicht vergessen
    pass


def main() -> None:
    """Liest, wertet aus und gibt die Kontrollwerte aus."""
    zeilen = lese_csv(DATEI)
    print(f"Zeilen: {len(zeilen)}")
    print("Durchschnitt tmax je Stadt:", durchschnitt_tmax_je_stadt(zeilen))
    warm = filtere_warme_tage(zeilen, GRENZE)
    print(f"Tage über {GRENZE} °C: {len(warm)}")
    schreibe_csv(warm, AUSGABE)


if __name__ == "__main__":
    main()
