# Vorbereitung: Modul 4 – Agentic Coding: KI als Entwicklungspartner

**Zeitaufwand:** ca. 60–75 Minuten, vor dem Unterricht (Modul 4: 27. Oktober 2026, 18:00–21:50)  
**Ziel:** Alle Werkzeuge laufen, bevor wir starten. Am Kurstag installieren wir nichts mehr, sondern arbeiten mit der KI.

Plane die Vorbereitung **nicht erst für den Abend vorher** ein. Die Installation kann Zeit brauchen, und bei Problemen sollst du noch Hilfe bekommen.

---

## Überblick

| Teil | Dauer | Inhalt |
| ---- | ----- | ------ |
| 1 | ca. 45 Min. | Pflicht-Setup: OpenCode oder Claude Code, Modell-Zugang, Skills, Setup-Check |
| 2 | ca. 20 Min. | Wiederholung: Funktionen, `pytest`, Git |
| 3 | 5 Min. | Überblick: Was wir am Kurstag machen |

Wer das Setup nicht schafft, meldet sich **vor dem Kurstag** (nicht erst am Abend). Teil 1 ist Pflicht, Teil 2 hilft beim Einstieg, ist aber ohne Folgen, wenn du ihn nur überfliegst.

---

## 1. Pflicht-Setup (ca. 45 Minuten)

Wir arbeiten mit einem **KI-Coding-Assistenten im Terminal**. Er liest deine Dateien, schlägt Änderungen vor und führt (mit deiner Erlaubnis) Befehle aus. Du kannst **OpenCode** oder **Claude Code** verwenden. Beide sind im Kurs gleichberechtigt, die Übungen funktionieren mit beiden:

- **Hast du ein Claude-Abo** (Pro/Max) oder einen Anthropic-API-Key? Nimm **Claude Code**.
- **Hast du keinen bezahlten Zugang?** Nimm **OpenCode**, das auch mit kostenlosen Modellen läuft.

Richte **eines** der beiden ein. Wer mag, kann beide installieren. In den Schritten 3 bis 5 steht jeweils ein Abschnitt pro Werkzeug, du folgst nur deinem.

Alle Befehle führst du im **Projektordner** aus, in dem auch dein Modul-3-Code liegt.

### Schritt 1: Voraussetzungen prüfen (5 Min.)

Du brauchst **Git**, **Node.js** (LTS-Version) und **uv**. Prüfe sie so:

```bash
git --version
node --version
uv --version
```

Fehlt etwas, installiere es von der jeweiligen Seite: [git-scm.com](https://git-scm.com/downloads), [nodejs.org](https://nodejs.org), [docs.astral.sh/uv](https://docs.astral.sh/uv/). Starte danach das Terminal neu.

Git muss deinen Namen kennen, sonst scheitern Commits:

```bash
git config --global user.name "Dein Name"
git config --global user.email "du@example.com"
```

### Schritt 2: `pytest` installieren (2 Min.)

```bash
uv add --dev pytest
```

### Schritt 3: Werkzeug installieren (5–10 Min.)

**Option A: OpenCode**

| System | Befehl |
| ------ | ------ |
| macOS / Linux | `curl -fsSL https://opencode.ai/install \| bash` |
| Windows, macOS, Linux (mit Node.js) | `npm install -g opencode-ai` |

Prüfen (nach einem Neustart des Terminals): `opencode --version`

**Option B: Claude Code**

| System | Befehl |
| ------ | ------ |
| macOS / Linux | `curl -fsSL https://claude.ai/install.sh \| bash` |
| Windows (PowerShell) | `irm https://claude.ai/install.ps1 \| iex` |
| Mit Node.js (alle Systeme) | `npm install -g @anthropic-ai/claude-code` |

Prüfen (nach einem Neustart des Terminals): `claude --version`

Gibt es `command not found` (macOS/Linux) oder «wird nicht erkannt» (Windows), ist der Installationsordner nicht im `PATH`. Schliesse alle Terminalfenster und öffne ein neues. Hilft das nicht, nimm den `npm`-Weg.

### Schritt 4: Modell-Zugang einrichten (10 Min.)

Das Werkzeug braucht ein KI-Modell, das die Arbeit macht.

**Option A: OpenCode**

Du hast zwei Möglichkeiten:

- **Kostenlos, ohne Konto:** OpenCode bringt Gratis-Modelle mit (im Namen steht `-free`). Du musst nichts einrichten. Wir verwenden am Kurstag `opencode/glm-5.3-flash-free`. Wähle es in OpenCode mit `/models` oder starte direkt damit: `opencode -m opencode/glm-5.3-flash-free`.
- **Eigener Zugang:** Hast du einen API-Key von Anthropic, OpenAI oder Google, richtest du ihn ein mit `opencode auth login`. Das ist optional, kann aber schnellere und stärkere Modelle bringen.

Prüfen: Der Probelauf in Schritt 7 antwortet. (`opencode auth list` zeigt nur eigene Zugänge, bei den Gratis-Modellen bleibt die Liste leer.)

**Option B: Claude Code**

Starte `claude` im Projektordner. Beim ersten Start meldest du dich an (Claude-Abo oder Anthropic Console). Später geht das auch mit `/login`.

Prüfen: `claude auth status` zeigt `"loggedIn": true`.

> **Wichtig:** Kostenlose Modelle und Abos haben Nutzungslimits. Meldet die KI am Kurstag «rate limit», ist das normal. Wir planen Wartezeiten ein.

> **Sicherheit:** Ein API-Key ist wie ein Passwort. Schreibe ihn nie in eine Datei, die du committest, und nie in einen Prompt.

### Schritt 5: Skills installieren (5 Min.)

Skills sind kleine Anleitungen, die der KI eine Arbeitsweise beibringen, zum Beispiel «erst Fragen stellen, dann planen» oder «erst den Test schreiben». Wir nutzen die Skills von Matt Pocock (`mattpocock/skills`). Sie sind englisch geschrieben. Das ist gewollt: Wir geben der KI auf Deutsch die Anweisung, wie sie antworten soll.

**Option A: OpenCode** (im Projektordner)

```bash
npx skills@latest add mattpocock/skills -a opencode -s grilling -s tdd -s code-review -s diagnosing-bugs -s domain-modeling --copy -y
```

Die Skills landen im Ordner `.agents/skills/` in deinem Projekt.

**Option B: Claude Code**

```bash
claude plugin install mattpocock-skills@claude-plugins-official
```

Die Skills sind danach mit dem Präfix `mattpocock-skills:` verfügbar (zum Beispiel `/mattpocock-skills:tdd`).

Installiere nicht beide Wege für dasselbe Werkzeug, sonst erscheint jeder Skill doppelt.

### Schritt 6: Setup-Check ausführen (3 Min.)

```bash
uv run python course/modul-4-agentic-coding/05-beispiele/check_setup.py
```

Erwartet (Beispiel mit OpenCode):

```text
OK: Python 3.13
OK: pytest 9.1.1
OK: git git version 2.52.0
OK: Git-Identität Dein Name
OK: node v24.15.0
OK: opencode opencode v2.0.24
OK: OpenCode-Skills grilling, tdd, diagnosing-bugs, domain-modeling
OK: OpenCode hat einen Modell-Zugang

Alles bereit für Modul 4.
```

Mit Claude Code stehen stattdessen `OK: claude …`, `OK: Claude-Code-Plugin mattpocock-skills` und `OK: Claude Code ist angemeldet` da. Hast du beide Werkzeuge installiert, genügt es, wenn eines vollständig bereit ist. Eine `FEHLER`-Zeile zum anderen darfst du dann ignorieren.

Die Versionsnummern dürfen abweichen. Bei jeder Zeile mit `FEHLER` steht direkt dabei, was zu tun ist. Starte das Skript im Projektordner, sonst findet es die Skills nicht.

### Schritt 7: Probelauf mit der KI (5 Min.)

Starte dein Werkzeug im Projektordner: `claude` oder, für OpenCode ohne eigenen Zugang, `opencode -m opencode/glm-5.3-flash-free`.

Gib diesen Prompt ein:

```text
Erkläre in drei Sätzen, was diese Projektstruktur enthält. Antworte auf Deutsch und schreibe «ss» statt «ß».
```

Kommt eine sinnvolle Antwort, ist alles bereit. Beenden kannst du mit `/exit` (OpenCode auch mit `Ctrl+C`).

> **Hinweis:** Beide Werkzeuge fragen, bevor sie Dateien ändert oder Befehle ausführt. Lies jede Anfrage und bestätige nur, was du verstehst. Das ist Teil des Kurses: **Vertrauen, aber prüfen.**

### Wenn es nicht klappt

| Problem | Lösung |
| ------- | ------ |
| `npx` oder `npm` läuft nicht | Node.js fehlt oder wurde nach der Installation nicht neu geladen. Terminal neu starten, `node --version` prüfen. |
| `opencode` oder `claude` wird nicht gefunden | Terminal neu starten. Sonst mit `npm install -g opencode-ai` bzw. `npm install -g @anthropic-ai/claude-code` installieren. |
| Der Check meldet fehlende Skills | OpenCode: Du bist nicht im Projektordner, führe Schritt 5 dort aus. Claude Code: Plugin-Installation wiederholen. |
| Die KI antwortet nicht oder meldet «rate limit» | Eine Minute warten und es erneut versuchen. Bleibt es dabei, melde dich mit dem Wortlaut der Fehlermeldung. |
| Etwas anderes | Melde dich **vor dem Kurstag** mit der Ausgabe von `check_setup.py` und deinem Betriebssystem. |

---

## 2. Wiederholung (ca. 20 Minuten)

Am Kurstag arbeiten wir an deinem Wetterbericht aus Modul 3 (`wetter_bericht.py`). Dafür brauchst du drei Dinge aus früheren Modulen.

### Funktionen mit Typ-Hinweisen und Docstring

```python
def durchschnitt(werte: list[float]) -> float:
    """Gibt den Durchschnitt einer nicht leeren Liste zurück."""
    return sum(werte) / len(werte)
```

Eine gute Funktion tut **eine** Sache, hat einen klaren Namen und lässt sich einzeln prüfen. Genau das macht sie auch für die KI gut verständlich.

### Tests mit `pytest`

Ein Test ist eine Funktion, deren Name mit `test_` beginnt und die mit `assert` etwas behauptet:

```python
# test_beispiel.py
from beispiel import durchschnitt


def test_durchschnitt_einfach():
    assert durchschnitt([10.0, 20.0]) == 15.0
```

Ausführen im Projektordner:

```bash
uv run pytest
```

Ein bestandener Test zeigt `1 passed`. Ein fehlgeschlagener zeigt, welche Behauptung nicht stimmt. Am Kurstag schreiben wir die Tests **zuerst** und lassen danach die KI den Code liefern.

### Git: Änderungen festhalten

```bash
git status                      # was hat sich geändert?
git add datei.py                # Änderung vormerken
git commit -m "Beschreibung"    # festhalten
git diff                        # Änderungen vor dem Commit ansehen
git restore datei.py            # Änderungen an einer Datei verwerfen
```

Wenn die KI Dateien ändert, ist Git dein Sicherheitsnetz: Mit `git diff` siehst du genau, was sie getan hat, und mit `git restore` machst du es rückgängig.

### Selbsttest

1. Schreibe eine Funktion `ist_regentag(niederschlag_mm: float) -> bool`, die `True` zurückgibt, wenn mehr als 0 mm gefallen sind.
2. Schreibe zwei Tests dafür: einen für `0.0` und einen für `2.5`.
3. Führe die Tests mit `uv run pytest` aus.
4. Committe beides mit einer sinnvollen Nachricht.

<details>
<summary>Lösung</summary>

```python
# regen.py
def ist_regentag(niederschlag_mm: float) -> bool:
    """Gibt True zurück, wenn mehr als 0 mm Niederschlag gefallen sind."""
    return niederschlag_mm > 0
```

```python
# test_regen.py
from regen import ist_regentag


def test_trockener_tag():
    assert ist_regentag(0.0) is False


def test_regentag():
    assert ist_regentag(2.5) is True
```

```bash
uv run pytest
git add regen.py test_regen.py
git commit -m "Regentag-Funktion mit Tests"
```

</details>

### Dein Wetterbericht

Halte `wetter_bericht.py` aus der Nachbearbeitung von Modul 3 bereit und stelle sicher, dass er läuft. Hast du ihn nicht fertig, ist das kein Problem. Sag uns vorher Bescheid, dann bekommst du am Kurstag einen lauffähigen Startpunkt.

---

## 3. Überblick: Was wir am Kurstag machen

Wir arbeiten den ganzen Abend an **einem Projekt**: deinem Wetterbericht. Du lernst, wie man mit einer KI zusammenarbeitet, ohne ihr blind zu vertrauen.

| Lektion | Zeit | Thema |
| ------- | ---- | ----- |
| 1 | 18:00–18:50 | Arbeitsweise, Prompting und Planen |
| 2 | 19:00–19:50 | Tests zuerst (TDD) mit der KI |
| 3 | 20:00–20:50 | Review, Refactoring und Fehlersuche |
| 4 | 21:00–21:50 | Dokumentation und ein kompletter Durchlauf |

Der rote Faden: **Plan → Test → Code → Review → Doku.** Die KI schreibt vieles davon, aber **du** entscheidest, was übernommen wird.

Du brauchst am Kurstag: Laptop mit Projektordner, funktionierendes OpenCode oder Claude Code, Internetzugang und einen geladenen Akku.

---

**Zurück zum Modul:** [Modul 4: Agentic Coding – KI als Entwicklungspartner](../README.md)
