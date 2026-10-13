---
description: Lint und format alle Python-Dateien im Projekt mit Ruff
---

# Python Code Linting und Formatting mit Ruff

Dieser Workflow führt Ruff Linting und Formatting auf alle Python-Dateien im Projekt aus.

1. Installiere Ruff falls nicht vorhanden (bevorzuge uv wenn verfügbar)

```bash
# Mit uv (bevorzugt)
uv add --dev ruff

# Fallback mit pip
pip install ruff
```

2. Führe Linting auf alle Python-Dateien aus

```bash
ruff check .
```

3. Behebe automatisch behebbare Linting-Probleme

```bash
ruff check --fix .
```

4. Formatiere Code (ersetzt black)

```bash
ruff format .
```

5. Finale Überprüfung - sowohl Linting als auch Formatting

```bash
ruff check . && ruff format --check .
```

## Zusätzliche Optionen

- `ruff check --select E,W` - Nur Fehler und Warnungen
- `ruff check --fix --unsafe-fixes` - Auch unsichere Fixes anwenden
- `ruff format --diff` - Zeige Änderungen ohne sie anzuwenden
- `ruff check --statistics` - Zeige Statistiken über gefundene Probleme
