# Lektionsplan Modul 1: Programmier-Mindset & KI-Tools Setup

**Kursbeginn:** Heute, 18:00 Uhr  
**Dauer:** 4 Lektionen à 50 Minuten + Pausen  
**Setup:** Wird gemeinsam im Unterricht durchgeführt.

---

## Überblick

| Lektion | Titel                        | Kernbotschaft                                                                                         |
| ------- | ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1       | Was ist Programmieren?       | Programmieren = Probleme zerlegen + Anweisungen präzise formulieren. KI ist ein Partner, kein Ersatz. |
| 2       | KI-Begriffswelt              | Prompt, Command, Skill, Agent, Hook, LLM, RAG – Begriffe verstehen und unterscheiden.                 |
| 3       | Setup gemeinsam              | VS Code, Python, uv, OpenCode installieren und startklar machen.                                      |
| 4       | Erste Python-Schritte mit KI | Ein erstes Script ausführen, KI als Erklär-Partner nutzen, ethische Grundlagen.                       |

---

## Lektion 1: Was ist Programmieren? (18:00–18:50)

### Ziele

- Teilnehmende verstehen, dass Programmieren primär Denken ist, nicht Tippen.
- Sie können eine Alltagsaufgabe in kleine, eindeutige Schritte zerlegen.
- Sie erkennen, wo KI hilft und wo menschliche Strukturierung nötig bleibt.

### Ablauf (50 Min)

| Zeit  | Aktivität                                                                                                                                        | Methode                |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| 0–10  | Begrüssung, Erwartungen, Ablauf des Abends                                                                                                       | Kurzvorstellung        |
| 10–25 | **Live-Demo:** «Rezept für ein Sandwich» – eine Anweisung so präzise formulieren, dass ein Mitstudent sie wörtlich ausführt                      | Interaktiv, humorvoll  |
| 25–40 | **Diskussion:** Was ist der Unterschied zwischen menschlicher und Computer-Anweisung? Einführung: Programmieren = Zerlegen + Präzise Formulieren | Plenum                 |
| 40–50 | **KI-Bezug:** Wie verändert KI diesen Prozess? KI generiert Code, aber der Mensch muss das Problem verstehen und überprüfen.                     | Kurzvortrag + Beispiel |

### Materialien

- Whiteboard/Flipchart
- Beispiel aus `01-praxis/01-introduction.adoc` (adaptiert)

### Hausaufgabe (kurz)

- Notiere eine Alltagsaufgabe, die du in 5–7 Schritten zerlegen kannst.

---

## Lektion 2: KI-Begriffswelt (19:00–19:50)

### Ziele

- Teilnehmende kennen die zentralen Begriffe der KI-gestützten Entwicklung.
- Sie können Prompt, Command, Skill, Agent, Hook, LLM und RAG unterscheiden.

### Ablauf (50 Min)

| Zeit  | Aktivität                                                                                                                                                     | Methode                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| 0–10  | Wiederholung: Was ist Programmieren?                                                                                                                          | Kurzes Quiz              |
| 10–30 | **Begriffswelt erarbeiten:** Jeder Begriff wird an einem konkreten Beispiel erklärt.                                                                          | Interaktive Präsentation |
| 30–45 | **Live-Demo:** Ein Prompt an ChatGPT/Claude formulieren und das Ergebnis diskutieren. Unterschied: Prompt vs. Command vs. Skill (z. B. `/commit` in OpenCode) | Demo                     |
| 45–50 | Ausblick: In späteren Modulen bauen wir eigene Agents und Skills.                                                                                             | Kurzer Ausblick          |

### Begriffe (mit Beispielen)

| Begriff     | Einfache Erklärung                                                           | Beispiel                                           |
| ----------- | ---------------------------------------------------------------------------- | -------------------------------------------------- |
| **LLM**     | Groses Sprachmodell, das Texte versteht und erzeugt.                         | ChatGPT, Claude                                    |
| **Prompt**  | Eine Anweisung in natürlicher Sprache an ein KI-Modell.                      | «Erkläre mir Python-Variablen wie einem Anfänger.» |
| **Command** | Ein vordefinierter Befehl, der einen bestimmten Workflow auslöst.            | `/commit` in OpenCode                              |
| **Skill**   | Ein wiederverwendbares Wissenspaket oder Verhaltensmuster für einen Agenten. | Ein Skill für Code-Reviews                         |
| **Agent**   | Ein KI-System, das mehrere Schritte selbstständig plant und ausführt.        | Ein Agent, der Recherche + Zusammenfassung macht   |
| **Hook**    | Ein Ereignis, das einen Agenten oder Workflow auslöst.                       | «Bei jedem Push ins Git-Repo starte Tests.»        |
| **RAG**     | Retrieval-Augmented Generation: KI holt sich Wissen aus Dokumenten.          | Chatbot über eigene Unterlagen                     |

### Materialien

- `01-praxis/01-introduction.adoc` (Abschnitt Begriffe)
- Browser mit ChatGPT/Claude

### Übung (in Lektion 2 oder als Brücke zu Lektion 3)

- Jede/r formuliert einen Prompt zu einem Python-Begriff und tauscht sich mit der Nachbarin/dem Nachbarn aus.

---

## Lektion 3: Setup gemeinsam durchführen (20:00–20:50)

### Ziele

- Alle Teilnehmenden haben VS Code, Python, uv und OpenCode installiert oder wissen, was noch fehlt.
- Der Terminal/Command-Palette ist keine Angstzone mehr.

### Ablauf (50 Min)

| Zeit  | Aktivität                                                                                                | Methode       |
| ----- | -------------------------------------------------------------------------------------------------------- | ------------- |
| 0–5   | Warum Setup wichtig ist: Reproduzierbarkeit, professioneller Workflow                                    | Kurzvortrag   |
| 5–35  | **Schritt-für-Schritt-Setup** anhand der Checkliste. Der Dozent führt vor, die Teilnehmenden machen mit. | Hands-On      |
| 35–45 | **Check:** Python läuft? `uv --version`? OpenCode startet?                                               | Gruppen-Check |
| 45–50 | Puffer für Probleme, erste Hilfestellungen                                                               | Individuell   |

### Setup-Checkliste

- [ ] VS Code installiert und geöffnet
- [ ] Python 3.12 oder 3.13 installiert (`python --version` bzw. `python3 --version`)
- [ ] uv installiert (`uv --version`)
- [ ] OpenCode installiert und eingerichtet (`opencode --version`)
- [ ] Terminal in VS Code funktioniert
- [ ] Git ist installiert (für spätere Module)

### Materialien

- `01-praxis/lesson-01-cli-setup.md`
- `01-praxis/uv.adoc`
- `02-uebungen/cli-installation.md`
- `00-vorbereitung/backup-environments-quickstart.adoc` als Referenz

---

## Lektion 4: Erste Python-Schritte mit KI (21:00–21:50)

### Ziele

- Teilnehmende führen ein erstes Python-Script aus.
- Sie nutzen KI, um Code zu erklären und kleine Änderungen vorzuschlagen.
- Sie kennen die ersten ethischen Grundregeln.

### Ablauf (50 Min)

| Zeit  | Aktivität                                                                                                                                                | Methode                  |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| 0–10  | Erstes Python-Script öffnen: `05-beispiele/hello-world.py` ausführen                                                                                     | Demo + Nachmachen        |
| 10–25 | **KI als Erklär-Partner:** Script in ChatGPT/Claude einfügen und erklären lassen. Was macht jede Zeile?                                                  | Hands-On                 |
| 25–40 | **Kleine Änderung mit KI:** «Füge eine zweite Ausgabezeile hinzu» – Teilnehmende formulieren den Prompt, testen das Ergebnis und korrigieren bei Bedarf. | Hands-On                 |
| 40–50 | **Ethik & Regeln:** Was darf ich mit KI teilen? Datenschutz, Urheberrecht, Transparenz.                                                                  | Kurzvortrag + Diskussion |

### Materialien

- `05-beispiele/hello-world.py`
- Browser mit ChatGPT/Claude

### Hausaufgabe (03-nachbearbeitung)

- Persönliches Setup in 3–5 Sätzen dokumentieren.
- Drei sinnvolle KI-Fragen zu Python stellen und die Antworten kurz reflektieren: Was war hilfreich? Was war ungenau?

---

## Benötigte Materialien für den Abend

- Whiteboard / Flipchart
- Beamer für Demos
- Browser-Tab mit ChatGPT/Claude geöffnet
- OpenCode bereit für Demo
- `hello-world.py` geöffnet
- Setup-Checkliste als Handout oder aufgeteilt auf Folien

---

## Anpassungen gegenüber dem ursprünglichen Modul 1

- **Setup nicht als Vorarbeit, sondern als gemeinsame Lektion 3.**
- **OpenCode als zusätzliches CLI-Tool** neben VS Code, Python und uv.
- **Begriffswelt erweitert:** Prompt, Command, Skill, Agent, Hook, LLM, RAG.
- **Windsurf entfernt, OpenCode aufgenommen.**
- **Starke KI-Integration von Beginn an:** Jede Lektion nutzt KI als Lernpartner.

---

_Lektionsplan erstellt: 2026-10-06_
