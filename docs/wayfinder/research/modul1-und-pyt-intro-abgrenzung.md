# Ist-Stand Modul 1 und Abgrenzung zu pyt-intro-2025 (Ticket 11)

**Frage:** Was hat Modul 1 tatsächlich an Python und Prompting vermittelt? Was deckt `pyt-intro-2025` Modul 2-4 ab? Welche Beispiele und Übungen darf Modul 2 (neu) nicht 1:1 kopieren?

**Quellen (alle lokal gelesen):**
- Modul 1: `/Users/daniel/GitRepository/ai-development/course/modul-1-programmier-mindset-ki-tools-setup/`
- pyt-intro-2025: `/Users/daniel/GitRepository/pyt-intro-2025/` (letzter Commit `d5da5aa`, 2026-06-02)
- Ziel Modul 2 neu: `/Users/daniel/GitRepository/ai-development/docs/wayfinder/modul-2-6-map.md` (Abschnitte «Notes», «Decisions so far»)
- Der verworfene Altentwurf `course/modul-2-*/` wurde bewusst ignoriert.

---

## 1. Was Modul 1 tatsächlich vermittelt hat

### 1.1 Python-Konzepte: praktisch keine Syntax

Modul 1 ist ein Setup- und Mindset-Modul. Python-Syntax kommt nur in Lektion 4 vor, und dort nur als Lesestoff, nicht als Lernziel.

| Konzept | Beleg | Tiefe |
|---|---|---|
| Script mit `uv run streamlit run ...` starten | `01-praxis/lektion-4-erste-python-schritte.md` (Abschnitt «Erstes Python-Script») | ausführen, nicht schreiben |
| `import` (streamlit, pandas, numpy) | gleiche Datei; Prompt «Wozu dienen die Imports `pandas` und `numpy`? Werden sie hier bereits verwendet?» | nur als Erkenntnis «ungenutzte Imports erkennen» |
| Funktionsaufruf mit String-Argument (`st.title("..")`, `st.write("..")`) | gleiche Datei | nur gelesen |
| `python --version`, Python 3.12/3.13, `uv` | `01-praxis/lektion-3-arbeitsumgebung.md` | reines Setup |
| Wochentag per KI ergänzen (Änderungsaufgabe) | `lektion-4-...md`, Abschnitt «Kleine Änderung mit KI» | KI schreibt, Teilnehmende testen |
| Namen und Gruss anzeigen (Hausaufgabe) | `lektion-4-...md`, Abschnitt «Hausaufgabe» | KI schreibt |

**Nicht vermittelt** (kein Beleg in irgendeiner Modul-1-Datei): Variablen, Datentypen, `print`/`input`, `if`, `for`/`while`, eigene Funktionen, Listen/Dicts, `try/except`. Die Wörter fallen nur in KI-Prompts als Themen: «Erkläre mir in 3 Sätzen, was eine Variable in Python ist» (`lektion-2-ki-begriffswelt.md`, Demo 1) und «Was ist eine Schleife in Python?» (ebd., Übung). Die Antworten holt sich die KI, Modul 1 erklärt sie nicht.

`01-praxis/lektion-1-was-ist-programmieren.md` ist konzeptionell: Programmierprozess in 6 Schritten (Problem verstehen, Zerlegen, Logik, Code, Testen, Verbessern), Alltagsaufgabe in 5-7 Schritte zerlegen. Es enthält keinen Code.

### 1.2 Prompting-Techniken, die Modul 1 eingeführt hat

| Technik | Beleg |
|---|---|
| Code einfügen und «Zeile für Zeile, als wäre ich Anfänger» erklären lassen (Zielgruppen-Rolle) | `lektion-4-...md`, «KI als Erklär-Partner» |
| Gezielte Nachfrage zu einem Detail (Imports, werden sie verwendet?) | ebd., «Weiterer Prompt» |
| Format-Vorgabe («Gib mir nur den geänderten Code zurück») | ebd., «Kleine Änderung mit KI» |
| Fehlerschleife: Fehlermeldung an die KI weitergeben, Lösung anfordern | ebd., Vorgehen Schritt 4 |
| Promptqualität bewerten: konkret, kurz, Kontext, Zielgruppe, Tiefe, Format | `lektion-2-ki-begriffswelt.md`, Demo 1 und Übung (Zweiergruppen bewerten Prompts) |
| Begriffe LLM, Prompt, Command, Skill, Agent, Hook, RAG; OpenCode-Slash-Command `/commit` | `lektion-2-...md`, `LEKTIONSPLAN.md` |
| Kritisches Prüfen («KI halluziniert», «Mensch muss den Code verstehen und überflüssige Teile erkennen») | `lektion-4-...md`, Erkenntnis und Ethik-Grundsatz 5 |
| Ethik: keine Passwörter/Kundendaten in öffentliche KI, Urheberrecht, Transparenz, Verantwortung | `lektion-4-...md`, «Ethik & Regeln» |

### 1.3 Auffälligkeiten (für die Planung relevant)

1. **Lektionstext und Beispieldatei weichen ab.** Die Lektion zeigt `hello-world.py` mit 5 Zeilen (`st.title`, `st.write`). Die echte Datei `05-beispiele/hello-world.py` ist rund 40 Zeilen lang: LaTeX, `st.code` mit Python- und Java-Snippet (`def hello(): print("Hello, Streamlit!")`), `pd.DataFrame(np.random.randn(30, 10), columns=(f"col {i}" ...))`, `st.metric`. Sie enthält ein f-String und einen Generator-Ausdruck, also Syntax, die Modul 1 nie erklärt hat. Wer Modul 1 «durchgemacht» hat, kennt diese Datei höchstens oberflächlich.
2. **Die Nachbearbeitung ist leer.** `03-nachbearbeitung/README.md` sagt «noch keine Dateien» (nur `.gitkeep`). Das Modul-README (`README.md`, Abschnitt `03-nachbearbeitung`) verspricht trotzdem «Persönliches Setup dokumentieren» und «Drei KI-Fragen zu Python mit Reflexion». Die Hausaufgabe steht nur am Ende von Lektion 2 und 4. Es gibt also keinen Nachweis, dass die Studierenden irgendetwas Python-Spezifisches geübt haben.
3. **Übungen:** `02-uebungen/` enthält nur `cli-installation.md` (Setup), keine Python-Übung. Das Modul-README nennt «Ein einfaches Python-Script ausführen und mit KI erklären lassen» als Übung, die Datei dazu fehlt.
4. `LEKTIONSPLAN.md` (Lektion 4) sagt «Füge eine zweite Ausgabezeile hinzu», die Lektion selbst sagt «aktueller Wochentag». Kleine Inkonsistenz, ohne Folgen für Modul 2.
5. `README.md` von Modul 1 nennt unter Inhalten «Einfache Berechnungen mit Python». Im gesamten Modul gibt es dafür keine Datei (nicht weiter geprüft, ob der Satz nur Planung war).

**Fazit Modul 1:** Voraussetzung für Modul 2 ist nur Tooling (VS Code, Python, uv, OpenCode), das Erklär-Prompting aus Lektion 4 und das Ethik-Grundgerüst. Modul 2 darf **keine** Python-Syntax als bekannt voraussetzen, aber den Prompt-Zyklus «Code einfügen, erklären lassen, nachfragen, kleine Änderung, Fehlermeldung zurückgeben» als Wiederholung aufgreifen, statt neu einzuführen.

---

## 2. Was pyt-intro-2025 Modul 2-4 abdeckt

Alle drei Module haben die Struktur `00-vorbereitung/`, `01-praxis/` (4 Lektionen), `02-uebungen/`, `03-nachbearbeitung/`, `04-materialien/`, `05-beispiele/`. Kernaussage jeder Lektion: Theorie 15 Min, Live-Coding 20 Min, Übung 15 Min. Didaktik: **selbst schreiben**, nicht lesen und erklären lassen. KI kommt erst in Modul 6 (`modul-6-ki-programmieren/`, nicht Teil dieser Abgrenzung).

### 2.1 Modul 2 «Datentypen» (`/Users/daniel/GitRepository/pyt-intro-2025/modul-2-datentypen/`)

- **Themen** (`README.md`, `01-praxis/lektion-1..4`): Strings (Indexing, Slicing, Methoden, f-Strings), Booleans/Vergleiche/`and`/`or`/`not`, Typkonvertierung (`int()`, `float()`, `str()`, `bool()`), `input`/`print`, interaktive Programme, Validierung mit String-Methoden und `try/except ValueError` (`lektion-4-interaktive-programme.md`, Abschnitt 1.2).
- **Live-Beispiele der Lektionen:** Namensschild-Generator, Text-Analyse, String-Manipulation (L1); Alterscheck, Zugangskontrolle (`Alter >= 18 UND Ticket ODER Mitglied`), String-Vergleiche (L2); Einfacher Rechner, Personalisierte Begrüssung, Typ-Demonstrator (L3); BMI-Rechner, Passwort-Validator, Text-Statistik (L4).
- **Beispieldateien** (`05-beispiele/`): `strings.py`, `vergleiche.py`, `typkonvertierung.py`, `input_output.py`, `formatierung.py`, `tabelle.py`, `textstatistik.py`, `email_validator.py`, `passwort_validator.py`.
- **Übungen** (`02-uebungen/`): 1 Textformatierung, 2 Vergleiche und Bedingungen, 3 Benutzereingaben verarbeiten, 4 Interaktiver Rechner, 5 String-Methoden, 6 Formatierung, 7 Input-Validierung, 8 Textanalyse.
- **Nachbereitung** (`03-nachbearbeitung/`): Textanalyse-Tool, Eingabe-Validator, Interaktives Quiz, Reflexion.

### 2.2 Modul 3 «Kontrollstrukturen» (`.../modul-3-kontrollstrukturen/`)

- **Themen** (`README.md`, `01-praxis/`): `if/elif/else`, ternärer Operator, `while` (Zähler, Akkumulator, `break`/`continue`), `for` über Listen/`range`/`enumerate`/`zip`, List Comprehensions (Einführung), verschachtelte Schleifen und Muster, Listen-Operationen, `try/except` in einer `while`-Eingabeschleife (`lektion-2-while-schleifen.md`, Beispiel 3 «Eingabe validieren»).
- **Live-Beispiele:** Alterscheck, Notensystem, Rabatt-Rechner (L1); Countdown, Summe berechnen, Eingabe validieren, Zahlenraten (L2); Multiplikationstabelle, Einkaufsliste, Statistik berechnen (L3); Muster zeichnen (Dreieck, Pyramide), Schachbrett, Primzahlen, Mini-Projekt «Kontakt-Manager» oder «Zahlenraten» (L4).
- **Beispieldateien** (`05-beispiele/`): `bedingungen.py`, `notensystem.py`, `while_schleifen.py`, `zahlenraten.py`, `for_schleifen.py`, `listen.py`, `einkaufsliste.py`, `gerade_zahlen.py`, `notenliste.py`, `verschachtelt.py`, `muster.py`, `primzahlen.py`, `menu.py`.
- **Übungen:** 1 Notensystem (Punkte 90-100 = Note 6 usw.), 2 Rabatt-Rechner, 3 Fakultät, 4 Zahlenraten, 5 Gerade Zahlen filtern, 6 Notenliste, 7 Multiplikationstabelle, 8 Zahlen-Pyramide.
- **Nachbereitung:** Zahlenspiel, Einkaufsliste, Primzahlen-Finder, Reflexion.

### 2.3 Modul 4 «Funktionen & Datenstrukturen» (`.../modul-4-funktionen-datenstrukturen/`)

- **Themen** (`README.md`, `01-praxis/`): Funktionen definieren, Parameter, `return`, Default-Parameter, Listen und Listen-Methoden, Dictionaries, Tupel/Sets, Tests mit `pytest`.
- **Live-Beispiele:** Einfache Begrüssung (`begruessung()`), Mehrere Funktionen, Funktionen in Schleifen (L1); Berechnung mit Return, Mehrere Parameter, Default-Parameter, Funktionen kombinieren (L2); Listen filtern/transformieren, Kontakte mit Dictionary, Datenstruktur wählen (L3); `ist_gerade()`, `berechne_durchschnitt()`, `erstelle_kontakt()` testen (L4).
- **Beispieldateien** (`05-beispiele/`): `01-begruessung.py`, `02-mehrere-funktionen.py`, `03-funktionen-in-schleifen.py`, `addiere.py`, `funktionen_basis.py`, `parameter.py`, `listen_operationen.py`, `dictionaries.py`, `tupel_sets.py`, `notensystem_improved.py`, `testen_beispiel.py`, `kontaktverwaltung.py`, `notenverwaltung.py`, `woerterbuch.py`, `datenanalyse.py`, `einkaufsliste_advanced.py`.
- **Übungen:** 1 Einfache Funktionen, 2 Funktionen mit Return, 3 Parameter-Varianten, 4 Funktionen und Listen, 5 Listen-Methoden, 6 Dictionary-Operationen (Dict `buch` mit titel/autor/jahr/seiten), 7 Erste Tests schreiben, 8 Tests für Kontakte.
- **Nachbereitung:** Kontaktverwaltung, Notenverwaltung, Deutsch-Englisch-Wörterbuch, Reflexion.

### 2.4 Überschneidung mit dem Modul-2-Wortschatz (neu)

Der Wortschatz von Modul 2 neu (Variablen/Typen, Ein-/Ausgabe, `if/elif/else`, `for/while`, Funktionen, Listen/Dicts lesend, `try/except`) liegt **vollständig innerhalb** von pyt-intro-2025 Modul 2-4. Inhaltlich gibt es also keine Lücke und kein Alleinstellungsmerkmal beim Stoff. Der Unterschied liegt allein in der Methode (lesen, vorhersagen, KI erklären lassen und prüfen, statt selbst schreiben). Wer pyt-intro-2025 absolviert hat, kennt den Stoff und soll in Modul 2 nicht dieselben Programme wiedererkennen. Wer es nicht hat (Quereinsteiger), muss den Stoff trotzdem nicht auswendig können, aber verstehen. Beide Gruppen profitieren von unbekanntem Code.

---

## 3. Ableitung: Was Modul 2 (neu) nicht 1:1 kopieren darf

### 3.1 Regel

Kein Beispiel, keine Übung und kein Challenge-Code aus `pyt-intro-2025` Modul 2-4 darf mit gleichem **Szenario und gleicher Lösungsstruktur** übernommen werden. Gleiche Konzepte sind erlaubt, gleiche Programme nicht. Grund: Teilnehmende mit pyt-intro-Vorkenntnissen (`modul-2-6-map.md`, Notes) erkennen das Programm sofort, überspringen das «Vorhersagen» und die Methodik «lesen und prüfen» läuft ins Leere. Zusätzlich vermischen sich die Lösungen aus pyt-intro mit dem Challenge-Ziel (Challenge-Code enthält absichtlich einen Fehler, den die KI-Erklärung übersieht): ein bekanntes Programm macht den Fehler leichter oder gar nicht mehr zu finden.

### 3.2 Zu meidende Szenarien (Sperrliste)

Konzeptweise geordnet, jeweils mit Quelle. Diese Szenarien tauchen in pyt-intro-2025 als Lektionsbeispiel, Beispieldatei oder Übung auf und sollen in Modul 2 neu **nicht** als Kernbeispiel dienen.

| Konzept in Modul 2 neu | Nicht verwenden (Szenario) | Quelle in pyt-intro-2025 |
|---|---|---|
| Variablen/Typen, Ein-/Ausgabe | Namensschild, Personalisierte Begrüssung, Einfacher Rechner (zwei Zahlen addieren), Typ-Demonstrator, BMI-Rechner, Textstatistik | `modul-2-datentypen/01-praxis/lektion-1..4`, `05-beispiele/{strings,typkonvertierung,input_output,textstatistik}.py`, Übungen 1, 3, 4, 8 |
| Ein-/Ausgabe, Validierung, `try/except` | Passwort-Validator, E-Mail-Validator, Eingabe-Validierung mit `int(input())` in `while True` + `except ValueError` | `modul-2-datentypen/05-beispiele/{passwort,email}_validator.py`, `uebung-7-validierung.md`, `aufgabe-2-validator.md`, `modul-3-kontrollstrukturen/01-praxis/lektion-2-while-schleifen.md` (Beispiel 3) |
| `if/elif/else` | Alterscheck, Zugangskontrolle, Notensystem (Punkte zu Note), Rabatt-Rechner | `modul-2-datentypen/01-praxis/lektion-2-booleans.md`, `modul-3-kontrollstrukturen/01-praxis/lektion-1-bedingungen.md`, `uebung-1-notensystem.md`, `uebung-2-rabatt.md`, `05-beispiele/{bedingungen,notensystem}.py` |
| `while` | Countdown, Summe berechnen, Zahlenraten (inkl. `random.randint`, `break`), Menü-Schleife | `modul-3-kontrollstrukturen/01-praxis/lektion-2-while-schleifen.md`, `uebung-4-zahlenraten.md`, `aufgabe-1-zahlenspiel.md`, `05-beispiele/{zahlenraten,menu,while_schleifen}.py` |
| `for`, Listen | Multiplikationstabelle, Einkaufsliste, Notenliste/Durchschnitt, Gerade Zahlen filtern, Fakultät, Primzahlen, Muster/Pyramide/Schachbrett | `modul-3-kontrollstrukturen/01-praxis/lektion-3,4`, `uebung-3,5,6,7,8`, `aufgabe-2,3`, `05-beispiele/{for_schleifen,listen,einkaufsliste,gerade_zahlen,notenliste,primzahlen,muster,verschachtelt}.py` |
| Funktionen | `begruessung()`, `addiere()`, `ist_gerade()`, `berechne_durchschnitt()`, Funktion mit Default-Parameter, «Funktionen in Schleifen» | `modul-4-funktionen-datenstrukturen/01-praxis/lektion-1,2`, `05-beispiele/{01-begruessung,02-mehrere-funktionen,03-funktionen-in-schleifen,addiere,funktionen_basis,parameter}.py`, `uebung-1,2,3` |
| Dicts/Listen lesend | Kontaktverwaltung, Notenverwaltung, Deutsch-Englisch-Wörterbuch, Dict `buch` (titel/autor/jahr/seiten), Kontakte als Dict | `modul-4-funktionen-datenstrukturen/01-praxis/lektion-3-listen.md`, `05-beispiele/{dictionaries,kontaktverwaltung,notenverwaltung,woerterbuch,notensystem_improved}.py`, `uebung-6-dict.md`, `aufgabe-1,2,3` |

**Merkmale, die zusätzlich Wiedererkennung auslösen** (also auch in neuen Beispielen vermeiden): Beispielnamen wie «Max Muster», Noten 2-6 mit Grenzen 90/80/70/60, die Folge `range(1, 11)` für Einmaleins, die Funktionsnamen auf Deutsch aus der Sperrliste und Ausgabebanner wie `"=" * 50`.

### 3.3 Konkrete Grenzfälle

- **Zahlenraten, Notensystem, Rabatt:** in pyt-intro sehr prominent (Beispieldatei **und** Übung **und** Hausaufgabe). Auch in abgewandelter Form riskant. Falls trotzdem gewünscht, andere Domäne und andere Logik wählen, nicht nur Zahlen austauschen.
- **BMI und Passwort-Validator:** Klassiker, die Studierende auch aus anderen Kursen kennen. Für Modul 2 neu ungeeignet als «unbekannter» Code.
- **`try/except ValueError` um `int(input())`:** das ist die einzige `try/except`-Form in pyt-intro 2-4. Modul 2 neu kann `try/except` lesen lassen, sollte aber andere Fehlerarten wählen (`KeyError`, `ZeroDivisionError`, `FileNotFoundError`-Meldung als Lesehilfe), die in pyt-intro 2-4 nicht vorkommen. Hinweis: `FileNotFoundError` und Dateien gehören in pyt-intro zu Modul 5 (`modul-5-dateien-module/`), das nicht Teil dieser Inventur ist. Vor einer Entscheidung dort gegenprüfen.
- **Streamlit-`hello-world`:** gehört zu Modul 1. Nicht als Modul-2-Einstieg wiederverwenden, sonst wirkt Modul 2 wie eine Fortsetzung von «Titel anzeigen».
- **Tests/pytest:** pyt-intro Modul 4 behandelt sie (`lektion-4-testing.md`). Modul 2 neu schliesst Testing laut `modul-2-6-map.md` aus, es entsteht also keine Kollision.

### 3.4 Was Modul 2 neu ausdrücklich übernehmen darf

- **Konzepte und Wortschatz** (siehe 2.4): Der Stoff darf identisch sein, nur die Aufgabenstellung unterscheidet sich.
- **Didaktik aus Modul 1:** den Erklär-Prompt, die Fehlerschleife und die Prompt-Bewertung (konkret, Kontext, Format) wiederholen und vertiefen (Beleg 1.2), statt sie neu einzuführen.
- **Cheatsheet-Idee:** Referenzblätter wie `pyt-intro-2025/modul-*/04-materialien/cheatsheet-*.md` sind als Nachschlagehilfe unproblematisch, solange die Beispiele darin nicht Kernmaterial der Lektion werden (nicht im Detail geprüft).

### 3.5 Empfehlungen für Ticket-Folgearbeit

1. Neue Modul-2-Beispiele aus **realistischen, kurzen Alltagsskripten** (20-40 Zeilen, siehe Kernziel in `modul-2-6-map.md`) ableiten, die in keinem der Sperrlisten-Szenarien liegen, z. B. Log-Auswertung, Kassenbon, Stundenplan, Zeit-/Datumsrechnung, Textbausteine.
2. Vor dem Ausformulieren jedes Beispiels gegen Abschnitt 3.2 prüfen (Szenario **und** Lösungsstruktur). Einfache Prüfung: `grep -ril "<Stichwort>" /Users/daniel/GitRepository/pyt-intro-2025/modul-{2,3,4}-*` auf Funktions- und Variablennamen des geplanten Beispiels.
3. Der Challenge-Code (mit absichtlichem Fehler) darf besonders nicht aus pyt-intro stammen, da deren `<details>`-Musterlösungen den korrekten Code enthalten und Studierende ihn kennen könnten.
4. In der Modul-2-Einleitung kurz benennen, dass Quereinsteiger und pyt-intro-Absolvent:innen denselben Wortschatz üben, aber andere Aufgaben bekommen. Das entschärft die Heterogenität.

### 3.6 Grenzen dieser Recherche

- pyt-intro Modul 5 (Dateien/Module, `try/except`, JSON) und 6 (KI) wurden **nicht** inventarisiert, nur deren Existenz geprüft.
- Beispieldateien und Übungen wurden anhand von Titeln, Docstrings, Lektionsüberschriften und Stichproben (Notensystem-Übung, Dict-Übung, `begruessung`, `zahlenraten`) geprüft, nicht jede Zeile gelesen. Die Sperrliste beruht auf Themen und Titeln. Eine Zeilen-Feinprüfung steht pro neues Beispiel an (siehe 3.5, Punkt 2).
- Die PDF/PPTX in `modul-1-*/04-materialien/` (`00 Einführung Basic.pdf`, `01 Einführung Development.pptx`) wurden nicht geöffnet. Falls dort Python-Folien existieren, gelten sie als nicht inventarisiert.
