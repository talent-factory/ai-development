# WAYFINDER-START: Module 2–6 Neu­konzeption

**Kurz-Version zum Kopieren & los­legen**

---

## TL;DR – Destination

Die **Module 2–6** sind strukturiert, inhaltlich durchkonzipiert und ready für Durchführung. Jedes Modul folgt dem Modul-1-Template (`00-05` Ordner + LEKTIONSPLAN + 4 Lektionen + Übungen + Hausaufgaben). **Keine Duplikationen** zu pyt-intro-2025, pyt-ai-intro, pyt-cisco. **KI als fester Partner** in jeder Lektion.

---

## Briefing (Copy-Paste)

### Kontext
- ✅ Modul 1 erfolgreich durchgeführt (Di, 2026-10-06)
- ✅ Modul 2 gerade fertiggestellt (Python-Grundlagen mit KI verstehen)
- 🎯 Modul 3–6 folgen jetzt
- 📌 Wichtig: IBAW-Curriculum, KI-Basics von Sabine Jungk, Vergleich-Kurse beachten

### Zielgruppe
**Junior-Softwareentwickler/innen, Post-Ausbildung, pre-Bachelor**
- Können: Python Basics (Modul 2), Dateien-Handling (Modul 3)
- Schwach: OOP, Testing, Deployment (lernen in Modul 4–6)
- Brauchen: Praktisch umsetzbar, nicht mathematisch-theoretisch

### Didaktik (aus Modul 1)
1. **KI als Partner** – Exploration, Pair-Programming, Debugging, Code-Review
2. **Live-Coding first** – keine Folien, sofortiges Ausprobieren
3. **Aufbauende Übungen** – Mini-Projekte verketten sich
4. **Reflexion** – Bogen: „Wo half KI? Wo nicht?"

### Besorgnis vermeiden
- ❌ Nicht: `pyt-intro-2025` nachbauen (deren Fokus: Python generisch)
- ❌ Nicht: `pyt-ai-intro` nachbauen (deren Fokus: viel No-Code)
- ✅ Sondern: Developer-centric, Code-First, Production-Ready, KI-Integration zentral

---

## Modul-Übersicht

| Modul | Titel | Kernkonzepte | Status |
|-------|-------|--------------|--------|
| 1 ✅ | Programmier-Mindset & KI-Tools Setup | Setup, Variablen, KI-Basics | Done |
| 2 ✅ | Python-Grundlagen mit KI verstehen | Variablen, Bedingungen, Schleifen, Funktionen | Done |
| 3 🔄 | Datenverarbeitung & Dateien | CSV, JSON, APIs, Error Handling, File I/O | **Nächste Priority** |
| 4 🔄 | Agentic Coding: KI als Entwicklungspartner | LLM APIs, Prompting, Tool Use, Agents | Danach |
| 5 🔄 | Fortgeschrittene KI-Integration | Embeddings, Vector DBs, RAG, LangChain | Danach |
| 6 🔄 | Eigenes Projekt & Abschluss | Projekt-Planning, Deployment, Ethik | Zum Schluss |

---

## Was jedes Modul braucht (Checklist)

```markdown
✅ LEKTIONSPLAN.md
   - 4 Lektionen à 50 Min mit Zielen, Ablauf, Materialien

✅ 01-praxis/ (4 Dateien)
   - lektion-1-[Konzept1].md
   - lektion-2-[Konzept2].md
   - lektion-3-[Konzept3].md
   - lektion-4-[Integration].md

✅ 02-uebungen/ (3 Dateien)
   - ex-01-[Aufgabe1].adoc (Lektion 2)
   - ex-02-[Aufgabe2].adoc (Lektion 3)
   - ex-03-[Aufgabe3].adoc (Lektion 4 + KI-Review Pflicht)

✅ 03-nachbearbeitung/ (2–3 Dateien)
   - README.md mit 2–3 Hausaufgaben
   - reflexionsbogen.md

✅ 04-materialien/ (3–4 Dateien)
   - cheatsheet-[Konzept1].adoc
   - cheatsheet-[Konzept2].adoc
   - prompting-guide.adoc

✅ 05-beispiele/ (4 Dateien)
   - 0N-konzept1_demo.py
   - 0N-konzept2_demo.py
   - 0N-konzept3_demo.py
   - 0N-integration_demo.py

✅ README.md (Modul-Übersicht)
```

---

## Duplikations-Check (Quick-Reference)

| Modul | Vergleich zu... | Risiko | Mitigations-Strategie |
|-------|---|---|---|
| **3** | pyt-intro-2025 | Beide CSV/JSON | **Raw Python** (`csv`, `json` Module) statt pandas |
| **4** | pyt-ai-intro | Beide LLM-APIs | **Code-First** statt No-Code; Flowise nur als Alternative |
| **5** | FFHS CAS AISE | Beide RAG | **Praktisch** (Dokumenten-Chatbot) statt Forschung |
| **Alle** | Sabine Jungk KI-Basics | Overlap in Modul 1 | Nur Handwaving in Modul 1 vermeiden; tiefere Prompting ab Modul 2 |

---

## KI-Touchpoints pro Lektion (Pattern)

| Lektion | KI-Rolle | Beispiel-Prompt |
|---------|----------|---|
| **1** | Erklären (parallel) | `"Erkläre mir [Konzept] wie einem Junior-Dev."` |
| **2** | Erklären + Varianten | `"Zeige mir 3 Wege, [Aufgabe] zu lösen."` |
| **3** | Debugging | `"Finde den Bug in diesem Code: [Code]. Erkläre die Ursache."` |
| **4** | Pair-Programming | `"Schreibe Code für [Aufgabe]. Ich review und ändere ab."` |
| **Übung 3** | Code-Review (Pflicht) | `"Review meinen Code auf Stil, Sicherheit, Performance: [Code]"` |

---

## Session-Plan (Modul 3 als Beispiel)

### Session 1 (2h)
- **Grilling (45 Min):** Modul 3 Ziele klar? Overlap mit pyt-intro-2025? Fokus: Raw Python, nicht pandas
- **Prototype (45 Min):** Lektionsplan skizzieren (4 Lektionen: CSV → JSON → APIs → Error Handling)
- **Break (10 Min)**
- **Delegation:** Research-Ticket: pyt-intro-2025 & pyt-ai-intro analysieren (parallel, async)

### Session 2 (2h)
- **Finalität (20 Min):** Lektionspläne review
- **Duplikations-Check (20 Min):** pyt-intro-2025 Research-Ergebnisse einbauen
- **KI-Integration (20 Min):** Prompting-Beispiele pro Lektion; Hausaufgaben-Reflexionsbogen
- **Task (40 Min):** Lektionsskripte, Übungen, Cheatsheets ausgefüllt
- **Reflexion (20 Min):** Zielgruppe-Fit? Ready für Durchführung?

---

## Referenzen (In diesem Repo)

| Dokument | Ort | Wann lesen |
|----------|-----|-----------|
| **Modul 1 als Template** | `course/modul-1-programmier-mindset-ki-tools-setup/` | Jetzt (Struktur-Referenz) |
| **IBAW-Curriculum** | `docs/Curriculum.md` | Vor Session 1 (Alignment-Check) |
| **KI-Basics Sabine Jungk** | `bibliography/**` | Vor Session 1 (Overlap-Check) |
| **Alte Materialien** | `docs/index.pdf` + `docs/wayfinder/**` | Optional (Recycling-Quelle) |
| **Wayfinder Skill** | `.opencode/skills/wayfinder/SKILL.md` | Referenz während Session |
| **Diese Prompts** | `docs/wayfinder/modul-2-6-redesign-prompt.md` + `modul-2-6-research-findings.md` | In der Session nutzen |

---

## Zum Start

**Terminal:**
```bash
cd /Users/daniel/GitRepository/ai-development

# Modul 2 prüfen (eben fertig)
ls -la course/modul-2-python-grundlagen-mit-ki/

# Struktur Modul 3 inspizieren (Skeleton vorhanden)
ls -la course/modul-3-datenverarbeitung-dateien/
```

**Dann:**
```
/wayfinder start docs/wayfinder/modul-2-6-redesign-prompt.md
```

---

## Schnelle Entscheidungen

Folgende Fragen sollten **vor Session 1** geklärt sein:

1. **Abgabe-Plattform:** GitHub Classroom, Moodle, E-Mail?
2. **Live-Format:** Präsenz, Hybrid, aufgezeichnet?
3. **Benotung:** Nur Projekte oder auch schriftliche Tests?
4. **Modul 6 Projekt:** Umfang, Solo/Gruppen, Bestehen-Kriterium?

---

_Ready? → `/wayfinder start` mit obigen Prompts_
