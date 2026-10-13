---
description: Validiert Command-Dateien, Dokumentation und Best Practices
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Command Validation Tool

Dieser Command validiert Claude Code Commands auf:

- YAML-Frontmatter Struktur
- Markdown-Syntax
- Dokumentation
- Best Practices (Progressive Disclosure, Naming Conventions)

## Usage

```bash
# Spezifischen Command prüfen
/check-commands agents/_shared/commands/commit.md

# Oder ohne Pfad für interaktive Auswahl
/check-commands
```

## Validierungs-Checks

### 1. YAML-Frontmatter

**Required**:

- `description` (String, 1-100 Zeichen)
- `category` (String, muss existierendem Ordner entsprechen)

**Optional**:

- `allowed-tools` (Array von Tool-Namen)

**Format**:

```yaml
---
description: Kurze Beschreibung des Commands
category: develop
allowed-tools:
  - Read
  - Write
---
```

### 2. Markdown-Struktur

- Muss mit Frontmatter beginnen
- Mindestens eine H1-Überschrift (`# Titel`)
- Valides CommonMark-Format
- Keine kaputten Links zu Detail-Dateien

### 3. Dokumentation

**Für umfangreiche Commands (Progressive Disclosure)**:

- Detail-Dateien in `references/<command-name>/`
- Referenzen im Haupt-Command auf Detail-Dateien via `../references/`

**Beispiel-Struktur**:

```text
_shared/
├── commands/
│   └── commit.md                    # Haupt-Command
└── references/
    └── commit/                      # Detail-Ordner
        ├── pre-commit-checks.md
        ├── commit-types.md
        ├── best-practices.md
        └── troubleshooting.md
```

### 4. Best Practices

**Naming Conventions**:

- ✅ Lowercase mit Bindestrichen: `check-commands.md`
- ❌ CamelCase oder Unterstriche: `checkCommands.md`, `check_commands.md`

**Progressive Disclosure**:

- Haupt-Command: 50-250 Zeilen (Übersicht + Workflow)
- Details: In separaten Dateien ausgelagert
- Referenzen: Links zu Detail-Dateien am Ende

**Description**:

- Kurz und prägnant (1-100 Zeichen)
- Beschreibt WAS der Command tut
- Imperativ-Form: "Erstellt..." nicht "Erstelle..."
- **Sprache: Deutsch** (technische Begriffe auf Englisch erlaubt)

**Dokumentation (Markdown-Body)**:

- **Primär auf Deutsch** verfasst
- Technische Begriffe können auf Englisch bleiben
- Fachbegriffe auf Englisch erlaubt
- Konsistente Sprache innerhalb eines Commands

## Validierungs-Workflow

Wenn du diesen Command ausführst, solltest du:

1. **Command-Pfad ermitteln**:
   - Falls kein Pfad angegeben: Alle `.md`-Dateien in `agents/_shared/commands/` listen
   - User wählt Command aus

2. **Datei einlesen**:
   - Read-Tool verwenden
   - Prüfen ob Datei existiert

3. **YAML-Frontmatter parsen**:
   - Ersten Block zwischen `---` extrahieren
   - Required-Felder prüfen: `description`
   - Optional-Felder validieren: `allowed-tools`
   - Format-Validierung (keine Syntax-Fehler)

4. **Markdown validieren**:
   - Mindestens eine H1-Überschrift vorhanden
   - Keine kaputten internen Links
   - Grundlegende CommonMark-Struktur

5. **Dokumentations-Check**:
   - Falls Command > 250 Zeilen: Warnung für Progressive Disclosure
   - Falls References existieren: Prüfe `../references/<command>/`
   - Falls Referenzen vorhanden: Existenz der Dateien prüfen

6. **Best Practices Check**:
   - Dateiname: Lowercase mit Bindestrichen
   - Description: 1-100 Zeichen

7. **Report ausgeben**:

   ```markdown
   ## Validation Report: /commit

   ✅ YAML-Frontmatter: Valid
   ✅ Markdown-Struktur: Valid
   ✅ Dokumentation: Complete
   ✅ Best Practices: Compliant
   ✅ Progressive Disclosure: Implemented (85 lines main, 1246 lines details)

   ### Details:
   - Description: "Erstellt professionelle Git-Commits..." (Valid length)
   - Detail files: 4 found in references/commit/ (all referenced ✓)
   - Naming: commit.md (compliant ✓)

   ✨ Command is fully compliant!
   ```

   Bei Problemen:

   ```markdown
   ## Validation Report: /example

   ❌ YAML-Frontmatter: Missing 'description' field
   ⚠️  Markdown-Struktur: No H1 heading found
   ✅ Best Practices: Compliant
   ⚠️  File size: 312 lines - consider Progressive Disclosure

   ### Issues to fix:
   1. Add 'description' field to YAML frontmatter
   2. Add H1 heading (# Title) at the beginning
   3. Consider splitting into main + detail files (>250 lines)

   ### Recommended actions:
   - Add description: "Brief command description"
   - Add # heading after frontmatter
   - Create detail folder: references/example/
   ```

## Error Handling

- **Datei nicht gefunden**: Klare Fehlermeldung mit Pfad
- **YAML-Parse-Fehler**: Zeige Zeile und Fehler
- **Fehlende Required-Felder**: Liste alle fehlenden Felder

## Integration mit anderen Commands

Dieser Command ist nützlich:

- **Vor dem Commit**: Commands validieren bevor sie commited werden
- **Nach Änderungen**: Sicherstellen dass alles noch funktioniert
- **Neue Commands**: Initiales Setup überprüfen

## Beispiele

**Erfolgreiche Validierung**:

```text
/check-commands agents/_shared/commands/commit.md
→ ✅ Alle Checks bestanden
```

**Fehlerhafte Validierung**:

```text
/check-commands agents/_shared/commands/broken.md
→ ❌ 3 Issues gefunden (siehe Report)
```

**Interaktive Auswahl**:

```text
/check-commands
→ Zeigt Liste aller Commands
→ User wählt aus
→ Validierung läuft
```

## Notes

- Dieser Command sollte selbst Best Practices folgen ✨
- Kann als Template für andere Validierungs-Commands dienen
- Erweiterbar für zusätzliche Checks (z.B. Security, Performance)
