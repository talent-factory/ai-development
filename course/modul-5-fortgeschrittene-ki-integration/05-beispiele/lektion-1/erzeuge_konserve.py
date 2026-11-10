"""Erzeugt die Konserven in `start/konserve/` (nur für die Dozentin / den Dozenten).

Braucht einen gültigen `GOOGLE_API_KEY` und ruft das echte Modell auf. Aufruf aus dem Ordner
`lektion-1/`:  uv run python erzeuge_konserve.py
"""

import json
import os
import sys
from pathlib import Path

import numpy as np
from pydantic import BaseModel
from pydantic_ai import Agent

START = Path(__file__).parent / "start"
sys.path.insert(0, str(START))
os.environ.pop("KONSERVE", None)

import hilfen  # noqa: E402


class Antwort(BaseModel):
    """Antwort mit Text, Sicherheit (0 bis 1) und Quelle."""

    text: str
    sicherheit: float
    quelle: str | None = None


def baue_prompt(frage: str, quellen: list[hilfen.Dokument], mit_regel: bool) -> str:
    """Setzt den Prompt zusammen wie in Lektion 4: optional Regel, dann Quellen, dann Frage."""
    teile = [hilfen.RAG_REGEL] if mit_regel else []
    teile.append("Quellen:\n" + "\n\n".join(f"[{d.name}]\n{d.text}" for d in quellen))
    teile.append(f"Frage: {frage}")
    return "\n\n".join(teile)


def main() -> None:
    wiki = hilfen.lade_wiki()
    fragen = hilfen.lade_testfragen()
    alle_fragen = [f["frage"] for f in fragen["fragen"]] + [fragen["mehrdeutig"]["frage"], fragen["falle"]]
    saetze = [satz for paar in fragen["satzpaare"] for satz in paar]

    doku_vektoren = hilfen.embed([d.text for d in wiki] + saetze)
    frage_vektoren = hilfen.embed(alle_fragen, ist_frage=True)
    texte = [d.text for d in wiki] + saetze
    vektoren = {
        "dokumente": {t: [round(float(x), 5) for x in v] for t, v in zip(texte, doku_vektoren, strict=True)},
        "fragen": {f: [round(float(x), 5) for x in v] for f, v in zip(alle_fragen, frage_vektoren, strict=True)},
    }

    agent = Agent(hilfen.CHAT_MODELL, output_type=Antwort)
    antworten = []
    ohne_wissen = agent.run_sync(f"{fragen['firmenfrage']} Gib auch an, wie sicher du dir bist (0 bis 1).").output
    antworten.append({"frage": fragen["firmenfrage"], "mit_regel": False, **ohne_wissen.model_dump()})
    for frage, vektor in zip(alle_fragen, frage_vektoren, strict=True):
        beste = np.argsort(-(doku_vektoren[: len(wiki)] @ vektor))[:3]
        quellen = [wiki[i] for i in beste]
        for mit_regel in (True, False):
            ausgabe = agent.run_sync(baue_prompt(frage, quellen, mit_regel)).output
            antworten.append({"frage": frage, "mit_regel": mit_regel, **ausgabe.model_dump()})
            print(
                f"{'MIT ' if mit_regel else 'OHNE'} | {frage} -> {ausgabe.text[:90]!r} (q={ausgabe.quelle}, s={ausgabe.sicherheit})"
            )

    (START / "konserve").mkdir(exist_ok=True)
    (START / "konserve" / "vektoren.json").write_text(json.dumps(vektoren, ensure_ascii=False), encoding="utf-8")
    (START / "konserve" / "antworten.json").write_text(
        json.dumps(antworten, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    print("Ohne Wissen:", ohne_wissen)


if __name__ == "__main__":
    main()
