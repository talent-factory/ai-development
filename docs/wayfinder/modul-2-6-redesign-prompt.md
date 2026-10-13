# Wayfinder-Prompt: Module 2–6 Neukonzeption & Ausarbeitung

**Zielgruppe:** Softwareentwickler/innen & Junior-Entwickler/innen (Level: Post-Ausbildung, pre-Bachelor)  
**Kontext:** Kursevaluation nach Modul 1 Durchführung (Di, 2026-10-06); KI bewegt sich rasch → Kurs-Neuaufbereitung  
**Ziel dieser Session:** Detailliertes Konzept für Module 2–6 mit Lektionsplänen, Übungen, Beispielen & Abgabenkritierien

---

## Destination

Die **Module 2–6** des Kurses «Python & KI: Vom Programmier-Mindset zum eigenen KI-Projekt» sind strukturiert, inhaltlich durchkonzipiert und ready für Durchführung/Iteration:

1. **Modul 2 – Python-Grundlagen mit KI verstehen** (✅ gerade fertiggestellt)
2. **Modul 3 – Datenverarbeitung & Dateien**
3. **Modul 4 – Agentic Coding: KI als Entwicklungspartner**
4. **Modul 5 – Fortgeschrittene KI-Integration (Embeddings, RAG)**
5. **Modul 6 – Eigenes Projekt & Abschluss**

Jedes Modul folgt der bewährten Struktur aus Modul 1 (`course/modul-N-name/` mit 00-05-Ordnern), ist **frei von Duplikationen** zu existierenden Kursen (pyt-ai-intro, pyt-intro-2025, pyt-cisco), berücksichtigt das IBAW-Curriculum, KI-Basics von Sabine Jungk und Modul 1 Inhalte.

---

## Context & Domain

### Bestehende Artefakte & Quellen

| Quelle | Ort | Relevanz |
|--------|-----|----------|
| **Modul 1 (Pilot)** | `course/modul-1-programmier-mindset-ki-tools-setup/` | ✅ Template: Struktur (00-05), Didaktik (KI als Partner), Lektionspläne |
| **Alte Materialien** | `docs/index.pdf` + `docs/wayfinder/**` | ✅ Lektionen, Übungen, Beispiele als Quelle (recyceln, nicht duplizieren) |
| **IBAW-Curriculum** | `docs/Curriculum.md` | ✅ Offizielle Lernziele & Modulstruktur |
| **KI Basics** | `bibliography/**` (Sabine Jungk, 15.+22.Sept) | ✅ Was ist bereits vermittelt → Overlap vermeiden |
| **Vergleich-Kurse** | `pyt-ai-intro`, `pyt-intro-2025`, `pyt-cisco` | ⚠️ Differentiation-Checkliste |
| **Konsolidierungs-Proposal** | `docs/kurskonsolidierung-proposal.md` | 📋 Cross-Selling/Upselling-Gedanken (optional einbauen) |
| **FFHS CAS AISE** | `/Users/daniel/GitRepository/ffhs-aise` | 📋 Reference: Bachelor-Level (bewusst NOT das Niveau dieses Kurses) |

### Zielgruppe Profil

- **Primary:** Softwareentwickler/innen mit 4-jähriger Ausbildung
- **Secondary:** Junior-Entwickler/innen, Quereinsteiger (z.B. ex-Cobol)
- **Level:** Post-Ausbildung, pre-Bachelor → **bewusst NICHT Fachhochschul-Niveau**
- **Implikation:** Praktisch-handwerklich, nicht wissenschaftlich; aktuelle KI-Tools nutzen, nicht ML-Theorie

### Kurs-Design-Prinzipien (aus Modul 1)

1. **KI als fester Partner** – nicht optional, sondern in jeder Lektion: Erklären → Pair-Programming → Debugging → Code-Review
2. **Live-Coding first** – keine Folien-Schlachten, sofortiges Ausprobieren in REPL/IDE
3. **Aufbauende Übungen** – kleine Projects, die aufeinander bauen (z.B. Taschenrechner → BMI → Modular)
4. **Reflexion & Dokumentation** – „Wo half KI? Wo nicht?" → Bewusstsein für Stärken/Schwächen
5. **No Duplication** – bestehende Kurse nicht nachbauen, sondern eigene USP klären

---

## Notes (Standing Preferences for this Wayfinder)

### Strukturelle Leitlinien

- **Template:** `modul-N-name/` mit `00-vorbereitung/`, `01-praxis/`, `02-uebungen/`, `03-nachbearbeitung/`, `04-materialien/`, `05-beispiele/`, `LEKTIONSPLAN.md`, `README.md`
- **Sprache:** Deutsch (Deutsch + Englisch für Code/Begriffe OK)
- **Format:** Markdown (`.md`) für Lektionen, AsciiDoc (`.adoc`) für Cheatsheets/Referenzen, Python (`.py`) für Demo-Code, YAML für strukturierte Daten
- **Detailgrad:** Pro Modul: Lektionsplan (50 Min × 4) + 4 Lektionsskripte + 3 Übungen + 2–3 Hausaufgaben + 3–4 Cheatsheets + 4 Demo-Scripts

### Inhaltliche Leitlinien

- **Synchronisation:** KI-Basics von Sabine Jungk prüfen & Overlap eliminieren
- **Modul 1 Build-on:** Nicht wiederholen, was Modul 1 lehrt (Programmier-Mindset, Setup, Variablen-Basics)
- **Differenzierung:** Explizit unterscheiden von `pyt-intro-2025` (Python generisch) & `pyt-ai-intro` (viel No-Code)
- **Zielgruppe-Fit:** Junior-Level: praktisch, nicht mathematisch; aktuelle KI-Tools (ChatGPT, Claude, GitHub Copilot, OpenCode)

### KI-Integration-Leitlinien

Jede Lektion hat explizite KI-Touchpoints:

| Phase | KI-Rolle |
|-------|----------|
| **Vorbereitung** | Leseauftrag selbst lesen, dann KI befragen zur Klärung |
| **Live-Coding** | KI erklärt Konzepte parallel, generiert Varianten zum Vergleichen |
| **Übung (Pair-Programming)** | KI schreibt 80%, Mensch reviewed & ändert ab |
| **Debugging** | KI findet Bugs, Mensch korrigiert & lernt |
| **Code-Review** | KI prüft auf Stil/Sicherheit/Performance, Mensch refaktoriert |
| **Reflection** | Strukturierter Bogen: Was half KI? Wo war KI falsch? |

---

## Decisions so far (aus voriger Map)

1. ✅ **Zielort:** Restrukturierung innerhalb `ai-development` (nicht Split in 2 Kurse)
2. ✅ **Scope:** Ein 6-Modul-Kurs mit Struktur `course/modul-N-name/00-05`
3. ✅ **Tiefe:** Erst Struktur + Mapping (✅ getan), dann iterative Befüllung
4. ✅ **Struktur:** Verzeichnisstruktur erstellt, Mapping-Dokument abgelegt
5. ✅ **Modul 1:** Pilot mit README-Vorlage, Lektionspläne, KI-Integration etabliert
6. ✅ **No-Code/Low-Code:** Flowise/Langflow als RAG-Option in Modul 5; n8n/Make als Ausblick
7. ✅ **READMEs 2–6:** Skeleton-READMEs mit Lernzielen & Struktur-Verweisen erstellt
8. ✅ **Migration:** Alte Materialien physisch verschoben, Verweise angepasst
9. ✅ **Modul 1 Lektionen:** 4 Lektionen + KI-Begriffswelt + gemeinsames Setup geplant & teilweise ausgefüllt
10. ✅ **Modul 2:** Lektionsplan, 4 Lektionsskripte, 3 Übungen, Cheatsheets, Demo-Scripts, Reflexionsbogen erstellt

---

## Not yet specified

### Modul 3: Datenverarbeitung & Dateien
- Lektionen 1–4 Detailkonzept (CSV, JSON, APIs, Fehlerbehandlung)
- Live-Coding-Demo Scripts für jede Lektion
- Übungen: Praktische Datei-Verarbeitung (CSV→Dict, JSON-API-Abruf, etc.)
- Hausaufgaben: Kleine Daten-Pipeline (CSV lesen → transformieren → JSON schreiben)

### Modul 4: Agentic Coding – KI als Entwicklungspartner
- Lektionen 1–4 Detailkonzept (Was sind Agents? Tool Use, Prompting für Code, Selbst-Reflektion)
- Verhältnis zu OpenCode-Skills/Commands klären (nicht duplizieren)
- GitHub Copilot vs. ChatGPT vs. Claude: Vergleich & When-to-use
- Übungen: KI-Pair-Programming mit strukturiertem Feedback
- Hausaufgaben: Mini-Agent (z.B. Dateiverwaltungs-Assistent)

### Modul 5: Fortgeschrittene KI-Integration (Embeddings, RAG, LangChain)
- Lektionen 1–4 Detailkonzept (Was sind Embeddings? Vector DBs, RAG-Pipeline, LangChain-Basics)
- Flowise/Langflow als No-Code-Alternative: Wann nutzen vs. Code?
- Praktische RAG-App: Dokumenten-Chatbot (z.B. über Kurs-Unterlagen)
- Abgrenzung zu `pyt-ai-intro` (die haben mehr No-Code-Fokus)

### Modul 6: Eigenes Projekt & Abschluss
- Projekt-Scaffold: Umfang, Zeitrahmen, Bewertungs-Rubrik
- Beispiel-Projekte für 3 Schwierigkeitsstufen
- Git-Workflow & Deployment (Streamlit Cloud / Hugging Face Spaces / lokaler Server)
- Presentations + Peer-Feedback-Struktur
- Zertifikat & Abschlussgespräch

### Übergeordnete Fragen
- Abgabe-Plattform: GitHub Classroom vs. Moodle vs. andere?
- Live-Durchführung: Präsenz vs. Hybrid? Termine fixiert?
- Prüfungs-/Benotungs-Modell: Nur Projekte oder auch schriftliche Leistungen?

---

## Out of scope

- **Marketingtexte & Zertifikatsdesign:** Aus Kurskonsolidierungs-Proposal; wird später iter­iert
- **Vollständige Neuschreibung:** Wo möglich, alte Materialien recyceln & kalibrieren
- **Zwei-Kurs-Split (Proposal):** Bleibt 6-Modul-Kurs; Split kann später aufsetzen
- **Fachhochschul-Niveau:** FFHS CAS AISE ist Referenz für Higher-End; **dieser Kurs bleibt post-Ausbildung**
- **Marketing/Cross-Selling-Kampagne:** Aus Kurskonsolidierungs-Proposal; separate Initiative

---

## Session Plan

Diese Wayfinder-Session arbeitet **Modul für Modul durch**. Pro Modul:

1. **Grilling (30 Min):** Ziele prüfen, Overlap mit KI-Basics/Modul 1/Vergleich-Kurse identifizieren, Fokus klären
2. **Prototyp (30 Min):** Lektionsplan skizzieren (Titel, Kernkonzepte, KI-Touchpoints)
3. **Research (async, parallel):** Vergleich-Kurse recherchieren, Best Practices sammeln
4. **Task (45 Min):** Lektionsskripte, Übungen, Cheatsheets ausgefüllt; Demo-Scripts gebaut
5. **Reflexion:** Duplikation-Check, Zielgruppe-Fit-Check, KI-Integration-Check

**Iteration:** Pro Modul 1–2 Sessions à ~2h. Evtl. parallel Research-Tickets für Vergleich-Kurse.

---

## Erste Prioritäten

1. **Modul 3 (Datenverarbeitung):** Logisch nächster Schritt nach Python-Basics; viele praktische Beispiele
2. **Modul 4 (Agentic Coding):** Kernthema des Kurses; Abgrenzung zu OpenCode & Copilot nötig
3. **Modul 5 (RAG/Embeddings):** Spannend, aber komplex; Good research-Kandidat
4. **Modul 6 (Projekt & Abschluss):** Letzte; bindet alles zusammen

---

## Acceptance Criteria

Für jede Modul-Durcharbeitung (am Ende dieser Wayfinder-Session):

- ✅ **Lektionsplan:** 4 Lektionen, je ~50 Min, mit Zielen, Ablauf (Zeit), Materialien
- ✅ **4 Lektionsskripte:** `.md`-Dateien mit Theorie, Beispielen, Live-Coding-Anweisungen, KI-Prompts
- ✅ **3 Übungen:** `.adoc`-Dateien mit Aufgabenstellung, Starthilfe, Erweiterungen, Abgabe-Kriterien
- ✅ **2–3 Hausaufgaben:** In `03-nachbearbeitung/` mit Reflexionsbogen
- ✅ **3–4 Cheatsheets:** `.adoc` (Datentypen, Befehle, Best Practices, Prompting)
- ✅ **4 Demo-Scripts:** `.py`-Dateien, je ~100–200 Zeilen, kommentiert, runnable
- ✅ **Duplikations-Check:** Mapping zu `pyt-intro-2025`, `pyt-ai-intro`, `pyt-cisco`
- ✅ **KI-Basics-Sync:** Overlap mit Sabine Jungk's KI-Basics geklärt & vermieden
- ✅ **Modul 1 Build-on:** Nicht redundant zu Modul 1 Inhalten

---

## Ressourcen & Tools

- **Issue Tracker:** GitHub Issues (label `wayfinder:map`, `wayfinder:task`, etc.)
- **Dokumentation:** Markdown in `docs/wayfinder/tickets/`, `.md`-Lektionen in `course/modul-N/01-praxis/`
- **Code:** Python 3.13+, `uv` als Package Manager, OpenCode für Live-Editing
- **Referenzen:** `docs/Curriculum.md`, `bibliography/**`, alte Modul-Dateien in `docs/index.pdf`

---

_Bereit für `/wayfinder` Session: Module 2–6 Neukonzeption_
