---
description: Erstelle einen Projektplan aus PRD (Filesystem oder Linear)
category: project
argument-hint: "[--prd <PRD-Pfad>] [--linear] [--interactive]"
allowed-tools:
  - Read
  - Write
  - TodoWrite
  - AskUserQuestion
  - Glob
  - mcp__linear__*
---

# Claude Command: Create Project Plan

Erstelle einen strukturierten Projektplan aus einem PRD-Dokument. Speichere Tasks im Filesystem (`.plans/`) oder in Linear (via `--linear` Flag).

## Rolle & Expertise

Du agierst als **Scrum Master, Product Owner und Entwicklungsleiter** mit folgender Expertise:

- **Akademischer Hintergrund**: MSc in Computer Science
- **Best Practices**: Aktuelle Standards von renommierten Universitäten und Fachhochschulen
- **Agile Methoden**: Scrum, Kanban, User Story Mapping
- **Task-Breakdown**: Atomic, testbare und schätzbare Tasks

## Verwendung

```bash
# Filesystem-basiert (Standard)
/create-plan                         # PRD.md im CWD
/create-plan --prd feature.md        # Spezifisches PRD
/create-plan PRDs/01-rag-system.md   # Direkter Pfad

# Linear-basiert
/create-plan --linear                # PRD.md im CWD
/create-plan --linear --prd feature.md

# Interaktiver Modus
/create-plan --interactive
```

## Provider-Auswahl

### Filesystem (Standard)

**Wann verwenden**: Lokales Projekt ohne Linear, schnelle Iteration, Offline-Arbeit.

**Output-Struktur**:
```
.plans/[feature-name]/
├── EPIC.md          # Feature-Übersicht
├── STATUS.md        # Progress-Tracking
└── tasks/
    ├── task-001-[slug].md
    ├── task-002-[slug].md
    └── ...
```

### Linear (`--linear`)

**Wann verwenden**: Team-Kollaboration, Projekt-Tracking, Integration mit anderen Tools.

**Voraussetzung**: Linear MCP Server konfiguriert:
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

### 1. PRD-Dokument einlesen

- **Standard**: `PRD.md` im aktuellen Verzeichnis
- **Custom**: Über `--prd <Pfad>` oder als direktes Argument
- **Fallback**: Interaktive Nachfrage falls nicht gefunden

**Validierung**:
- PRD-Struktur vollständig?
- Ziele & Erfolgsmetriken definiert?
- Anforderungen priorisiert (MoSCoW)?

### 2. Feature-Namen ableiten

Aus dem PRD einen Feature-Namen in `kebab-case` generieren:

**Beispiele**:
- "Dark Mode Toggle" → `dark-mode-toggle`
- "RAG-basiertes System" → `rag-basiertes-system`
- "User Authentication" → `user-authentication`

### 3. EPIC erstellen

| Provider | Speicherort | Format |
|----------|-------------|--------|
| Filesystem | `.plans/[feature-name]/EPIC.md` | Markdown-Datei |
| Linear | Linear Project/EPIC | API-basiert |

**Duplikat-Check**:
- Prüfe existierende EPICs/Pläne mit gleichem Namen
- Interaktive Bestätigung bei Duplikaten
- Optionen: Überschreiben, anderen Namen, abbrechen

### 4. Task-Breakdown durchführen

Leite aus dem PRD **in sich abgeschlossene Tasks** ab:

**Kriterien für gute Tasks (ATOMIC)**:
- ✅ **A**ctionable: Sofort umsetzbar
- ✅ **T**estable: Akzeptanzkriterien definiert
- ✅ **O**wnable: Für einen Entwickler/Agenten
- ✅ **M**easurable: Story Points (1, 2, 3, 5, 8)
- ✅ **I**ndependent: Minimal Dependencies
- ✅ **C**omplete: In sich abgeschlossen

### 5. Tasks speichern

| Provider | Speicherort | Format |
|----------|-------------|--------|
| Filesystem | `.plans/[feature]/tasks/task-NNN-*.md` | Markdown-Dateien |
| Linear | Linear Issues unter EPIC | API-basiert |

### 6. Status-Tracking erstellen

| Provider | Speicherort | Inhalt |
|----------|-------------|--------|
| Filesystem | `.plans/[feature]/STATUS.md` | Progress, Dependencies-Graph, Next Steps |
| Linear | Linear Dashboard | Automatisch via UI |

### 7. Konsistenz-Check

**Vor dem Speichern**:
- [ ] Keine Duplikate oder Redundanzen
- [ ] Konsistentes Gesamtbild
- [ ] Tasks sind vollständig und umsetzbar
- [ ] Dependencies korrekt verknüpft
- [ ] Priorisierung logisch
- [ ] Story Points realistisch

## Agent-Empfehlungen

Basierend auf Task-Typ werden KI-Agenten empfohlen:

| Task-Typ | Empfohlene Agenten | Verwendung |
|----------|-------------------|------------|
| **Code Review** | `code-reviewer` | Qualitätssicherung |
| **Java Development** | `java-developer` | Spring Boot, Enterprise Java |
| **Python Development** | `python-expert` | Django, FastAPI, Data Science |
| **AI/ML Features** | `ai-engineer` | LLM-Integration, ML-Pipelines |
| **Agent Development** | `agent-expert` | KI-Agenten-Entwicklung |
| **Documentation** | `markdown-syntax-formatter` | Docs, READMEs |
| **Testing** | `test-automator` | Unit/Integration Tests |

**Details**: [agent-mapping.md](../references/create-plan/agent-mapping.md)

## Qualitätskriterien

### Tasks müssen erfüllen:

- [ ] **Präzise Formulierung**: Entwickler können ohne Nachfragen umsetzen
- [ ] **Klare Akzeptanzkriterien**: Testbar und messbar
- [ ] **Dependencies dokumentiert**: Reihenfolge klar
- [ ] **Realistische Schätzung**: Story Points basierend auf Komplexität
- [ ] **Agent-Empfehlung**: Passender KI-Agent vorgeschlagen (falls verfügbar)

### EPIC muss enthalten:

- [ ] **Executive Summary**: Kurze Übersicht
- [ ] **Business Value**: Warum wird das gebaut?
- [ ] **Success Metrics**: Messbare Ziele
- [ ] **Timeline**: Grobe Meilensteine
- [ ] **Dependencies**: Externe Abhängigkeiten

## Duplikat-Vermeidung

**Vor EPIC/Plan-Erstellung**:
1. Suche existierende EPICs/Pläne mit ähnlichem Namen
2. Prüfe aktive Tasks mit überlappenden Anforderungen
3. Interaktive Bestätigung bei Duplikaten:
   - Neu erstellen (anderen Namen wählen)
   - Existierenden erweitern
   - Abbrechen und PRD anpassen

**Vor Task-Erstellung**:
1. Prüfe existierende Tasks im EPIC/Plan
2. Vermeide redundante Aufgaben
3. Merge ähnliche Tasks

## Task-Breakdown Strategien

**Aus funktionalen Anforderungen**:
- Eine Anforderung = Ein oder mehrere Tasks
- Must-Have → Höchste Priorität
- Should/Could-Have → Mittlere/Niedrige Priorität

**Aus nicht-funktionalen Anforderungen**:
- Performance-Tasks separat
- Security-Review als eigene Tasks
- Accessibility nach Feature-Tasks

**Cross-Cutting Concerns**:
- Testing als separate Tasks
- Documentation Tasks
- CI/CD Setup
- Monitoring & Observability

**Details**: [task-breakdown.md](../references/create-plan/task-breakdown.md)

## Best Practices

**DO ✅**:
- PRD vollständig analysieren vor Task-Erstellung
- Atomic Tasks: Eine logische Einheit pro Task
- Klare Akzeptanzkriterien definieren
- Dependencies explizit dokumentieren
- Realistische Schätzungen (T-Shirt Sizing)
- Agent-Empfehlungen basierend auf Expertise
- Duplikat-Check vor Erstellung

**DON'T ❌**:
- Zu große Tasks (> 8 Story Points)
- Vage Beschreibungen ohne Akzeptanzkriterien
- Tasks ohne Priorisierung
- Redundante oder überlappende Tasks
- Dependencies ignorieren
- Linear ohne Duplikat-Check befüllen

**Vollständiger Guide**: [best-practices.md](../references/create-plan/best-practices.md)

## Beispiel-Workflows

### Filesystem (Standard)

```bash
# 1. PRD erstellen
/create-prd "Dark Mode Toggle"

# 2. Plan aus PRD generieren
/create-plan PRD.md

# Output:
# ✅ PRD eingelesen: PRD.md
# ✅ Feature-Name: dark-mode-toggle
# ✅ Verzeichnis: .plans/dark-mode-toggle/
# ✅ EPIC.md erstellt
# ✅ 8 Tasks generiert:
#    - task-001-ui-toggle-component.md (3 SP) [frontend-developer]
#    - task-002-theme-state-management.md (5 SP) [frontend-developer]
#    - ...
# ✅ STATUS.md erstellt mit Dependencies-Graph
# ✅ Total: 21 SP

# 3. Task implementieren
/implement-task task-001
```

### Linear (`--linear`)

```bash
# 1. PRD erstellen
/create-prd "Dark Mode Toggle"

# 2. Plan in Linear generieren
/create-plan --linear --prd PRD.md

# Output:
# ✅ PRD eingelesen: PRD.md
# ✅ EPIC erstellt: "Dark Mode Toggle" (LIN-123)
# ✅ 8 Issues generiert:
#    - LIN-124: UI Toggle Component (3 SP)
#    - LIN-125: Theme State Management (5 SP)
#    - ...
# ✅ Dependencies verknüpft
# ✅ Labels hinzugefügt

# 3. Task implementieren
/implement-task --linear LIN-124
```

## Detail-Dokumentation

### Allgemein
- **[task-breakdown.md](../references/create-plan/task-breakdown.md)** - Task-Sizing, Dependencies, Story Points
- **[agent-mapping.md](../references/create-plan/agent-mapping.md)** - Agent-Empfehlungen pro Task-Typ
- **[best-practices.md](../references/create-plan/best-practices.md)** - Atomic Tasks, Akzeptanzkriterien

### Provider-spezifisch
- **[filesystem.md](../references/create-plan/filesystem.md)** - Verzeichnisstruktur, Templates (EPIC.md, STATUS.md, Task-Dateien)
- **[linear-integration.md](../references/create-plan/linear-integration.md)** - Linear-API, EPIC/Issue-Struktur, Labels

## Siehe auch

- **[/create-prd](./create-prd.md)** - PRD-Erstellung
- **[/implement-task](./implement-task.md)** - Task-Implementation

---

**PRD-Pfad**: $ARGUMENTS
