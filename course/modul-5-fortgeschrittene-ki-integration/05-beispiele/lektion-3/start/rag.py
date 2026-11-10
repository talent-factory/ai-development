"""Lektion 3: Die passende Textstelle finden (Gerüst).

Lektion 1 und 2 sind fertig (`frage_llm`, `aehnlichkeit`). Ersetze jedes `TODO` durch Code
und prüfe mit:
    uv run python pruefe.py 3
"""

from functools import cache

import numpy as np
from hilfen import MODELL, Dokument, embed, lade_wiki  # noqa: F401 (Dokument, lade_wiki brauchst du für die TODOs)
from pydantic import BaseModel
from pydantic_ai import Agent


class Antwort(BaseModel):
    """Antwort des Modells: Text und wie sicher es sich ist (0 bis 1)."""

    text: str
    sicherheit: float


def frage_llm(frage: str) -> Antwort:
    """Stellt dem Modell eine Frage und gibt die Antwort als `Antwort` zurück."""
    agent = Agent(
        MODELL,
        output_type=Antwort,
        instructions="Antworte auf Deutsch, Schweizer Orthografie (ss statt ß). Gib an, wie sicher du dir bist (0 bis 1).",
    )
    return agent.run_sync(frage).output


def aehnlichkeit(a: str, b: str) -> float:
    """Gibt die Ähnlichkeit zweier Texte zurück (1.0 = gleiche Bedeutung)."""
    vektor_a, vektor_b = embed([a, b])
    return float(np.dot(vektor_a, vektor_b))


@cache
def _wiki_vektoren() -> tuple[list[Dokument], np.ndarray]:
    """Berechnet die Vektoren der Wiki einmal und merkt sie sich."""
    # TODO 1: Lade die zehn Texte mit `lade_wiki()`.
    # TODO 2: Berechne ihre Vektoren mit `embed(...)` (übergib eine Liste mit dem Text jedes Dokuments).
    # TODO 3: Gib beides zurück: die Dokumente und die Vektoren.
    raise NotImplementedError("Lektion 3: `_wiki_vektoren` ist noch nicht fertig, siehe die TODOs.")


def suche(frage: str, k: int = 3) -> list[tuple[Dokument, float]]:
    """Gibt die `k` ähnlichsten Wiki-Texte mit ihrer Ähnlichkeit zurück, die besten zuerst."""
    # TODO 4: Hole Dokumente und Vektoren mit `_wiki_vektoren()`.
    # TODO 5: Verwandle die Frage mit `embed([frage], ist_frage=True)` in einen Vektor (die erste Zeile).
    # TODO 6: Berechne die Ähnlichkeit zu allen Texten auf einmal: `vektoren @ frage_vektor`.
    # TODO 7: Hole die Positionen der `k` besten Werte mit `np.argsort(-werte)[:k]`.
    # TODO 8: Gib für jede Position das Dokument und den Wert (als `float`) zurück, den besten zuerst.
    raise NotImplementedError("Lektion 3: `suche` ist noch nicht fertig, siehe die TODOs.")


if __name__ == "__main__":
    from hilfen import lade_testfragen

    for eintrag in lade_testfragen()["fragen"]:
        treffer = ", ".join(f"{d.name} ({wert:.2f})" for d, wert in suche(eintrag["frage"]))
        print(f"{eintrag['frage']}\n  -> {treffer}")
