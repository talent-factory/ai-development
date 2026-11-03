"""Lektion 4: Suche und Modell verbinden, das Mini-RAG (Gerüst).

Lektion 1 bis 3 sind fertig (`frage_llm`, `aehnlichkeit`, `suche`). Ersetze jedes `TODO` durch Code
und prüfe mit:
    uv run python pruefe.py 4
"""

from functools import cache

import numpy as np
from hilfen import MODELL, RAG_REGEL, Dokument, embed, lade_wiki  # noqa: F401 (RAG_REGEL brauchst du für TODO 3)
from pydantic import BaseModel
from pydantic_ai import Agent


class Antwort(BaseModel):
    """Antwort des Modells: Text, wie sicher es sich ist (0 bis 1) und die Quelle."""

    text: str
    sicherheit: float
    # TODO 1: Feld `quelle` ergänzen: `str | None = None` (der Dateiname der Quelle, oder leer).


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
    # TODO 2: Hole die Treffer mit `suche(frage)` und baue daraus den Quellen-Text:
    #         pro Treffer `[Dateiname]`, dann eine neue Zeile mit dem Text, die Treffer durch eine Leerzeile getrennt.
    # TODO 3: Baue den Prompt aus drei Teilen: der `RAG_REGEL` (nur wenn `mit_regel` wahr ist),
    #         dem Block "Quellen:" mit dem Quellen-Text und der Zeile "Frage: <die Frage>".
    #         Die Teile trennst du durch eine Leerzeile.
    # TODO 4: Erstelle den Agenten wie in `frage_llm` (`MODELL`, `output_type=Antwort`, gleiche `instructions`),
    #         rufe ihn mit dem Prompt auf (`run_sync`) und gib `.output` zurück.
    raise NotImplementedError("Lektion 4: `beantworte` ist noch nicht fertig, siehe die TODOs.")


if __name__ == "__main__":
    from hilfen import lade_testfragen

    for frage in (lade_testfragen()["fragen"][0]["frage"], lade_testfragen()["falle"]):
        print(frage, "->", beantworte(frage))
