---
description: Initialisiere ein neues OpenSource-Projekt mit GitHub Best Practices
allowed-tools:
  - Bash
  - Write
  - Read
  - Glob
---

# OpenSource-Projekt initialisieren

Erstellt ein neues OpenSource-Projekt mit vollständiger GitHub-Infrastruktur und Community-Standards.

## Verwendung

```bash
# Standard Git-Projekt
/init-project --git

# Python-Projekt mit uv
/init-project --uv

# Mit Projektnamen
/init-project --git --name "my-awesome-project"

# Interaktiv
/init-project --interactive
```

## Features

- ✅ **Community Standards**: LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- ✅ **GitHub Templates**: Issue Templates, PR Template, Security Advisories
- ✅ **Dokumentation**: README.md mit Badges, Struktur und Best Practices
- ✅ **Git Setup**: .gitignore, .gitattributes, Branch Protection Empfehlungen
- ✅ **Python Support**: uv-basierte Projektstruktur (optional)
- ✅ **CI/CD Ready**: GitHub Actions Workflows

## Prozess

### 1. Projekt-Typ ermitteln

**Bei `--interactive`**:
- Frage Projekt-Typ: Git, Python (uv), Node.js, Go, Rust, Java
- Frage Projektname
- Frage License-Typ: MIT, Apache 2.0, GPL-3.0, BSD-3-Clause
- Frage Primary Language

**Bei `--git`**:
- Standard Git-Projekt
- Erkenne Sprache aus vorhandenen Dateien

**Bei `--uv`**:
- Prüfe ob `uv` installiert ist
- Falls nicht: `pip install uv --break-system-packages`
- Führe `uv init` aus
- Erweitere mit GitHub Standards

### 2. Basis-Initialisierung

**Git-Projekt** (`--git`):
```bash
git init
git branch -M main
git commit --allow-empty -m "🎉 Initial commit"
```

**Python-Projekt** (`--uv`):
```bash
# uv installieren falls nötig
command -v uv || pip install uv --break-system-packages

# Projekt initialisieren
uv init [projekt_name]
cd [projekt_name]

# Virtual Environment erstellen
uv venv
source .venv/bin/activate  # oder .venv\Scripts\activate (Windows)
```

### 3. Community Standards erstellen

**LICENSE** (MIT als Standard):
```markdown
MIT License

Copyright (c) [YEAR] [AUTHOR]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Standard MIT License Text]
```

**CONTRIBUTING.md**:
- Feature-Branch Workflow
- PR Process
- Code Standards
- Testing Requirements

**CODE_OF_CONDUCT.md**:
- Contributor Covenant 2.1
- Contact Information
- Enforcement Guidelines

**SECURITY.md**:
- Supported Versions
- Reporting Process
- Security Advisories Link

### 4. GitHub Templates erstellen

**.github/ISSUE_TEMPLATE/**:
- `bug_report.yml` - Strukturiertes Bug-Report-Formular
- `feature_request.yml` - Feature-Request mit Priorisierung
- `documentation.yml` - Dokumentations-Issues
- `config.yml` - Links zu Discussions/Security

**.github/PULL_REQUEST_TEMPLATE.md**:
- Beschreibung
- Änderungstyp (Feature, Fix, Docs, etc.)
- Testing Checklist
- Breaking Changes

**.github/workflows/** (optional):
- `ci.yml` - Basis CI/CD Pipeline
- `lint.yml` - Code Quality Checks

### 5. README.md erstellen

**Struktur**:
```markdown
# [Projektname]

[Badges: License, Platform, CI Status, etc.]

[1-2 Sätze Beschreibung]

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

[Sprach-spezifische Installation]

## Quick Start

[Minimales Beispiel]

## Documentation

- [Link to Docs]
- [Link to API Reference]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

[License Type] - See [LICENSE](LICENSE)

## Support

- GitHub Issues: Bug Reports & Feature Requests
- GitHub Discussions: Questions & Community
- Security: See [SECURITY.md](SECURITY.md)
```

### 6. .gitignore erstellen

**Python**:
```gitignore
# Virtual Environment
.venv/
venv/
env/

# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Testing
.pytest_cache/
.coverage
htmlcov/
```

**Node.js**:
```gitignore
node_modules/
npm-debug.log*
.env
dist/
build/
```

### 7. Erste Commits erstellen

**Initial Commit**:
```bash
git add .
git commit -m "🎉 feat: Initial OpenSource Setup

- MIT License
- Community Standards (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY)
- GitHub Templates (Issues, PRs)
- README mit Badges und Struktur
- .gitignore für [Language]
- CI/CD Workflows
"
```

### 8. GitHub Repository erstellen (optional)

```bash
# Mit gh CLI
gh repo create [name] --public --description "[description]"
gh repo edit --enable-issues --enable-discussions
gh repo edit --enable-wiki=false

# Remote hinzufügen
git remote add origin https://github.com/[user]/[name].git
git push -u origin main
```

## Sprach-spezifische Setups

### Python (uv)

**Projektstruktur**:
```text
projekt_name/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
├── src/
│   └── projekt_name/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── docs/
├── .gitignore
├── pyproject.toml
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── SECURITY.md
```

**pyproject.toml** (erweitert):
```toml
[project]
name = "projekt-name"
version = "0.1.0"
description = "Project description"
authors = [{name = "Author", email = "email@example.com"}]
readme = "README.md"
license = {file = "LICENSE"}
requires-python = ">=3.9"

[project.urls]
Homepage = "https://github.com/user/repo"
Documentation = "https://github.com/user/repo#readme"
Repository = "https://github.com/user/repo"
Issues = "https://github.com/user/repo/issues"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### JavaScript/TypeScript

**package.json** (erweitert):
```json
{
  "name": "projekt-name",
  "version": "0.1.0",
  "description": "Project description",
  "license": "MIT",
  "author": "Author <email@example.com>",
  "repository": {
    "type": "git",
    "url": "https://github.com/user/repo"
  },
  "bugs": "https://github.com/user/repo/issues",
  "homepage": "https://github.com/user/repo#readme"
}
```

### Go

**go.mod & Struktur**:
```text
projekt_name/
├── cmd/
│   └── main.go
├── internal/
├── pkg/
├── README.md
├── LICENSE
├── go.mod
└── .github/
```

## Best Practices

### LICENSE-Auswahl

| License | Use Case | Kommerzielle Nutzung | Copyleft |
|---------|----------|----------------------|----------|
| **MIT** | Permissive, maximale Freiheit | ✅ Ja | ❌ Nein |
| **Apache 2.0** | Permissive + Patent-Grant | ✅ Ja | ❌ Nein |
| **GPL-3.0** | Strong Copyleft | ✅ Ja (mit Einschränkungen) | ✅ Ja |
| **BSD-3-Clause** | Permissive + Namensschutz | ✅ Ja | ❌ Nein |

**Empfehlung**: MIT für maximale Adoption, Apache 2.0 für Patent-Schutz

### README Best Practices

✅ **Gut**:
- Badges zeigen Status auf einen Blick
- Quick Start unter 5 Minuten
- Screenshots/GIFs für UI-Projekte
- Klare Installation-Schritte
- Links zu ausführlicher Docs

❌ **Schlecht**:
- Keine Badges oder veraltete Badges
- Fehlende Installation-Anweisungen
- Keine Beispiele
- Broken Links

### Contributing Guidelines

**Essentials**:
- Branch-Naming: `feature/`, `fix/`, `docs/`
- PR-Prozess mit Review-Requirements
- Code-Style (Linter, Formatter)
- Test-Coverage Requirements
- Commit-Message Format

## Troubleshooting

**uv nicht gefunden**:
```bash
pip install uv --break-system-packages
# oder
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**gh CLI nicht verfügbar**:
```bash
# macOS
brew install gh

# Linux
sudo apt install gh

# Windows
winget install GitHub.cli
```

**Git nicht konfiguriert**:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Weitere Informationen

**Verwandte Commands**:
- `/commit` - Professionelle Commits erstellen
- `/create-pr` - Pull Requests mit Template
- `/run-ci` - CI-Checks ausführen

**Referenzen**:
- [GitHub Community Standards](https://docs.github.com/en/communities)
- [Contributor Covenant](https://www.contributor-covenant.org/)
- [Choose a License](https://choosealicense.com/)
- [uv Documentation](https://docs.astral.sh/uv/)
