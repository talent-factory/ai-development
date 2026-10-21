"""Lektion 1 – Musterlösung: Wetter Zürich aus einer Textdatei auswerten."""

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
    with open(pfad, encoding="utf-8") as datei:
        for zeile in datei:
            datum, _stadt, tmin, tmax, niederschlag = zeile.strip().split(";")
            tage.append(
                {
                    "datum": datum,
                    "tmin": float(tmin),
                    "tmax": float(tmax),
                    "niederschlag": float(niederschlag),
                }
            )
    return tage


def finde_heissesten_tag(tage: list[dict]) -> dict:
    """Gibt den Tag mit der höchsten Maximaltemperatur zurück."""
    heissester = tage[0]
    for tag in tage:
        if tag["tmax"] > heissester["tmax"]:
            heissester = tag
    return heissester


def zaehle_regentage(tage: list[dict]) -> int:
    """Zählt die Tage mit Niederschlag über 0 mm."""
    anzahl = 0
    for tag in tage:
        if tag["niederschlag"] > 0:
            anzahl += 1
    return anzahl


def liste_regentage(tage: list[dict]) -> list[str]:
    """Gibt alle Regentage als Zeilen wie '2026-10-01: 3.8 mm' zurück (Kür)."""
    zeilen = []
    for tag in tage:
        if tag["niederschlag"] > 0:
            zeilen.append(f"{tag['datum']}: {tag['niederschlag']} mm")
    return zeilen


def schreibe_zusammenfassung(tage: list[dict], pfad: Path) -> None:
    """Schreibt eine kurze Zusammenfassung in eine Textdatei."""
    heissester = finde_heissesten_tag(tage)
    with open(pfad, "w", encoding="utf-8") as datei:
        datei.write(f"Anzahl Tage: {len(tage)}\n")
        datei.write(f"Heissester Tag: {heissester['datum']} mit {heissester['tmax']} °C\n")
        datei.write(f"Regentage: {zaehle_regentage(tage)}\n")
        for zeile in liste_regentage(tage):  # Kür
            datei.write(f"{zeile}\n")


def main() -> None:
    """Liest, wertet aus und gibt die Kontrollwerte aus."""
    tage = lese_tage(DATEI)
    schreibe_zusammenfassung(tage, AUSGABE)
    print(AUSGABE.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
