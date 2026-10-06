# professional-commit-workflow

Professioneller Git-Commit-Workflow mit automatisierten Pre-Commit-Checks, Emoji Conventional Commits und deutschen Commit-Nachrichten.

## Verwendung

### Über OpenCode Skill

```bash
/commit --with-skills
```

### Direkt als Python-Skript

```bash
cd .opencode/skills/professional-commit-workflow
python scripts/main.py
```

### Optionen

```bash
python scripts/main.py --no-verify      # Checks überspringen
python scripts/main.py --skip-tests     # Tests nicht ausführen
python scripts/main.py --force-push     # Force-Push anbieten
python scripts/main.py --dry-run        # Commit nicht erstellen
```

## Unterstützte Projekttypen

- **Python**: Ruff, Black, pytest, mypy, uv
- **Java**: Maven, Gradle
- **React/Node.js**: ESLint, Prettier, TypeScript, Jest/Vitest
- **Dokumentation**: Markdown, LaTeX, AsciiDoc

## Commit-Typen

| Emoji | Typ | Beschreibung |
|-------|-----|--------------|
| ✨ | `feat` | Neue Funktionalität |
| 🐛 | `fix` | Bugfix |
| 📚 | `docs` | Dokumentation |
| 💎 | `style` | Code-Formatierung |
| ♻️ | `refactor` | Restrukturierung |
| ⚡ | `perf` | Performance |
| 🧪 | `test` | Tests |
| 🔧 | `chore` | Wartung/Konfiguration |
| 🚀 | `ci` | CI/CD |
| 🔒 | `security` | Sicherheit |
| 🗑️ | `remove` | Entfernen |
| 🐎 | `build` | Build-System |

## Konfiguration

Die Datei `config.json` enthält die Mapping-Regeln für Commit-Typen und Projekt-Erkennung. Sie kann bei Bedarf angepasst werden.
