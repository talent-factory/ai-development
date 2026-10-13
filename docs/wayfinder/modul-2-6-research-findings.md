# Recherche-Findings: Module 2–6 Neukonzeption

**Erstellt:** 2026-10-07  
**Basis:** Bestandsaufnahme der Kursmaterialien, Vergleich-Kurse, KI-Basics, Modul 1

---

## 1. Bestehende Kurse – Differenzierungs-Analyse

### `pyt-intro-2025` (Talent Factory)
**Fokus:** Python Programmierung generisch (ohne KI-Schwerpunkt)

| Aspekt | pyt-intro-2025 | ai-development (unser Kurs) |
|--------|---|---|
| **Zielgruppe** | Anfänger (keine Voraussetzung) | Post-Ausbildung, Junior-Devs |
| **Python-Level** | A–C: Basics → Objekte → Flask | A–B: Basics → Datenverarbeitung |
| **KI-Integration** | Minimal (optional in späteren Modulen) | **Zentral von Tag 1** |
| **Fokus-Apps** | Web-Apps (Flask), Datenanalyse | KI-gestützte Entwicklung, RAG, Agents |
| **Dauer** | ~40 Stunden | ~24 Stunden (Wochenend-Kurs) |

**USP ai-development:** KI als Entwicklungspartner (Prompting, Pair-Programming, Code-Review), nicht Python generisch

---

### `pyt-ai-intro` (Talent Factory)
**Fokus:** AI/ML Basics mit Python (viel No-Code, wenig Software-Engineering)

| Aspekt | pyt-ai-intro | ai-development |
|--------|---|---|
| **Zielgruppe** | Anfänger (keine Tech-Voraussetzung) | Junior-Devs (Ausbildung voraus) |
| **No-Code-Tools** | Flowise, Langflow, n8n (Schwerpunkt) | Code-First; No-Code nur als Alternative |
| **ML/AI-Tiefe** | Basics: Was ist AI? Erste Modelle | Praktisch: LLMs, Embeddings, RAG |
| **Software-Engineering** | Minimal | **Git, Testing, Deployment, Best Practices** |

**USP ai-development:** Developer-centric, nicht BI-Analyst-centric; Production-ready Code, nicht Prototypen

---

### `pyt-cisco` (Talent Factory)
**Fokus:** Python für Netzwerk-Administratoren (Spezialisiert)

**Fazit:** Kaum Overlap mit ai-development (andere Zielgruppe, andere Use Cases)

---

## 2. KI Basics von Sabine Jungk (Sept 2026)

**Themen (aus `bibliography/**` geschätzt):**
- Was ist KI? (Definition, Geschichte, aktuelle Trends)
- Large Language Models (GPT-4, Claude, etc.) – Architektur, Fähigkeiten, Grenzen
- Prompt Engineering Basics
- Praktische Anwendungen (Code-Generierung, Text-Analyse, etc.)
- Ethik & Governance

**Implikation für ai-development:**
- ✅ Keine Wiederholung von „Was ist KI?" in Modul 1 (schon getan)
- ⚠️ Prompt Engineering: Prüfen, ob Sabines Tiefe ausreichend für „KI als Pair-Programmer"
- ⚠️ Ethik: Evtl. in Modul 6 vertiefen statt Modul 1

---

## 3. IBAW-Curriculum

**Offizielle Lernziele (aus `docs/Curriculum.md`):**
1. KI verstehen (Def, Trends, Chancen, Risiken)
2. Python Grundlagen (Variablen, Schleifen, Funktionen)
3. Datenverarbeitung (CSV, JSON, APIs)
4. KI-Integration in Entwicklung (LLMs, Prompting, Agents)
5. Fortgeschrittene Techniken (RAG, Embeddings)
6. Eigenes Projekt & Production-Readiness

**Alignment ai-development:** ✅ Modul 1–6 decken Curriculum ab

---

## 4. Modul 1 – Gelerntes & Etablierte Patterns

### Was Modul 1 bereits abdeckt (→ nicht wiederholen):
- Programmier-Mindset (Denken vs. Tippen)
- Setup (VS Code, Python, uv, OpenCode)
- Variablen, Datentypen (int, float, str, bool)
- Erste Python-Schritte mit KI als Erklär-Partner
- KI-Begriffswelt (Prompt, Command, Skill, Agent, Hook, RAG)
- Ethik & Rechtliches (Intro-Level)

### Didaktische Patterns (→ übernehmen):

| Pattern | Modul 1 Beispiel | Modul 2–6 Nutzung |
|---------|---|---|
| **Live-Coding** | 4 × 50 Min Lektionen mit Demo | ✅ Gleich beibehalten |
| **KI-Pair-Programming** | „KI schreibt 80%, Du reviewst" | ✅ Übungen mit Prompting-Guide |
| **KI-Debugging** | „KI findet Bugs, Du lernst" | ✅ Lektion 3 (Schleifen) schon implementiert |
| **Reflexionsbogen** | Strukturierte Selbsteinschätzung | ✅ Pro Modul adaptieren |
| **Cheatsheets** | AsciiDoc (Datentypen, Operatoren) | ✅ Pro Modul (3–4 pro Modul) |
| **Demo-Scripts** | 4 `.py`-Dateien pro Modul | ✅ Weiternutzen |

---

## 5. Bestehende Materialien (aus `docs/index.pdf` & `docs/wayfinder/`)

### Wiederverwendbar (High Quality):
- **Modul 2 Lektionen:** Übersichten Variablen, Schleifen, Funktionen gut strukturiert
- **Modul 3 Übungen:** CSV-Parsing, JSON-Handling bereits konzipiert
- **Modul 4 Materialien:** Teilweise; No-Code-Beispiele

### Zu Überarbeiten (Outdated / Level-Mismatch):
- **Streamlit-Apps** in `05-beispiele/`: Sind eher Modul 5/6, nicht Modul 2
- **Flowise/Langflow-Übungen:** Gehört in Modul 5 als Alternative, nicht Modul 2
- **Transfer Learning Artikel:** Gehört in Modul 5, nicht Modul 2
- **PowerPoint-Folien** in `docs/slides/`: Evtl. für Dozenten-Vorbereitung erhalten, aber nicht als Lehrformat

### Archiviert (Modul 2):
- `transfer.adoc` → `archive/` (gehört in Modul 5)
- `example-files/` mit Streamlit-App → `archive/` (gehört in Modul 5)

---

## 6. Zielgruppe-Profil (Junior-Devs, Post-Ausbildung)

**Charakterisierung:**
- ✅ Können: Grundlagen Python, Variablen, if/for-Schleifen, einfache Funktionen
- ⚠️ Schwach: OOP, Design Patterns, Testing, Git (fortgeschritten)
- ❌ Nicht: Mathematik-Heavy (Lineare Algebra, Kalkül) – zu viel für dieses Niveau
- 🎯 Brauchen: Praktisch umsetzbare Skills; aktuelle Tools (ChatGPT, Copilot, Claude)

**Implikation für Modul 2–6:**
- Keine theoretischen Exkurse (z.B. ML-Math, Transformer-Architektur im Detail)
- Stattdessen: „Wie nutze ich RAG in meinem Projekt?" (Hands-On)
- Fokus: Developer Experience, Production Readiness, Best Practices

---

## 7. KI-Integration-Strategie (Modul 2–6)

### Pattern pro Modul:

**Lektion 1–3:** Basics lehren
- KI erklärt parallel (Tool-Outputs vergleichen)
- KI debuggt Schüler-Code

**Lektion 4:** Integration
- Größeres Projekt mit KI-Pair-Programming
- KI als Code-Reviewer

**Hausaufgaben:** Reflexion
- Bogen: „Wo half KI? Wo war sie falsch?"
- Dokumentation der KI-Prompts (Lerneffekt)

**Optional:** KI-Fehler absichtlich einbauen
- Schüler/innen finden KI-Halluzinationen
- Kritisches Denken trainieren

---

## 8. Modul-Reihenfolge & Abhängigkeiten

```
Modul 1: Mindset & Setup
    ↓
Modul 2: Python Basics (Variablen, Schleifen, Funktionen) ← WIR SIND HIER
    ↓
Modul 3: Datenverarbeitung (CSV, JSON, APIs)
    ↓
Modul 4: Agentic Coding (KI als Entwicklungspartner)
    ↓
Modul 5: Fortgeschrittene KI (Embeddings, RAG, LangChain)
    ↓
Modul 6: Eigenes Projekt & Deployment
```

**Abhängigkeiten:**
- Modul 3 braucht: Modul 2 Funktionen, File-Handling
- Modul 4 braucht: Modul 2–3 Basics, Prompting-Handwerk
- Modul 5 braucht: Modul 3–4 (APIs, LLM-Integration)
- Modul 6 braucht: Alles (es ist das Projekt)

---

## 9. Duplikations-Check: Detailliert

### Modul 3 vs. pyt-intro-2025:
- **pyt-intro-2025:** CSV/JSON als Datenanalyse (pandas, matplotlib)
- **ai-development:** CSV/JSON als Datenquelle für KI-Apps (Embedding, RAG)
- **Unterschied:** Panda-Heavy vs. Raw-Python
- **Empfehlung:** Raw Python `csv`, `json` Module; pandas optional in Modul 5

### Modul 4 vs. pyt-ai-intro:
- **pyt-ai-intro:** No-Code LLM-Apps (Flowise, Langflow, Hugging Face Spaces)
- **ai-development:** Code-First LLM-Integration (ChatGPT API, Claude API, LangChain)
- **Unterschied:** UI-basiert vs. Python-basiert
- **Empfehlung:** Flowise/Langflow als _Alternative_ in Modul 5, nicht Schwerpunkt

### Modul 5 vs. FFHS CAS AISE:
- **FFHS:** Vector Databases, Advanced RAG, Production ML Pipelines
- **ai-development:** Praktische RAG-App (Dokumenten-Chatbot), nicht Research-fokussiert
- **Unterschied:** Fachhochschul-Level (mathematisch, theoretisch) vs. Junior-Level (praktisch)
- **Empfehlung:** Keine Duplikation; völlig andere Zielgruppe

---

## 10. Offene Fragen für Grilling-Phase

1. **Abgabe-Plattform:** GitHub Classroom, Moodle, oder E-Mail?
2. **Live-Durchführung:** Präsenz, Hybrid, oder aufgezeichnet?
3. **Prüfungs-Modell:** Nur Projekte, oder auch schriftliche Tests?
4. **Modul 6 Projekt:** Umfang? Solo oder Gruppen? Benotung?
5. **Flexibilität:** Können Schüler/innen zwischen Python & No-Code wählen?
6. **Zertifikat:** Bestehen-Kriterium (50%, 60%, etc.)?

---

## 11. Quick-Start für Modul-Planung

**Template pro Modul:**

```markdown
# Modul N: [Name]

## Destination (Learning Objectives)
- ✅ Lernziel 1
- ✅ Lernziel 2
- ✅ Lernziel 3

## Lektionen (4 × 50 Min)
1. Titel: [Konbegriff 1] – KI-Role: Erklären
2. Titel: [Konzept 2] – KI-Role: Erklären
3. Titel: [Konzept 3] – KI-Role: Debugging
4. Titel: [Integration] – KI-Role: Pair-Programming & Code-Review

## Übungen
- Übung 1 (nach Lektion 2): Grundlagen üben
- Übung 2 (nach Lektion 3): Komplexität erhöhen
- Übung 3 (nach Lektion 4): Mini-Projekt mit KI-Review

## Hausaufgaben
- Hausaufgabe 1: Praktisches Projekt
- Hausaufgabe 2: Kleine Data-Pipeline / Mini-Agent / etc.
- Reflexionsbogen: Selbsteinschätzung + KI-Nutzung

## Cheatsheets (3–4)
- cheatsheet-[Konzept1].adoc
- cheatsheet-[Konzept2].adoc
- prompting-guide.adoc

## Demo-Scripts (4)
- 0N-konzept1_demo.py
- 0N-konzept2_demo.py
- 0N-konzept3_demo.py
- 0N-integration_demo.py
```

---

## 12. Angestrebter Rhythmus

**Pro Modul: 2 Wayfinder-Sessions à ~2 Stunden**

| Session 1 | Zeit | Session 2 | Zeit |
|-----------|------|----------|------|
| Grilling (Ziele, Overlap, Fokus) | 45 Min | Finalität-Check | 20 Min |
| Prototype (Lektionsplan-Skizze) | 45 Min | Duplikations-Check | 20 Min |
| Break | 10 Min | KI-Integration-Check | 20 Min |
| Research-Delegation (async) | – | Abschließende Anpassungen | 40 Min |
| – | – | Reflexion & Handoff zu nächstem Modul | 20 Min |

**Parallel (Research-Tickets):**
- Vergleich-Kurse analysieren (pyt-intro-2025, pyt-ai-intro)
- Best Practices sammeln (Prompt-Templates, Test-Patterns)
- Materialien aus `docs/index.pdf` recyceln

---

_Nächste Schritte: `/wayfinder start` mit Modul 3 planen_
