---
description: Erstellt, ergänzt und verbessert Docstrings und Kommentare in Python-Dateien (eine Datei, ein Verzeichnis oder das ganze Projekt)
argument-hint: "[pfad] [--nur-pruefen]"
allowed-tools: Agent, Read, Glob, Bash(git status:*), Bash(ruff:*), Bash(python3 -I .claude/skills/python-docstrings/scripts/check_nur_doku.py:*)
---

Dokumentiere Python-Code nach den Regeln des Skills `python-docstrings`.

Argumente: $ARGUMENTS

## 1. Ziel bestimmen

- Enthält `$ARGUMENTS` `--nur-pruefen`, ist das der Modus «nur prüfen»: Es wird nichts geändert. Entferne das Flag aus dem Pfad.
- **Pfad ist eine `.py`-Datei:** genau diese Datei.
- **Pfad ist ein Verzeichnis:** alle `.py`-Dateien darin, rekursiv.
- **Kein Pfad:** alle `.py`-Dateien im Projekt.
- Ausgeschlossen sind immer `.venv`, `.git`, `__pycache__`, `.claude/worktrees`, `node_modules`, `.opencode` und leere Dateien. `__init__.py` ohne Inhalt wird übersprungen.
- Existiert der Pfad nicht oder gibt es keine `.py`-Dateien, brich mit einer klaren Meldung ab.

Nenne dem Benutzer die Zahl der gefundenen Dateien. Sind es mehr als 20 und ist der Modus nicht «nur prüfen», frage vor dem Start einmal nach, ob wirklich alle bearbeitet werden sollen.

## 2. Sauberer Ausgangszustand

Ausser im Modus «nur prüfen»: Führe `git status --porcelain -- <ziel>` aus. Hat eine Zieldatei ungespeicherte Änderungen, brich ab und bitte darum, diese zuerst zu committen oder zu stashen. Nur so lässt sich später beweisen, dass ausschliesslich Dokumentation geändert wurde, und die Änderungen bleiben in einem separaten Diff reviewbar.

## 3. Verteilen

- Bis 5 Dateien: ein einziger Aufruf des Agenten `docstring-writer`.
- Mehr Dateien: Gruppen von je etwa 5 Dateien, ein `docstring-writer` pro Gruppe. Starte die Gruppen **parallel in einer Nachricht**, höchstens 5 Agenten gleichzeitig.
- Gib jedem Agenten die Dateiliste und den Modus mit. Keine Dateien doppelt vergeben.

## 4. Gesamtprüfung

Nach Abschluss aller Agenten, selbst und über alle bearbeiteten Dateien:

```bash
python3 -I .claude/skills/python-docstrings/scripts/check_nur_doku.py <dateien>
ruff check --select D --config 'lint.pydocstyle.convention = "google"' <dateien>
```

Im Modus «nur prüfen» entfällt die erste Prüfung.

## 5. Bericht

Fasse knapp zusammen: Anzahl bearbeiteter Dateien, was sich geändert hat, Stellen mit unklarem Verhalten, Beobachtungen ausserhalb des Auftrags und das Ergebnis der Gesamtprüfung. Committe nicht. Verweise auf `git diff` zur Kontrolle.
