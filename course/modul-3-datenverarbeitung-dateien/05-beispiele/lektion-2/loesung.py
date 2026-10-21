"""Lektion 2 – Musterlösung: Wetterdaten aus einer CSV-Datei auswerten."""

import csv
from pathlib import Path

DATEI = Path(__file__).parent / "wetter_30tage.csv"
AUSGABE = Path(__file__).parent / "warme_tage.csv"
GRENZE = 20.0
SPALTEN = ["stadt", "datum", "tmin", "tmax", "niederschlag_mm", "wettercode"]


def lese_csv(pfad: Path) -> list[dict]:
    """Liest die CSV-Datei und gibt pro Zeile ein Dictionary zurück.

    Args:
        pfad: Pfad zur CSV-Datei (mit Kopfzeile).

    Returns:
        Liste von Dictionaries. tmin, tmax und niederschlag_mm sind float.
    """
    zeilen = []
    with open(pfad, newline="", encoding="utf-8") as datei:
        for zeile in csv.DictReader(datei):
            for feld in ("tmin", "tmax", "niederschlag_mm"):
                zeile[feld] = float(zeile[feld])
            zeilen.append(zeile)
    return zeilen


def durchschnitt_tmax_je_stadt(zeilen: list[dict]) -> dict[str, float]:
    """Berechnet den Durchschnitt von tmax pro Stadt (auf 1 Stelle gerundet)."""
    werte: dict[str, list[float]] = {}
    for zeile in zeilen:
        werte.setdefault(zeile["stadt"], []).append(zeile["tmax"])
    return {stadt: round(sum(w) / len(w), 1) for stadt, w in werte.items()}


def filtere_warme_tage(zeilen: list[dict], grenze: float) -> list[dict]:
    """Gibt alle Zeilen zurück, deren tmax über der Grenze liegt."""
    warm = []
    for zeile in zeilen:
        if zeile["tmax"] > grenze:
            warm.append(zeile)
    return warm


def filtere_stadt(zeilen: list[dict], stadt: str) -> list[dict]:
    """Gibt nur die Zeilen einer Stadt zurück (Kür)."""
    return [zeile for zeile in zeilen if zeile["stadt"] == stadt]


def schreibe_csv(zeilen: list[dict], pfad: Path) -> None:
    """Schreibt Zeilen mit Kopfzeile in eine CSV-Datei."""
    with open(pfad, "w", newline="", encoding="utf-8") as datei:
        schreiber = csv.DictWriter(datei, fieldnames=SPALTEN)
        schreiber.writeheader()
        schreiber.writerows(zeilen)


def pruefe_testdaten(zeilen: list[dict]) -> None:
    """Prüft KI-erzeugte Testdaten (KI-Moment): wirft AssertionError bei Fehlern."""
    for zeile in zeilen:
        assert list(zeile) == SPALTEN, f"Spalten stimmen nicht: {list(zeile)}"
        assert zeile["tmin"] < zeile["tmax"], f"tmin >= tmax: {zeile}"


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
