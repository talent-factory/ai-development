# Troubleshooting

## Pre-Commit-Checks schlagen fehl

### Problem

Ruff, ESLint oder ein anderer Check meldet Fehler.

### Lösung

1. Fehlerausgabe lesen und verstehen.
2. Fehler beheben.
3. Check erneut ausführen.
4. Erst dann committen.

Für automatische Formatierung:

```bash
# Python
ruff format .

# Node.js
npm run format
```

## Keine Dateien zum Commit

### Problem

`git status` zeigt keine Änderungen an.

### Lösung

- Änderungen wurden möglicherweise noch nicht gespeichert.
- Neue Dateien müssen mit `git add` gestaged werden.
- Prüfe, ob Dateien in `.gitignore` stehen.

## Commit enthält zu viele Änderungen

### Problem

Ein Commit umfasst mehrere logische Änderungen.

### Lösung

Mit `git reset --soft HEAD~1` den letzten Commit rückgängig machen und die Änderungen in mehrere Commits aufteilen.

```bash
git reset --soft HEAD~1
git add -p
```

## Falsche Commit-Nachricht

### Problem

Die Commit-Nachricht ist ungenau oder enthält verbotene Suffixe.

### Lösung

Letzte Nachricht korrigieren:

```bash
git commit --amend
```

## Push wurde abgelehnt

### Problem

`git push` schlägt aufgrund von Remote-Änderungen fehl.

### Lösung

Zuerst Änderungen vom Remote holen:

```bash
git pull --rebase
```

Danach erneut pushen. Verwende `--force-push` nur, wenn du dir sicher bist.

## `--no-verify` funktioniert nicht

### Problem

Checks werden trotz `--no-verify` ausgeführt.

### Lösung

Stelle sicher, dass `--no-verify` direkt nach `git commit` steht:

```bash
git commit --no-verify -m "Nachricht"
```

## Skill wird nicht geladen

### Problem

`/commit --with-skills` aktiviert den Skill nicht.

### Lösung

- Prüfe, ob `.opencode/skills/professional-commit-workflow/SKILL.md` existiert.
- Starte OpenCode neu.
- Überprüfe die YAML-Frontmatter in `SKILL.md`.
