"""Lektion 4: Suche und Modell verbinden, das Mini-RAG (baut auf Lektion 3 auf)."""

from functools import cache

import numpy as np
from hilfen import MODELL, RAG_REGEL, Dokument, embed, lade_wiki
from pydantic import BaseModel
from pydantic_ai import Agent


class Antwort(BaseModel):
    """Antwort des Modells: Text, wie sicher es sich ist (0 bis 1) und die Quelle."""

    text: str
    sicherheit: float
    quelle: str | None = None


def frage_llm(frage: str) -> Antwort:
    """Stellt dem Modell eine Frage ohne Quellen und gibt die Antwort als `Antwort` zurück."""
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
    wiki = lade_wiki()
    return wiki, embed([dokument.text for dokument in wiki])


def suche(frage: str, k: int = 3) -> list[tuple[Dokument, float]]:
    """Gibt die `k` ähnlichsten Wiki-Texte mit ihrer Ähnlichkeit zurück, die besten zuerst."""
    wiki, vektoren = _wiki_vektoren()
    frage_vektor = embed([frage], ist_frage=True)[0]
    werte = vektoren @ frage_vektor
    beste = np.argsort(-werte)[:k]
    return [(wiki[i], float(werte[i])) for i in beste]


def beantworte(frage: str, mit_regel: bool = True) -> Antwort:
    """Sucht passende Wiki-Texte und lässt das Modell daraus antworten.

    Mit `mit_regel=False` fehlt die Anweisung, nur aus den Quellen zu antworten.
    """
    quellen = "\n\n".join(f"[{dokument.name}]\n{dokument.text}" for dokument, _ in suche(frage))
    teile = [RAG_REGEL] if mit_regel else []
    teile += [f"Quellen:\n{quellen}", f"Frage: {frage}"]
    agent = Agent(
        MODELL,
        output_type=Antwort,
        instructions="Antworte auf Deutsch, Schweizer Orthografie (ss statt ß). Gib an, wie sicher du dir bist (0 bis 1).",
    )
    return agent.run_sync("\n\n".join(teile)).output


if __name__ == "__main__":
    from hilfen import lade_testfragen

    for frage in (lade_testfragen()["fragen"][0]["frage"], lade_testfragen()["falle"]):
        print(frage, "->", beantworte(frage))
