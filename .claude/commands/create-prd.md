---
description: Erstelle ein Produkt-Anforderungsdokument (PRD) für eine Produktfunktion
category: project
argument-hint: "<Funktionsbeschreibung> [Ausgabepfad]"
allowed-tools:
  - Write
  - TodoWrite
  - Read
---

# Claude Command: Create PRD

Erstelle ein umfassendes, professionelles Product Requirements Document (PRD) basierend auf Industry-Best-Practices.

## Verwendung

```bash
/create-prd "Funktionsbeschreibung"
/create-prd "Funktionsbeschreibung" /path/to/output.md
```

**Beispiele**:

```bash
/create-prd "Dark Mode Toggle zu Einstellungen hinzufügen"
/create-prd "KI-gestützte Budgetierung" docs/prds/budget-ai.md
```

## Workflow

1. **Analyse der Funktionsbeschreibung**
   - Verstehe Umfang und Komplexität
   - Identifiziere Projekttyp (Feature, Initiative, Technical)
   - Wähle passendes PRD-Template

2. **Strukturiertes PRD erstellen**
   - Executive Summary (Problem, Lösung, Impact)
   - Problemstellung mit Evidenz
   - Messbare Ziele & Erfolgsmetriken
   - User Stories mit Akzeptanzkriterien
   - Funktionale & Nicht-funktionale Anforderungen
   - Klare Abgrenzung (Out of Scope)
   - Risikobewertung mit Mitigation
   - Timeline & Meilensteine

3. **TodoWrite für Tracking**
   - Nutze TodoWrite um PRD-Abschnitte während Erstellung zu verfolgen
   - Stelle Vollständigkeit sicher

4. **Ausgabe**
   - Speichere PRD am angegebenen Pfad
   - Standard: `PRD.md` im aktuellen Verzeichnis

## PRD-Grundprinzipien

### Nutzer-zentriert, nicht lösungszentriert

**Fokus auf**:

- **Problem**: Welches Problem lösen wir?
- **Nutzer**: Für wen lösen wir es?
- **Impact**: Welchen Wert schaffen wir?

**NICHT auf**:

- Technische Implementierung
- Spezifische Lösungsansätze
- Code/Architektur-Details

### SMART Ziele

- **S**pezifisch: Klar definiert
- **M**essbar: Quantifizierbar
- **A**rreichbar: Realistisch
- **R**elevant: Wichtig für Business/User
- **T**erminiert: Klarer Zeitrahmen

### Klare Priorisierung

**MoSCoW-Methode**:

- **Must-Have**: Kritisch für MVP
- **Should-Have**: Wichtig, nicht kritisch
- **Could-Have**: Nice-to-Have
- **Won't-Have**: Explizit ausgeschlossen

## PRD-Struktur

### 1. Executive Summary (3-5 Sätze)

Was, Für wen, Warum, Impact, Timeline

### 2. Problemstellung

- Aktueller Zustand
- Problembeschreibung
- Auswirkungen (quantifiziert)
- Evidenz (Daten, Research)
- Warum jetzt?

### 3. Ziele & Erfolgsmetriken

- Produkt-Ziele
- Business-Ziele
- Primäre Metriken (mit Baseline & Target)
- Sekundäre Metriken
- Guardrail Metriken

### 4. User Stories & Personas

- Detaillierte Personas (datenbasiert)
- User Stories (Als X möchte ich Y damit Z)
- Akzeptanzkriterien (testbar)
- Kontext & Rationale

### 5. Funktionale Anforderungen

- Nach Priorität geordnet (Must/Should/Could/Won't)
- Detaillierte Beschreibung
- Akzeptanzkriterien
- Edge Cases
- User Flows

### 6. Nicht-funktionale Anforderungen

- Performance (Geschwindigkeit, Latenz)
- Security & Privacy (GDPR, etc.)
- Scalability (Wachstum)
- Usability & Accessibility (WCAG 2.1)
- Reliability (Uptime, Error Rate)

### 7. Abgrenzung (Out of Scope)

- Was NICHT gebaut wird
- Rationale für Ausschlüsse
- Geplante Timeline für Future Features

### 8. Risikobewertung

- Risiko-Matrix (Impact × Likelihood)
- Mitigation-Strategien
- Contingency-Pläne
- Owner-Zuweisung

### 9. Timeline & Meilensteine

- Phasen-Plan
- Key Milestones
- Dependencies
- Approvals

## Template-Auswahl

Basierend auf Projekt-Komplexität:

| Typ              | Dauer          | Template         |
|------------------|----------------|------------------|
| Small Feature    | < 2 Wochen     | Minimal MVP      |
| Standard Feature | 4-8 Wochen     | Standard Feature |
| Major Initiative | > 2 Monate     | Major Initiative |
| Platform/Infra.  | Variabel       | Technical PRD    |

**Details**: [templates.md](../references/create-prd/templates.md)

## Best Practices

**DO ✅**:

- Nutzerbedürfnisse und Business Value fokussieren
- Messbare, SMART-Ziele definieren
- Konkrete Akzeptanzkriterien schreiben
- Daten und Evidenz einbinden
- Risiken proaktiv adressieren
- Klare Abgrenzung kommunizieren

**DON'T ❌**:

- Technische Implementierung vorschreiben
- Vage Ziele ("mehr Nutzer")
- Anforderungen ohne Priorisierung
- Features ohne Rationale
- Out-of-Scope ignorieren

**Vollständiger Guide**: [best-practices.md](../references/create-prd/best-practices.md)

## Qualitätskriterien

### Inhalt

- [ ] Executive Summary prägnant (< 5 Sätze)
- [ ] Problem klar mit Evidenz definiert
- [ ] Ziele sind SMART
- [ ] User Stories mit Akzeptanzkriterien
- [ ] Anforderungen priorisiert (Must/Should/Could)
- [ ] NFRs für Performance, Security, Usability
- [ ] Erfolgsmetriken mit konkreten Zahlen
- [ ] Risiken identifiziert mit Mitigation
- [ ] "Out of Scope" definiert

### Format

- [ ] Konsistente Formatierung
- [ ] Hierarchische Struktur
- [ ] Listen & Tabellen für Übersicht
- [ ] Professionelle Sprache

### Prozess

- [ ] Vollständig und actionable
- [ ] Verständlich für alle Stakeholder
- [ ] Keine Widersprüche
- [ ] Realistischer Scope

## Weitere Informationen

- **Best Practices**: [best-practices.md](../references/create-prd/best-practices.md)
  - Grundprinzipien
  - Erfolgsmetriken definieren
  - Stakeholder-Management
  - Häufige Fehler vermeiden

- **Templates**: [templates.md](../references/create-prd/templates.md)
  - Minimal MVP Template
  - Standard Feature Template
  - Major Initiative Template
  - Technical PRD Template

- **Abschnitte-Guide**: [sections-guide.md](../references/create-prd/sections-guide.md)
  - Detaillierte Anleitung für jeden Abschnitt
  - Beispiele (Gut vs. Schlecht)
  - Häufige Fehler pro Abschnitt
  - Schreibtipps

---

**Feature description**: $ARGUMENTS
