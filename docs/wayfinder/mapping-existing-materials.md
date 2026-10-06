# Mapping bestehender Materialien auf die 6 neuen Module

*Erstellt im Rahmen des Wayfinder-Tickets 4.*

> **Hinweis:** Die Spalte «Bestehendes Material» zeigt die ursprünglichen Pfade vor der Migration. Die Dateien wurden physisch in die unter «Zielordner» genannten Verzeichnisse verschoben.

---

## Neue Modulstruktur

```
course/
├── modul-1-programmier-mindset-ki-tools-setup/
├── modul-2-python-grundlagen-mit-ki/
├── modul-3-datenverarbeitung-dateien/
├── modul-4-agentic-coding/
├── modul-5-fortgeschrittene-ki-integration/
└── modul-6-eigenes-projekt-abschluss/
```

Jedes Modul folgt dem Template aus `pyt-intro-2025`:

```
modul-N-name/
├── 00-vorbereitung/
├── 01-praxis/
├── 02-uebungen/
├── 03-nachbearbeitung/
├── 04-materialien/
├── 05-beispiele/
└── README.md
```

---

## Inventar & Zuordnung

### Modul 1: Programmier-Mindset & KI-Tools Setup

| Bestehendes Material | Typ | Zielordner | Begründung |
|----------------------|-----|------------|------------|
| `docs/chapters/01-introduction.adoc` | Lektion | `01-praxis/` | Einstieg, Mindset, KI-Überblick |
| `docs/chapters/software.adoc` | Material | `04-materialien/` | Tooling-Übersicht |
| `docs/chapters/uv.adoc` | Lektion | `01-praxis/` | Python-Package-Management |
| `docs/final-session/lesson-01-cli-setup.md` | Lektion | `01-praxis/` | CLI & Setup |
| `docs/final-session/exercises/cli-installation.md` | Übung | `02-uebungen/` | Setup-Übung |
| `streamlit/hello-world.py` | Beispiel | `05-beispiele/` | Erste lauffähige App |
| `docs/slides/00 Einführung Basic.pdf` | Material | `04-materialien/` | Folien Einstieg |
| `docs/slides/01 Einführung Development.pptx` | Material | `04-materialien/` | Folien Development-Einführung |
| `docs/exercises/backup-environments-quickstart.adoc` | Vorbereitung | `00-vorbereitung/` | Vorbereitung Installation |

### Modul 2: Python-Grundlagen mit KI verstehen

| Bestehendes Material | Typ | Zielordner | Begründung |
|----------------------|-----|------------|------------|
| `docs/chapters/exercises.adoc` | Lektion | `01-praxis/` | Python-Übungen & Basics |
| `docs/exercises/ex-01.adoc` | Übung | `02-uebungen/` | Grundlegende Übung |
| `docs/exercises/ex-02.adoc` | Übung | `02-uebungen/` | Vertiefende Übung |
| `docs/chapters/references.adoc` | Material | `04-materialien/` | Nachschlagewerk |
| `docs/chapters/transfer.adoc` | Lektion | `01-praxis/` | Wissenstransfer & KI-Prompting für Basics |
| `docs/exercises/example-files/` | Beispiele | `05-beispiele/` | Begleitende Code-Beispiele |

### Modul 3: Datenverarbeitung & Dateien

| Bestehendes Material | Typ | Zielordner | Begründung |
|----------------------|-----|------------|------------|
| `docs/chapters/platforms.adoc` | Lektion | `01-praxis/` | APIs & Plattformen als Datenquelle |
| `docs/solutions/homework-week-2-3/aufgabe-2/konzept-map.md` | Übung | `02-uebungen/` | Konzept-Mapping zu Daten/Plattformen |
| `docs/solutions/homework-week-2-3/aufgabe-2/langchain-vergleich.md` | Übung | `02-uebungen/` | Framework-Vergleich |
| `docs/exercises/homework-week-2-3.adoc` | Nachbearbeitung | `03-nachbearbeitung/` | Hausaufgaben zu Daten & APIs |
| `docs/exercises/homework-week-2-3-zeitplan.adoc` | Material | `04-materialien/` | Zeitplan |
| `docs/exercises/homework-week-2-3-rubrik.adoc` | Material | `04-materialien/` | Bewertungsrubrik |

### Modul 4: Agentic Coding – KI als Entwicklungspartner

| Bestehendes Material | Typ | Zielordner | Begründung |
|----------------------|-----|------------|------------|
| `docs/chapters/07-slash-commands-workflows.md` | Lektion | `01-praxis/` | AI-Workflows & Slash Commands |
| `docs/final-session/lesson-02-tools-action.md` | Lektion | `01-praxis/` | KI-Tools in Aktion |
| `docs/final-session/lesson-03-new-trends.md` | Lektion | `01-praxis/` | Aktuelle Entwicklungen |
| `docs/final-session/lesson-04-own-commands.md` | Lektion | `01-praxis/` | Eigene Commands erstellen |
| `docs/final-session/exercises/command-examples/generate-tests.md` | Übung | `02-uebungen/` | Testgenerierung mit KI |
| `docs/final-session/exercises/command-examples/security-audit.md` | Übung | `02-uebungen/` | Security-Audit mit KI |
| `docs/final-session/resources/cli-comparison.md` | Material | `04-materialien/` | CLI-Tool-Vergleich |
| `src/pydantic/tool/01-05_simple_tool_agent.py` | Beispiel | `05-beispiele/` | Einfache Tool-Agents |
| `src/pydantic/tool/README.md` | Material | `04-materialien/` | Erklärung Tool-Agents |
| `docs/chapters/pydantic-ai.adoc` | Lektion | `01-praxis/` | Strukturierte KI-Agenten mit Pydantic |

### Modul 5: Fortgeschrittene KI-Integration

| Bestehendes Material | Typ | Zielordner | Begründung |
|----------------------|-----|------------|------------|
| `docs/chapters/03-langchain.adoc` | Lektion | `01-praxis/` | LangChain-Grundlagen |
| `docs/chapters/04-vector-stores.adoc` | Lektion | `01-praxis/` | Vektordatenbanken |
| `docs/chapters/05-embeddings.adoc` | Lektion | `01-praxis/` | Embeddings |
| `docs/chapters/06-rag-praxis.adoc` | Lektion | `01-praxis/` | RAG in der Praxis |
| `docs/chapters/rag.adoc` | Lektion | `01-praxis/` | RAG-Konzept |
| `docs/exercises/vector-store-similarity-exercise.adoc` | Übung | `02-uebungen/` | Ähnlichkeit & Vektoren |
| `docs/exercises/embeddings-mit-word2vec.py` | Beispiel | `05-beispiele/` | Embeddings-Experiment |
| `docs/solutions/homework-week-2-3/aufgabe-3/` | Übung | `02-uebungen/` | RAG-Anwendungsfall, Diagramm, Reflexion |
| `docs/solutions/homework-week-2-3/aufgabe-4/` | Übung | `02-uebungen/` | Similarity-Experiment, Vektordatenbank-Vergleich |
| `docs/solutions/homework-week-2-3/aufgabe-5/` | Beispiel/Übung | `05-beispiele/` | Mini-RAG mit Code |
| `scripts/rag-praxis/` | Beispiel | `05-beispiele/` | RAG-Scripts |
| `streamlit/embeddings.py` | Beispiel | `05-beispiele/` | Embeddings-Visualisierung |
| `streamlit/vector_chatbot.py` | Beispiel | `05-beispiele/` | Vektorbasierter Chatbot |
| `docs/faiss.adoc` | Material | `04-materialien/` | FAISS als Vektordatenbank |
| `docs/hugging-face.adoc` | Material | `04-materialien/` | Hugging Face |
| `docs/slides/02 Erster Einsatz eigener von FlowiseAI.pptx` | Material | `04-materialien/` | Flowise-Einstieg (No-Code RAG) |
| `docs/chapters/02-no-code.adoc` | Lektion | `01-praxis/` | No-Code/Low-Code Einführung |
| `rag-system/` | Projekt | `05-beispiele/` | Selbstständiges RAG-System |

### Modul 6: Eigenes Projekt, Abschluss, Fragen

| Bestehendes Material | Typ | Zielordner | Begründung |
|----------------------|-----|------------|------------|
| `docs/chapters/streamlit.adoc` | Lektion | `01-praxis/` | Streamlit für Abschlussprojekte |
| `streamlit/chatbot.py` | Beispiel | `05-beispiele/` | Chatbot-App |
| `streamlit/translator.py` | Beispiel | `05-beispiele/` | Übersetzer-App |
| `docs/exercises/ai-course-assistant-readme-template.md` | Material | `04-materialien/` | Projektdokumentation-Vorlage |
| `docs/exercises/ai-course-assistant-deployment.adoc` | Lektion | `01-praxis/` | Deployment |
| `docs/exercises/replicate-exercise.adoc` | Übung | `02-uebungen/` | Modell-Deployment-Übung |
| `docs/exercises/replicate-exercise-advanced.adoc` | Übung | `02-uebungen/` | Vertiefung Deployment |
| `replicate/` | Beispiele | `05-beispiele/` | Deployment-Beispiele |
| `docs/exercises/platform-comparison-exercise.adoc` | Übung | `02-uebungen/` | Plattformvergleich |
| `docs/final-session/README.md` | Material | `04-materialien/` | Abschlusssession-Übersicht |
| `docs/final-session/resources/ai-news-summary.md` | Material | `04-materialien/` | Ausblick Trends |

---

## Nicht modul-spezifisch / Kurs-weit

| Bestehendes Material | Vorschlag |
|----------------------|-----------|
| `docs/course-roadmap.adoc` | In `course/README.md` überführen oder als Kurs-Übersicht behalten |
| `docs/index.adoc` | Kurs-Index / Einstiegsdokumentation |
| `docs/prompt.md` | Allgemeine Prompting-Ressource |
| `docs/images/` | Zentrale Bildersammlung, Verweise aus den Modulen |
| `docs/slides/template.pptx` | Folien-Template für alle Module |
| `docs/slides/powerpoint-template-guide.md` | Anleitung Folien-Template |
| `docs/slides/course-roadmap.html` | Kurs-Roadmap |
| `docs/slides/course-progress-slide.adoc` | Fortschrittsfolie |
| `docs/Alles über KI und wie es unser Leben prägt.pdf` | Hintergrundmaterial |
| `docs/Infoveranstaltungen KI.pptx` | Marketingmaterial |
| `docs/Inhalte AI Professional - Fachrichtung Development v1.1.*` | Ausschreibungs-Referenz |

---

## Offene Entscheidungen

1. **No-Code/Low-Code-Tools:** Flowise/Langflow und n8n/Make sind im Proposal erwähnt. Aktuell existiert nur `docs/chapters/02-no-code.adoc` und Flowise-Folien. Sollen diese Tools in M4/M5 vertieft werden?
2. **Migrationsstrategie:** Sollen Dateien physisch verschoben, kopiert oder verlinkt werden?
3. **`rag-system/` Unterprojekt:** Als ganzes in M5 integrieren oder als separaten Referenz-Ordner belassen?
