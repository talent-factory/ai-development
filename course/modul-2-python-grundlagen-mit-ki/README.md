# Modul 2: Python-Grundlagen mit KI verstehen

**Dauer:** 1 Tag (4 Lektionen à 50 Minuten)  
**Voraussetzung:** Modul 1 abgeschlossen (Setup funktionsfähig: VS Code, Python, uv, OpenCode)

---

## 🎯 Lernziele

Nach diesem Modul können Sie:

1. ✅ Variablen, Datentypen (`int`, `float`, `str`, `bool`) und Operatoren sicher nutzen.
2. ✅ Eingaben entgegennehmen (`input()`), Typen umwandeln (`int()`, `float()`) und validieren (`try/except`).
3. ✅ Bedingte Anweisungen (`if`/`elif`/`else`) und logische Operatoren (`and`/`or`/`not`) verstehen und anwenden.
4. ✅ Schleifen (`while`, `for`, `range()`) einsetzen, `break`/`continue` kennen.
5. ✅ Funktionen definieren (`def`), parametrisieren (Defaults, `*args`, `**kwargs`), Typ-Hinweise & Docstrings schreiben.
6. ✅ KI gezielt einsetzen: als Erklär-Partner, Pair-Programmer, Debugger und Code-Reviewer.
7. ✅ Grössere Aufgaben in kleine, testbare Funktionen zerlegen (Modulare Programmierung).

---

## 📚 Modulstruktur

### [00-vorbereitung/](./00-vorbereitung/)
**Zeitaufwand:** 2–3 Stunden Selbststudium vor dem Präsenztag

- Modul 1 wiederholen (Setup prüfen, `hello-world.py` laufen lassen)
- Leseauftrag: Python-Basics (Variablen, Operatoren, `input()`, `if`, Schleifen, Funktionen)
- Erste REPL-Experimente (`python` im Terminal)
- KI als Lernpartner testen: `"Erkläre mir Variablen wie einem 12-Jährigen."`

> **Material:** `00-vorbereitung/README.md`

---

### [01-praxis/](./01-praxis/)
**Präsenzunterricht:** 4 Lektionen à 50 Minuten

| Lektion | Titel | Datei | Kerninhalt |
|---------|-------|-------|------------|
| 1 | Variablen, Datentypen & Operatoren | `lektion-1-variablen.md` | `int`/`float`/`str`/`bool`, Rechen- & String-Operatoren, f-Strings, KI-Exploration |
| 2 | Eingaben, Typumwandlung & Bedingungen | `lektion-2-bedingungen.md` | `input()`, `int()`/`float()` + `try/except`, Vergleichs- & logische Operatoren, `if`/`elif`/`else`, BMI-Rechner |
| 3 | Schleifen – `while`, `for`, `range()` | `lektion-3-schleifen.md` | `while` vs `for`, `range()`, `break`/`continue`, `enumerate()`, Zahlenraten, FizzBuzz, KI-Debugging |
| 4 | Funktionen – Definieren & Wiederverwenden | `lektion-4-funktionen.md` | `def`, Parameter/Defaults/`*args`/`**kwargs`, `return`/`None`, Typ-Hinweise, Google-Docstrings, KI-Code-Review, modulare Taschenrechner |

> **Materialien:** `01-praxis/lektion-*.md`, `05-beispiele/0*-demo.py`, `02-uebungen/ex-*.adoc`

---

### [02-uebungen/](./02-uebungen/)
**Übungen während der Präsenz** (je 15–25 Min)

| Übung | Lektion | Datei | Beschreibung |
|-------|---------|-------|--------------|
| 1 | 2 | `ex-01-taschenrechner.adoc` | Taschenrechner mit `input()`, Casting, `if`/`elif`/`else`, Fehlerbehandlung |
| 2 | 3 | `ex-02-zahlenraten.adoc` | Zahlenraten mit `while`, `random`, Zähler, Schwierigkeitsgrade, Highscore (optional) |
| 3 | 4 | `ex-03-funktionen.adoc` | Modularer Taschenrechner mit Funktionen, Typ-Hinweisen, Docstrings, **Pflicht: KI-Code-Review** |

---

### [03-nachbearbeitung/](./03-nachbearbeitung/)
**Hausaufgaben vor Modul 3** (ca. 3–4 Std)

| Aufgabe | Datei | Beschreibung |
|---------|-------|--------------|
| Währungsrechner | `waehrungsrechner.py` | CHF↔EUR, Funktionen, Typ-Hinweise, Docstrings, Menü-Schleife |
| Text-Analyse | `textanalyse.py` | Zeichen/Wörter/Sätze zählen, `Counter`, KI-Optimierung |
| Reflexionsbogen | `reflexion.md` | Selbstständige Reflexion: Lernfortschritt, KI-Nutzung, Schwierigkeiten |
| *Freiwillig* | `zahlenraten_pro.py` | Highscore (JSON), Statistik, Versuch-Limits |

> **Abgabe:** Per GitHub Classroom / Moodle / E-Mail bis Modul 3

---

### [04-materialien/](./04-materialien/)
**Handouts & Ressourcen** (Cheatsheets & Guides)

| Datei | Inhalt |
|-------|--------|
| `cheatsheet-datentypen.adoc` | Datentypen, Operatoren, Strings, Vergleiche, Truthiness, f-Strings |
| `cheatsheet-schleifen.adoc` | `while`/`for`/`range`, `break`/`continue`, `enumerate`/`zip`, List Comprehensions |
| `cheatsheet-funktionen.adoc` | `def`, Parameter, Return, Typ-Hinweise, Docstrings, Scoping, Lambdas, Decorators |
| `prompting-guide.adoc` | Prompt-Templates für Erklären, Generieren, Debuggen, Reviewen, Lernen |
| `references.adoc` | Literatur- & Tool-Links (bestehend) |

---

### [05-beispiele/](./05-beispiele/)
**Code-Beispiele vom Dozenten** (Live-Coding & Nachschlagen)

| Datei | Lektion | Demo-Inhalt |
|-------|---------|-------------|
| `01-variablen_demo.py` | 1 | Typen, Operatoren, Strings, Kreisberechnung, Casting |
| `02-bedingungen_demo.py` | 2 | `input()`/`try/except`, BMI, Taschenrechner, logische Operatoren |
| `03-schleifen_demo.py` | 3 | `while`/`for`/`range`, `break`/`continue`, Zahlenraten, FizzBuzz, Gauß |
| `04-funktionen_demo.py` | 4 | Parameter-Varianten, Return/Tupel, Docstrings, Typ-Hinweise, Scoping, Lambdas, modularer Taschenrechner, Text-Analyse |

---

## ⏱️ Zeitplan

| Phase | Aktivität | Dauer |
|-------|-----------|-------|
| **Vor Tag 2** | Vorbereitung (Lesen, REPL, KI-Test) | 2–3 Std |
| **Tag 2 – 18:00–18:50** | Lektion 1: Variablen & Operatoren | 50 Min |
| **Pause** | | 10 Min |
| **19:00–19:50** | Lektion 2: Eingaben & Bedingungen | 50 Min |
| **Pause** | | 10 Min |
| **20:00–20:50** | Lektion 3: Schleifen | 50 Min |
| **Pause** | | 10 Min |
| **21:00–21:50** | Lektion 4: Funktionen | 50 Min |
| **Nach Tag 2** | Übungen + Hausaufgaben + Reflexion | 3–4 Std |

---

## 🔗 Verknüpfungen

- **Vorheriges Modul:** [Modul 1 – Programmier-Mindset & KI-Tools Setup](../modul-1-programmier-mindset-ki-tools-setup/)
- **Nächstes Modul:** [Modul 3 – Datenverarbeitung & Dateien](../modul-3-datenverarbeitung-dateien/)
- **Detaillierter Lektionsplan:** [LEKTIONSPLAN.md](./LEKTIONSPLAN.md)
- **Kurs-Übersicht:** [../README.md](../README.md)

---

## 🎓 Didaktische Prinzipien (wie Modul 1)

- **KI als fester Partner** in jeder Lektion (Exploration, Pair-Programming, Debugging, Review)
- **Live-Coding first** – keine Folien-Schlachten, sofortiges Ausprobieren
- **Fehlerkultur:** Bugs sind Lernmomente; KI hilft beim Verstehen, nicht beim Abkürzen
- **Typ-Hinweise früh** (PEP 484), aber nicht dogmatisch
- **Übungen bauen aufeinander auf** → am Ende steht ein modulare Taschenrechner mit Funktionen
- **Reflexion:** Was half KI? Was nicht? → Bewusstsein für Stärken/Schwächen schaffen

---

*Letzte Aktualisierung: 2026-10-07*  
*Basiert auf Modul-1-Vorlage (Programmier-Mindset & KI-Tools Setup)*