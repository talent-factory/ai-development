---
description: Führe CI-Checks aus und behebe alle Fehler bis alle Tests bestehen
allowed-tools:
  - Bash
  - Edit
  - Read
  - Glob
---

# CI-Checks ausführen

Führe CI-Checks für das Projekt aus und behebe alle Fehler bis alle Tests bestehen.

## Verwendung

```bash
# CI-Checks ausführen
/run-ci
```

## Prozess

1. **CI-System erkennen**:
   - Prüfe auf CI-Konfigurationsdateien:
     - `.github/workflows/*.yml` (GitHub Actions)
     - `.gitlab-ci.yml` (GitLab CI)
     - `.circleci/config.yml` (CircleCI)
     - `Jenkinsfile` (Jenkins)
     - `.travis.yml` (Travis CI)
     - `bitbucket-pipelines.yml` (Bitbucket)

2. **Build-System erkennen**:
   - JavaScript/TypeScript: package.json scripts
   - Python: Makefile, tox.ini, setup.py, pyproject.toml
   - Go: Makefile, go.mod
   - Rust: Cargo.toml
   - Java: pom.xml, build.gradle
   - Andere: Suche nach gängigen CI-Scripts

3. **CI-Befehle ausführen**:
   - Prüfe auf CI-Scripts: `ci`, `test`, `check`, `validate`, `verify`
   - Gängige Script-Standorte:
     - `./scripts/ci.sh`, `./ci.sh`, `./run-tests.sh`
     - Package Manager Scripts (npm/yarn/pnpm run test)
     - Make-Targets (make test, make ci)
   - Virtuelle Umgebungen aktivieren falls nötig (Python, Ruby, etc.)

4. **Fehler beheben**:
   - Fehlerausgabe analysieren
   - Code-Probleme, Test-Fehler oder Konfigurationsprobleme beheben
   - CI-Checks nach jeder Behebung erneut ausführen

5. **Gängige CI-Aufgaben**:
   - Linting/Formatierung
   - Type-Checking
   - Unit-Tests
   - Integrationstests
   - Build-Verifikation
   - Dokumentationsgenerierung

## Beispiele

**JavaScript/TypeScript**:
```bash
npm test           # Standard-Tests
npm run ci         # Vollständige CI-Pipeline
npm run lint       # Linting
npm run type-check # TypeScript Type-Checking
```

**Python**:
```bash
make test          # Makefile-basiert
pytest             # Direkte Test-Ausführung
tox                # Multi-Environment Testing
ruff check .       # Linting
mypy .             # Type-Checking
```

**Go**:
```bash
go test ./...      # Alle Tests
make test          # Makefile-basiert
go vet ./...       # Code-Analyse
golangci-lint run  # Linting
```

**Rust**:
```bash
cargo test         # Tests
cargo check        # Kompilierung prüfen
cargo clippy       # Linting
cargo fmt --check  # Formatierung prüfen
```

**Java**:
```bash
mvn test           # Maven Tests
gradle test        # Gradle Tests
mvn verify         # Vollständige Verifikation
```

## Workflow

1. **Erkennung**: Identifiziere CI-System und Build-Tools
2. **Ausführung**: Führe relevante CI-Checks aus
3. **Analyse**: Bei Fehlern, analysiere Fehlerausgabe
4. **Behebung**: Fixe identifizierte Probleme
5. **Iteration**: Wiederhole bis alle Checks bestehen

**Wichtig**: Behebe weiterhin Probleme und führe CI-Checks erneut aus, bis alle Tests erfolgreich durchlaufen.
