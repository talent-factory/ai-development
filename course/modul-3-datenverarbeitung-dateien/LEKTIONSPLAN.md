# Lektionsplan Modul 3: Datenverarbeitung & Dateien

**Voraussetzung:** Modul 2 abgeschlossen (Variablen, Bedingungen, Schleifen, Funktionen) sowie die [Vorbereitung](./00-vorbereitung/README.md) (`uv add requests`, Listen und Dicts)  
**Dauer:** 1 Abend, 18:00–21:50 (4 Lektionen à 50 Minuten + 3 Pausen à 10 Minuten)

---

## Überblick

| Zeit | Lektion | Titel | Kernbotschaft |
| ---- | ------- | ----- | ------------- |
| 18:00–18:50 | 1 | Textdateien | Daten aus einer Datei lesen, zerlegen, umwandeln und das Ergebnis zurückschreiben. |
| 18:50–19:00 | | Pause | |
| 19:00–19:50 | 2 | CSV | Tabellen mit `DictReader` auswerten, filtern, exportieren. |
| 19:50–20:00 | | Pause | |
| 20:00–20:50 | 3 | JSON & API | Verschachtelte Daten speichern und eine Wetter-API abrufen. |
| 20:50–21:00 | | Pause | |
| 21:00–21:50 | 4 | Fehlerbehandlung & Abschluss | Kaputte Daten und ausgefallene APIs abfangen, ohne Fehler zu verschlucken. |

Es gibt **keinen freien Puffer**: 4 × 50 + 3 × 10 = 230 Minuten. Der Puffer steckt in den Kür-Blöcken (siehe Streichreihenfolge).

## Roter Faden

Ein Szenario für den ganzen Abend: **Wetter von fünf Schweizer Städten** (Zürich, Bern, Genf, Basel, Lugano) vom 20. September bis 19. Oktober 2026. Der Datensatz ist ein eingefrorener Snapshot (alle haben dieselben Zahlen), nur die API-Demo in Lektion 3 ruft live ab.

| Lektion | Startordner (`05-beispiele/`) | Inhalt |
| ------- | ----------------------------- | ------ |
| 1 | `lektion-1/` | `wetter_zuerich.txt` (30 Zeilen, `datum;stadt;tmin;tmax;niederschlag`) |
| 2 | `lektion-2/` | `wetter_30tage.csv` (150 Zeilen, 5 Städte × 30 Tage) |
| 3 | `lektion-3/` | `beispiel_antwort.json`, `beispiel_antwort_5_staedte.json`, Ergebnis aus L2 im Code |
| 4 | `lektion-4/` | `wetter_defekt.csv` (24 Zeilen, 5 defekt), `beispiel_fehler.json` |

Jede Lektion hat einen eigenen Startordner, der Einstieg ist also auch für Studierende möglich, die eine Lektion verpasst haben.

## Wiederkehrende Elemente

- **Rückblick (5 Min.)** zu Beginn von L2 bis L4: «Was lief, was hakt?», immer im gleichen Muster, ohne Aufgabe.
- **KI-Moment (5 Min.)** in jeder Lektion mit kopierfertigem Prompt. Command nur als Abkürzung.
- **Prüfregel «Vertrauen, aber prüfen»:** 1. ausführen, 2. gegen Kontrollwert oder `assert` prüfen, 3. erst dann übernehmen. Steht als Box in jeder Lektionsdatei.
- **Übung mit Kontrollwerten** und Gerüst `start.py` (TODO-Kommentare). Keine Abgabe am Präsenztag.
- **Musterlösung** `loesung.py` nach jeder Übung freigeben.
- **Kür-Block (5 Min.)** am Ende jeder Lektion, freiwillig.

---

## Lektion 1: Textdateien (18:00–18:50)

### Ziele
- `with open(...)` lesen und schreiben, `encoding="utf-8"` immer angeben.
- Zeilen mit `strip()` und `split(";")` zerlegen, Text mit `float()` umwandeln.
- Listen und Dictionaries sicher anwenden.

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Begrüssung, Tagesüberblick, Szenario | Kurzvortrag |
| 5–10 | Startdateien holen, `check_setup.py`, Check Listen/Dicts | Einzelarbeit |
| 10–25 | Live-Coding: `open`, `with`, `split`, Schreiben, `pathlib` | Demo + Mitmachen |
| 25–30 | **KI-Moment:** `/erklaere` auf ein `open()`-Snippet; «Datei fehlt» selbst auslösen | Einzelarbeit + KI |
| 30–45 | **Übung 1:** Wetter Zürich auswerten | Einzelarbeit |
| 45–50 | Kür: Regentage auflisten | Einzelarbeit |

**Kontrollwerte:** 30 Tage · heissester Tag 2026-09-30 mit 27.5 °C · 10 Regentage.

**Materialien:** `01-praxis/lektion-1-textdateien.md`, `02-uebungen/ex-01-textdatei.adoc`, `05-beispiele/lektion-1/`

---

## Lektion 2: CSV (19:00–19:50)

### Ziele
- `csv.DictReader` und `csv.DictWriter`, `newline=""`.
- Zahlen einmal beim Einlesen umwandeln; Auswerten je Stadt mit `setdefault`.
- KI-erzeugte Testdaten mit `assert` prüfen.

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Rückblick L1 | Plenum |
| 5–20 | Live-Coding: `DictReader`, Typumwandlung, Durchschnitt, Filter, `DictWriter` | Demo + Mitmachen |
| 20–25 | **KI-Moment:** Testdaten erzeugen lassen und prüfen | Einzelarbeit + KI |
| 25–45 | **Übung 2:** Durchschnitt, Filter, Export | Einzelarbeit |
| 45–50 | Kür: Stadt per `input()` wählen | Einzelarbeit |

**Kontrollwerte:** 150 Zeilen · Ø `tmax` Zürich 20.7 / Bern 19.9 / Genf 21.4 / Basel 21.6 / Lugano 21.8 · 100 Tage über 20 °C · `warme_tage.csv` mit 101 Zeilen.

**Materialien:** `01-praxis/lektion-2-csv.md`, `02-uebungen/ex-02-csv.adoc`, `05-beispiele/lektion-2/`

---

## Lektion 3: JSON & API (20:00–20:50)

### Ziele
- `json.dump` / `json.load` mit `indent=2, ensure_ascii=False`.
- `requests.get(url, params=..., timeout=...)`, `raise_for_status()`, `.json()`.
- Die Antwortstruktur lesen (`daily` als parallele Listen), WMO-Wettercodes in einem Dict übersetzen.

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Rückblick L2 | Plenum |
| 5–15 | JSON speichern und laden | Demo + Mitmachen |
| 15–25 | Geführte API-Demo (Open-Meteo, Bern) | Dozentin / Dozent |
| 25–30 | **KI-Moment:** API-Aufruf ohne Doku schreiben lassen, gegen die Doku prüfen | Einzelarbeit + KI |
| 30–45 | **Übung 3:** JSON, Wettercode-Dict, Bern abrufen | Einzelarbeit |
| 45–50 | Kür: alle fünf Städte in einem Request | Einzelarbeit |

**Kontrollwerte (`OFFLINE = True`):** 3 Tage · «heute: leichter Regen, 14.4 °C». Live ändern sich die Werte, dann nur Struktur prüfen.

**Materialien:** `01-praxis/lektion-3-json-api.md`, `02-uebungen/ex-03-json-api.adoc`, `05-beispiele/lektion-3/`

---

## Lektion 4: Fehlerbehandlung & Abschluss (21:00–21:50)

### Ziele
- Traceback lesen, `try/except/else/finally`, spezifische Fehlerarten, Reihenfolge der `except`-Blöcke.
- `requests`-Fehler unterscheiden (`HTTPError`, `ConnectionError`, `Timeout`, `JSONDecodeError`).
- Fehler nie verschlucken (`except: pass`).

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Rückblick L3 | Plenum |
| 5–17 | Input: Traceback, `try/except`, API-Fehler | Demo + Mitmachen |
| 17–22 | **KI-Moment:** `/debug` auf `ValueError`; Vorschläge beurteilen | Einzelarbeit + KI |
| 22–35 | **Übung 4:** defekte CSV und API-Fehler | Einzelarbeit |
| 35–42 | Kür (Logdatei) oder Puffer | Einzelarbeit |
| 42–50 | **Abschluss:** Feedback-Blitzrunde, Ausblick Modul 4 | Plenum |

**Kontrollwerte:** 19 gültige, 5 übersprungene Zeilen (24 insgesamt).

**Materialien:** `01-praxis/lektion-4-fehlerbehandlung.md`, `02-uebungen/ex-04-fehlerbehandlung.adoc`, `05-beispiele/lektion-4/`

---

## Streichreihenfolge bei Zeitnot

Entschieden vorab, damit unter Druck nichts neu abgewogen werden muss:

1. Alle Kür-Blöcke (insgesamt etwa 25 Minuten).
2. Wettercode-Eigenbau in L3: Die Studierenden nehmen `WETTERCODES_VOLL` aus `start.py`.
3. Live-API in L3 wird zur reinen Dozenten-Demo: Alle setzen `OFFLINE = True`.
4. Zusatzteil von Übung 4 (API-Fehler wird Demo).

Was **nie** entfällt: `try/except` in L4 und die Feedback-Runde.

## Vor dem Unterricht prüfen

- [ ] Vorbereitung an die Studierenden verschickt, Repo mit `05-beispiele/` gepusht.
- [ ] `uv run python 05-beispiele/check_setup.py` läuft (Python und `requests`).
- [ ] Beamer, Live-Coding-Umgebung, Zugang zu Claude Code oder KI-Chat.
- [ ] Open-Meteo kurz testen: `uv run python 05-beispiele/lektion-3/loesung.py` mit `OFFLINE = False`.
- [ ] Prüfen, ob eine API ohne Koordinaten weiterhin mit HTTP 200 und leerem Body antwortet (am 20.10.2026 beobachtet, siehe Hinweis in Lektion 3).
- [ ] Notfall: `OFFLINE = True` ansagen. Alle Beispieldateien liegen lokal.

## Nach dem Unterricht

- Musterlösungen `loesung.py` freigeben (nach jeder Lektion).
- Nachbearbeitung und Reflexionsbogen verteilen: `03-nachbearbeitung/`.
- Feedback-Notizen (was war unklar?) für den Start von Modul 4 festhalten.

## Material und Raum

- Beamer für Live-Coding, Whiteboard oder Flipchart
- Je Teilnehmende: Laptop mit Projektordner (Modul 1), Internetzugang, KI-Zugang

---

**Zurück zum Modul:** [Modul 3: Datenverarbeitung & Dateien](./README.md)
