---
name: tdd
description: Testgetriebene Entwicklung (TDD) mit Python und pytest. Verwenden, wenn Features oder Bugfixes test-first entstehen sollen, bei "Red-Green-Refactor", bei Characterization Tests für Legacy-Code oder wenn Integrationstests gewünscht sind.
---

# Testgetriebene Entwicklung (TDD)

TDD ist der Zyklus Red → Green → Refactor. Dieser Skill ist die Referenz dafür, dass der Zyklus Tests hervorbringt, die sich zu behalten lohnen: was ein guter Test ist, wo Tests ansetzen, welche Anti-Patterns es gibt und welche Regeln der Zyklus hat. Jeder Abschnitt gilt in jedem Durchlauf: vor und während des Zyklus nachschlagen, nicht erst danach.

Standardsprache ist Python mit `pytest`. Details zu Werkzeugen und Mustern stehen in [python.md](python.md).

Beim Erkunden des Codes zuerst `GLOSSARY.md` lesen (falls vorhanden), damit Testnamen und Schnittstellenvokabular zur Fachsprache des Projekts passen. ADRs im betroffenen Bereich respektieren. Testnamen, Docstrings und Kommentare folgen der Sprache des Projekts (im Kurs: Deutsch).

## Was einen guten Test ausmacht

Tests prüfen Verhalten über öffentliche Schnittstellen, nicht Implementierungsdetails. Der Code darf sich komplett ändern, die Tests nicht. Ein guter Test liest sich wie eine Spezifikation: `test_checkout_mit_gueltigem_warenkorb_wird_bestaetigt` sagt genau, welche Fähigkeit existiert, und übersteht Refactorings, weil er die interne Struktur nicht kennt.

Beispiele in [tests.md](tests.md), Regeln zum Mocken in [mocking.md](mocking.md).

## Seams: Wo Tests ansetzen

Ein **Seam** ist die öffentliche Grenze, an der getestet wird: die Schnittstelle, an der sich Verhalten beobachten lässt, ohne ins Innere zu greifen. Tests leben an Seams, nie an Interna.

**Seams vor dem ersten Test benennen.** Schreibe auf, an welchen Seams getestet wird, und schlage sie dem Nutzer vor. So landet der Testaufwand auf kritischen Pfaden und komplexer Logik statt auf jedem Randfall.

- Ist der Seam offensichtlich (kleine Funktion, Bugfix an einer bestehenden öffentlichen Schnittstelle), nenne ihn kurz und fahre fort.
- Ist er unklar oder berührt er mehrere Module, frage nach: «Was ist die öffentliche Schnittstelle, und an welchen Seams sollen wir testen?»

Steht die Form der Schnittstelle selbst in Frage (Tiefe des Moduls, Lage des Seams, was die Schnittstelle offenlegt), rufe das Skill-Tool mit `codebase-design` auf. Es ist die gemeinsame Quelle für Begriffe wie Modul, Schnittstelle, Tiefe, Seam, Adapter, Leverage und Locality. Es ist ein Nachschlagewerk, keine Sitzung.

## Anti-Patterns

- **Implementierungsgekoppelt**: mockt interne Kollaborateure, testet private Methoden oder prüft über einen Nebenkanal (Datenbank abfragen statt die Schnittstelle zu nutzen). Erkennbar daran, dass der Test beim Refactoring bricht, obwohl das Verhalten gleich bleibt.
- **Tautologisch**: Die Assertion berechnet den erwarteten Wert genauso wie der Code (`assert add(a, b) == a + b`, ein von Hand gleich hergeleiteter Snapshot, eine Konstante gegen sich selbst). Der Test besteht per Konstruktion und kann dem Code nie widersprechen. Erwartete Werte kommen aus einer unabhängigen Quelle: ein bekanntes Literal, ein durchgerechnetes Beispiel, die Spezifikation. Bei Parsern und Berechnungen helfen Eigenschaften (Property-Based Testing, siehe [python.md](python.md)).
- **Horizontales Schneiden**: erst alle Tests, dann die ganze Implementierung. Vorratstests prüfen *vorgestelltes* Verhalten, nur die *Form* der Dinge, werden unempfindlich gegen echte Änderungen und legen die Teststruktur fest, bevor die Implementierung verstanden ist. Stattdessen in **vertikalen Slices** arbeiten: ein Test → eine Implementierung → wiederholen. Jeder Test ist ein **Tracer Bullet**, der auf das reagiert, was der letzte Durchlauf gezeigt hat.
- **Falscher Grund für Rot**: Der Test scheitert an `ImportError`, `NameError` oder einem Tippfehler statt an der erwarteten Assertion. Dann ist «Rot» wertlos.
- **Unkontrollierte Umgebung**: abhängig von Uhrzeit, Netzwerk, Zufall, Reihenfolge oder globalem Zustand. Solche Tests werden flaky.

## Regeln des Zyklus

1. **Red vor Green.** Zuerst den fehlschlagenden Test schreiben, dann nur so viel Code, dass er besteht. Keine kommenden Tests vorwegnehmen, keine spekulativen Features.
2. **Rot verifizieren.** Den Test ausführen und prüfen, dass er an der erwarteten Assertion scheitert, mit sinnvoller Fehlermeldung. Nicht an Import- oder Syntaxfehlern.
3. **Ein Slice nach dem anderen.** Ein Seam, ein Test, eine minimale Implementierung pro Durchlauf.
4. **Refactor nur bei Grün.** Ist alles grün, Duplikate entfernen, Namen klären, Struktur vereinfachen. Verhalten bleibt gleich, die Tests laufen nach jedem Schritt. Keine neuen Features im Refactor-Schritt. Das umfassende Review bleibt Sache des `code-review`-Skills.
5. **Gesamte Suite am Ende jedes Durchlaufs ausführen**, nicht nur den neuen Test.
6. **Mindestens 90 % Testabdeckung (Zweigabdeckung)** je Projekt bzw. Übung. Das ist eine harte Untergrenze: Vor Abschluss einer Aufgabe mit `uv run pytest --cov` messen und fehlende Zeilen mit weiteren Tests schliessen. Weil im Zyklus jeder Code durch einen Test entsteht, sollte die Abdeckung ohnehin fast von selbst erreicht werden. Liegt sie darunter, ist das ein Hinweis auf Code ohne Test, nicht auf zu wenig Tests. Abdeckung ist nur ein Minimum und beweist keine Qualität: Nie Tests ohne Assertion oder tautologische Tests schreiben, nur um die Zahl zu erreichen. Details in [python.md](python.md).

## Bugfix-Ablauf

1. Den Bug über den öffentlichen Seam mit einem fehlschlagenden Test reproduzieren. Der Test benennt das erwartete Verhalten, nicht den Bug.
2. Rot verifizieren: Der Test scheitert genau an dem gemeldeten Fehlverhalten.
3. Minimal fixen, bis der Test grün ist.
4. Der Test bleibt als Regressionstest in der Suite.

Ist die Ursache unklar, zuerst den Skill `diagnosing-bugs` verwenden und erst mit bekannter Ursache den Test schreiben.

## Legacy-Code ohne Tests

Vor einer Änderung mit **Characterization Tests** das aktuelle Verhalten festhalten: Funktion mit repräsentativen Eingaben aufrufen und die tatsächliche Ausgabe als Erwartung eintragen. Diese Tests sind ein Sicherheitsnetz, keine Spezifikation. Erst danach ändern, im üblichen Red-Green-Refactor-Zyklus.
