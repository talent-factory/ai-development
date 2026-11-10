"""Mini-RAG über die Wiki der Talwerk AG.

Diese Datei wächst mit jeder Lektion. Lektion 1: ein Sprachmodell befragen (`frage_llm`).
Ersetze jedes `TODO` durch Code und prüfe mit: uv run python pruefe.py 1
"""

from hilfen import MODELL  # noqa: F401 (brauchst du für TODO 3)
from pydantic import BaseModel
from pydantic_ai import Agent  # noqa: F401 (brauchst du für TODO 3)


class Antwort(BaseModel):
    """Antwort des Modells: Text und wie sicher es sich ist (0 bis 1)."""

    # TODO 1: Feld `text` ergänzen (Typ str)
    # TODO 2: Feld `sicherheit` ergänzen (Typ float, 0 bis 1)


def frage_llm(frage: str) -> Antwort:
    """Stellt dem Modell eine Frage und gibt die Antwort als `Antwort` zurück."""
    # TODO 3: Erstelle einen `Agent` mit `MODELL` und `output_type=Antwort`.
    #         Gib ihm diese Anweisung mit (`instructions=`):
    #         "Antworte auf Deutsch, Schweizer Orthografie (ss statt ß). Gib an, wie sicher du dir bist (0 bis 1)."
    # TODO 4: Rufe den Agenten mit `run_sync(frage)` auf und gib `.output` zurück.
    raise NotImplementedError("Lektion 1: `frage_llm` ist noch nicht fertig, siehe die TODOs.")


if __name__ == "__main__":
    from hilfen import lade_testfragen

    print(frage_llm(lade_testfragen()["firmenfrage"]))
