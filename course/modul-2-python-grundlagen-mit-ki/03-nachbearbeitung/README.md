# Nachbearbeitung: Modul 2: Python-Grundlagen mit KI verstehen

**Zeitaufwand:** 3–4 Stunden bis Modul 3

---

## 1. Pflicht-Aufgaben (ca. 2 Std)

### A) Währungsrechner `waehrungsrechner.py` (45 Min)

Schreibe ein Programm, das:

1. Betrag in CHF einliest (`float`)
2. Wechselkurs EUR→CHF einliest (Default: 0.95, per `input` änderbar)
3. Umrechnung in **beide Richtungen** anbietet (Menü)
4. Ergebnis mit 2 Nachkommastellen ausgibt
5. **Funktionen** nutzt: `chf_zu_eur(betrag, kurs)`, `eur_zu_chf(betrag, kurs)`
6. Typ-Hinweise & Docstrings für alle Funktionen

**Beispiel:**
```
=== WÄHRUNGSRECHNER ===
Aktueller Kurs: 1 EUR = 0.95 CHF
1. CHF → EUR
2. EUR → CHF
3. Kurs ändern
4. Beenden

Wahl: 1
Betrag CHF: 100
100.00 CHF = 105.26 EUR
```

---

### B) Text-Analyse `textanalyse.py` (45 Min)

Schreibe ein Programm, das:

1. Einen Text vom Benutzer einliest (mehrzeilig, Ende mit leerer Zeile oder `STRG+D`)
2. Folgende Funktionen implementiert & aufruft:
   - `zaehle_zeichen(text)` – ohne Leerzeichen
   - `zaehle_woerter(text)` – `split()`
   - `zaehle_saetze(text)` – `.`, `!`, `?`
   - `haeufigste_woerter(text, n=5)` – `collections.Counter`
3. Ergebnisse übersichtlich ausgibt
4. **KI-Prompt:** `"Optimiere die Funktion haeufigste_woerter für grosse Texte (Generator, Speicher)."`

---

### C) Reflexionsbogen `reflexion.md` (30 Min)

Erstelle eine Datei `reflexion.md` mit deinen Antworten:

```markdown
# Reflexion Modul 2

## 1. Was war neu für mich?
- [ ] Variablen & Datentypen
- [ ] input() & Casting
- [ ] if/elif/else
- [ ] while / for / range
- [ ] Funktionen (def, return, Docstring, Typ-Hinweise)

## 2. Wo hat KI mir geholfen?
| Situation | Prompt | War hilfreich? (1-5) | Warum? |
|-----------|--------|---------------------|--------|
| z.B. Endlosschleife debuggen | "Finde den Bug..." | 4 | Zeigte fehlende Erhöhung |
| z.B. Docstring schreiben | "Google-Style Docstring..." | 5 | Vorlage war perfekt |

## 3. Wo hat KI **nicht** geholfen / falsch gelegen?
- ...

## 4. Mein grösster "Aha!"-Moment:
> ...

## 5. Was ich vor Modul 3 noch üben will:
- [ ] ...
```

---

## 2. Zusatz-Aufgaben (freiwillig, +1–2 Std)

### D) Erweitertes Zahlenraten `zahlenraten_pro.py`

- Highscore in `highscore.json` speichern (`json` Modul)
- Schwierigkeitsgrade mit unterschiedlichen Versuch-Limits
- Statistik: Ø-Versuche, Bestzeit, Spiele gesamt

### E) Projekt-Euler-Aufgabe #1

> Summe aller Vielfachen von 3 oder 5 unter 1000.

```python
# Mit Schleife
summe = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        summe += i

# Mit List Comprehension (Vorschau Modul 3)
summe = sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
```

**KI:** `"Erkläre mir den Unterschied zwischen der Schleifen- und der Generator-Version."`

### F) Eigene Idee

Setze eine kleine Idee um, die **nur** Modul-2-Wissen nutzt (z. B. Passwort-Generator, To-Do-Liste im Speicher, Unit-Converter).

---

## 3. Vorbereitung Modul 3 (Datenverarbeitung & Dateien)

- [ ] Lese: [Python Docs: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [ ] Verstehe: `open()`, `with`, `read()`, `readlines()`, `write()`
- [ ] KI: `"Zeige mir 3 Arten, eine CSV-Datei in Python zu lesen (csv, pandas, numpy)."`

---

## 4. Abgabe

**Bis Modul 3 (nächster Kurstag):**

1. `waehrungsrechner.py` in `03-nachbearbeitung/`
2. `textanalyse.py` in `03-nachbearbeitung/`
3. `reflexion.md` in `03-nachbearbeitung/`
4. Optional: `zahlenraten_pro.py`, Euler-Lösung, eigene Idee

**Format:** Dateien per GitHub Classroom / Moodle / E-Mail (lt. Dozent)

---

## 5. Bewertungskriterien (für Dozent)

| Kriterium | Gewichtung |
|-----------|------------|
| Funktionalität (läuft fehlerfrei) | 40% |
| Struktur (Funktionen, Typ-Hinweise, Docstrings) | 30% |
| KI-Nutzung dokumentiert & reflektiert | 20% |
| Code-Qualität (Namensgebung, Einrückung, Kommentare) | 10% |

---

*Datei: `03-nachbearbeitung/README.md`*  
*Zurück zum Modul: [Modul 2: Python-Grundlagen mit KI verstehen](../README.md)*