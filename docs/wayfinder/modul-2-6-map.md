# Wayfinder Map: Kurs-Überarbeitung Module 2–6 (Fokus Modul 2)

**Label:** `wayfinder:map`
**Tracker:** lokal (`docs/wayfinder/tickets/`), kein Linear (Linear ist nur für Talent-Factory-Projekte)
**Vorgänger:** [Session 1](./kurs-redesign-map.md) (Struktur, Modul 1)

---

## Destination

Zwei Ergebnisse:

1. **Kursüberblick Modul 2–6:** Jeder Punkt aus Curriculum und Ausschreibung (`docs/Curriculum.md`) hat ein Modul als Zuhause. Grob, ohne Detailplanung.
2. **Modul 2 ist entschieden und durchführbar** (Durchführung nächste Woche): Lernziele, 4 Lektionen, Übungen inkl. Challenge, Nachbearbeitung und Branch-Workflow sind festgelegt. Ausformulieren der Dateien geschieht danach (Implementierung), nicht in dieser Map.

Module 3–6 werden erst **nach der Durchführung von Modul 2** konkretisiert, mit dem Feedback der Studierenden.

## Notes

- **Zielgruppe:** Junior-Entwickler:innen (vierjährige Ausbildung, unter Bachelor-Niveau) und Quereinsteiger (z.B. ehemalige Cobol-Entwickler). Einige haben `pyt-intro-2025` bereits absolviert.
- **Haltung:** praxisnah, handwerklich, keine Hochschultheorie, holt Quereinsteiger ab.
- **Keine Duplikate** zu: IBAW-Curriculum, KI-Basics (Sabine Jungk, `bibliography/`), Modul 1, `pyt-intro-2025`.
- **Format:** online, ohne Aufzeichnung; 4 × 50 Min Präsenz plus ca. 2–3 h Selbststudium pro Modul.
- **Abgabe:** GitHub; jede:r Studierende arbeitet auf einem eigenen Branch. Keine Benotung, keine bewerteten Tests.
- **Skills:** grilling, domain-modeling, research.
- **Modul-2-Altentwurf** (uncommitted in `course/modul-2-python-grundlagen-mit-ki/`) wird verworfen und nach `archive/` verschoben; Altmaterial nur übernehmen, wenn es in den neuen Plan passt.

## Decisions so far

Beim Kartieren gesetzt (Grilling-Runden 1–3, 2026-10-09):

- **Zuschnitt:** Wayfinder plant; Inhalte entstehen später über Epics/Tickets (lokal).
- **Modul-2-Kernziel:** Unbekannten Python-Code (20–40 Zeilen) lesen, erklären, Lücken per gezieltem Prompt an die KI schliessen und deren Erklärung selbst prüfen. Eigenes Schreiben ist nur Nebenziel.
- **Wortschatz Modul 2:** Kern = Variablen/Typen, Ein-/Ausgabe, `if`/`elif`/`else`, `for`/`while`, Funktionen. Dazu Listen/Dicts (nur lesend) und `try/except` (Fehlermeldungen lesen). Raus: OOP, Dekoratoren, Comprehensions, Generatoren, Testing (kommt in Modul 4).
- **Methodik:** fester Zyklus je Lektion: vorhersagen, ausführen, KI erklären lassen, Erklärung prüfen, kleine Änderung. Du coddest ca. 10 Min live pro Lektion.
- **Heterogene Vorkenntnisse:** ein Weg für alle plus Challenge; Challenge-Code enthält absichtlich einen Fehler, den die KI-Erklärung übersieht.

Aus Tickets (wird beim Schliessen ergänzt):

_noch keine_

## Not yet specified

- Module 3–6 im Detail (Inhalte, Übungen, Hausaufgaben), erst nach Modul-2-Feedback.
- Modul-6-Abschlussprojekt: Solo oder Gruppe, Umfang, Bestehen-Kriterium.
- Wo TDD/Refactoring/Code-Review/Doku und das Web-App-Praxisprojekt konkret landen (grob geklärt im Curriculum-Mapping, Details offen).
- Verhältnis Agentic Coding (Modul 4) zu OpenCode-Skills/Commands.
- Ob Flowise/Langflow (No-Code-RAG) bleiben.

## Out of scope

- Ausarbeitung von Modul 3–6 in dieser Runde (bewusst nach Modul 2).
- Zwei-Kurs-Split aus `kurskonsolidierung-proposal.md` und Marketing/Cross-Selling.
- Fachhochschul-Niveau (FFHS CAS AISE dient nur als Gedankenstütze).
- Linear-Tickets.

## Tickets (Frontier-Übersicht)

| # | Ticket | Typ | Blockiert von |
|---|--------|-----|---------------|
| 10 | [KI-Basics-Überschneidung für Modul 2](./tickets/10-ki-basics-ueberschneidung.md) | research | – |
| 11 | [Ist-Stand Modul 1 und Abgrenzung zu pyt-intro-2025](./tickets/11-modul1-und-pyt-intro-abgrenzung.md) | research | – |
| 12 | [Curriculum-Mapping Modul 2–6](./tickets/12-curriculum-mapping.md) | grilling | – |
| 13 | [Lektionsplan Modul 2](./tickets/13-lektionsplan-modul-2.md) | grilling | 10, 11 |
| 14 | [Übungen und Challenge Modul 2](./tickets/14-uebungen-und-challenge.md) | grilling | 13 |
| 15 | [Nachbearbeitung, Branch-Workflow und Reflexion](./tickets/15-nachbearbeitung-und-branch-workflow.md) | grilling | 13 |

_Stand: 2026-10-09_
