# Konserve 3: Review-Funde einordnen

*Echte Ausgabe von `code-review` in Claude Code 2.1.311 (2026-10-27), geprüft wurde `vergleiche_staedte` aus einer früheren Fassung der Musterlösung gegen `plan.md`. Gekürzt auf die wichtigsten Funde. Der Skill schrieb selbst: «Ich habe die Funde nicht selbst nachgeprüft.»*

| # | Fund der KI | Schwere |
| - | ----------- | ------- |
| 1 | `tmax_differenz` wird aus bereits gerundeten Durchschnitten berechnet (doppelte Rundung). Der Plan verlangt Ø A minus Ø B, einmal gerundet. | hoch |
| 2 | `naessere_stadt` vergleicht auf 0.1 mm gerundete Summen. Beispiel: 10.04 mm gegen 10.01 mm ergäbe Gleichstand. | hoch |
| 3 | Der `ValueError` bei leerer Liste kommt nur zufällig aus `max()` in `berechne_kennzahlen`, es gibt keine eigene Prüfung. | mittel |
| 4 | Der Stadtname wird blind aus der ersten Zeile gelesen. Gemischte Listen werden nicht erkannt. | mittel |
| 5 | `berechne_kennzahlen` wird zweimal komplett aufgerufen, obwohl nur Ø tmax und Niederschlag gebraucht werden. | mittel |
| 6 | Leere Liste wird nur für `zeilen_a` getestet, nicht für `zeilen_b`. | niedrig |
| 7 | `__pycache__/` und `uv.lock` sind untracked, es gibt keine `.gitignore`. | niedrig |

**Einordnung (Lösung für die Dozentin oder den Dozenten):**

| # | Ergebnis | Begründung |
| - | -------- | ---------- |
| 1 | **Bestätigt, echter Fehler** | Zürich–Lugano ergab `-1.1`, exakt sind es `-1.2`. Die Tests merkten es nicht, weil ihre Werte glatt waren. Danach behoben und Test ergänzt. |
| 2 | **Scheinfund** | Die CSV hat nur eine Dezimale, ein Beispiel wie 10.04 mm kommt nicht vor. Das Runden der Summe auf 0.1 verhindert gerade Float-Artefakte wie `36.300000000000004`. |
| 3 | **Bestätigt** | Stimmt. Die Prüfung steht jetzt am Anfang der Funktion. Derselbe Punkt kommt im Teil «Diagnose» für `berechne_kennzahlen` wieder. |
| 4 | **Bestätigt, aber bewusste Entscheidung** | Der Plan lässt gemischte Listen offen (nicht geprüft). Ein Hinweis, kein Fehler. |
| 5 | **Bestätigt** | Folgt aus Fund 1: Die Durchschnitte werden direkt berechnet. |
| 6 | **Bestätigt** | Test für `vergleiche_staedte(BERN, [])` ergänzt. |
| 7 | **Nebensache** | Betrifft das Projekt, nicht die Funktion. |

**Übersehen** (Diskussion): Der Review schlug nichts zu `main` oder zur Anzeige vor. Der Plan schliesst beides aus, die Spec-Achse hat das also richtig behandelt.

**Lehre:** Ein Fund mit überzeugendem Rechenbeispiel (Fund 2) kann trotzdem falsch sein, ein unscheinbarer (Fund 1) einen echten Fehler zeigen. Prüfen heisst: nachrechnen, im Code nachsehen oder einen Test schreiben.
