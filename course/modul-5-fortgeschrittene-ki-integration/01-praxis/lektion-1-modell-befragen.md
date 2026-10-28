# Lektion 1: Ein Sprachmodell aus Python befragen

**Dauer:** 50 Minuten (18:00–18:50)  
**Ziel:** Ein Sprachmodell aus Python ansprechen und seine Antwort als Pydantic-Modell zurückbekommen. Du siehst, dass es unsere Firma nicht kennt, und lernst, warum wir ihm Wissen mitgeben müssen.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Begrüssung, **Start-Check** (`check_setup.py`) | Kurzvortrag + Einzelarbeit |
| 5–15 | **Einstieg:** Frage zur Firma, die das Modell nicht kennt; Live-Coding `frage_llm` | Live-Coding |
| 15–40 | **Übung 1:** `frage_llm` mit strukturierter Antwort ([ex-01](../02-uebungen/ex-01-modell-befragen.adoc)) | Einzelarbeit |
| 40–45 | **Kür** (freiwillig) | Einzelarbeit |
| 45–50 | **Puffer** | |

---

## 1. Der Abend im Überblick

Wir bauen heute Schritt für Schritt ein kleines System, das Fragen zur **Wiki einer erfundenen Firma** (der Talwerk AG) beantwortet. Die Fakten sind frei erfunden. Also kann nur die Suche sie liefern, nicht das Modell.

| Lektion | Neu | Ergebnis |
| ------- | --- | -------- |
| 1 | Prompt, strukturierte Ausgabe | `frage_llm()` |
| 2 | Embedding, Ähnlichkeit | `aehnlichkeit()` |
| 3 | Vektorsuche, Top-k | `suche()` |
| 4 | RAG, Quellenangabe | `beantworte()` |

Am Ende jeder Lektion läuft dein Code. Wer den Anschluss verliert, steigt bei der Musterlösung der letzten Lektion (`05-beispiele/lektion-N/loesung/rag.py`) wieder ein. Der rote Faden für alles: **Fragen → Suchen → Antworten → Prüfen.**

---

## 2. Start-Check (2–3 Minuten)

```bash
uv run python course/modul-5-fortgeschrittene-ki-integration/05-beispiele/check_setup.py
```

Heb die Hand, wenn eine Zeile `FEHLER` zeigt. Wir lösen das **nicht im Plenum**: Arbeite mit deiner Sitznachbarin oder deinem Sitznachbarn, wir klären es in der Pause. Bei «rate limit» oder Netzausfall wartest du nicht: Setze `KONSERVE=1`, dann laufen die Beispiele des Kurses mit aufgezeichneten Antworten.

---

## 3. Einstieg: Das Modell kennt unsere Firma nicht (10 Minuten)

Kopiere `05-beispiele/lektion-1/start/` in deinen Projektordner. Dort liegen die Wiki (`wiki/`), `testfragen.json` und `hilfen.py`.

**KI-Moment:** Wir stellen dem Modell die Firmenfrage («Wann finden bei der Talwerk AG die Deployments statt?»):

```python
from pydantic_ai import Agent
from hilfen import MODELL

print(Agent(MODELL).run_sync("Wann finden bei der Talwerk AG die Deployments statt?").output)
```

Das Modell sagt ehrlich, dass es die Firma nicht kennt. Das ist gut, denn es erfindet nichts. Aber es heisst auch: **Antworten zur Firma muss die Wiki liefern.** Genau dafür bauen wir heute die Suche.

### Eine strukturierte Antwort

Statt freiem Text lassen wir das Modell ein Pydantic-Modell ausfüllen. Dann ist die Antwort ein Python-Objekt mit festen Feldern:

```python
class Antwort(BaseModel):
    text: str
    sicherheit: float  # 0 bis 1
```

`Agent(MODELL, output_type=Antwort)` liefert ein `Antwort`-Objekt. Die Anweisung (`instructions=`) trägt immer die Schlusszeile: *Antworte auf Deutsch, Schweizer Orthografie (ss statt ß).*

**Merksatz:** Ein Prompt hat Kontext, Aufgabe und Format. Das Format übernimmt hier das Pydantic-Modell.

---

## 4. Übung 1 (25 Minuten)

[ex-01-modell-befragen.adoc](../02-uebungen/ex-01-modell-befragen.adoc): `frage_llm(frage) -> Antwort`. Mindestziel: `uv run python pruefe.py 1` meldet «Mindestziel erreicht».

---

**Weiter:** [Lektion 2: Texte in Zahlen verwandeln](./lektion-2-embeddings.md)
