# [KI Professional – Fachrichtung Development](https://ibaw.ch/bildungsangebote/informatik/digital-collaboration-transformation/ki-professional-development/#rowno5)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Daniel%20Senften-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dsenften/)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-blue?logo=github&logoColor=white)](https://github.com/talent-factory/ki-development)
&nbsp;
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
&nbsp;
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

Python-Grundlagen mit KI-gestütztem Programmieren verbinden – das ist der rote Faden dieses Kurses. Sie lernen, Probleme sauber zu zerlegen, in einer professionellen Entwicklungsumgebung zu arbeiten und mittels effektivem Prompting hochwertige, KI-generierte Lösungen zu erstellen.

Der Kurs vermittelt zentrale Python-Konzepte, Datenverarbeitung, APIs und Debugging direkt mit LLM-Unterstützung. Moderne Kerntechniken wie Refactoring, TDD, Code-Review, Embeddings, RAG und der Einsatz von AI Agents als aktive Entwicklungspartner werden praxisnah umgesetzt. Das Gelernte fliesst in ein eigenes Abschlussprojekt ein.

## 🚀 Projekt-Setup

Dieses Projekt verwendet `uv` als Paketmanager und Build-System. `uv` ist ein schneller, zuverlässiger und kompatibler Ersatz für pip und pip-tools, der in Rust geschrieben wurde.

### Voraussetzungen

- Python 3.10 oder höher
- `uv` installieren:

  ```bash
  pip install uv
  ```

### Installation

1. Abhängigkeiten aus dem Lockfile installieren:

   ```bash
   uv sync
   ```

2. Lokale Pakete importierbar machen (optional, für `src/utils` etc.):

   ```bash
   uv pip install -e .
   ```

### Entwicklung

- **Neue Abhängigkeit hinzufügen**:

  ```bash
  uv add <paketname>
  ```

- **Streamlit-App starten**:

  ```bash
  uv run streamlit run course/modul-X/05-beispiele/<app_name>.py
  ```

- **Python-Script ausführen**:

  ```bash
  uv run python <pfad_zum_script.py>
  ```

## LERNZIELE

---

Am Ende dieses Lerngangs …

- verstehen Sie, was KI ist und wie sie grundsätzlich funktioniert.
- kennen Sie die wichtigsten KI-Begriffe und können mitreden.
- wissen Sie, was Sie mit KI dürfen und was nicht – rechtlich, ethisch und beim Datenschutz.
- erkennen Sie, wo KI hilft, wo sie schadet und wo ihre Grenzen liegen.
- verstehen Sie, was Programmieren ist – klassisch und mit KI – und können grosse Aufgaben in kleine Schritte zerlegen.
- richten Sie Ihre Arbeitsumgebung ein und finden sich darin zurecht.
- schreiben Sie eigene Python-Programme mit den wichtigsten Bausteinen (Variablen, Schleifen, Funktionen).
- lesen und verarbeiten Sie Daten aus verschiedenen Dateien und holen Informationen aus dem Internet – stabil und mit sauberer Fehlerbehandlung.
- prüfen Sie Ihren Code automatisch auf Fehler, verbessern ihn Schritt für Schritt und dokumentieren ihn so, dass auch andere damit weiterarbeiten können.
- nutzen Sie KI-Tools, um schneller und besser zu programmieren.
- bauen Sie einfache KI-Helfer, die selbständig mehrere Schritte erledigen, und können sie testen und Fehler beheben.
- planen und bauen Sie eine produktionsreife KI-Anwendung, die sicher ist, Daten schützt und fair mit allen Nutzern umgeht.

## INHALT

Der Kurs ist modular in sechs aufeinanderaufbaumende Module strukturiert. Detaillierte Lektionspläne, Übungen und Materialien finden sich in [`course/README.md`](course/README.md).

### Modul 1: Programmier-Mindset & KI-Tools Setup

- Was ist Programmieren? Klassisch und mit KI.
- KI-Begriffswelt: Prompt, Command, Skill, Agent, Hook, LLM, RAG.
- Einrichten der Arbeitsumgebung: VS Code, Python, uv, OpenCode.
- Erste Python-Schritte mit KI als Erklär-Partner.

### Modul 2: Python-Grundlagen mit KI verstehen

- Variablen, Datentypen, Operatoren.
- Bedingte Anweisungen und Schleifen.
- Funktionen definieren und wiederverwenden.
- KI gezielt für Code-Erklärung und Erweiterung nutzen.

### Modul 3: Datenverarbeitung & Dateien

- Textdateien, CSV und JSON lesen und schreiben.
- HTTP-APIs ansprechen und Daten verarbeiten.
- Fehlerbehandlung und stabile Scripts.
- Datenverarbeitung mit KI-Unterstützung.

### Modul 4: Agentic Coding – KI als Entwicklungspartner

- KI-Tools im Coding-Workflow: Copilot, Chat, Commands, Agents.
- Prompt Engineering für Entwickler.
- Eigene Commands und Workflows bauen.
- Einfache Tool-Agents mit Python.

### Modul 5: Fortgeschrittene KI-Integration

- LLM-APIs direkt aus Python nutzen.
- Embeddings erzeugen und verstehen.
- Vektordatenbanken und Ähnlichkeitssuche.
- Einfache RAG-Systeme bauen (Code und No-Code-Optionen).

### Modul 6: Eigenes Projekt & Abschluss

- Projektidee planen und umsetzen.
- Streamlit-App bauen.
- Deployment-Grundlagen und -Optionen.
- Ethik, Datenschutz und verantwortungsvolle KI.

## 🤝 Beiträge

Wir freuen uns über Beiträge! Bitte lesen Sie unsere [Contributing Guidelines](CONTRIBUTING.md) und [Code of Conduct](CODE_OF_CONDUCT.md) bevor Sie einen Pull Request erstellen.

### Wie Sie beitragen können

- 🐛 Fehler melden über [Issues](https://github.com/talent-factory/ki-development/issues)
- 💡 Neue Features vorschlagen
- 📖 Dokumentation verbessern
- 🧪 Beispiele und Tutorials hinzufügen
- 🔧 Code-Verbesserungen einreichen

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für detaillierte Informationen.

## 📄 Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert. Sie dürfen den Code frei verwenden, modifizieren und verteilen.

## 🔒 Sicherheit

Sicherheit ist uns wichtig. Wenn Sie eine Sicherheitslücke entdecken, lesen Sie bitte unsere [Sicherheitsrichtlinie](SECURITY.md) für Informationen zur verantwortungsvollen Meldung.

## 📞 Kontakt

- **LinkedIn**: [Daniel Senften](https://www.linkedin.com/in/dsenften/)
- **GitHub Issues**: [Problem melden](https://github.com/talent-factory/ki-development/issues)
- **Kurs-Website**: [IBAW KI Professional](https://ibaw.ch/bildungsangebote/informatik/digital-collaboration-transformation/ki-professional-development/)

## 🙏 Danksagungen

Vielen Dank an alle [Contributors](https://github.com/talent-factory/ki-development/graphs/contributors), die zu diesem Projekt beigetragen haben!

---

**Hinweis**: Dieses Repository wird aktiv für Bildungszwecke verwendet. Fragen und Diskussionen sind willkommen!
