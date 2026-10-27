# Nachbearbeitung: Modul 4: Agentic Coding

**Zeitaufwand:** ca. 2–3 Stunden bis Modul 5

---

## 1. Pflicht-Aufgabe (ca. 2 Std)

### A) Dein eigener Durchlauf

Im Kurs haben wir den Durchlauf **Plan → Test → Code → Review → Doku** gemeinsam geübt. Jetzt führst du ihn allein an einem kleinen Feature für den Wetterbericht durch. Starte mit der Musterlösung von Lektion 4 (`05-beispiele/lektion-4/loesung/`) oder mit deinem eigenen Stand.

Wähle **eines** der drei Features (oder schlage ein eigenes vor, das eine reine Funktion auf den CSV-Daten ist):

| Feature | Beschreibung | Rückgabe |
| ------- | ------------ | -------- |
| `finde_laengste_regenserie(zeilen)` | Längste Folge aufeinanderfolgender Regentage (`niederschlag_mm > 0`). Bei Gleichstand gilt die erste Serie. | `{"start": "2026-10-07", "laenge": 4}` (Beispiel Zürich); ohne Regentag `{"start": None, "laenge": 0}`; leere Liste: `ValueError` |
| `berechne_wochenmittel(zeilen)` | Durchschnitt von `tmax` pro ISO-Kalenderwoche, eine Dezimale | `{"2026-W38": 24.1, …}` (Beispiel Bern); leere Liste: `ValueError` |
| `zaehle_sommertage(zeilen, grenze=25.0)` | Anzahl Tage mit `tmax` mindestens `grenze` | Ganzzahl; leere Liste: `0` |

Die Funktion arbeitet nur mit den Zeilen aus `lese_stadt(...)`, nicht mit dem Live-Abruf, und lässt sich offline testen.

### Was du abgibst

1. **`plan.md`:** erstellt mit dem Skill `grilling`. Enthält Ziel, Signatur, Rückgabe, Randfälle und was nicht zum Feature gehört.
2. **`test_wetter_bericht.py`:** deine Tests, test-first geschrieben und alle grün. Mindestens ein Randfall (leere Liste oder keine Treffer).
3. **`wetter_bericht.py`:** mit deinem Feature, ohne Ungefragtes in anderen Funktionen.
4. **`README.md`:** kurze Doku des Features (Zweck, Aufruf, Beispiel, Randfälle). Sie beschreibt nur, was der Code wirklich tut.
5. **`review-notiz.md`:** ca. eine halbe Seite. Wende den **3-Punkte-Check** auf mindestens zwei KI-Schritte an (läuft es? passt es zu `plan.md`? wurde etwas Ungefragtes geändert?) und halte mindestens **einen Fall** fest, in dem die KI falsch lag oder etwas Unnötiges getan hat.
6. **`reflexion.md`:** der ausgefüllte [Reflexionsbogen](./reflexionsbogen.md) (ca. 30 Min).

**Kontrollwerte aus der CSV** (`lese_stadt(CSV_DATEI, …)`, nur für dein gewähltes Feature):

| Stadt | Längste Regenserie | Wochen (Anzahl) | Ø `tmax` KW 38 / KW 39 | Sommertage (ab 25 °C) |
| ----- | ------------------ | --------------- | ---------------------- | --------------------- |
| Bern | ab 2026-10-07, 4 Tage | 6 | 24.1 / 23.2 | 3 |
| Lugano | ab 2026-10-05, 6 Tage | 6 | 25.7 / 23.7 | 2 |

Die erste und die letzte Woche sind unvollständig; das ist erwartet.

**Kontrollwerte:** Rechne ein Beispiel von Hand oder mit einem separaten Skript nach und prüfe, dass dein Test denselben Wert erwartet. Ein Test, der nur das Ergebnis der KI abschreibt, zählt nicht als Beleg.

---

## 2. Zusatz-Aufgaben (freiwillig)

### B) Kürzer, klarer, besser

Wende `code-review` oder deinen Review-Prompt auf dein Feature an und setze einen Fund um, den du für berechtigt hältst. Halte fest, welche Funde du abgelehnt hast und warum.

### C) Glossar

Lass mit `domain-modeling` ein `GLOSSARY.md` für den Wetterbericht erstellen (Stadt, Wettercode, Regentag, …) und korrigiere, was nicht stimmt.

### D) Zweites Feature

Wiederhole den Durchlauf für ein zweites Feature und vergleiche: Was ging schneller als beim ersten Mal?

---

## 3. Vorbereitung Modul 5

- [ ] Lies deine `review-notiz.md` noch einmal und notiere, welche Prüfung dir am meisten gebracht hat.
- [ ] Überlege: Welche Schritte des Durchlaufs würdest du einer KI künftig ohne Rückfrage überlassen, und welche nie?

---

## 4. Abgabe

**Bis Modul 5 (nächster Kurstag):** die sechs Dateien aus Abschnitt 1 in einem Ordner `03-nachbearbeitung/`.

**Format:** per GitHub Classroom / Moodle / E-Mail (laut Dozent)

---

## 5. Bewertungskriterien (für Dozent)

| Kriterium | Gewichtung |
| --------- | ---------- |
| Plan (`plan.md` klar, Randfälle, Abgrenzung) | 25 % |
| Tests (test-first, grün, Randfall, eigene Erwartung) | 30 % |
| Code (funktioniert, nichts Ungefragtes, verständlich) | 20 % |
| Review und Doku (3-Punkte-Check, ehrlicher KI-Fehlerfall, README) | 25 % |

---

*Datei: `03-nachbearbeitung/README.md`*  
*Zurück zum Modul: [Modul 4: Agentic Coding](../README.md)*
