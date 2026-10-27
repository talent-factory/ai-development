# Modul 4: Agentic Coding – KI als Entwicklungspartner

**Dauer:** 1 Tag (4 Lektionen à 50 Minuten)  
**Voraussetzung:** Modul 3 abgeschlossen (Dateien, APIs, Fehlerbehandlung).

---

## 🎯 Lernziele

Nach diesem Modul können Sie:

1. ✅ Mit einem Coding-Agenten (OpenCode oder Claude Code) arbeiten und eine Änderung zuerst planen (`plan.md`).
2. ✅ Funktionen test-first mit dem Agenten entwickeln (TDD).
3. ✅ KI-Code gegen Plan und Standards prüfen und in Kleinschritten verbessern.
4. ✅ Fehler systematisch diagnostizieren statt raten.
5. ✅ Den Durchlauf Plan → Test → Code → Review → Doku selbständig durchführen.
6. ✅ Zwischen Vertrauen und Prüfen abwägen (3-Punkte-Check).

---

## 📚 Modulstruktur

### [00-vorbereitung/](./00-vorbereitung/)

**Zeitaufwand:** ca. 60–75 Minuten

- Pflicht-Setup: OpenCode oder Claude Code, Modell-Zugang, Skills, `check_setup.py`
- Wiederholung: Funktionen, `pytest`, Git

### [01-praxis/](./01-praxis/)

**Präsenzunterricht:** 4 Lektionen à 50 Minuten

- **Lektion 1:** Arbeitsweise und Planen: Code erklären lassen, mit `grilling` einen `plan.md` schreiben.
- **Lektion 2:** TDD mit dem Agenten: Tests für den Ist-Stand, dann `vergleiche_staedte` test-first.
- **Lektion 3:** Review, Refactoring und Diagnose: KI-Code gegen `plan.md` prüfen, `hole_live_wetter` entflechten, Fehler reproduzieren.
- **Lektion 4:** Dokumentation und Durchlauf: Doku, dann `finde_kaeltesten_tag` durch Plan → Test → Code → Review → Doku.

> Altmaterial (archiviert): `01-praxis/archive/`

### [02-uebungen/](./02-uebungen/)

**Übungen während der Präsenz**

- ex-01 Plan: `plan.md` für `vergleiche_staedte`
- ex-02 TDD: Tests für den Ist-Stand und `vergleiche_staedte` test-first
- ex-03 Review, Refactoring, Diagnose
- ex-04 Mini-Durchlauf mit `finde_kaeltesten_tag`

> Altmaterial (archiviert): `02-uebungen/archive/command-examples/`

### [03-nachbearbeitung/](./03-nachbearbeitung/)

**Hausaufgaben vor Modul 5**

- Eigener Durchlauf an einem kleinen Feature (`plan.md`, Tests, Code, `README.md`, `review-notiz.md`)
- Reflexionsbogen

### [04-materialien/](./04-materialien/)

**Handouts & Ressourcen**

- `cheatsheet-prompts.adoc` und `cheatsheet-skills.adoc`
- `weitere-frameworks.md`
- `cli-comparison.md` (älterer Vergleich, ohne OpenCode)


### [05-beispiele/](./05-beispiele/)

**Code-Beispiele vom Dozenten**

- Startpunkt `wetter_bericht/` und je Lektion eine Musterlösung `lektion-N/loesung/`

> Vorhandenes Material: `05-beispiele/wetter_bericht/` (Startpunkt), `05-beispiele/check_setup.py`. Altmaterial (archiviert): `05-beispiele/archive/tool/`

---

## ⏱️ Zeitplan

| Phase | Aktivität | Dauer |
|-------|-----------|-------|
| **Vor Tag 4** | Vorbereitung: Setup + Wiederholung | 60–75 Min |
| **Tag 4** | 4 Lektionen Präsenzunterricht | 4 × 50 Min |
| **Tag 4** | Pausen | 30 Min |
| **Nach Tag 4** | Eigener Durchlauf + Reflexion | 2–3 Std |

---

## 🔗 Verknüpfungen

- **Vorheriges Modul:** [Modul 3 – Datenverarbeitung & Dateien](../modul-3-datenverarbeitung-dateien/)
- **Nächstes Modul:** [Modul 5 – Fortgeschrittene KI-Integration](../modul-5-fortgeschrittene-ki-integration/)
