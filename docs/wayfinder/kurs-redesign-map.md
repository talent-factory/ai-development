# Wayfinder Map: Kurs-Redesign Python & KI

**Label:** `wayfinder:map`

---

## Destination

Der `ai-development`-Repo ist als einheitlicher 6-Modul-Kurs **«Python & KI: Vom Programmier-Mindset zum eigenen KI-Projekt»** neu strukturiert. Jedes Modul folgt dem bewährten Format aus `pyt-intro-2025`:

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

Bestehende Materialien (Kapitel, Übungen, Lösungen, Scripts, Streamlit-Apps, Folien) sind sinnvoll den Modulen zugeordnet. Die Struktur und das Inhalts-Mapping liegen als Review-fähige Artefakte vor; vollständige Lektionen werden danach Modul für Modul ausgefüllt.

---

## Notes

- **Domain:** Bildung / Kursdesign / AI-Assisted Development
- **Skills:** wayfinder, grilling, domain-modeling, research
- **Präferenzen:**
  - Bewährtes Template aus `pyt-intro-2025` übernehmen (00-05 + README)
  - Bestehende Inhalte möglichst erhalten und umstrukturieren statt neu schreiben
  - Deutsch als Kurs- und Dokumentationssprache beibehalten
  - Erst Struktur + Mapping, dann Befüllung

---

## Decisions so far

- [Q1 – Zielort: Neuaufbau oder Restrukturierung?](./tickets/01-zielort.md): Restrukturierung innerhalb von `ai-development`.
- [Q2 – Scope: Ein Kurs oder zwei?](./tickets/02-scope.md): Ein 6-Modul-Kurs; Zwei-Kurs-Split aus Proposal ist out of scope.
- [Q3 – Tiefe des ersten Deliverables](./tickets/03-tiefe.md): Zuerst Struktur + Inhalts-Mapping, dann iterative Befüllung.
- [Struktur & Mapping](./tickets/04-struktur-und-mapping.md): Verzeichnisstruktur `course/modul-N-name/` mit 00-05-Ordnern erstellt; Mapping-Dokument abgelegt.
- [Pilot-Modul 1](./tickets/05-pilot-modul.md): README-Vorlage in Modul 1 etabliert.
- [No-Code/Low-Code](./tickets/06-no-code-tools.md): Flowise/Langflow als No-Code-RAG-Option in Modul 5, n8n/Make als Ausblick in Modul 6 (Deployment/Automatisierung); Entscheidung ist review-fähig.
- [READMEs Modul 2–6](./tickets/07-module-2-bis-6.md): Alle Modul-READMEs mit Lernzielen, Struktur und Material-Verweisen erstellt.
- [Migration](./tickets/08-migration.md): Bestehende Materialien physisch in `course/modul-X/` verschoben, interne Verweise angepasst, `AGENTS.md` und `.windsurfrules` aktualisiert.

---

## Not yet specified

- Umgang mit den verbleibenden PowerPoint-Folien (`docs/slides/`)
- Detaillierte Lernziele und Lektionen pro Modul (jenseits der README-Grobplanung)
- Abschlussprojekt: Umfang, Bewertung, Vorlage

---

## Out of scope

- **Zwei-Kurs-Split** aus `kurskonsolidierung-proposal.md` (Kurs 1 «Python Basis» + Kurs 2 «Python & KI Professional»). Die aktuelle Ausschreibung definiert einen 6-Modul-Kurs; ein späterer Split kann auf dieser Basis aufsetzen.
- Marketingtexte, Ausschreibungsformulierungen oder Zertifikatsdesign.
- Vollständige Neuschreibung aller Lektionen in diesem Durchgang.

---

## Tickets

| # | Ticket | Type | Status | Blocked by |
|---|--------|------|--------|------------|
| 1 | [Inventarisiere Materialien und erstelle Modulstruktur + Mapping](./tickets/04-struktur-und-mapping.md) | task | closed | – |
| 2 | [Erstelle Modul-README-Vorlage und Pilot-Modul 1](./tickets/05-pilot-modul.md) | prototype | closed | #1 |
| 3 | [Entscheide über No-Code/Low-Code-Integration](./tickets/06-no-code-tools.md) | grilling | closed | #1 |
| 4 | [Erstelle READMEs für Modul 2–6](./tickets/07-module-2-bis-6.md) | task | closed | #2, #3 |
| 5 | [Migriere bestehende Übungen, Scripts und Beispiele](./tickets/08-migration.md) | task | closed | #4 |

---

*Letzte Aktualisierung: 2026-10-06*
