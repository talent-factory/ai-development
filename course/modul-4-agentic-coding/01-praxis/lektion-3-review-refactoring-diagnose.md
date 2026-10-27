# Lektion 3: Review, Refactoring und Diagnose

**Dauer:** 50 Minuten (20:00–20:50)  
**Ziel:** KI-Code prüfen statt glauben, Code in Kleinschritten verbessern und Fehler erst reproduzieren, bevor man sie behebt.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick**, Startstand holen | Gespräch |
| 5–15 | **Demo:** `code-review` gegen `plan.md`, Funde sammeln | Demo (Dozent) |
| 15–30 | **Übung 3, Teil A:** Refactoring in Kleinschritten ([ex-03](../02-uebungen/ex-03-review-refactoring-diagnose.adoc)) | Einzelarbeit |
| 30–40 | **Übung 3, Teil B:** Diagnose mit `diagnosing-bugs` | Einzelarbeit |
| 40–45 | **KI-Moment:** Funde einordnen | Auswertung |
| 45–50 | **Puffer** | |

---

## 1. Rückblick und Startstand (5 Minuten)

«Was lief, was hakt?» Dann kopiert alle `05-beispiele/lektion-2/loesung/` als Startstand.

---

## 2. Demo: `code-review` (10 Minuten)

`code-review` prüft zwei Dinge parallel: Folgt der Code den **Standards** des Projekts, und entspricht er der **Spec**, also unserem `plan.md`? Dafür startet der Skill zwei Subagenten. Das braucht ein starkes Kontingent und fällt im Gratis-Modell schnell ins Limit. Deshalb **zeigt der Dozent** den Lauf in Claude Code, du schaust zu.

```text
Nutze den Skill `code-review`.
Kontext: Spec ist `plan.md`, geprüft wird `vergleiche_staedte`.
Aufgabe: Prüfe gegen den Plan und gegen die Standards des Projekts.
Format: Funde nach Schwere, je Fund mit Datei und Zeile.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

*Während die KI arbeitet:* Schreibe dir vorab auf, was du selbst finden würdest, wenn du `vergleiche_staedte` gegen `plan.md` prüfst.

**Danach prüfst du selbst:** Lege deine Funktion neben `plan.md` und hake ab: Signatur, Schlüssel der Rückgabe, Definition «nässer», Gleichstand, leere Liste. Halte Funde der KI und deine eigenen in einer Liste fest. Sie werden in Abschnitt 5 eingeordnet.

> Wer ein funktionierendes Setup hat, probiert den Skill im Puffer oder zu Hause selbst aus.

---

## 3. Teil A: Refactoring in Kleinschritten (15 Minuten)

Es gibt keinen eigenen Refactoring-Skill. Wir verbessern deshalb in **kleinen Schritten**, und nach jedem Schritt laufen die Tests. Das ist die «Aufräumen»-Phase aus `tdd`.

**Problem:** `hole_live_wetter` ruft die API ab **und** bereitet die Antwort auf. Der Abruf lässt sich nicht offline testen, die Aufbereitung schon, wenn man sie herauslöst.

**Schritt 1:** Die reine Aufbereitung in eine neue Funktion `bereite_live_wetter_auf(antwort)` auslagern. Nur dieser Schritt.

```text
Kontext: `hole_live_wetter` ruft die API ab und bereitet die Antwort auf.
Aufgabe: Löse nur die reine Aufbereitung in eine neue Funktion `bereite_live_wetter_auf(antwort)` heraus. Der Parameter ist das Dictionary aus `antwort.json()`, kein `requests.Response`. Nur dieser eine Schritt, keine anderen Änderungen. Führe danach `pytest` aus.
Format: Diff und Ausgabe von `pytest`.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

**Schritt 2:** Für `bereite_live_wetter_auf` einen Test schreiben. Eine kleine Beispiel-Antwort als Dictionary reicht, kein Netz nötig.

**Schritt 3:** `hole_live_wetter` ruft nur noch ab und übergibt die Antwort an die neue Funktion.

Nach jedem Schritt: `uv run pytest`, dann der 3-Punkte-Check. Kommst du bis hierher, hast du aus Untestbarem etwas Testbares gemacht.

*Während die KI arbeitet:* Lies den Diff mit. Zählt er mehr Zeilen, als du erwartest?

---

## 4. Teil B: Diagnose mit `diagnosing-bugs` (10 Minuten)

Zwei Schwächen stecken im Startstand:

1. `berechne_kennzahlen([])` bricht für eine leere Stadt mit einer unklaren Meldung ab.
2. 21 von 150 CSV-Zeilen haben Wettercodes, die in `WETTERCODES` fehlen (`1`, `2`, `63`, `96`) und als «unbekannt» erscheinen.

Die KI will bei Fehlern gern sofort «fixen». Die Regel hier: **erst reproduzieren, dann ändern.**

```text
Nutze den Skill `diagnosing-bugs`.
Kontext: `berechne_kennzahlen([])` bricht ab (leere Stadt).
Aufgabe: Baue zuerst einen Test, der den Fehler reproduziert und rot ist. Ändere noch keinen Code. Nenne danach die Ursache mit Beleg.
Format: Test, Hypothese, Beleg.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

Erst wenn der Test rot ist, wird der Fix gemacht, bis er grün ist. Mach dasselbe für die unbekannten Codes (die Klartexte stehen in der Übung).

---

## 5. KI-Moment: Funde einordnen (5 Minuten)

Nimm die Liste aus der Demo (KI-Funde und deine eigenen) und ordne jeden Fund einer Spalte zu:

| Fund | Bestätigt | Scheinfund | Übersehen |
| ---- | --------- | ---------- | --------- |
| … | ☐ | ☐ | ☐ |

- **Bestätigt:** Du hast es im Code nachgeprüft, es stimmt.
- **Scheinfund:** Die KI meldet etwas, das im Code nicht so ist.
- **Übersehen:** Du hast etwas gefunden, das die KI nicht gemeldet hat.

Eine Aussage der KI über Code ist eine **Behauptung**, kein Beweis. Prüfen heisst: im Code nachsehen oder einen Test schreiben.

---

## Dozentenhinweise

- **Zeitnot (in dieser Reihenfolge):** Diagnose nur als Demo; Refactoring nur Schritt 1 und 2 (kein Umbau von `main`); sonst nichts streichen, Kür entfällt ohnehin.
- **Probelauf (2026-10-27, Claude Code 2.1.311):** `code-review` mit Subagenten in ca. 63 s (neun Funde); Refactoring-Schritt 1 in ca. 29 s; `diagnosing-bugs` in ca. 46 s (roter Test, Hypothese, Beleg, fragt vor dem Fix nach). Zwei Beobachtungen: (1) Ohne den Zusatz «Parameter ist das Dictionary aus `antwort.json()`» baute die KI `bereite_live_wetter_auf(antwort: requests.Response)`, die intern `.json()` aufruft. Dann ist die Funktion nicht rein, und der Test mit einem Dictionary scheitert. Das ist ein echter 3-Punkte-Fund (Punkt 2: passt es?). (2) Der erste Review fand einen echten Fehler in der damaligen Musterlösung (doppeltes Runden von `tmax_differenz`), inzwischen behoben; der Review ist also kein Theater. Echter Lauf: [`konserven/ki-moment-3-review-funde.md`](../05-beispiele/konserven/ki-moment-3-review-funde.md).
- **Rate-Limit:** Pair, Konserven: [`konserven/ki-moment-3-review-funde.md`](../05-beispiele/konserven/ki-moment-3-review-funde.md).
- **Musterlösung:** `05-beispiele/lektion-3/loesung/` (17 Tests grün; Codes ergänzt, `berechne_kennzahlen` mit klarer Meldung, `main` fängt sie ab).

---

*Datei: `01-praxis/lektion-3-review-refactoring-diagnose.md`*  
*Zurück zum Modul: [Modul 4](../README.md)*
