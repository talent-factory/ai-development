"""Hilfsfunktionen für Modul 5: Wiki laden, Texte in Vektoren verwandeln, Modell wählen.

Dieses Modul nimmt dir die technischen Details ab (zum Beispiel das asynchrone Warten auf
das Embedding-Modell), damit du dich auf die Aufgaben konzentrieren kannst.

Mit `KONSERVE=1` (Umgebungsvariable) laufen alle bekannten Beispiele ohne Internet und ohne
Schlüssel: `embed()` liest die Vektoren aus `konserve/vektoren.json`, und `MODELL` spielt die
aufgezeichneten Antworten aus `konserve/antworten.json` ab.
"""

import asyncio
import json
import os
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from pydantic_ai import Embedder
from pydantic_ai.messages import ModelMessage, ModelResponse, TextPart, ToolCallPart, UserPromptPart
from pydantic_ai.models.function import AgentInfo, FunctionModel

ORDNER = Path(__file__).parent
KONSERVE = os.environ.get("KONSERVE") == "1"

CHAT_MODELL = "google:gemini-3.5-flash-lite"
EMBEDDING_MODELL = "google:gemini-embedding-2"

# Die Regel für das RAG aus Lektion 4. Lässt du sie im Prompt weg, erfindet das Modell Antworten.
RAG_REGEL = (
    "Beantworte die Frage nur aus den folgenden Quellen. Nenne den Dateinamen der Quelle. "
    "Steht die Antwort nicht in den Quellen, antworte genau: Ich finde dazu nichts."
)


@dataclass
class Dokument:
    """Ein Text aus der Wiki: `name` ist der Dateiname, `text` der Inhalt."""

    name: str
    text: str


def lade_wiki() -> list[Dokument]:
    """Liest alle Texte aus dem Ordner `wiki/`, sortiert nach Dateiname."""
    return [
        Dokument(datei.name, datei.read_text(encoding="utf-8").strip())
        for datei in sorted((ORDNER / "wiki").glob("*.md"))
    ]


def lade_testfragen() -> dict:
    """Liest die Testfragen mit den richtigen Quellen aus `testfragen.json`."""
    return json.loads((ORDNER / "testfragen.json").read_text(encoding="utf-8"))


def embed(texte: list[str], ist_frage: bool = False) -> np.ndarray:
    """Verwandelt Texte in Vektoren und gibt eine Tabelle mit einer Zeile pro Text zurück.

    `ist_frage=True` sagt dem Modell, dass es um eine Suchfrage geht und nicht um ein Dokument.
    Die Vektoren haben die Länge 1, deshalb ist ihre Ähnlichkeit einfach das Skalarprodukt.
    """
    if KONSERVE:
        return _embed_aus_konserve(texte, ist_frage)
    # Pro Aufruf ein frischer Embedder in einem einzigen asyncio.run: so gibt es keine Probleme mit Event-Loops.
    return np.array(asyncio.run(_embed_async(texte, ist_frage)))


async def _embed_async(texte: list[str], ist_frage: bool) -> list[list[float]]:
    embedder = Embedder(EMBEDDING_MODELL)
    if ist_frage:
        ergebnisse = [await embedder.embed_query(text) for text in texte]
        return [ergebnis.embeddings[0] for ergebnis in ergebnisse]
    return (await embedder.embed_documents(texte)).embeddings


def _embed_aus_konserve(texte: list[str], ist_frage: bool) -> np.ndarray:
    vektoren = json.loads((ORDNER / "konserve" / "vektoren.json").read_text(encoding="utf-8"))
    tabelle = vektoren["fragen" if ist_frage else "dokumente"]
    unbekannt = [text for text in texte if text not in tabelle]
    if unbekannt:
        raise KeyError(
            f"KONSERVE=1 kennt nur die Beispiele aus dem Kurs, nicht: {unbekannt[0][:60]!r}. "
            "Für eigene Texte brauchst du den Schlüssel (KONSERVE=1 weglassen)."
        )
    return np.array([tabelle[text] for text in texte])


def _modell_aus_konserve() -> FunctionModel:
    """Baut ein Modell, das die aufgezeichneten Antworten abspielt (für `KONSERVE=1`)."""
    antworten = json.loads((ORDNER / "konserve" / "antworten.json").read_text(encoding="utf-8"))

    def antworte(nachrichten: list[ModelMessage], info: AgentInfo) -> ModelResponse:
        prompt = _letzter_prompt(nachrichten)
        mit_regel = "Ich finde dazu nichts" in prompt
        for eintrag in antworten:
            if eintrag["frage"] in prompt and eintrag["mit_regel"] == mit_regel:
                return _antwort(eintrag, info)
        raise KeyError("KONSERVE=1 kennt diese Frage nicht. Lass KONSERVE=1 weg und nutze deinen Schlüssel.")

    return FunctionModel(antworte, model_name="konserve")


def _letzter_prompt(nachrichten: list[ModelMessage]) -> str:
    for nachricht in reversed(nachrichten):
        for teil in reversed(getattr(nachricht, "parts", [])):
            if isinstance(teil, UserPromptPart) and isinstance(teil.content, str):
                return teil.content
    return ""


def _antwort(eintrag: dict, info: AgentInfo) -> ModelResponse:
    """Gibt die Antwort als Text zurück, oder als ausgefüllte Struktur, wenn das Programm eine verlangt."""
    if info.output_tools:
        werkzeug = info.output_tools[0]
        felder = werkzeug.parameters_json_schema.get("properties", {})
        # Felder, die in der Aufzeichnung fehlen, bleiben leer (None).
        argumente = {name: eintrag.get(name) for name in felder}
        return ModelResponse(parts=[ToolCallPart(werkzeug.name, argumente)])
    return ModelResponse(parts=[TextPart(eintrag["text"])])


MODELL = _modell_aus_konserve() if KONSERVE else CHAT_MODELL
