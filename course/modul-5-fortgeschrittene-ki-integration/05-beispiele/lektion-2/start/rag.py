"""Lektion 2: Texte in Vektoren verwandeln und Ähnlichkeit messen (Gerüst).

Lektion 1 ist fertig (`frage_llm`). Ersetze jedes `TODO` durch Code und prüfe mit:
    uv run python pruefe.py 2
"""

import numpy as np  # noqa: F401 (brauchst du für TODO 2)
from hilfen import MODELL, embed  # noqa: F401 (embed brauchst du für TODO 1)
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
    """Gibt die Ähnlichkeit zweier Texte zurück (1.0 = gleiche Bedeutung).

    Die Vektoren haben die Länge 1, deshalb genügt das Skalarprodukt.
    """
    # TODO 1: Berechne die Vektoren beider Texte mit `embed([a, b])` und packe sie in zwei Variablen aus.
    # TODO 2: Gib das Skalarprodukt der beiden Vektoren (`np.dot`) als `float` zurück.
    raise NotImplementedError("Lektion 2: `aehnlichkeit` ist noch nicht fertig, siehe die TODOs.")


if __name__ == "__main__":
    from hilfen import lade_testfragen

    for text_a, text_b in lade_testfragen()["satzpaare"]:
        print(f"{aehnlichkeit(text_a, text_b):.2f}  {text_a} | {text_b}")
