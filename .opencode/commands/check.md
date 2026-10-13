---
description: Führe Projekt-Checks aus und behebe Fehler ohne zu committen
category: code-analysis-testing
allowed-tools: Bash, Edit, Read
---

# Projekt-Validierung durchführen

Führe Projekt-Validierungs-Checks durch und löse alle gefundenen Fehler.

## Prozess

1. **Package Manager erkennen** (für JavaScript/TypeScript Projekte):
   - npm: Suche nach package-lock.json
   - pnpm: Suche nach pnpm-lock.yaml
   - yarn: Suche nach yarn.lock
   - bun: Suche nach bun.lockb

2. **Verfügbare Scripts prüfen**:
   - package.json lesen um Check/Validierungs-Scripts zu finden
   - Häufige Script-Namen: `check`, `validate`, `verify`, `test`, `lint`

3. **Entsprechenden Check-Befehl ausführen**:
   - JavaScript/TypeScript:
     - npm: `npm run check` oder `npm test`
     - pnpm: `pnpm check` oder `pnpm test`
     - yarn: `yarn check` oder `yarn test`
     - bun: `bun check` oder `bun test`

   - Andere Sprachen:
     - Python: `pytest`, `flake8`, `mypy`, oder `make check`
     - Go: `go test ./...` oder `golangci-lint run`
     - Rust: `cargo check` oder `cargo test`
     - Ruby: `rubocop` oder `rake test`

4. **Fehler beheben**:
   - Fehler-Output analysieren
   - Code-Probleme, Syntax-Fehler oder Test-Failures beheben
   - Checks nach Behebung erneut ausführen

5. **Wichtige Einschränkungen**:
   - KEINEN Code committen
   - KEINE Versionsnummern ändern
   - Nur Fehler beheben um Checks zum Bestehen zu bringen

Falls kein Check-Script existiert, führe die passendste Validierung für den Projekttyp aus.
