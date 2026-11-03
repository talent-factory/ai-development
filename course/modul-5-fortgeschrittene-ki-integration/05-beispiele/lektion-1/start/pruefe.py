"""Prüft das Mindestziel einer Übung: `uv run python pruefe.py 1` (Lektionsnummer 1 bis 4).

Das Skript importiert deine Datei `rag.py` aus diesem Ordner. Es braucht deinen Schlüssel,
oder `KONSERVE=1` für die Beispiele aus dem Kurs.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from hilfen import lade_testfragen  # noqa: E402


def ok(bedingung: bool, meldung: str) -> bool:
    """Gibt OK oder FEHLER mit der Meldung aus."""
    print(f"{'OK' if bedingung else 'FEHLER'}: {meldung}")
    return bedingung


def pruefe_1(rag) -> bool:
    """Übung 1: `frage_llm` liefert ein `Antwort`-Objekt mit Text und Sicherheit zwischen 0 und 1."""
    antwort = rag.frage_llm(lade_testfragen()["firmenfrage"])
    return ok(isinstance(antwort.text, str) and antwort.text != "", "Antwort hat einen Text") & ok(
        0 <= antwort.sicherheit <= 1, f"Sicherheit liegt zwischen 0 und 1 ({antwort.sicherheit})"
    )


def pruefe_2(rag) -> bool:
    """Übung 2: Gleiche Sätze sind (fast) gleich, unterschiedliche Sätze deutlich weniger ähnlich."""
    paare = lade_testfragen()["satzpaare"]
    gleich = rag.aehnlichkeit(paare[0][0], paare[0][0])
    anders = rag.aehnlichkeit(paare[2][0], paare[2][1])
    return ok(gleich > 0.99, f"gleicher Satz ergibt etwa 1.0 ({gleich:.3f})") & ok(
        anders < gleich, f"unterschiedliche Sätze sind weniger ähnlich ({anders:.3f})"
    )


def pruefe_3(rag) -> bool:
    """Übung 3: Zu jeder Testfrage steht der richtige Text unter den besten drei Treffern."""
    alle_ok = True
    for eintrag in lade_testfragen()["fragen"]:
        namen = [dokument.name for dokument, _ in rag.suche(eintrag["frage"], k=3)]
        alle_ok &= ok(eintrag["quelle"] in namen, f"{eintrag['frage']} -> {namen[0]} (Soll: {eintrag['quelle']})")
    return alle_ok


def pruefe_4(rag) -> bool:
    """Übung 4: `beantworte` nennt die Quelle, und die Fallen-Frage ergibt «Ich finde dazu nichts»."""
    testfragen = lade_testfragen()
    frage = testfragen["fragen"][0]
    antwort = rag.beantworte(frage["frage"])
    erste = ok(
        frage["quelle"] in antwort.text or frage["quelle"] == antwort.quelle,
        f"Antwort nennt die Quelle {frage['quelle']}",
    )
    falle = rag.beantworte(testfragen["falle"])
    return erste & ok("Ich finde dazu nichts" in falle.text, "Fallen-Frage ergibt «Ich finde dazu nichts»")


def main() -> None:
    """Liest die Lektionsnummer und führt die passende Prüfung aus."""
    if len(sys.argv) != 2 or sys.argv[1] not in {"1", "2", "3", "4"}:
        sys.exit("Aufruf: uv run python pruefe.py <Lektionsnummer 1-4>")
    import rag

    bestanden = {"1": pruefe_1, "2": pruefe_2, "3": pruefe_3, "4": pruefe_4}[sys.argv[1]](rag)
    print("\nMindestziel erreicht." if bestanden else "\nNoch nicht erreicht. Lies die FEHLER-Zeilen oben.")


if __name__ == "__main__":
    main()
