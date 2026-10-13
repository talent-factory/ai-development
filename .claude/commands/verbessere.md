---
description: Verbessert eine Python-Datei nach Best Practices (Docstrings, Typ-Hinweise, Funktionen, DRY) ohne das Verhalten zu ändern
---

Verbessere die folgende Python-Datei. Ich bin Lernender in Modul 2 und möchte, dass der Code den gängigen Python-Regeln entspricht.

Die Datei ist: $ARGUMENTS

Lies zuerst die komplette Datei. Prüfe und verbessere dann anhand dieser Regeln:

1. **Modul-Docstring:** Am Anfang der Datei steht ein kurzer Docstring, der beschreibt, was das Programm tut.
2. **Funktionen:** Jede Funktion hat einen Docstring im Google-Style mit `Args`, `Returns` und `Raises` (falls relevant). Ein kurzes `Example` ist erlaubt, wenn es hilft.
3. **Typ-Hinweise:** Alle Parameter und Rückgabewerte haben Typ-Hinweise.
4. **Struktur:** Wiederholter Code wird in Funktionen ausgelagert (DRY). Jede Funktion erledigt genau eine Aufgabe. Logik steht nicht direkt auf Modulebene, sondern in `main()`, mit `if __name__ == "__main__":`.
5. **Keine Magic Numbers oder Strings:** Feste Werte wie Grenzwerte bekommen sprechende Namen, zum Beispiel als Konstante in Grossbuchstaben.
6. **Namensgebung und Stil:** Namen sind beschreibend und auf Deutsch, passend zum restlichen Projekt. PEP 8 gilt für Einrückung, Leerzeilen und Zeilenlänge.
7. **Eingaben und Fehler:** Benutzereingaben werden geprüft, und ungültige Eingaben führen zu einer verständlichen Meldung statt zu einem Absturz. Die Fehlerbehandlung wird wiederverwendet, nicht pro Eingabe kopiert.
8. **Kommentare:** Kommentare erklären das Warum, nicht das Offensichtliche.

Wichtig:
- Das Verhalten des Programms darf sich nicht ändern. Gleiche Eingaben müssen gleiche Ausgaben erzeugen. Ausnahme: Ein Absturz bei ungültiger Eingabe gilt als Fehler und darf behoben werden, zum Beispiel durch eine Wiederholung der Frage. Ändere keine Ausgabetexte, ausser um einen Fehler zu beheben, und benenne jede solche Änderung in der Zusammenfassung.
- Ändere nur die Datei, die ich angegeben habe.
- Setze die Verbesserungen direkt im Code um, ohne vorher nachzufragen.

Gehe danach so vor:
1. Wende die Änderungen mit dem Edit-Werkzeug an.
2. Falls Ruff verfügbar ist, führe `ruff format` auf der Datei aus und danach `ruff check`. Behebe die Meldungen von `ruff check`, die sich nicht automatisch beheben lassen, von Hand.
3. Führe das Programm mit `python3 -I` aus. Starte es aus dem Ordner der Datei, nicht aus dem Projektordner. Falls das Programm `input()` nutzt, übergib die Eingaben per Pipe, zum Beispiel `printf '30\n70\n1.75\n' | python3 -I datei.py`, und prüfe, dass die Ausgabe wie vorher ist.

Schliesse mit einer kurzen Liste ab:
- Was du geändert hast, Regel für Regel.
- Was du bewusst nicht geändert hast und warum.
- Das Ergebnis der Prüfungen aus Schritt 2 und 3.
