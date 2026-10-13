# Pre-Commit-Checks

Bevor ein Commit erstellt wird, führt der Workflow automatisch projektspezifische Qualitätschecks aus.

## Übersicht

| Projekttyp | Erkannte Dateien | Ausgeführte Checks |
|------------|------------------|--------------------|
| Python | `pyproject.toml`, `setup.py`, `requirements.txt`, `uv.lock`, `Pipfile` | Ruff, Black/Formatter, mypy, pytest |
| Java | `pom.xml`, `build.gradle`, `build.gradle.kts` | Maven Verify, Gradle Check |
| React/Node.js | `package.json`, `vite.config.*`, `next.config.*` | ESLint, Prettier, TypeScript, Jest/Vitest |
| Docs | `README.md`, `*.md`, `*.tex`, `*.adoc` | Markdown-Link-Check, LaTeX-Build (falls vorhanden) |

## Reihenfolge

1. **Projekt erkennen** anhand der Dateien im Repository-Root.
2. **Linter/Formatter** ausführen.
3. **Typprüfung** ausführen (falls konfiguriert).
4. **Tests** ausführen (außer `--skip-tests`).
5. Bei Fehlern: Workflow abbrechen und Fehlerausgabe anzeigen.

## Python-Projekte

### Ruff

```bash
ruff check .
# oder mit uv
uv run ruff check .
```

### Formatter

```bash
ruff format --check .
# oder mit uv
uv run ruff format --check .
```

### mypy

```bash
mypy .
# oder mit uv
uv run mypy .
```

### pytest

```bash
pytest
# oder mit uv
uv run pytest
```

## Java-Projekte

### Maven

```bash
./mvnw verify
# oder mit Tests überspringen
./mvnw verify -DskipTests
```

### Gradle

```bash
./gradlew check
# oder nur Build
./gradlew build
```

## React/Node.js-Projekte

### ESLint

```bash
npm run lint
# oder
pnpm lint
```

### Prettier

```bash
npm run format:check
# oder
pnpm format:check
```

### TypeScript

```bash
npm run typecheck
# oder
pnpm typecheck
```

### Tests

```bash
npm run test
# oder
pnpm test
```

## Optionen

| Option | Auswirkung |
|--------|------------|
| `--no-verify` | Alle Pre-Commit-Checks überspringen |
| `--skip-tests` | Testausführung überspringen, andere Checks werden trotzdem ausgeführt |

## Empfehlung

Nutze `--no-verify` nur in Ausnahmefällen. Wenn Checks fehlschlagen, sollten die Fehler zuerst behoben werden, bevor committet wird.
