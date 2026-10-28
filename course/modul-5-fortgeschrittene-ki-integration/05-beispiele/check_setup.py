"""Prüft, ob die Umgebung für Modul 5 bereit ist (Python, uv, Git, Pydantic AI, NumPy, Gemini-Key, Modell- und Embedding-Aufruf)."""

import asyncio
import os
import shutil
import subprocess
import sys
from importlib.metadata import PackageNotFoundError, version

# Werte aus dem Probelauf vom 2026-10-28 (siehe .wayfinder/modul-5/tickets/06-*).
PYDANTIC_AI_VERSION = "2.63.0"
CHAT_MODELL = "google:gemini-3.5-flash-lite"
EMBEDDING_MODELL = "google:gemini-embedding-2"

# Ohne diese Einstellung druckt Pydantic AI bei jedem Start ein mehrzeiliges Banner.
os.environ.setdefault("PYDANTIC_AI_NO_BANNER", "1")


def platzhalter_offen(wert: str) -> bool:
    """Gibt True zurück, wenn ein Wert noch einen Platzhalter (`<…>` oder `x`) enthält."""
    return "<" in wert or wert.endswith(".x")


def ausfuehren(befehl: list[str]) -> str | None:
    """Führt einen Befehl aus und gibt dessen Ausgabe zurück, oder `None` bei einem Fehler."""
    try:
        ergebnis = subprocess.run(befehl, capture_output=True, text=True, timeout=30, check=True)
    except (OSError, subprocess.SubprocessError):
        return None
    return (ergebnis.stdout or ergebnis.stderr).strip()


def pruefe_python() -> bool:
    """Gibt die Python-Version aus (das Projekt verlangt 3.11 oder neuer und startet über `uv run`)."""
    print(f"OK: Python {sys.version_info.major}.{sys.version_info.minor}")
    return True


def pruefe_programm(name: str, versionsbefehl: list[str], hinweis: str) -> bool:
    """Prüft, ob ein Programm gefunden wird, und gibt dessen Version aus."""
    if shutil.which(name) is None:
        print(f"FEHLER: `{name}` nicht gefunden. {hinweis}")
        return False
    ausgabe = ausfuehren(versionsbefehl)
    print(f"OK: {name} {ausgabe.splitlines()[0] if ausgabe else '(Version unbekannt)'}")
    return True


def pruefe_git_identitaet() -> bool:
    """Prüft, ob Git einen Namen und eine E-Mail-Adresse kennt (nötig für Commits)."""
    name = ausfuehren(["git", "config", "user.name"])
    email = ausfuehren(["git", "config", "user.email"])
    if not name or not email:
        print('FEHLER: Git kennt deinen Namen nicht. Setze ihn mit: git config --global user.name "Dein Name"')
        print('  und: git config --global user.email "du@example.com"')
        return False
    print(f"OK: Git-Identität {name}")
    return True


def pruefe_paket(name: str, erwartet: str | None = None) -> bool:
    """Prüft, ob ein Python-Paket installiert ist (und optional, ob die Version stimmt)."""
    try:
        installiert = version(name)
    except PackageNotFoundError:
        print(f"FEHLER: Paket `{name}` fehlt. Installiere es mit dem Befehl aus Schritt 2 der Vorbereitung.")
        return False
    if erwartet and not platzhalter_offen(erwartet) and installiert != erwartet:
        print(f"FEHLER: {name} {installiert} ist installiert, im Kurs gilt {erwartet}.")
        print(f'  Installiere die richtige Version: uv add "{name}[google]=={erwartet}"')
        return False
    print(f"OK: {name} {installiert}")
    return True


def pruefe_schluessel() -> bool:
    """Prüft, ob `GOOGLE_API_KEY` gesetzt ist (ohne den Schlüssel auszugeben)."""
    if not os.environ.get("GOOGLE_API_KEY"):
        print("FEHLER: Die Umgebungsvariable `GOOGLE_API_KEY` ist nicht gesetzt (Vorbereitung, Schritt 4).")
        print("  Öffne nach dem Setzen ein neues Terminal, sonst sieht Python die Variable nicht.")
        return False
    print("OK: GOOGLE_API_KEY ist gesetzt")
    return True


def pruefe_chat_aufruf() -> bool:
    """Schickt eine kurze Frage an das Chat-Modell und prüft, ob eine Antwort kommt."""
    if platzhalter_offen(CHAT_MODELL):
        print(
            "FEHLER: Im Skript steht noch ein Platzhalter für das Chat-Modell (Dozent: bitte vor dem Versand füllen)."
        )
        return False
    try:
        from pydantic_ai import Agent

        antwort = Agent(CHAT_MODELL).run_sync("Antworte mit einem Wort: Hauptstadt der Schweiz?").output
    except Exception as fehler:  # noqa: BLE001 – jede Störung soll als Hinweis erscheinen, nicht als Absturz
        print(f"FEHLER: Der Aufruf von {CHAT_MODELL} ist gescheitert: {type(fehler).__name__}: {str(fehler)[:200]}")
        print("  Prüfe den Schlüssel und die Internetverbindung. Bei «rate limit»: eine Minute warten.")
        return False
    print(f"OK: Chat-Modell antwortet ({antwort.strip()[:40]})")
    return True


def pruefe_embedding_aufruf() -> bool:
    """Berechnet einen Embedding-Vektor und prüft, dass er Zahlen enthält."""
    if platzhalter_offen(EMBEDDING_MODELL):
        print(
            "FEHLER: Im Skript steht noch ein Platzhalter für das Embedding-Modell (Dozent: bitte vor dem Versand füllen)."
        )
        return False
    try:
        from pydantic_ai import Embedder

        ergebnis = asyncio.run(Embedder(EMBEDDING_MODELL).embed_query("Wie läuft ein Deployment ab?"))
        laenge = len(ergebnis.embeddings[0])
    except Exception as fehler:  # noqa: BLE001 – siehe oben
        print(
            f"FEHLER: Der Embedding-Aufruf mit {EMBEDDING_MODELL} ist gescheitert: {type(fehler).__name__}: {str(fehler)[:200]}"
        )
        return False
    print(f"OK: Embedding-Modell antwortet (Vektor mit {laenge} Zahlen)")
    return True


def main() -> None:
    """Gibt für jede Voraussetzung OK oder eine Anleitung zur Behebung aus."""
    ergebnisse = [
        pruefe_python(),
        pruefe_programm("uv", ["uv", "--version"], "Installation: https://docs.astral.sh/uv/"),
        pruefe_programm("git", ["git", "--version"], "Installation: https://git-scm.com/downloads"),
        pruefe_git_identitaet(),
        pruefe_paket("pydantic-ai-slim", PYDANTIC_AI_VERSION),
        pruefe_paket("numpy"),
    ]
    schluessel_ok = pruefe_schluessel()
    ergebnisse.append(schluessel_ok)
    if schluessel_ok and all(ergebnisse):
        ergebnisse += [pruefe_chat_aufruf(), pruefe_embedding_aufruf()]
    else:
        print("HINWEIS: Die Modell-Aufrufe werden erst geprüft, wenn alles darüber OK ist.")
        ergebnisse.append(False)

    print()
    if all(ergebnisse):
        print("Alles bereit für Modul 5.")
    else:
        print("Es gibt noch offene Punkte (siehe FEHLER oben). Melde dich vor dem Kurstag, wenn du nicht weiterkommst.")


if __name__ == "__main__":
    main()
