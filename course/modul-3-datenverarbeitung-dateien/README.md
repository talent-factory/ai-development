# Modul 3: Datenverarbeitung & Dateien

**Dauer:** 1 Abend, 18:00–21:50 (4 Lektionen à 50 Minuten, 3 Pausen à 10 Minuten)  
**Voraussetzung:** Modul 2 abgeschlossen (Variablen, Bedingungen, Schleifen, Funktionen) und die [Vorbereitung](./00-vorbereitung/README.md).

**Lektionsplan für Dozierende:** [LEKTIONSPLAN.md](./LEKTIONSPLAN.md)

---

## 🎯 Lernziele

Nach diesem Modul können Sie:

1. ✅ Daten aus Textdateien lesen und schreiben (`with open(...)`).
2. ✅ CSV-Dateien mit `csv.DictReader` und `csv.DictWriter` verarbeiten.
3. ✅ JSON-Daten laden, strukturieren und speichern.
4. ✅ Eine HTTP-API mit `requests` abrufen und die Antwort auswerten.
5. ✅ Fehler gezielt mit `try/except` behandeln, ohne sie zu verschlucken.
6. ✅ KI-Ergebnisse prüfen: «Vertrauen, aber prüfen».

---

## 🌦️ Das Szenario

Wir arbeiten den ganzen Abend mit einem Datensatz: dem **Wetter von fünf Schweizer Städten** (Zürich, Bern, Genf, Basel, Lugano) vom 20. September bis 19. Oktober 2026. Datenquelle: Weather data by Open-Meteo.com (CC BY 4.0).

Jede Lektion bringt ihren eigenen Startordner mit. So kann auch einsteigen, wer eine Lektion verpasst hat.

---

## 📚 Modulstruktur

### [00-vorbereitung/](./00-vorbereitung/)

**Zeitaufwand:** ca. 30 Minuten

- `uv add requests` und `check_setup.py`
- Leseauftrag Listen und Dictionaries mit Selbsttest

### [01-praxis/](./01-praxis/)

**Präsenzunterricht:** 4 Lektionen à 50 Minuten

| Zeit | Lektion |
| ---- | ------- |
| 18:00–18:50 | [Lektion 1: Textdateien](./01-praxis/lektion-1-textdateien.md) |
| 19:00–19:50 | [Lektion 2: CSV](./01-praxis/lektion-2-csv.md) |
| 20:00–20:50 | [Lektion 3: JSON & API](./01-praxis/lektion-3-json-api.md) |
| 21:00–21:50 | [Lektion 4: Fehlerbehandlung & Abschluss](./01-praxis/lektion-4-fehlerbehandlung.md) |

### [02-uebungen/](./02-uebungen/)

**Je Lektion eine Übung** (13–20 Minuten, mit Kontrollwerten, Gerüst als `start.py`)

- [Übung 1: Textdatei auswerten](./02-uebungen/ex-01-textdatei.adoc)
- [Übung 2: CSV auswerten](./02-uebungen/ex-02-csv.adoc)
- [Übung 3: JSON und API](./02-uebungen/ex-03-json-api.adoc)
- [Übung 4: Fehlerbehandlung](./02-uebungen/ex-04-fehlerbehandlung.adoc)

### [03-nachbearbeitung/](./03-nachbearbeitung/)

**Hausaufgabe vor Modul 4** (ca. 3–4 Stunden)

- Ein Skript `wetter_bericht.py`, das alle Techniken kombiniert
- Reflexionsbogen

### [04-materialien/](./04-materialien/)

**Handouts**

- [Cheatsheet Dateien: TXT, CSV, JSON](./04-materialien/cheatsheet-dateien.adoc)
- [Cheatsheet Fehlerbehandlung & HTTP-APIs](./04-materialien/cheatsheet-fehler-api.adoc)

### [05-beispiele/](./05-beispiele/)

**Daten, Gerüste und Musterlösungen**

- `check_setup.py`
- `lektion-1/` bis `lektion-4/`: Daten, `start.py` (Gerüst), `loesung.py` (Musterlösung)

---

## ⏱️ Zeitplan

| Zeit | Aktivität |
| ---- | --------- |
| **Vor dem Abend** | Vorbereitung (ca. 30 Min.) |
| 18:00–18:50 | Lektion 1 |
| 18:50–19:00 | Pause |
| 19:00–19:50 | Lektion 2 |
| 19:50–20:00 | Pause |
| 20:00–20:50 | Lektion 3 |
| 20:50–21:00 | Pause |
| 21:00–21:50 | Lektion 4 mit Feedback-Runde |
| **Danach** | Nachbearbeitung (3–4 Std.) |

---

## 🗄️ Archiv

Material aus einer früheren Kursfassung (Replicate, LangChain/RAG) liegt in den `archive/`-Unterordnern der jeweiligen Abschnitte und gehört nicht mehr zu diesem Modul.

---

## 🔗 Verknüpfungen

- **Vorheriges Modul:** [Modul 2 – Python-Grundlagen mit KI](../modul-2-python-grundlagen-mit-ki/)
- **Nächstes Modul:** [Modul 4 – Agentic Coding](../modul-4-agentic-coding/)
