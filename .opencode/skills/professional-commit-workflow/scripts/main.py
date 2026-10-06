#!/usr/bin/env python3
"""
Professional Commit Workflow

Erstellt professionelle Git-Commits mit automatisierten Checks und
Emoji Conventional Commits. Alle Nachrichten sind auf Deutsch verfasst.

Usage:
    python main.py [--no-verify] [--skip-tests] [--force-push] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

CONFIG_PATH = Path(__file__).parent.parent / "config.json"


def load_config() -> dict[str, Any]:
    """Lädt die Skill-Konfiguration."""
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def run_command(
    cmd: list[str],
    cwd: Path | None = None,
    check: bool = False,
    capture: bool = True,
) -> subprocess.CompletedProcess[str]:
    """Führt einen Shell-Befehl aus und gibt das Ergebnis zurück."""
    return subprocess.run(
        cmd,
        cwd=cwd,
        check=check,
        capture_output=capture,
        text=True,
    )


def get_repo_root() -> Path:
    """Ermittelt das Repository-Root."""
    result = run_command(["git", "rev-parse", "--show-toplevel"], check=True)
    return Path(result.stdout.strip())


def detect_project_types(root: Path, config: dict[str, Any]) -> list[str]:
    """Erkennt die Projekttypen anhand der Marker-Dateien."""
    detected: list[str] = []
    for project_type, project_config in config["project_types"].items():
        markers = project_config.get("markers", [])
        for marker in markers:
            if marker.startswith("*"):
                # Glob-Muster
                if list(root.glob(marker)):
                    detected.append(project_type)
                    break
            elif (root / marker).exists():
                detected.append(project_type)
                break
    return detected or ["docs"]


def command_exists(name: str) -> bool:
    """Prüft, ob ein Kommando im PATH verfügbar ist."""
    return shutil.which(name) is not None


def has_uv_env(root: Path) -> bool:
    """Prüft, ob uv im Projekt verwendet wird."""
    return (root / "uv.lock").exists() or (root / "pyproject.toml").exists()


def run_check(cmd: list[str], root: Path, use_uv: bool = False) -> tuple[bool, str]:
    """Führt einen einzelnen Check aus und gibt (ok, output) zurück."""
    if use_uv and command_exists("uv"):
        full_cmd = ["uv", "run"] + cmd
    else:
        full_cmd = cmd

    if not command_exists(full_cmd[0]):
        return True, f"{full_cmd[0]} nicht gefunden, überspringe Check"

    result = run_command(full_cmd, cwd=root)
    ok = result.returncode == 0
    output = result.stdout + result.stderr
    return ok, output


def run_pre_commit_checks(
    root: Path,
    project_types: list[str],
    config: dict[str, Any],
    skip_tests: bool,
    no_verify: bool,
) -> bool:
    """Führt die Pre-Commit-Checks aus."""
    if no_verify:
        print("⏭️  Pre-Commit-Checks aufgrund von --no-verify übersprungen.")
        return True

    print("🔍 Führe Pre-Commit-Checks aus...")
    all_ok = True

    for project_type in project_types:
        project_config = config["project_types"].get(project_type, {})
        checks = project_config.get("checks", {})
        use_uv = project_type == "python" and has_uv_env(root)

        for check_name, check_cmd in checks.items():
            if skip_tests and "test" in check_name.lower():
                print(f"⏭️  {check_name} aufgrund von --skip-tests übersprungen.")
                continue

            print(f"  ▸ {check_name}...", end=" ")
            ok, output = run_check(check_cmd, root, use_uv=use_uv)
            if ok:
                print("✅")
            else:
                print("❌")
                print(output)
                all_ok = False

    if not all_ok:
        print("\n❌ Pre-Commit-Checks fehlgeschlagen. Behebe die Fehler vor dem Commit.")
        return False

    print("✅ Alle Pre-Commit-Checks bestanden.\n")
    return True


def git_status(root: Path) -> list[tuple[str, str]]:
    """Gibt den Git-Status als Liste von (status, datei) zurück."""
    result = run_command(["git", "status", "--short"], cwd=root)
    entries: list[tuple[str, str]] = []
    for line in result.stdout.strip().splitlines():
        if not line:
            continue
        status = line[:2].strip()
        file_path = line[3:].strip()
        entries.append((status, file_path))
    return entries


def stage_all(root: Path) -> None:
    """Staged alle Änderungen."""
    run_command(["git", "add", "--all"], cwd=root, check=True)


def get_staged_diff(root: Path, stat_only: bool = False) -> str:
    """Holt den gestageden Diff."""
    cmd = ["git", "diff", "--cached"]
    if stat_only:
        cmd.append("--stat")
    result = run_command(cmd, cwd=root)
    return result.stdout


def classify_change(status: str) -> str:
    """Klassifiziert eine Statusänderung für die Anzeige."""
    mapping = {
        "M": "geändert",
        "A": "neu",
        "D": "gelöscht",
        "R": "umbenannt",
        "C": "kopiert",
        "U": "aktualisiert",
        "??": "unversioniert",
        "MM": "geändert (Index+Worktree)",
        "AM": "neu (Index+Worktree)",
        "AD": "neu (Index, gelöscht Worktree)",
        "MD": "geändert (Index, gelöscht Worktree)",
        " T": "Typänderung",
        "T ": "Typänderung (Index)",
    }
    return mapping.get(status, status)


def detect_commit_type(
    files: list[tuple[str, str]],
    diff: str,
    config: dict[str, Any],
) -> str:
    """Ermittelt den wahrscheinlichsten Commit-Typ anhand von Heuristiken."""
    heuristics = config.get("type_heuristics", {})
    scores: dict[str, int] = {key: 0 for key in heuristics}
    scores["feat"] = 0
    scores["fix"] = 0
    scores["refactor"] = 0

    has_code_changes = False
    has_only_docs = True
    has_only_tests = True
    has_only_formatting = True

    code_extensions = {".py", ".js", ".ts", ".tsx", ".java", ".go", ".rs", ".c", ".cpp"}

    for status, path in files:
        ext = Path(path).suffix.lower()
        if ext in code_extensions:
            has_code_changes = True
            has_only_docs = False
            has_only_tests = False
        if ext in {".md", ".rst", ".tex", ".adoc"}:
            has_only_tests = False
        else:
            has_only_docs = False

        for commit_type, rules in heuristics.items():
            patterns = rules.get("file_patterns", [])
            for pattern in patterns:
                if pattern.endswith("/"):
                    if pattern.rstrip("/") in path.split("/"):
                        scores[commit_type] += 2
                elif re.search(pattern.replace("*", ".*").replace("?", "."), path):
                    scores[commit_type] += 2

        # Add/Modify-Status
        if status in {"A", "??"}:
            scores["feat"] += 1
        if status == "D":
            scores["remove"] = scores.get("remove", 0) + 3

    # Diff-basierte Heuristiken
    if diff:
        lower_diff = diff.lower()
        if re.search(r"\bfix\b|\bbugfix\b|\bbug\b", lower_diff):
            scores["fix"] += 3
        if re.search(r"\btest\b|\btests\b", lower_diff):
            scores["test"] += 1
        if re.search(r"\brefactor\b|\brename\b|\bmove\b", lower_diff):
            scores["refactor"] += 2

    # Nur Docs
    if has_only_docs and scores.get("docs", 0) > 0:
        return "docs"

    # Nur Tests
    if has_only_tests and scores.get("test", 0) > 0:
        return "test"

    # Nur Formatierung erkennen (sehr eingeschränkt, da Diff-Analyse komplex ist)
    if has_only_formatting and not has_code_changes:
        # Platzhalter: könnte Style sein
        pass

    # Besten Typ auswählen
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    if sorted_scores[0][1] > 0:
        return sorted_scores[0][0]

    return "feat" if any(status in {"A", "??"} for status, _ in files) else "fix"


def detect_scope(files: list[tuple[str, str]], project_types: list[str], root: Path) -> str | None:
    """Versucht, einen passenden Scope zu ermitteln."""
    # Docs-Scope
    if all(Path(p).suffix in {".md", ".rst", ".tex", ".adoc"} for _, p in files):
        return "docs"

    # CI-Scope
    if any(".github/workflows" in p or ".gitlab-ci" in p for _, p in files):
        return "ci"

    # Tests-Scope
    if any("test" in p.lower() for _, p in files):
        return "tests"

    # Python-Modul aus pyproject.toml
    if "python" in project_types and (root / "pyproject.toml").exists():
        content = (root / "pyproject.toml").read_text(encoding="utf-8")
        match = re.search(r'^\[project\]\s*\n(?:.*\n)*?name\s*=\s*"([^"]+)"', content, re.MULTILINE)
        if match:
            return match.group(1)

    # Node-Scope aus package.json
    if "node" in project_types and (root / "package.json").exists():
        data = json.loads((root / "package.json").read_text(encoding="utf-8"))
        return data.get("name")

    # Häufigster Ordner
    dirs = [Path(p).parts[0] for _, p in files if Path(p).parts]
    if dirs:
        from collections import Counter
        most_common = Counter(dirs).most_common(1)[0][0]
        if most_common not in {"src", ".", ""}:
            return most_common

    return None


def build_commit_message(
    commit_type: str,
    scope: str | None,
    description: str,
    config: dict[str, Any],
) -> str:
    """Baut die finale Commit-Nachricht."""
    emoji = config["commit_types"][commit_type]["emoji"]
    scope_part = f"({scope})" if scope else ""
    header = f"{emoji} {commit_type}{scope_part}: {description}"

    max_len = config["commit_message"]["max_header_length"]
    if len(header) > max_len:
        header = header[: max_len - 3].rstrip() + "..."

    return header


def prompt_user(prompt: str, default: str = "") -> str:
    """Fragt den Benutzer interaktiv."""
    if default:
        full_prompt = f"{prompt} [{default}]: "
    else:
        full_prompt = f"{prompt}: "
    try:
        answer = input(full_prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print("\nAbgebrochen.")
        sys.exit(0)
    return answer if answer else default


def confirm(prompt: str, default: bool = True) -> bool:
    """Ja/Nein-Abfrage."""
    suffix = " [J/n]: " if default else " [j/N]: "
    answer = prompt_user(prompt + suffix).lower()
    if not answer:
        return default
    return answer.startswith(("j", "y"))


def sanitize_description(description: str) -> str:
    """Bereinigt die Commit-Beschreibung."""
    description = description.strip()
    # Kleinschreibung am Anfang
    if description:
        description = description[0].lower() + description[1:]
    # Kein Punkt am Ende
    description = description.rstrip(".").rstrip()
    # Verbotene Suffixe entfernen
    forbidden = [
        "Generated with Claude Code",
        "Co-Authored-By",
        "generated-by",
    ]
    for suffix in forbidden:
        description = description.replace(suffix, "").strip()
    return description


def main() -> int:
    parser = argparse.ArgumentParser(description="Professional Commit Workflow")
    parser.add_argument("--no-verify", action="store_true", help="Checks überspringen")
    parser.add_argument("--skip-tests", action="store_true", help="Tests nicht ausführen")
    parser.add_argument("--force-push", action="store_true", help="Force-Push anbieten")
    parser.add_argument("--dry-run", action="store_true", help="Commit nicht erstellen")
    args = parser.parse_args()

    config = load_config()
    root = get_repo_root()
    project_types = detect_project_types(root, config)

    print(f"📁 Repository: {root}")
    print(f"🔎 Erkannte Projekttypen: {', '.join(project_types)}\n")

    # Pre-Commit-Checks
    if not run_pre_commit_checks(
        root, project_types, config, args.skip_tests, args.no_verify
    ):
        return 1

    # Staging-Analyse
    status_entries = git_status(root)
    if not status_entries:
        print("✅ Keine Änderungen zum Committen vorhanden.")
        return 0

    print("📋 Geänderte Dateien:")
    staged = [entry for entry in status_entries if entry[0] != "??"]
    unstaged = [entry for entry in status_entries if entry[0] == "??"]

    for status, path in status_entries:
        print(f"  {status:2} {classify_change(status):12} {path}")

    if not staged and unstaged:
        if confirm("Keine Dateien gestaged. Sollen alle Änderungen automatisch gestaged werden?"):
            stage_all(root)
            status_entries = git_status(root)
        else:
            print("❌ Commit abgebrochen. Bitte stage die gewünschten Dateien manuell.")
            return 1

    # Diff-Analyse
    diff_stat = get_staged_diff(root, stat_only=True)
    diff = get_staged_diff(root)

    if diff_stat:
        print("\n📊 Diff-Statistik:")
        print(diff_stat)

    # Commit-Typ ermitteln
    commit_type = detect_commit_type(status_entries, diff, config)
    scope = detect_scope(status_entries, project_types, root)

    # Vorschlag generieren
    suggested_description = ""
    if diff:
        # Einfache Heuristik: erste geänderte Datei als Basis
        first_file = status_entries[0][1]
        suggested_description = f"{Path(first_file).name} anpassen"

    print(f"\n🤖 Vorgeschlagener Commit-Typ: {config['commit_types'][commit_type]['emoji']} {commit_type}")
    if scope:
        print(f"🤖 Vorgeschlagener Scope: {scope}")

    # Benutzer-Eingaben
    chosen_type = prompt_user("Commit-Typ", commit_type).strip() or commit_type
    chosen_scope = prompt_user("Scope (optional, Enter für keine)", scope or "").strip()
    chosen_scope = chosen_scope if chosen_scope else None

    description = prompt_user("Beschreibung (deutsch, imperativ)", suggested_description)
    description = sanitize_description(description)
    if not description:
        print("❌ Keine Beschreibung angegeben. Commit abgebrochen.")
        return 1

    message = build_commit_message(chosen_type, chosen_scope, description, config)

    print("\n📝 Commit-Nachricht:")
    print(f"   {message}\n")

    if not confirm("Mit dieser Nachricht committen?"):
        print("❌ Commit abgebrochen.")
        return 0

    if args.dry_run:
        print("🏃 Dry-Run: Kein Commit erstellt.")
        return 0

    # Commit erstellen
    commit_cmd = ["git", "commit"]
    if args.no_verify:
        commit_cmd.append("--no-verify")
    commit_cmd.extend(["-m", message])

    result = run_command(commit_cmd, cwd=root, check=False)
    if result.returncode != 0:
        print("❌ Commit fehlgeschlagen:")
        print(result.stderr)
        return 1

    print("✅ Commit erfolgreich erstellt.")

    # Push anbieten
    if args.force_push:
        if confirm("⚠️  Force-Push ausführen?"):
            push_result = run_command(["git", "push", "--force-with-lease"], cwd=root, check=False)
            if push_result.returncode != 0:
                print("❌ Push fehlgeschlagen:")
                print(push_result.stderr)
                return 1
            print("🚀 Force-Push erfolgreich.")
    else:
        if confirm("Commit pushen?"):
            push_result = run_command(["git", "push"], cwd=root, check=False)
            if push_result.returncode != 0:
                print("❌ Push fehlgeschlagen:")
                print(push_result.stderr)
                return 1
            print("🚀 Push erfolgreich.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
