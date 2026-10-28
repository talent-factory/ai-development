"""Lektion 1: Ein Sprachmodell aus Python befragen."""

from hilfen import MODELL
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


if __name__ == "__main__":
    from hilfen import lade_testfragen

    print(frage_llm(lade_testfragen()["firmenfrage"]))
