# Lektion 2: KI-Begriffswelt

**Dauer:** 50 Minuten  
**Ziel:** Die zentralen Begriffe der KI-gestützten Entwicklung verstehen und unterscheiden.

---

## 🎯 Lernziele

Nach dieser Lektion können die Teilnehmenden:

- Die Begriffe LLM, Prompt, Command, Skill, Agent, Hook und RAG erklären.
- Einordnen, welches KI-Tool für welche Aufgabe geeignet ist.
- Einen sinnvollen Prompt an ein KI-Chat-Tool formulieren.
- Den Unterschied zwischen Chat-, Command- und Agent-Workflows benennen.

---

## ⏱️ Zeitplan

| Zeit      | Phase              | Inhalt                                                 |
| --------- | ------------------ | ------------------------------------------------------ |
| 0–5 min   | Wiederholung       | Kurzes Quiz: Was ist Programmieren?                    |
| 5–25 min  | Begriffswelt       | LLM, Prompt, Command, Skill, Agent, Hook, RAG          |
| 25–40 min | Live-Demo          | Prompt an ChatGPT/Claude; `/commit` in OpenCode zeigen |
| 40–50 min | Übung & Diskussion | Teilnehmende formulieren eigene Prompts                |

---

## 📖 Begriffswelt

| Begriff     | Einfache Erklärung                                                           | Beispiel                                           |
| ----------- | ---------------------------------------------------------------------------- | -------------------------------------------------- |
| **LLM**     | Grosses Sprachmodell, das Texte versteht und erzeugt.                        | ChatGPT, Claude                                    |
| **Prompt**  | Eine Anweisung in natürlicher Sprache an ein KI-Modell.                      | «Erkläre mir Python-Variablen wie einem Anfänger.» |
| **Command** | Ein vordefinierter Befehl, der einen bestimmten Workflow auslöst.            | `/commit` in OpenCode                              |
| **Skill**   | Ein wiederverwendbares Wissenspaket oder Verhaltensmuster für einen Agenten. | Ein Skill für Code-Reviews                         |
| **Agent**   | Ein KI-System, das mehrere Schritte selbstständig plant und ausführt.        | Ein Agent, der Recherche + Zusammenfassung macht   |
| **Hook**    | Ein Ereignis, das einen Agenten oder Workflow auslöst.                       | «Bei jedem Push ins Git-Repo starte Tests.»        |
| **RAG**     | Retrieval-Augmented Generation: KI holt sich Wissen aus Dokumenten.          | Chatbot über eigene Unterlagen                     |

### Hintergrund aus `01-introduction.adoc`

KI (Artificial Intelligence) ist ein breites Feld der Informatik, das sich mit der Schaffung von Maschinen oder Programmen beschäftigt, die Arbeitsweisen des menschlichen Gehirns nachahmen können, um Probleme zu lösen oder bestimmte Aufgaben durchzuführen.

Wichtige Teilbereiche:

- **Machine Learning:** Algorithmen lernen aus Daten.
- **Deep Learning:** Neuronale Netze mit vielen Schichten.
- **Neural Networks:** Von der Hirnstruktur inspirierte Algorithmen.
- **Robotics:** KI-gesteuerte Roboter.

> Weiterführende Details und Übungen zur Begriffswelt befinden sich in `01-praxis/01-introduction.adoc`.

---

## 🔧 KI-Tools für Entwickler

| Tool                 | Typ             | Einsatz                                     |
| -------------------- | --------------- | ------------------------------------------- |
| **ChatGPT / Claude** | Chat-Interface  | Erklärungen, Code-Entwürfe, Debugging-Hilfe |
| **GitHub Copilot**   | IDE-Integration | Code-Vervollständigung im Editor            |
| **Cursor**           | KI-Editor       | Chat + Edit direkt im Code                  |
| **OpenCode**         | KI-CLI / Editor | Slash-Commands, Skills, Agent-Workflows     |

**Wichtig:** Tools ändern sich schnell. Das Prinzip – präzise Anweisungen geben und Ergebnisse prüfen – bleibt.

---

## 🎬 Live-Demo (15 Min)

### Demo 1: Prompt an ChatGPT/Claude

```text
Prompt: "Erkläre mir in 3 Sätzen, was eine Variable in Python ist.
Nutze ein Alltagsbeispiel."
```

**Diskussion:**

- Was macht den Prompt gut? (Konkret, kurz, Kontext)
- Was könnte man verbessern? (Zielgruppe, Tiefe, Format)

### Demo 2: Command in OpenCode

```bash
/commit
```

Zeigen, wie ein Slash-Command einen Workflow auslöst (z. B. Commit-Nachricht generieren).

**Diskussion:**

- Was ist der Unterschied zwischen einem Prompt und einem Command?
- Wann nutzt man was?

---

## ✍️ Übung (10 Min)

1. Jede/r formuliert einen Prompt zu einem der folgenden Themen:
   - «Was ist eine Schleife in Python?»
   - «Erkläre mir den Unterschied zwischen einem Agent und einem Skill.»
   - «Wie installiere ich Python auf macOS?»
2. In Zweiergruppen: Tauscht die Prompts aus und bewertet sie.
   - Ist der Prompt klar?
   - Fehlt Kontext?
   - Ist das gewünschte Format angegeben?

---

## 📚 Materialien

- `01-praxis/01-introduction.adoc`
- Browser mit ChatGPT/Claude
- OpenCode für Command-Demo

---

## 🏠 Hausaufgabe (Nachbereitung)

- Formuliere drei sinnvolle KI-Fragen zu Python.
- Speichere die Antworten und schreibe zu jeder 2–3 Sätze Reflexion: Was war hilfreich? Was war ungenau?
