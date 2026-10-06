---
description: Implementiere Task mit Worktree, Branch-Erstellung und PR (Filesystem oder Linear)
argument-hint: "[task-ID] [--linear]"
allowed-tools:
  - Read
  - Write
  - Edit
  - TodoWrite
  - AskUserQuestion
  - Glob
  - Bash
---

# Implement Task

Automatisierte Umsetzung von Tasks: Worktree erstellen, Branch erstellen (inkl. Submodule), implementieren und Pull Request erstellen.

## Übersicht

Dieser Command orchestriert den kompletten Workflow von Task bis Pull Request:

1. **Task auswählen** - Aus Filesystem oder Linear (via `--linear` Flag)
2. **Worktree erstellen** - In `.worktrees/task-<task-id>/` für parallele Arbeit
3. **Branch erstellen** - Im Hauptrepo und allen Submodulen
4. **Status aktualisieren** - Task auf "In Progress" setzen
5. **Implementierung** - Code-Änderungen basierend auf Task-Beschreibung
6. **PR erstellen** - Pull Request mit Task-Verlinkung
7. **Finalisierung** - Task-Status auf "Completed", Tracking aktualisieren

## Verwendung

```bash
# Filesystem-basiert (Standard)
/implement-task              # Interaktive Auswahl
/implement-task task-001     # Mit Task-ID
/implement-task --plan dark-mode task-003  # Mit Plan-Kontext

# Linear-basiert
/implement-task --linear           # Interaktive Auswahl
/implement-task --linear PROJ-123  # Mit Issue-ID
```

## Provider-Auswahl

### Filesystem (Standard)

**Wann verwenden**: Tasks wurden via `/create-plan` erstellt und liegen in `.plans/*/tasks/`.

**Erwartete Struktur**:
```
.plans/[feature-name]/
├── EPIC.md
├── STATUS.md
└── tasks/
    ├── task-001-*.md
    ├── task-002-*.md
    └── ...
```

### Linear (`--linear`)

**Wann verwenden**: Tasks werden in Linear verwaltet.

**Voraussetzung**: Linear MCP Server muss konfiguriert sein.

```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-linear"],
      "env": { "LINEAR_API_KEY": "<your-api-key>" }
    }
  }
}
```

## Gemeinsamer Workflow

### 1. Task-Identifikation

**Mit Argument**: Task-ID validieren und abrufen
**Ohne Argument**: Verfügbare Tasks auflisten, User wählt interaktiv

### 2. Task-Daten einlesen

Folgende Informationen extrahieren:
- **Titel & Beschreibung** - Für Branch-Name und Kontext
- **Labels/Tags** - Für Commit-Typ-Bestimmung
- **Status** - Muss "pending" / "Backlog" sein
- **Akzeptanzkriterien** - Als Test-Plan-Checkliste
- **Dependencies** - Vor Start prüfen (nur Filesystem)

### 3. Worktree & Branch-Erstellung

> ⚠️ **WICHTIG**: Für paralleles Arbeiten an mehreren Tasks werden Git Worktrees verwendet!

#### Worktree-Konzept

Jeder Task wird in einem eigenen Worktree bearbeitet:
- **Verzeichnis**: `.worktrees/task-<task-id>/`
- **Ermöglicht**: Parallele Arbeit an mehreren Tasks ohne Branch-Wechsel
- **Isoliert**: Jeder Task hat seine eigene Arbeitskopie

#### Workflow

```bash
# 1. Vorbereitungen im Hauptrepo
git fetch origin
git status  # Muss sauber sein

# 2. Worktree-Verzeichnis erstellen (falls nicht vorhanden)
mkdir -p .worktrees

# 3. Branch-Name bestimmen (basierend auf Issue-Type/Labels)
# Labels → Branch-Prefix Mapping:
# - bug, fix → bugfix/<task-id>-<description>
# - feature, enhancement → feature/<task-id>-<description>
# - docs, documentation → docs/<task-id>-<description>
# - refactor → refactor/<task-id>-<description>
# - performance → perf/<task-id>-<description>
# - test → test/<task-id>-<description>
# Default: feature/<task-id>-<description>
BRANCH_NAME="<type>/<task-id>-<description>"

# 4. Worktree mit neuem Branch erstellen
git worktree add -b "$BRANCH_NAME" ".worktrees/task-<task-id>" origin/main

# 5. In Worktree wechseln
cd ".worktrees/task-<task-id>"
```

#### Submodule-Handling

> ⚠️ **Bei Projekten mit Submodulen**: Auch diese müssen in eigene Branches ausgecheckt werden!

```bash
# 1. Im Worktree: Submodule initialisieren
cd ".worktrees/task-<task-id>"
git submodule update --init --recursive

# 2. Für jedes Submodul: Branch erstellen (gleicher Type wie Hauptrepo)
git submodule foreach --recursive '
  git fetch origin
  git checkout -b "<type>/<task-id>-<description>" origin/main
'
```

**Submodule-Check**:
```bash
# Prüfen ob Submodule vorhanden sind
git submodule status
```

#### Branch-Naming

**Format basierend auf Issue-Type/Labels**:

```
<type>/<ISSUE-ID>-<description>
```

**Labels → Branch-Prefix Mapping**:
- `bug`, `fix` → `bugfix/`
- `feature`, `enhancement` → `feature/`
- `docs`, `documentation` → `docs/`
- `refactor` → `refactor/`
- `performance` → `perf/`
- `test` → `test/`
- Default: `feature/`

| Type | Filesystem | Linear |
|------|------------|--------|
| Feature | `feature/task-001-ui-toggle-component` | `feature/proj-123-user-auth` |
| Bug | `bugfix/task-002-login-crash` | `bugfix/proj-124-api-error` |
| Docs | `docs/task-003-api-documentation` | `docs/proj-125-readme-update` |
| Refactor | `refactor/task-004-auth-module` | `refactor/proj-126-db-layer` |

#### Pre-Worktree-Checks

- ✅ Working Directory sauber (git status)
- ✅ Remote ist up-to-date (git fetch)
- ✅ `.worktrees/` existiert oder wird erstellt
- ✅ Worktree existiert noch nicht für diese Task-ID

### 4. Status-Update

| Provider | Transition |
|----------|------------|
| Filesystem | `pending` → `in_progress` in Task-Datei |
| Linear | `Backlog` → `In Progress` via MCP |

### 5. Implementierung

1. **Task-Beschreibung analysieren** - Betroffene Dateien identifizieren
2. **Akzeptanzkriterien als Checklist** - Schritt für Schritt abarbeiten
3. **Code-Änderungen durchführen** - Basierend auf Task-Beschreibung
4. **Tests schreiben** - Unit/Integration Tests für Akzeptanzkriterien

**Labels → Commit-Typ Mapping**:
- `bug`, `fix` → 🐛 fix
- `feature`, `enhancement` → ✨ feat
- `docs`, `documentation` → 📚 docs
- `refactor` → ♻️ refactor
- `performance` → ⚡ perf
- `test` → 🧪 test
- Default: ✨ feat

### 6. PR-Erstellung

PR mit Task-Verlinkung erstellen:
- Titel: Task-Titel
- Body: Beschreibung, Änderungen, Test-Plan
- Labels: Basierend auf Task-Labels

### 7. Finalisierung (OBLIGATORISCH)

> ⚠️ **WICHTIG**: Dieser Schritt ist NICHT optional!

| Provider | Aktionen |
|----------|----------|
| Filesystem | Task-Status → `completed`, STATUS.md aktualisieren |
| Linear | Issue-Status → `In Review` oder `Done` via MCP |

#### Worktree-Cleanup (nach PR-Merge)

Nach erfolgreichem Merge kann der Worktree aufgeräumt werden:

```bash
# Vom Hauptrepo aus
git worktree remove .worktrees/task-<task-id>
git branch -d <type>/<task-id>-<description>  # lokaler Branch

# Bei Submodulen: Branches dort auch löschen (falls nicht gemerged)
```

## Error Handling

- **Task nicht gefunden**: Validierung, Alternativen vorschlagen
- **Worktree existiert bereits**: Warnung, Option zum Wechseln in existierenden Worktree
- **Branch existiert bereits**: Warnung, Option zum Wechseln
- **Submodule-Branch-Konflikt**: Interaktive Auflösung anbieten
- **Dependencies nicht erfüllt** (FS): Liste anzeigen, User-Entscheidung
- **Linear MCP nicht verfügbar**: Fehlermeldung mit Setup-Anleitung

## Detail-Dokumentation

### Allgemein
- **[workflow.md](../references/implement-task/workflow.md)** - Detaillierter Workflow mit Beispielen
- **[best-practices.md](../references/implement-task/best-practices.md)** - Branch-Naming, Commits, PR-Gestaltung
- **[troubleshooting.md](../references/implement-task/troubleshooting.md)** - Häufige Probleme und Lösungen

### Provider-spezifisch
- **[filesystem.md](../references/implement-task/filesystem.md)** - Filesystem-Tasks, STATUS.md
- **[linear.md](../references/implement-task/linear.md)** - Linear MCP Setup, API-Details

## Siehe auch

- **[/create-plan](./create-plan.md)** - Projektplanung (Filesystem/Linear)
- **[/commit](./commit.md)** - Professionelle Git-Commits
- **[/create-pr](./create-pr.md)** - Pull Request-Erstellung

---

**Arguments**: $ARGUMENTS

