---
name: python-docstrings
description: Erstellt, ergänzt und verbessert Docstrings und Kommentare in Python-Dateien nach aktuellen Best Practices (PEP 257, Google-Style, Typ-Hinweise statt Typen im Text). Verwenden, wenn Python-Code dokumentiert, Docstrings geprüft oder die Dokumentation eines Moduls, Verzeichnisses oder Projekts vereinheitlicht werden soll.
---

# Python-Docstrings

Dieser Skill ändert **ausschliesslich Dokumentation**: Docstrings und Kommentare. Code, Signaturen und Verhalten bleiben unverändert.

## Vorgehen je Datei

1. Datei vollständig lesen und verstehen, was jede Funktion tatsächlich tut (nicht nur, wie sie heisst).
2. Fehlende Docstrings ergänzen, veraltete oder falsche korrigieren, überflüssige kürzen.
3. Kommentare prüfen: Sie erklären das **Warum**, nicht das Offensichtliche.
4. Prüfen (siehe unten). Erst wenn alles grün ist, ist die Datei fertig.

## Regeln (Kurzfassung)

- **Stil:** Google-Style, Sprache Deutsch (wie im Rest des Projekts). Details und Beispiele: [references/google-style.md](references/google-style.md).
- **Modul:** Jede Datei beginnt mit einem Docstring, der den Zweck beschreibt.
- **Zusammenfassung:** Erste Zeile, ein Satz, endet mit Punkt, steht direkt hinter den Anführungszeichen, danach eine Leerzeile.
- **Keine Typen im Text:** Typen stehen in den Typ-Hinweisen der Signatur. `Args` nennt nur Name und Bedeutung.
- **Öffentliche API immer dokumentieren:** Module, Klassen, öffentliche Funktionen und Methoden. Private Helfer (`_name`) nur, wenn ihre Logik nicht offensichtlich ist.
- **`Raises` nur für Ausnahmen, die die Funktion selbst auslöst** oder die zum Vertrag gehören. Nicht jede mögliche Systemausnahme auflisten.
- **Nichts erfinden:** Ist das Verhalten aus dem Code nicht eindeutig, den Docstring vorsichtig formulieren und die Stelle in der Zusammenfassung melden.
- **Doctests nur, wenn sie wirklich laufen.** Keine ausgedachten Ausgaben.
- **Direktiv-Kommentare nie anfassen:** `# noqa`, `# type:`, `# pragma`, `# pylint:`, `# fmt:`, `# nosec` und die Kodierungszeile (`# coding:`) bleiben unverändert. Sie steuern Linter, Typprüfer und Parser und werden von der Prüfung unten nicht erfasst. Das gilt auch für `>>>`-Beispiele in bestehenden Docstrings: nicht umschreiben, ausser sie sind nachweislich falsch.
- **Wahrheit vor Schönheit:** Ein kurzer korrekter Docstring ist besser als ein langer, der den Code nur wiederholt.

## Prüfen

Aus dem Projektordner ausführen, `<dateien>` durch die bearbeiteten Dateien ersetzen:

```bash
# 1. Es wurde nur Dokumentation geändert (AST ohne Docstrings identisch zu HEAD)
python3 -I .claude/skills/python-docstrings/scripts/check_nur_doku.py <dateien>

# 2. Docstring-Regeln (pydocstyle über Ruff, Google-Konvention)
ruff check --select D --config 'lint.pydocstyle.convention = "google"' <dateien>

# 3. Formatierung
ruff format <dateien>
```

Schlägt Prüfung 1 fehl, hat sich Code verändert. Änderung rückgängig machen, nicht erklären.
