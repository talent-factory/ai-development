# Lektion 3: Arbeitsumgebung einrichten

**Dauer:** 50 Minuten  
**Ziel:** VS Code, Python, uv und OpenCode gemeinsam installieren und startklar machen.

---

## 🎯 Lernziele

Nach dieser Lektion können die Teilnehmenden:

- VS Code, Python, uv und OpenCode installieren und starten.
- Den Terminal in VS Code öffnen und grundlegende Befehle ausführen.
- Die Versionen der installierten Tools prüfen.
- Verstehen, warum eine reproduzierbare Umgebung wichtig ist.

---

## ⏱️ Zeitplan

| Zeit      | Phase             | Inhalt                                      |
| --------- | ----------------- | ------------------------------------------- |
| 0–5 min   | Einstieg          | Warum Setup wichtig ist; Reproduzierbarkeit |
| 5–35 min  | Gemeinsames Setup | Schritt für Schritt alle Tools installieren |
| 35–45 min | Check             | Versionen prüfen, erste Befehle ausführen   |
| 45–50 min | Puffer & Hilfe    | Individuelle Probleme lösen                 |

---

## 🛠️ Setup-Checkliste

Die Teilnehmenden arbeiten die folgende Checkliste Schritt für Schritt ab.

### 1. VS Code

- Download: <https://code.visualstudio.com/>
- Installieren und öffnen.
- Terminal öffnen: `View → Terminal` (oder `` Ctrl + ` `` / `` Cmd + ` ``).

### 2. Python

```bash
# Version prüfen
python --version
# oder auf macOS/Linux
python3 --version
```

**Ziel:** Python 3.12 oder 3.13.

Falls Python fehlt: <https://www.python.org/downloads/>

### 3. uv

```bash
# Installation
pip install uv

# oder auf macOS mit Homebrew
brew install astral-sh/tap/uv

# Version prüfen
uv --version
```

**Hintergrund aus `01-praxis/uv.adoc`:**

- `uv` ist ein modernes, schnelles Python-Paketmanagement-Tool.
- Es ersetzt `pip`, `poetry` und `pip-tools` in vielen Fällen.
- Wichtige Befehle: `uv sync`, `uv add`, `uv run`.

### 4. OpenCode

```bash
# Installation
npm install -g opencode

# Version prüfen
opencode --version
```

**Ziel:** OpenCode startet im Terminal.

### 5. Git (optional für heute, wird später gebraucht)

```bash
git --version
```

---

## ✅ Abschluss-Check

Jede/r führt folgende Befehle im Terminal aus und dokumentiert die Ausgabe:

```bash
python --version
uv --version
opencode --version
git --version
```

**Wenn alle Befehle eine Versionsnummer zurückgeben, ist das Setup erfolgreich.**

---

## 📋 Hilfestellung bei Problemen

| Problem                   | Mögliche Lösung                                        |
| ------------------------- | ------------------------------------------------------ |
| `python` nicht gefunden   | `python3` statt `python` probieren                     |
| `uv` nicht gefunden       | Terminal neu starten oder `pip install uv` wiederholen |
| `opencode` nicht gefunden | Node.js installieren: <https://nodejs.org/>            |
| Berechtigungsfehler       | Admin-Rechte oder `sudo` (macOS/Linux) prüfen          |

> Detaillierte Anleitungen befinden sich in `02-uebungen/cli-installation.md` und `00-vorbereitung/backup-environments-quickstart.adoc`.

---

## 📚 Materialien

- `01-praxis/uv.adoc`
- `01-praxis/lesson-01-cli-setup.md`
- `02-uebungen/cli-installation.md`
- `00-vorbereitung/backup-environments-quickstart.adoc`

---

## 🏠 Hausaufgabe (Nachbereitung)

- Persönliches Setup in 3–5 Sätzen dokumentieren.
- Notiere, welches Tool am schwierigsten zu installieren war und warum.
