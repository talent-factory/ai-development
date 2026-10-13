---
name: professional-commit-workflow
description: Creates professional Git commits with automated quality checks, Emoji Conventional Commits, and German imperative messages. Use when the user runs /commit --with-skills or asks for a professional commit workflow.
category: development
allowed-tools:
  - Bash
  - Read
  - Glob
  - Write
  - Edit
---

# Professional Commit Workflow

Erstellt professionelle Git-Commits mit automatisierten Qualitätschecks, korrekter Staging-Analyse und Emoji Conventional Commits. Alle Commit-Nachrichten sind auf Deutsch verfasst.

## Auslöser

- Benutzer führt `/commit --with-skills` aus.
- Benutzer fragt nach einem professionellen Commit-Workflow.
- Benutzer möchte einen Commit mit automatischen Checks erstellen.

## Optionen

| Option | Bedeutung |
|--------|-----------|
| `--no-verify` | Pre-Commit-Checks überspringen |
| `--force-push` | Force-Push ausführen (mit Warnung) |
| `--skip-tests` | Testausführung überspringen |
| `--with-skills` | Diesen Skill aktivieren |

## Workflow

### 1. Projekt erkennen

Führe im Repository-Root aus:

```bash
git rev-parse --show-toplevel
```

Erkenne den Projekttyp anhand der Dateien:

| Projekttyp | Erkennungsmerkmale |
|------------|--------------------|
| Python | `pyproject.toml`, `setup.py`, `requirements.txt`, `uv.lock`, `Pipfile` |
| Java | `pom.xml`, `build.gradle`, `build.gradle.kts` |
| React/Node.js | `package.json`, `vite.config.*`, `next.config.*`, `tsconfig.json` |
| Docs | `README.md`, `*.md`, `*.tex`, `*.adoc`, `docs/` |

### 2. Pre-Commit-Checks (überspringen mit `--no-verify`)

Führe je nach Projekttyp die passenden Checks aus:

**Python**
- `ruff check .` oder `uv run ruff check .`
- `ruff format --check .` oder `uv run ruff format --check .`
- `mypy .` oder `uv run mypy .` (falls konfiguriert)
- `pytest` oder `uv run pytest` (außer `--skip-tests`)

**Java**
- Maven: `./mvnw verify -DskipTests` (oder mit Tests, wenn nicht `--skip-tests`)
- Gradle: `./gradlew check` (oder `build`)

**React/Node.js**
- `npm run lint` oder `pnpm lint`
- `npm run typecheck` (falls vorhanden)
- `npm run test` (außer `--skip-tests`)

**Docs**
- Markdown-Link-Check, falls vorhanden
- LaTeX-Build, falls vorhanden

Bei Fehlern: Breche ab, zeige die Fehlerausgabe und schlage eine Behebung vor.

### 3. Staging-Analyse

```bash
git status --short
```

- Zeige eine übersichtliche Liste der geänderten, neuen und gelöschten Dateien.
- Falls keine Dateien gestaged sind, frage den Benutzer, ob alle Änderungen automatisch gestaged werden sollen (`git add .`).
- Falls `--no-verify` gesetzt ist, trotzdem `git status` anzeigen.

### 4. Diff-Analyse

```bash
git diff --cached --stat
git diff --cached
```

- Analysiere den Umfang der Änderungen.
- Erkenne mehrere logische Änderungen (z. B. Feature + Refactoring + Docs).
- Schlage bei gemischten Änderungen eine Aufteilung in mehrere Commits vor.
- Falls der Benutzer ablehnt, fahre mit einem zusammenfassenden Commit fort.

### 5. Commit-Typ ermitteln

Wähle den Typ basierend auf den geänderten Dateien und dem Diff:

| Emoji | Typ | Wann verwenden |
|-------|-----|----------------|
| ✨ | `feat` | Neue Funktionalität |
| 🐛 | `fix` | Bugfix |
| 📚 | `docs` | Dokumentation |
| 💎 | `style` | Formatierung, keine Logikänderung |
| ♻️ | `refactor` | Code-Restrukturierung |
| ⚡ | `perf` | Performance-Verbesserung |
| 🧪 | `test` | Tests hinzufügen/fixen |
| 🔧 | `chore` | Build, Tools, Konfiguration |
| 🚀 | `ci` | CI/CD-Änderungen |
| 🔒 | `security` | Sicherheitsrelevante Änderungen |
| 🗑️ | `remove` | Code/Dateien entfernen |
| 🐎 | `build` | Build-System oder externe Abhängigkeiten |

Heuristiken:
- `test/` oder `*_test.py`, `*.test.ts` → `test`
- `README.md`, `docs/`, `*.md` ohne Code-Änderungen → `docs`
- `package.json`, `pyproject.toml`, `Makefile`, `.github/workflows/` → `chore` oder `ci`/`build`
- Nur Formatierungsänderungen → `style`
- Imports neu sortiert, Variablen umbenannt, Code verschoben ohne Verhaltensänderung → `refactor`
- Neue Dateien mit Geschäftslogik → `feat`
- Fehlerbehebung → `fix`

### 6. Scope ermitteln

Leite einen optionalen Scope aus dem Projekt ab:

- Python-Paket-Name oder Hauptmodul
- React-Komponentenbereich (`components`, `api`, `ui`)
- `docs`, `ci`, `build`, `tests`

Falls kein eindeutiger Scope erkennbar ist, lasse ihn weg.

### 7. Commit-Nachricht erstellen

Format:

```text
<emoji> <type>(<scope>): <deutsche imperative Beschreibung>

<body>

<footer>
```

Regeln:
- Beschreibung auf Deutsch, imperativ, klein geschrieben, ohne Punkt am Ende.
- Länge der ersten Zeile maximal 72 Zeichen.
- Body optional, aber sinnvoll bei komplexen Änderungen.
- Keine Suffixe wie `Generated with Claude Code` oder `Co-Authored-By`.
- Keine Meta-Informationen, die nicht zum Inhalt gehören.

Beispiele:

```text
✨ feat(api): Endpunkt für Benutzerregistrierung hinzufügen

Implementiert POST /users mit Validierung und Tests.
```

```text
🐛 fix(parser): Leerzeichen in CSV-Zeilen korrekt behandeln
```

```text
📚 docs(readme): Installationsanleitung aktualisieren
```

### 8. Benutzer bestätigen lassen

Zeige die vorgeschlagene Commit-Nachricht und eine Zusammenfassung der gestageden Dateien. Erlaube dem Benutzer:

- Nachricht zu akzeptieren
- Nachricht zu bearbeiten
- Commit abzubrechen

### 9. Commit erstellen

```bash
git commit -m "<message>"
```

Falls `--no-verify` gesetzt:

```bash
git commit --no-verify -m "<message>"
```

### 10. Optional: Push anbieten

Frage den Benutzer, ob er den Commit pushen möchte:

```bash
git push
```

Falls `--force-push` gesetzt:

```bash
git push --force-with-lease
```

## Wichtige Hinweise

- Füge niemals automatische Suffixe wie `Generated with Claude Code` oder `Co-Authored-By` hinzu.
- Halte die erste Zeile kurz und prägnant.
- Teile gemischte Änderungen in mehrere Commits auf, wenn es sinnvoll ist.
- Respektiere `--no-verify` und `--skip-tests`, aber dokumentiere die Entscheidung.
- Verwende ausschließlich die definierten Emoji Conventional Commit-Typen.
