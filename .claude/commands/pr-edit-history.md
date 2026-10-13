---
description: Zeige die Bearbeitungshistorie einer GitHub Pull Request Beschreibung
category: github
allowed-tools: Bash
---

# Pull Request Edit History anzeigen

Rufe die vollständige Bearbeitungshistorie einer Pull Request Beschreibung ab und zeige sie in einer formatierten Tabelle an.

## Verwendung

Standard (interaktiv - fragt nach Parametern):

```bash
/pr-edit-history
```

Mit Parametern:

```bash
/pr-edit-history owner/repo#123
```

Oder einzeln angegeben:

```bash
/pr-edit-history --owner anthropics --repo claude-code --pr 456
```

## Workflow

1. **Parameter ermitteln**:
   - Falls keine Parameter übergeben wurden, frage den Benutzer nach:
     - Repository Owner (z.B. "anthropics")
     - Repository Name (z.B. "claude-code")
     - Pull Request Nummer (z.B. "123")
   - Falls im Format `owner/repo#pr` übergeben, parse die Parameter
   - Falls einzeln übergeben (`--owner`, `--repo`, `--pr`), verwende diese

2. **GitHub GraphQL Query ausführen**:
   - Verwende `gh api graphql` um die Edit-Historie abzurufen
   - Query:
     ```graphql
     query {
       repository(owner: "OWNER", name: "REPO") {
         pullRequest(number: PR_NUMBER) {
           userContentEdits(first: 100) {
             nodes {
               editedAt
               editor {
                 login
               }
             }
           }
         }
       }
     }
     ```

3. **Daten verarbeiten**:
   - Parse die JSON-Response
   - Extrahiere editedAt (Zeitstempel) und editor.login (Benutzername)
   - Sortiere nach Zeitstempel (älteste zuerst)

4. **Tabelle formatieren**:
   - Erstelle eine Markdown-Tabelle mit folgenden Spalten:
     - `#` (fortlaufende Nummer)
     - `Edited At (UTC)` (Zeitstempel in lesbarem Format)
     - `Editor` (Benutzername)
   - Formatiere Zeitstempel als: `YYYY-MM-DD HH:MM:SS`
   - Beispiel:
     ```
     | #  | Edited At (UTC)     | Editor    |
     |----|---------------------|-----------|
     | 1  | 2025-12-01 00:08:34 | dsenften  |
     | 2  | 2025-12-01 15:57:21 | dsenften  |
     | 3  | 2025-12-01 16:24:33 | dsenften  |
     ```

5. **Ausgabe**:
   - Zeige die Tabelle an
   - Füge Zusammenfassung hinzu:
     - Gesamtanzahl der Edits
     - Zeitspanne (erste bis letzte Bearbeitung)
     - Liste der Editoren (eindeutig)

## Fehlerbehandlung

- **gh CLI nicht installiert**: Melde dem Benutzer, dass `gh` CLI installiert werden muss
- **Nicht authentifiziert**: Hinweis auf `gh auth login`
- **Repository nicht gefunden**: Überprüfe Owner und Repo-Name
- **PR nicht gefunden**: Überprüfe PR-Nummer
- **Keine Edit-Historie**: Melde, dass die PR-Beschreibung nie bearbeitet wurde
- **Mehr als 100 Edits**: Hinweis, dass nur die ersten 100 angezeigt werden

## Beispiele

### Beispiel 1: Interaktive Verwendung
```bash
/pr-edit-history
# Fragt nach: Owner? Repo? PR-Nummer?
# Zeigt Tabelle an
```

### Beispiel 2: Mit kompakter Syntax
```bash
/pr-edit-history anthropics/claude-code#789
```

### Beispiel 3: Mit expliziten Parametern
```bash
/pr-edit-history --owner anthropics --repo claude-code --pr 789
```

## Erweiterte Optionen

Optional kann der Benutzer zusätzliche Optionen angeben:

- `--limit N`: Begrenze auf die letzten N Edits (Standard: alle bis 100)
- `--json`: Ausgabe als JSON statt Tabelle
- `--export FILE`: Exportiere Tabelle in Datei (Markdown oder CSV)

## Technische Details

- **GraphQL API**: Verwendet GitHub GraphQL API v4
- **Rate Limits**: Beachtet GitHub API Rate Limits (5000 Anfragen/Stunde für authentifizierte Anfragen)
- **Authentifizierung**: Verwendet die Authentifizierung der `gh` CLI
- **Zeitzone**: Alle Zeitstempel werden in UTC angezeigt

## Hinweise

- Die erste Erstellung der PR-Beschreibung zählt nicht als Edit
- Nur manuelle Bearbeitungen werden angezeigt (keine automatischen Updates)
- Bot-Edits (z.B. durch GitHub Actions) werden ebenfalls angezeigt
