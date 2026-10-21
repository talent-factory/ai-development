"""Prüft, ob die Umgebung für Modul 4 bereit ist (Python, pytest, Git, Node, OpenCode oder Claude Code, Skills, Modell-Zugang)."""

import shutil
import subprocess
import sys
from pathlib import Path

PFLICHT_SKILLS = ["grilling", "tdd", "diagnosing-bugs", "domain-modeling"]


def ausfuehren(befehl: list[str]) -> str | None:
    """Führt einen Befehl aus und gibt dessen Ausgabe zurück, oder `None` bei einem Fehler."""
    try:
        ergebnis = subprocess.run(befehl, capture_output=True, text=True, timeout=30, check=True)
    except (OSError, subprocess.SubprocessError):
        return None
    return (ergebnis.stdout or ergebnis.stderr).strip()


def pruefe_python() -> bool:
    """Gibt die Python-Version aus (das Projekt verlangt 3.13 und startet über `uv run`)."""
    print(f"OK: Python {sys.version_info.major}.{sys.version_info.minor}")
    return True


def pruefe_pytest() -> bool:
    """Prüft, ob `pytest` importiert werden kann."""
    try:
        import pytest
    except ImportError:
        print("FEHLER: `pytest` fehlt. Installiere es mit:  uv add --dev pytest")
        return False
    print(f"OK: pytest {pytest.__version__}")
    return True


def pruefe_programm(name: str, versionsbefehl: list[str], hinweis: str) -> bool:
    """Prüft, ob ein Programm gefunden wird, und gibt dessen Version aus."""
    if shutil.which(name) is None:
        print(f"FEHLER: `{name}` nicht gefunden. {hinweis}")
        return False
    version = ausfuehren(versionsbefehl)
    print(f"OK: {name} {version.splitlines()[0] if version else '(Version unbekannt)'}")
    return True


def pruefe_git_identitaet() -> bool:
    """Prüft, ob Git einen Namen und eine E-Mail-Adresse kennt (nötig für Commits)."""
    name = ausfuehren(["git", "config", "user.name"])
    email = ausfuehren(["git", "config", "user.email"])
    if not name or not email:
        print('FEHLER: Git kennt deinen Namen nicht. Setze ihn mit:  git config --global user.name "Dein Name"')
        print('        und:  git config --global user.email "du@example.com"')
        return False
    print(f"OK: Git-Identität {name}")
    return True


def pruefe_skills(opencode: bool, claude: bool) -> bool:
    """Prüft die Skills (OpenCode: `.agents/skills/`, Claude Code: Plugin). Ein Werkzeug genügt."""
    ergebnisse = []
    if opencode:
        skills_ordner = Path.cwd() / ".agents" / "skills"
        fehlend = [s for s in PFLICHT_SKILLS if not (skills_ordner / s / "SKILL.md").is_file()]
        if fehlend:
            print(f"FEHLER: OpenCode-Skills fehlen in {skills_ordner}: {', '.join(fehlend)}")
            print("        Starte das Skript im Projektordner und installiere die Skills (Vorbereitung, Schritt 5).")
            ergebnisse.append(False)
        else:
            ergebnisse.append(True)
            print(f"OK: OpenCode-Skills {', '.join(PFLICHT_SKILLS)}")
    if claude:
        plugins = ausfuehren(["claude", "plugin", "list"]) or ""
        if "mattpocock-skills" not in plugins:
            print("FEHLER: Claude-Code-Plugin `mattpocock-skills` fehlt (Vorbereitung, Schritt 5).")
            ergebnisse.append(False)
        else:
            ergebnisse.append(True)
            print("OK: Claude-Code-Plugin mattpocock-skills")
    return any(ergebnisse)


def pruefe_modell_zugang(opencode: bool, claude: bool) -> bool:
    """Prüft, ob mindestens ein Werkzeug einen Modell-Zugang hat."""
    if opencode:
        ausgabe = ausfuehren(["opencode", "auth", "list"]) or ""
        if any(wort in ausgabe for wort in ("stored", "environment")):
            print("OK: OpenCode hat einen Modell-Zugang")
            return True
    if claude:
        ausgabe = ausfuehren(["claude", "auth", "status"]) or ""
        if '"loggedIn": true' in ausgabe:
            print("OK: Claude Code ist angemeldet")
            return True
    if opencode:
        print(
            "HINWEIS: Kein eigener Zugang gespeichert. OpenCode nutzt dann Gratis-Modelle (opencode/glm-5.3-flash-free)."
        )
        print("         Prüfe sie mit dem Probelauf in Schritt 7.")
        return True
    print("FEHLER: Claude Code ist nicht angemeldet. Starte  claude  und melde dich an (oder /login).")
    return False


def main() -> None:
    """Gibt für jede Voraussetzung OK oder eine Anleitung zur Behebung aus."""
    opencode = shutil.which("opencode") is not None
    claude = shutil.which("claude") is not None
    ergebnisse = [
        pruefe_python(),
        pruefe_pytest(),
        pruefe_programm("git", ["git", "--version"], "Installation: https://git-scm.com/downloads"),
        pruefe_git_identitaet(),
        pruefe_programm("node", ["node", "--version"], "Installation: https://nodejs.org (LTS-Version)"),
    ]
    if opencode:
        pruefe_programm("opencode", ["opencode", "--version"], "")
        if not (ausfuehren(["opencode", "--version"]) or "").lstrip("opencode v").startswith("2"):
            print(
                "HINWEIS: Wir verwenden OpenCode 2. Installation:  npm install -g @opencode/cli  (Vorbereitung, Schritt 3)"
            )
    if claude:
        pruefe_programm("claude", ["claude", "--version"], "")
    if not (opencode or claude):
        print("FEHLER: Weder `opencode` noch `claude` gefunden. Installiere eines davon (Vorbereitung, Schritt 3).")
        ergebnisse.append(False)
    else:
        ergebnisse += [pruefe_skills(opencode, claude), pruefe_modell_zugang(opencode, claude)]
    print()
    if all(ergebnisse):
        print("Alles bereit für Modul 4.")
    else:
        print("Es gibt noch offene Punkte (siehe FEHLER oben). Melde dich vor dem Kurstag, wenn du nicht weiterkommst.")


if __name__ == "__main__":
    main()
