# Vorbereitung: Modul 5 – Fortgeschrittene KI-Integration

**Zeitaufwand:** ca. 60 Minuten, vor dem Unterricht (Modul 5: 4. November 2026, 18:00–21:50)  
**Ziel:** Alle Werkzeuge laufen und die wichtigsten Begriffe sind geklärt, bevor wir starten. Am Kurstag installieren wir nichts mehr, sondern bauen.

Plane die Vorbereitung **nicht erst für den Abend vorher** ein. Die Kontoeinrichtung kann Zeit brauchen, und bei Problemen sollst du noch Hilfe bekommen.

---

## Überblick

| Teil | Dauer | Inhalt |
| ---- | ----- | ------ |
| 1 | ca. 25 Min. | Pflicht-Setup: Projekt, Pydantic AI, Gemini-Schlüssel, Setup-Check |
| 2 | ca. 25 Min. | Begriffe: Embedding, Vektor, Ähnlichkeit, RAG |
| 3 | 5–10 Min. | Überblick: Was wir am Kurstag machen |

Wer das Setup nicht schafft, meldet sich **vor dem Kurstag** (nicht erst am Abend). Teil 1 ist Pflicht. Teil 2 nimmt dem Abend die Theorie ab, damit wir mehr Zeit zum Bauen haben.

---

## 1. Pflicht-Setup (ca. 25 Minuten)

Am Kurstag sprechen wir ein KI-Modell **aus Python** an, statt es im Terminal-Assistenten zu bedienen. Dafür verwenden wir **Pydantic AI** (ein Python-Paket) und einen kostenlosen **Gemini-Schlüssel** von Google. Der Schlüssel ist dein Zugang zum Modell, ähnlich einem Passwort.

Alle Befehle führst du im **Projektordner** aus. Du kannst den Ordner aus Modul 4 weiterverwenden oder einen neuen anlegen.

### Schritt 1: Voraussetzungen prüfen (3 Min.)

Du brauchst **Git** und **uv**. Beides hast du aus Modul 4. Prüfe es:

```bash
git --version
uv --version
```

Python 3.11 oder neuer wird von `uv` automatisch bereitgestellt.

### Schritt 2: Pakete installieren (3 Min.)

Wir verwenden eine **feste Version** von Pydantic AI, damit bei allen dasselbe Verhalten gilt:

```bash
uv add "pydantic-ai-slim[google]==2.63.0" numpy
```

> **Hinweis:** Installiere nicht mit `pip install pydantic-ai`. Das holt eine viel grössere Installation (mehrere hundert MB) mit anderen Versionen.

### Schritt 3: Gemini-Schlüssel anlegen (10 Min.)

1. Öffne [aistudio.google.com/apikey](https://aistudio.google.com/apikey) und melde dich mit einem **privaten Google-Konto** an. Ein Firmen- oder Schulkonto (Google Workspace) kann blockiert sein, nimm dann dein privates.
2. Akzeptiere die Nutzungsbedingungen.
3. Klicke auf **Create API key**. Google legt dafür automatisch ein Projekt an.
4. Kopiere den Schlüssel.

Du brauchst **keine Kreditkarte** und kein Zahlungskonto. Der kostenlose Zugang («Free Tier») reicht für den Abend.

> **Datenschutz:** Im kostenlosen Zugang darf Google deine Eingaben zur Verbesserung der Produkte verwenden. Gib deshalb **nie echte Firmen- oder Personendaten** ein. Am Kurstag arbeiten wir mit erfundenen Texten.

> **Sicherheit:** Ein Schlüssel ist wie ein Passwort. Schreibe ihn nie in eine Datei, die du committest, nie in einen Prompt und nie in einen Chat.

**Hast du schon einen Schlüssel von Anthropic oder OpenAI?** Du kannst ihn für die Chat-Aufrufe nutzen. Den Gemini-Schlüssel brauchst du trotzdem, denn die Embeddings (siehe Teil 2) rechnen wir mit Gemini. Wie du das Modell wechselst, zeigen wir am Kurstag.

### Schritt 4: Schlüssel als Umgebungsvariable setzen (3 Min.)

Wir legen den Schlüssel in der Variable `GOOGLE_API_KEY` ab. Pydantic AI liest sie selbst, du musst nichts in den Code schreiben.

| System | Befehl (ersetze `DEIN_SCHLÜSSEL`) |
| ------ | ---------------------------------- |
| macOS (zsh) | `echo 'export GOOGLE_API_KEY="DEIN_SCHLÜSSEL"' >> ~/.zshrc` |
| Linux (bash) | `echo 'export GOOGLE_API_KEY="DEIN_SCHLÜSSEL"' >> ~/.bashrc` |
| Windows (PowerShell) | `setx GOOGLE_API_KEY "DEIN_SCHLÜSSEL"` |

**Öffne danach ein neues Terminalfenster.** Das alte kennt die Variable noch nicht.

### Schritt 5: Setup-Check ausführen (3 Min.)

```bash
uv run python course/modul-5-fortgeschrittene-ki-integration/05-beispiele/check_setup.py
```

Erwartet (Beispiel):

```text
OK: Python 3.13
OK: uv uv 0.9.x
OK: git git version 2.52.0
OK: Git-Identität Dein Name
OK: pydantic-ai-slim 2.63.0
OK: numpy 2.x.x
OK: GOOGLE_API_KEY ist gesetzt
OK: Chat-Modell antwortet (Bern)
OK: Embedding-Modell antwortet (Vektor mit 3072 Zahlen)

Alles bereit für Modul 5.
```

Die Versionsnummern dürfen bei `uv`, `git` und `numpy` abweichen. Bei jeder Zeile mit `FEHLER` steht direkt dabei, was zu tun ist.

### Wenn es nicht klappt

| Problem | Lösung |
| ------- | ------ |
| `GOOGLE_API_KEY ist nicht gesetzt` | Terminal neu öffnen. Prüfe, ob der Befehl aus Schritt 4 ohne Fehler lief. |
| Der Chat- oder Embedding-Aufruf scheitert mit «rate limit» | Eine Minute warten und den Check wiederholen. |
| Der Aufruf scheitert mit «permission» oder «API key not valid» | Du verwendest vermutlich ein Workspace-Konto oder hast den Schlüssel falsch kopiert. Lege mit einem privaten Konto einen neuen an. |
| Falsche Version von `pydantic-ai-slim` | Schritt 2 mit der genauen Versionsnummer wiederholen. |
| Du bekommst keinen Schlüssel | Melde dich **vor dem Kurstag**. Mit vorbereiteten Antworten (Konserven) kannst du den Abend auch ohne Schlüssel mitmachen, aber nicht alles selbst ausprobieren. |
| Etwas anderes | Melde dich mit der Ausgabe von `check_setup.py` und deinem Betriebssystem. |

---

## 2. Begriffe (ca. 25 Minuten)

Am Kurstag bauen wir ein kleines System, das Fragen zu einer Wissensbasis beantwortet. Damit wir dort nicht mit Theorie beginnen, klären wir vier Begriffe jetzt. Lies den Abschnitt in Ruhe und beantworte danach die Kontrollfragen.

### Was ist ein Embedding?

Ein Computer kann Wörter nicht «verstehen», aber er kann **rechnen**. Ein **Embedding** übersetzt einen Text in eine Liste von Zahlen, zum Beispiel `[0.12, -0.53, 0.88, …]`, mit einigen hundert bis tausend Einträgen. Diese Liste nennen wir einen **Vektor**.

Das Besondere: Das Modell wählt die Zahlen so, dass Texte mit ähnlicher **Bedeutung** ähnliche Vektoren bekommen. «Wie deploye ich?» und «Ablauf einer Veröffentlichung» liegen nahe beieinander, obwohl sie kein gemeinsames Wort haben. «Wie deploye ich?» und «Kantinenmenü» liegen weit auseinander.

### Was ist Ähnlichkeit?

Wie nah zwei Vektoren beieinander liegen, messen wir mit einer Zahl, der **Kosinus-Ähnlichkeit**. Sie liegt meist zwischen 0 und 1: Nahe bei 1 heisst «sehr ähnliche Bedeutung», nahe bei 0 heisst «hat nichts miteinander zu tun». Du musst die Formel nicht auswendig kennen. Am Kurstag rechnen wir sie mit wenigen Zeilen NumPy.

### Was ist eine Suche mit Vektoren?

Wir wandeln alle Texte einer Sammlung einmal in Vektoren um und merken sie uns. Kommt eine Frage, wandeln wir auch sie in einen Vektor um und suchen die Texte mit der **höchsten Ähnlichkeit**. Das ist eine **Bedeutungssuche**: Sie findet auch Treffer, die andere Wörter benutzen als die Frage.

### Was ist RAG?

**RAG** heisst «Retrieval-Augmented Generation», auf Deutsch etwa «Antworten mit vorheriger Suche». Es besteht aus zwei Schritten:

1. **Suchen:** Wir finden die passenden Textstellen zur Frage (mit der Vektorsuche).
2. **Antworten:** Wir geben diese Stellen zusammen mit der Frage an das Sprachmodell und bitten es, **nur** daraus zu antworten und die Quelle zu nennen.

So beantwortet das Modell auch Fragen zu Wissen, das es nie gesehen hat, zum Beispiel zu den internen Regeln einer Firma. Wichtig: Das Modell kann sich trotzdem irren. Deshalb prüfen wir am Kurstag jede Antwort gegen die Quelle.

### Kontrollfragen

Beantworte sie für dich, die Lösungen stehen darunter.

1. Was ist ein Vektor im Zusammenhang mit einem Embedding?
2. Warum findet eine Bedeutungssuche auch Texte, die nicht dieselben Wörter wie die Frage enthalten?
3. Aus welchen zwei Schritten besteht RAG, und was gibst du dem Modell im zweiten Schritt mit?

<details>
<summary>Lösungen</summary>

1. Eine Liste von Zahlen, die die Bedeutung eines Textes beschreibt.
2. Weil Texte mit ähnlicher Bedeutung ähnliche Vektoren haben. Verglichen werden die Vektoren, nicht die Wörter.
3. Suchen und Antworten. Im zweiten Schritt gibst du dem Modell die Frage und die gefundenen Textstellen mit, und die Anweisung, nur daraus zu antworten.

</details>

### Kurze Erinnerung an Modul 4

In Modul 4 hast du gesehen, dass eine KI nicht nur Text schreibt, sondern Werkzeuge benutzen kann (Dateien lesen, Befehle ausführen). Am Ende des Abends zeigen wir, dass eine **Suche** auch so ein Werkzeug sein kann, das ein Modell selbst aufruft. Das ist nur ein Ausblick, du musst dafür nichts vorbereiten.

---

## 3. Überblick: Was wir am Kurstag machen

Wir arbeiten den ganzen Abend an **einem Projekt**: einer kleinen Frage-Antwort-Anwendung über die erfundene **Entwickler-Wiki einer Firma** (Deployment-Ablauf, Review-Regeln, Bereitschaftsdienst). Alle Fakten sind frei erfunden, also kann nur die Suche sie liefern.

| Lektion | Zeit | Ergebnis |
| ------- | ---- | -------- |
| 1 | 18:00–18:50 | Ein Sprachmodell aus Python befragen, mit strukturierter Antwort |
| 2 | 19:00–19:50 | Texte in Vektoren verwandeln und Ähnlichkeit messen |
| 3 | 20:00–20:50 | Eine eigene Vektorsuche mit NumPy bauen |
| 4 | 21:00–21:50 | Alles zu einem Mini-RAG verbinden, mit Quellenangabe |

Jede Lektion endet mit einem lauffähigen Stand. Wer den Anschluss verliert, steigt bei der Musterlösung der letzten Lektion wieder ein.

Du brauchst am Kurstag: Laptop mit Projektordner, bestandenen Setup-Check (Teil 1), Internetzugang und einen geladenen Akku.

---

**Zurück zum Modul:** [Modul 5: Fortgeschrittene KI-Integration](../README.md)
