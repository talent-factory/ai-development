"""Lektion 3: Die passende Textstelle finden (baut auf Lektion 2 auf)."""

from functools import cache

import numpy as np
from hilfen import MODELL, Dokument, embed, lade_wiki
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
    wiki = lade_wiki()
    return wiki, embed([dokument.text for dokument in wiki])


def suche(frage: str, k: int = 3) -> list[tuple[Dokument, float]]:
    """Gibt die `k` ähnlichsten Wiki-Texte mit ihrer Ähnlichkeit zurück, die besten zuerst."""
    wiki, vektoren = _wiki_vektoren()
    frage_vektor = embed([frage], ist_frage=True)[0]
    werte = vektoren @ frage_vektor
    beste = np.argsort(-werte)[:k]
    return [(wiki[i], float(werte[i])) for i in beste]


if __name__ == "__main__":
    from hilfen import lade_testfragen

    for eintrag in lade_testfragen()["fragen"]:
        treffer = ", ".join(f"{d.name} ({wert:.2f})" for d, wert in suche(eintrag["frage"]))
        print(f"{eintrag['frage']}\n  -> {treffer}")
