# Ticket 8: Migriere bestehende Übungen, Scripts und Beispiele

**Type:** `wayfinder:task`
**Status:** closed
**Blocked by:** #7

## Question

Wie werden die im Mapping als «übernehmen» markierten Materialien physisch in die neue Modulstruktur verschoben oder verlinkt?

## Acceptance Criteria

- [x] Entscheidung pro Material: verschieben (mv), kopieren (cp), verlinken (symlink) oder belassen + Verweis
- [x] Durchführung der Migration für alle markierten Materialien
- [x] Anpassung interner Verweise (Pfade, Bilder, Code-Importe)
- [x] Keine doppelten Inhalte ohne Grund

## Resolution

**Strategie pro Materialart:**

- **Kapitel/Übungen/Lösungen (`.adoc`, `.md`):** Physisch in die entsprechenden `course/modul-X/`-Ordner verschoben; relative Pfade zu `docs/locale/` und `docs/images/` angepasst.
- **Code-Beispiele (`.py`):** Verschoben in `05-beispiele/`. Import-Pfade in `src/pydantic/tool/` aktualisiert (`parents[3]` → `parents[4]`), damit `src.utils` weiterhin erreichbar bleibt.
- **Slides (`.pdf`, `.pptx`):** In `04-materialien/` der jeweiligen Module verschoben.
- **Grosse Projekte (`rag-system/`, `replicate/`):** Belassen im Repo-Root, aber als Symlinks in `course/modul-5/05-beispiele/` bzw. `course/modul-6/05-beispiele/` eingebunden.
- **Legacy-Index (`docs/index.adoc`):** Als Verweis auf die neue Struktur umgeschrieben.
- **Projektdokumentation (`AGENTS.md`, `.windsurfrules`, `.gitignore`):** Aktualisiert, damit Pfade und Befehle zur neuen Struktur passen.

Ticket geschlossen.
