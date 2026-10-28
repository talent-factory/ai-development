"""Lektion 2: Texte in Vektoren verwandeln und Ähnlichkeit messen (baut auf Lektion 1 auf)."""

import numpy as np
from hilfen import MODELL, embed
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
    vektor_a, vektor_b = embed([a, b])
    return float(np.dot(vektor_a, vektor_b))


if __name__ == "__main__":
    from hilfen import lade_testfragen

    for text_a, text_b in lade_testfragen()["satzpaare"]:
        print(f"{aehnlichkeit(text_a, text_b):.2f}  {text_a} | {text_b}")
