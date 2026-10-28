"""Demo für den Ausblick in Lektion 4: Das Modell ruft die Suche selbst als Werkzeug auf.

Nur für die Dozentin / den Dozenten. Läuft im Ordner mit `hilfen.py`, `rag.py` (Lektion 4) und der Wiki:
    uv run python demo_tool_use.py
Braucht den Schlüssel (kein `KONSERVE=1`).
"""

from hilfen import MODELL
from pydantic_ai import Agent

from rag import suche

agent = Agent(
    MODELL,
    instructions=(
        "Du beantwortest Fragen zur Wiki der Talwerk AG. Nutze dafür das Werkzeug `suche_in_wiki`. "
        "Antworte nur aus den Treffern und nenne den Dateinamen. Steht die Antwort nicht darin, "
        "antworte genau: Ich finde dazu nichts. Antworte auf Deutsch, Schweizer Orthografie (ss statt ß)."
    ),
)


@agent.tool_plain
def suche_in_wiki(suchbegriff: str) -> str:
    """Sucht in der Wiki der Talwerk AG und gibt die drei besten Texte mit Dateinamen zurück."""
    print(f"  [Werkzeug aufgerufen: suche_in_wiki({suchbegriff!r})]")
    return "\n\n".join(f"[{dokument.name}]\n{dokument.text}" for dokument, _ in suche(suchbegriff, k=3))


if __name__ == "__main__":
    for frage in ["Wann ist der Deployment-Freeze?", "Wie viele Ferientage habe ich pro Jahr?"]:
        print(frage)
        print("->", agent.run_sync(frage).output, "\n")
