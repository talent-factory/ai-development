# Lektionsplan Modul 2: Python-Grundlagen mit KI verstehen

**Voraussetzung:** Modul 1 abgeschlossen (Setup funktionsfähig: VS Code, Python, uv, OpenCode) sowie Claude (Claude Code oder Browser)  
**Dauer:** 1 Tag (4 Lektionen à 50 Minuten + Pausen)

---

## Überblick

| Lektion | Titel | Kernbotschaft |
| ------- | ----- | ------------- |
| 1 | Variablen, Datentypen & Operatoren | Daten benennen, speichern und verknüpfen – KI hilft beim Erkunden. |
| 2 | Eingaben, Typumwandlung & Bedingungen | Programme reagieren auf Nutzer – `if`/`elif`/`else` strukturieren Entscheidungen. |
| 3 | Schleifen (`while`, `for`, `range`) | Wiederholungen automatisieren – Muster erkennen, KI als Debugging-Partner. |
| 4 | Funktionen definieren & wiederverwenden | Wiederverwendbare Bausteine bauen – Parameter, Rückgabe, Docstrings, KI-Review. |

---

## Lektion 1: Variablen, Datentypen & Operatoren (50 Min)

### Ziele
- Teilnehmende verstehen: Variable = Name für einen Speicherplatz mit Wert.
- Du unterscheidest `int`, `float`, `str`, `bool` und wendest Grundrechenarten an.
- Du nutzt KI, um Fehlermeldungen zu verstehen und Alternativen zu vergleichen.

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Rückblick Modul 1: Was hat geklappt? Was war unklar? | Kurzrunde |
| 5–20 | **Live-Coding:** Variablen anlegen, `print()`, `type()`, Rechenoperatoren (`+`, `-`, `*`, `/`, `//`, `%`, `**`), Strings verketten (`+`, `f-Strings`) | Demo + Mitmachen |
| 20–35 | **KI-Exploration:** Teilnehmende lassen sich von KI 3 Varianten für „Berechne Fläche eines Kreises“ zeigen, vergleichen und wählen die verständlichste. Dozent zeigt einmal, wie derselbe Prompt als Befehl `/erklaere` läuft (siehe Abschnitt Slash-Commands). | Paararbeit + KI |
| 35–45 | **Mini-Übung:** Eigene Variablen für: Alter, Körpergrösse, Lieblingsfarbe, Ist_Student – ausgeben mit `f-String`. | Einzelarbeit |
| 45–50 | Reflexion: Was war neu? Wo half KI? | Plenum |

### Materialien
- `01-praxis/lektion-1-variablen.md` (dieses Skript)
- `05-beispiele/01-variablen_demo.py`
- Claude (Browser oder Claude Code), OpenCode
- Slash-Command `/erklaere`
- Whiteboard für Typ-Übersicht

### Hausaufgabe (Brücke zu Lektion 2)
- Notiere 3 Alltagssituationen, in denen eine Entscheidung (ja/nein) getroffen wird.

---

## Lektion 2: Eingaben, Typumwandlung & Bedingungen (50 Min)

### Ziele
- `input()` nutzen, Rückgabe als `str` verstehen, in `int`/`float` umwandeln (`int()`, `float()`).
- Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`) und logische Operatoren (`and`, `or`, `not`).
- `if` / `elif` / `else` strukturiert einsetzen, Einrückung beachten.

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Wiederholung: `type()`, f-Strings – Kurze Demo durch TN | Plenum |
| 5–20 | **Live-Coding:** Eingabe → Umwandlung → Vergleich → Verzweigung. Beispiel: Altersprüfung, Notenbereich. | Demo + Mitmachen |
| 20–35 | **KI-Pair-Programming:** TN formulieren Prompt: „Schreibe ein Programm, das zwei Zahlen einliest und die grössere ausgibt – mit Fehlerbehandlung.“ Ergebnis testen, besprechen. Bewusst ohne Slash-Command: hier wird das freie Formulieren geübt. | Paararbeit + KI |
| 35–45 | **Mini-Übung:** BMI-Rechner: Gewicht & Grösse einlesen, BMI berechnen, Kategorie ausgeben (Untergewicht/Normal/Übergewicht). | Einzelarbeit |
| 45–50 | Sammlung: Typische Fehler (String vs. Int, Einrückung, `=` vs `==`) | Plenum |

### Materialien
- `01-praxis/lektion-2-bedingungen.md`
- `05-beispiele/02-bedingungen_demo.py`
- `02-uebungen/ex-01-taschenrechner.adoc`

### Hausaufgabe
- Schreibe ein Programm, das fragt: „Wie geht es dir?“ und auf „gut“, „mittel“, „schlecht“ unterschiedlich reagiert.

---

## Lektion 3: Schleifen – `while`, `for`, `range()` (50 Min)

### Ziele
- `while`-Schleife: Bedingung geprüft vor jedem Durchlauf, Abbruchbedingung zwingend.
- `for`-Schleife über `range()`, Listen, Strings.
- `break`, `continue` kennen. KI nutzt, um Endlosschleifen zu finden.

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Quiz: Was macht `range(3)`? `range(1, 5)`? `range(0, 10, 2)`? | Mentimeter/Handzeichen |
| 5–20 | **Live-Coding:** Zahlenraten-Spiel (`while`), Summe 1–100 (`for`), Multiplikationstabelle (verschachtelt). | Demo + Mitmachen |
| 20–35 | **KI-Debugging:** TN erhalten Code mit Endlosschleife & Off-by-One-Fehler. KI soll Fehler finden & erklären. Korrigieren & testen. Einstieg mit `/debug` (Fehlermeldung und Code hinter den Befehl einfügen). | Gruppenarbeit + KI |
| 35–45 | **Mini-Übung:** „FizzBuzz“: 1–100 ausgeben, bei 3 „Fizz“, bei 5 „Buzz“, bei 15 „FizzBuzz“. | Paararbeit |
| 45–50 | Vergleich: `while` vs. `for` – wann was? Merksatz bilden. | Plenum |

### Materialien
- `01-praxis/lektion-3-schleifen.md`
- `05-beispiele/03-schleifen_demo.py`
- `02-uebungen/ex-02-zahlenraten.adoc`
- Slash-Command `/debug`

### Hausaufgabe
- Erstelle ein Muster deiner Wahl mit verschachtelten Schleifen (z. B. Pyramide, Weihnachtsbaum).

---

## Lektion 4: Funktionen – Definieren, Parameter, Rückgabe, Docstrings (50 Min)

### Ziele
- `def name(parameter):` – Aufbau verstehen: Signatur, Körper, `return`.
- Parameter mit Default-Werten, Typ-Hinweise (optional), mehrere Rückgabewerte (Tupel).
- Docstring (`"""..."""`) als Dokumentation & KI-Kontext.
- KI als Code-Review: „Prüfe diese Funktion auf Lesbarkeit, Typsicherheit, Randfälle.“

### Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Warum Funktionen? DRY, Lesbarkeit, Testbarkeit – 3-Satz-Impuls | Kurzvortrag |
| 5–20 | **Live-Coding:** `quadrat(zahl)`, `begruesse(name="Gast")`, `min_max(liste)` → Tupel. Docstring zeigen, `help()` nutzen. | Demo + Mitmachen |
| 20–35 | **KI-Code-Review:** TN schreiben eine Funktion für „Währungsrechner EUR→CHF“. KI prüft: Typ-Hinweise, Docstring, Edge-Cases (negativ, None). Überarbeitung. Pflicht-Review mit `/review` (Checkliste ist im Command enthalten). | Einzelarbeit + KI |
| 35–45 | **Mini-Projekt:** „Taschenrechner-Funktionen“: `add`, `sub`, `mul`, `div` (mit ZeroDivision-Check), `main()`-Menü. | Paararbeit |
| 45–50 | Ausblick Modul 3: Daten aus Dateien lesen → Funktionen wiederverwenden. Reflexionsbogen austeilen. | Plenum |

### Materialien
- `01-praxis/lektion-4-funktionen.md`
- `05-beispiele/04-funktionen_demo.py`
- `02-uebungen/ex-03-funktionen.adoc`
- `03-nachbearbeitung/reflexionsbogen.md`
- Slash-Command `/review`

---

## Slash-Commands (Modul 2)

Drei Befehle, die die Prompts aus `04-materialien/prompting-guide.adoc` als Befehl bereitstellen:

| Command | Lektion | Zweck |
| ------- | ------- | ----- |
| `/erklaere` | 1 (Demo), 3 | Code Zeile für Zeile erklären lassen |
| `/debug` | 3 | Fehlermeldung und Code analysieren, ohne komplette Lösung |
| `/review` | 4 (Pflicht) | Checkliste: Typ-Hinweise, Docstring, Edge-Cases, Lesbarkeit; drei Verbesserungen |

**Ablage:** `.claude/commands/` (Claude Code) und `.opencode/commands/` (OpenCode) im Repo-Root. Beide Verzeichnisse enthalten identische Dateien. Symlinks werden nicht verwendet, da sie unter Windows nicht zuverlässig funktionieren. Änderungen immer in beiden Verzeichnissen vornehmen.

**Start:** Claude Code bzw. OpenCode aus dem Repo-Root starten, sonst werden die Commands nicht gefunden.

**Fallback ohne Abo:** Jeder Command entspricht einem Prompt im Prompting-Guide und kann dort kopiert und im Browser eingefügt werden.

---

## Benötigte Materialien für den Tag

- Whiteboard / Flipchart
- Beamer für Live-Coding
- Je TN: Laptop mit funktionsfähigem Setup (Modul 1), Claude Code oder Browser-Zugang zu Claude
- Browser-Tab: Claude; OpenCode-Docs
- Beispiel-Dateien in `05-beispiele/` vorbereitet & getestet
- Übungsblätter in `02-uebungen/` (gedruckt oder digital)
- Reflexionsbögen in `03-nachbearbeitung/`

---

## Anpassungen gegenüber klassischem Python-Grundkurs

- **KI als fester Partner** in jeder Lektion (Exploration, Pair-Programming, Debugging, Review).
- **Keine Folien-Schlachten** – Live-Coding + sofortiges Ausprobieren.
- **Fehlerkultur:** Bugs sind Lernmomente; KI hilft beim Verstehen, nicht beim Abkürzen.
- **Typ-Hinweise** früh eingeführt (PEP 484), aber nicht dogmatisch.
- **Übungen bauen aufeinander auf** → am Ende steht ein kleiner Taschenrechner mit Funktionen.

---

_Lektionsplan erstellt: 2026-10-07_