# Wayfinder Navigation – Module 2–6 Neukonzeption

**Übersicht aller Wayfinder-Dokumente für diesen Kurs-Redesign**

---

## 🗺️ Die Wayfinder Map (Hauptartefakt)

**→ [`kurs-redesign-map.md`](./kurs-redesign-map.md)**

Das zentrale Tracking-Dokument mit:
- **Destination:** Ein 6-Modul-Kurs «Python & KI: Vom Programmier-Mindset zum eigenen KI-Projekt»
- **Decisions so far:** 10 closed tickets (Struktur, Pilot Modul 1, Migrations, etc.)
- **Not yet specified:** Lektionen Modul 3–6, Projekt-Scaffold, Abschlussprojekt
- **Open Tickets:** Tracking der In-Progress-Arbeit

---

## 📋 Aktuelle Session-Prompts (für `/wayfinder`)

### 1️⃣ START HIER – Kurz-Einstieg
**→ [`WAYFINDER-START.md`](./WAYFINDER-START.md)**

TL;DR für eilige:
- Destination (1 Satz)
- Kontext & Zielgruppe
- Modul-Übersicht
- Was jedes Modul braucht (Checklist)
- Duplikations-Check
- KI-Integration Pattern
- Session-Plan Modul 3 Beispiel

**Nutzung:** Kopieren → in OpenCode Prompt einfügen → `/wayfinder start`

---

### 2️⃣ Detaillierter Wayfinder-Prompt
**→ [`modul-2-6-redesign-prompt.md`](./modul-2-6-redesign-prompt.md)**

Vollständiger Prompt mit:
- **Destination** (ausführlich)
- **Context & Domain** (Quellen, Zielgruppe, Prinzipien)
- **Notes** (Standing Preferences für diese Wayfinder)
- **Decisions so far** (Was schon entschieden ist)
- **Not yet specified** (Was offen ist, pro Modul)
- **Out of scope** (Was bewusst ausgeschlossen)
- **Session Plan** (Wie wir vorgehen)
- **Akzeptanz-Kriterien** (Wann ist Modul fertig?)
- **Ressourcen & Tools** (Was nutzen wir?)

**Nutzung:** Für tiefere Sessions → ganzes Dokument als Prompt

---

### 3️⃣ Recherche-Befunde & Kontext
**→ [`modul-2-6-research-findings.md`](./modul-2-6-research-findings.md)**

Hintergrund-Recherche mit:
- **Differenzierungs-Analyse** zu pyt-intro-2025, pyt-ai-intro, pyt-cisco
- **KI-Basics Sync** (was Sabine Jungk vermittelt hat)
- **IBAW-Curriculum Alignment** (offizielle Lernziele)
- **Modul 1 Gelerntes** (Pattern übernehmen, nicht duplizieren)
- **Bestehende Materialien** (was recyclen, was archivieren)
- **Zielgruppe-Profil** (Junior-Devs, Post-Ausbildung)
- **KI-Integration-Strategie** (Pattern pro Modul)
- **Modul-Abhängigkeiten** (Reihenfolge)
- **Duplikations-Check Detailliert** (was genau unterscheidet uns)
- **Offene Fragen für Grilling** (vor Session klären)
- **Quick-Start Modul-Template** (Copy-Paste für nächste Module)
- **Angestrebter Rhythmus** (2h × 2 Sessions pro Modul)

**Nutzung:** Referenz während Sessions, für Kontext in Grilling-Phase

---

## 📂 Ticket-Struktur (GitHub Issues)

### Geschlossene Tickets (✅ Getan)

| # | Titel | Type | Link |
|---|-------|------|------|
| 01 | Zielort: Neuaufbau oder Restrukturierung? | grilling | [`01-zielort.md`](./tickets/01-zielort.md) |
| 02 | Scope: Ein Kurs oder zwei? | grilling | [`02-scope.md`](./tickets/02-scope.md) |
| 03 | Tiefe des ersten Deliverables | grilling | [`03-tiefe.md`](./tickets/03-tiefe.md) |
| 04 | Struktur & Mapping erstellen | task | [`04-struktur-und-mapping.md`](./tickets/04-struktur-und-mapping.md) |
| 05 | Pilot Modul 1 (README-Template) | prototype | [`05-pilot-modul.md`](./tickets/05-pilot-modul.md) |
| 06 | No-Code/Low-Code Integration | grilling | [`06-no-code-tools.md`](./tickets/06-no-code-tools.md) |
| 07 | READMEs Modul 2–6 | task | [`07-module-2-bis-6.md`](./tickets/07-module-2-bis-6.md) |
| 08 | Materialien-Migration | task | [`08-migration.md`](./tickets/08-migration.md) |
| 09 | Modul 1 Lektionen planen | grilling | [`09-modul-1-lektionen.md`](./tickets/09-modul-1-lektionen.md) |

### Nächste Tickets (🔄 Open)

| # | Titel | Voraussetzung | Priorität |
|---|-------|---|---|
| 10 | Modul 3 Lektionplan & Lektionen | #09 | 🔥 Jetzt |
| 11 | Modul 4 Lektionplan & Lektionen | #10 | 📌 Danach |
| 12 | Modul 5 Lektionplan & Lektionen | #11 | 📌 Danach |
| 13 | Modul 6 Projekt & Abschluss | #12 | 📌 Zum Schluss |

---

## 🎓 Bestehende Kursmaterialien (Referenzen)

### Alte Wayfinder-Maps (Archive)
- `docs/wayfinder/kurs-redesign-map.md` (aktuelle; geschlossene Tickets)

### Kursmaterialien
- **Modul 1 (Vorbild):** `course/modul-1-programmier-mindset-ki-tools-setup/`
- **Modul 2 (gerade fertig):** `course/modul-2-python-grundlagen-mit-ki/`
- **Modul 3–6 (Skeleton):** `course/modul-N-datenverarbeitung-dateien/` etc.

### Externe Referenzen
- **IBAW-Curriculum:** `docs/Curriculum.md`
- **Alte PDF-Materialien:** `docs/index.pdf`
- **KI-Basics:** `bibliography/**` (Sabine Jungk, Sept 2026)
- **Konsolidierungs-Proposal:** `docs/kurskonsolidierung-proposal.md`
- **FFHS CAS AISE (Bachelor-Level Referenz):** `/Users/daniel/GitRepository/ffhs-aise/`

---

## 🚀 Quick-Start (Kopieren & Loslegen)

### Option A: Kurz-Version
```bash
# Dieses Dokument öffnen
cat docs/wayfinder/WAYFINDER-START.md

# Dann kopieren & starten
/wayfinder start docs/wayfinder/WAYFINDER-START.md
```

### Option B: Ausführlich
```bash
# Modul 2 anschauen (eben fertig, als Template)
ls -la course/modul-2-python-grundlagen-mit-ki/

# Detaillierte Prompts lesen
cat docs/wayfinder/modul-2-6-redesign-prompt.md
cat docs/wayfinder/modul-2-6-research-findings.md

# Dann starten
/wayfinder start docs/wayfinder/modul-2-6-redesign-prompt.md
```

### Option C: Map tracken
```bash
# Zentrale Wayfinder Map (GitHub Issues)
open docs/wayfinder/kurs-redesign-map.md

# Tickets durchgehen
ls docs/wayfinder/tickets/
```

---

## 📊 Status Übersicht

| Modul | Status | Datei | Lektionen | Übungen | Hausaufgaben | Cheatsheets | Demo-Scripts |
|-------|--------|-------|-----------|---------|--------------|-------------|---|
| 1 ✅ | Done | README.md | 4 ✅ | 3 ✅ | 2 ✅ | 1 | 4 ✅ |
| 2 ✅ | Done | README.md | 4 ✅ | 3 ✅ | 2 ✅ | 4 ✅ | 4 ✅ |
| 3 🔄 | In Progress | README.md | 0 | 0 | 0 | 0 | 0 |
| 4 🔄 | Planning | README.md | 0 | 0 | 0 | 0 | 0 |
| 5 🔄 | Planning | README.md | 0 | 0 | 0 | 0 | 0 |
| 6 🔄 | Planning | README.md | 0 | 0 | 0 | 0 | 0 |

---

## 📖 Wie man diese Wayfinder nutzt

### Für eine neue Session

1. **Lesen:** [`WAYFINDER-START.md`](./WAYFINDER-START.md) (5 Min)
2. **Kontext:** [`modul-2-6-research-findings.md`](./modul-2-6-research-findings.md) (10 Min)
3. **Prompt:** [`modul-2-6-redesign-prompt.md`](./modul-2-6-redesign-prompt.md) (Kopieren)
4. **Starten:** `/wayfinder start modul-2-6-redesign-prompt.md`

### Während einer Session

- **Referenzen:** Research-Findings für Duplikations-Check
- **Template:** Modul 1 & 2 als Struktur-Vorbild
- **Checklists:** Acceptance Criteria im Prompt

### Nach einer Session

- **Map updaten:** `kurs-redesign-map.md` (Decision zu Decisions-so-far)
- **Tickets schließen/öffnen:** GitHub Issues
- **Nächste Prompt:** Neue Datei für nächstes Modul (analog `modul-2-6-redesign-prompt.md`)

---

## 🤝 Unterstützende Ressourcen

### Skills (im Prompt integriert)
- **wayfinder** – Diese Navigation
- **grilling** – Tiefe Fragen stellen
- **domain-modeling** – Domänen-Vokabular klären
- **research** – Externe Quellen recherchieren
- **prototype** – Schnelle Prototypen bauen

### Tools
- **OpenCode** – Editor & Git
- **GitHub Issues** – Ticket-Tracking (mit Labels `wayfinder:*`)
- **Markdown & AsciiDoc** – Dokumentation
- **Python 3.13 + uv** – Code & Demo-Scripts

---

## 💡 Tips für diese Wayfinder

### Wenn du feststeckst
- Lies den entsprechenden Ticket (`tickets/NN-*.md`)
- Prüfe: Ist die Frage bereits in "Decisions so far"?
- Falls nicht: Neue Grilling-Frage stellen → neuen Ticket erstellen

### Wenn du parallele Sessions brauchst
- Research-Tickets spin up (z.B. "Analysiere pyt-intro-2025 Modul 3")
- Diese laufen async, während du aktuelle Session fortfährst

### Wenn die Map wächst
- Fog-Abschnitt ("Not yet specified") mit neuen Erkenntnissen updaten
- Neue Tickets erstellen, sobald Frage scharf ist
- Alte Tickets sind lieber closed & out-of-scope als zombie-offen

---

_Letzte Aktualisierung: 2026-10-07_  
_Ready: Modul 1 & 2 fertig → Modul 3 planen_
