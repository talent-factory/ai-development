---
description: Erstelle einen neuen Branch, committe Änderungen und erstelle einen Pull Request mit automatischer Commit-Aufteilung
category: develop
allowed-tools:
  - "Bash(git *)"
  - "Bash(gh *)"
  - "Bash(biome *)"
  - Read
  - Glob
---

# Claude Command: Pull Request erstellen

Erstelle automatisch einen neuen Branch, analysiere Änderungen und erstelle einen professionellen Pull Request.

**Alle Commit-Nachrichten und PR-Beschreibungen werden in Deutsch verfasst.**

## Verwendung

Standard-Pull-Request:

```bash
/create-pr
```

Mit Optionen:

```bash
/create-pr --draft          # Erstellt Draft-PR
/create-pr --no-format      # Überspringt Code-Formatierung
/create-pr --single-commit  # Alle Änderungen in einem Commit
/create-pr --target main    # Ziel-Branch angeben (Standard: main)
/create-pr --with-skills    # Erstelle einen Pull Request mit professional-pr-workflow
```

## Workflow

### Bei `--with-skills` Option

Wenn `--with-skills` verwendet wird, wird der **professional-pr-workflow Skill** aktiviert und der restliche Command-Workflow wird ignoriert:

1. **Skill-Ausführung**: Nutze den professional-pr-workflow Skill
   - Location: `../skills/professional-pr-workflow/`
   - Features: Intelligentes Branch-Management, Code-Formatierung, GitHub CLI Integration
   - Integration mit professional-commit-workflow für Commits

2. **Skill-Details**: Siehe [professional-pr-workflow README](../skills/professional-pr-workflow/README.md)

### Standard Workflow (ohne `--with-skills`)

1. **Branch-Status prüfen** ⚠️ WICHTIG
   - Prüfe aktuellen Branch: `git branch --show-current`
   - **Geschützte Branches** (`main`, `master`, `develop`):
     - ➡️ Neuer Branch MUSS erstellt werden
     - Keine Commits direkt auf geschützten Branches
   - **Feature-Branch** (z.B. `feature/xyz`, `bugfix/abc`):
     - ➡️ Kein neuer Branch nötig, verwende aktuellen Branch
   - Details: [commit-workflow.md](../references/create-pr/commit-workflow.md)

2. **Änderungen prüfen**
   - Erkenne uncommitted oder bereits committete Änderungen
   - Falls uncommitted Changes → Rufe `/commit` auf
   - Falls Commits vorhanden → Verwende diese
   - Details: [commit-workflow.md](../references/create-pr/commit-workflow.md)

3. **Branch erstellen** (nur wenn auf geschütztem Branch)
   - Generiere aussagekräftigen Branch-Namen: `<type>/<description>-<date>`
   - Prüfe auf bestehende Branches
   - Erstelle Branch vom aktuellen HEAD
   - Beispiel: `feature/user-dashboard-2024-10-30`
   - **Überspringe** wenn bereits auf Feature-Branch

4. **Code-Formatierung** (optional mit `--no-format` überspringen)
   - **JavaScript/TypeScript**: Biome
   - **Python**: Black, isort, Ruff
   - **Java**: Google Java Format
   - **Markdown**: markdownlint
   - Details: [code-formatting.md](../references/create-pr/code-formatting.md)

5. **Pull Request erstellen**
   - Push Branch zum Remote
   - Generiere aussagekräftigen PR-Titel
   - Erstelle detaillierte PR-Beschreibung mit Test-Plan
   - Verlinke relevante Issues
   - Setze passende Labels
   - Template: [pr-template.md](../references/create-pr/pr-template.md)

## Integration mit /commit

**Wichtig**: Dieser Command erstellt KEINE eigenen Commits!

- **Uncommitted Changes**: Ruft `/commit` auf
- **Bestehende Commits**: Verwendet diese für PR
- **Keine Commit-Duplikation**: Commit-Logik nur in `/commit`

**Workflow-Details**: [commit-workflow.md](../references/create-pr/commit-workflow.md)

## PR-Template

```markdown
## Beschreibung

[Kurze Beschreibung der Änderungen]

## Änderungen

- Änderung 1
- Änderung 2

## Test-Plan

- [ ] Manuelle Tests durchgeführt
- [ ] Automatische Tests laufen durch
- [ ] Code-Review bereit

## Breaking Changes

[Falls vorhanden]
```

**Vollständiges Template**: [pr-template.md](../references/create-pr/pr-template.md)

## Best Practices

- **Aussagekräftige Titel**: Beschreibe das "Was" in 50 Zeichen
- **Detaillierte Beschreibung**: Erkläre das "Warum" und "Wie"
- **Self-Review**: Prüfe eigene Änderungen vor Submission
- **Kleine PRs**: Halte PRs fokussiert und reviewbar (150-400 Zeilen)
- **Klare Commits**: Jeder Commit sollte eigenständig verständlich sein

**Weitere Best Practices**: [pr-template.md](../references/create-pr/pr-template.md)

## Professional PR Workflow Skill

Die `--with-skills` Option nutzt den **professional-pr-workflow Skill** für verbesserte Performance und erweiterte Features.

### Vorteile vs. Standard Command

| Feature | Standard Command | Skill (`--with-skills`) |
|---------|------------------|------------------------|
| Performance | Standard | ✅ Optimiert |
| Branch-Management | Manuell | ✅ Intelligent |
| Code-Formatierung | Optional | ✅ Integriert |
| GitHub CLI | Manuell | ✅ Automatisiert |
| Draft-PR Support | Basic | ✅ Erweitert |
| Dependencies | Python | ✅ Zero Dependencies |

### Skill Features

- **Intelligentes Branch-Management**: Automatische Branch-Erstellung mit aussagekräftigen Namen
- **Integration mit professional-commit-workflow**: Nahtlose Commit-Integration
- **Code-Formatierung**: Biome, Black, Prettier, Google Java Format
- **GitHub CLI Integration**: Automatische PR-Erstellung mit Labels und Templates
- **Draft-PR Support**: Erweiterte Draft-PR Funktionalität
- **Zero Python Dependencies**: Nur Python Standard Library

### Skill Verwendung

```bash
# Direkte Skill-Ausführung (Alternative)
cd ../skills/professional-pr-workflow
python scripts/main.py

# Oder via Command mit --with-skills
/create-pr --with-skills
```

**Skill-Dokumentation**: [professional-pr-workflow/README.md](../skills/professional-pr-workflow/README.md)

## Weitere Informationen

- **Code-Formatierung**: [code-formatting.md](../references/create-pr/code-formatting.md)
- **Commit-Workflow**: [commit-workflow.md](../references/create-pr/commit-workflow.md)
- **PR-Template & Best Practices**: [pr-template.md](../references/create-pr/pr-template.md)
- **Troubleshooting**: [troubleshooting.md](../references/create-pr/troubleshooting.md)
