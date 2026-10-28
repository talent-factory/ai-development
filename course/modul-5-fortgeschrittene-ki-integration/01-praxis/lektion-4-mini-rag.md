# Lektion 4: Suche und Modell verbinden

**Dauer:** 50 Minuten (21:00–21:50)  
**Ziel:** Aus Suche und Sprachmodell ein Mini-RAG bauen, das mit Quelle antwortet, und seine Antworten gegen die Quelle prüfen.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–3 | **Rückblick** | Gespräch |
| 3–10 | **Input:** der RAG-Prompt | Live-Coding |
| 10–25 | **Übung 4:** `beantworte(frage)` ([ex-04](../02-uebungen/ex-04-mini-rag.adoc)) | Einzelarbeit |
| 25–30 | **Fallen-Frage** und Quellencheck, **KI-Moment** | Einzelarbeit + Gespräch |
| 30–40 | **Ausblick:** Tool-Use-Demo (5 Min), No-Code-Demo (5 Min) | Demo |
| 40–48 | **Feedback** | Gespräch |
| 48–50 | **Puffer** | |

---

## 1. Der RAG-Prompt (7 Minuten)

RAG besteht aus zwei Schritten: **Suchen** (`suche`) und **Antworten** (das Modell bekommt die Treffer mit). Der Prompt trägt drei Teile:

```text
<Regel>

Quellen:
[02-freeze.md]
<Text>
...

Frage: <die Frage>
```

Die Regel steht fertig in `hilfen.py` (`RAG_REGEL`): nur aus den Quellen antworten, den Dateinamen nennen, sonst «Ich finde dazu nichts.»

Gibt `beantworte(frage)` seine Antwort als `Antwort` mit den Feldern `text`, `sicherheit` und `quelle` zurück, kannst du sie direkt später in einer Oberfläche anzeigen. Das nutzen wir in Modul 6.

---

## 2. Übung 4 (15 Minuten)

[ex-04-mini-rag.adoc](../02-uebungen/ex-04-mini-rag.adoc): `beantworte(frage, mit_regel=True) -> Antwort`. Mindestziel: `uv run python pruefe.py 4`.

---

## 3. Antworten prüfen (5 Minuten)

### KI-Moment: Die Antwort prüfen

Die Fallen-Frage («Wie viele Ferientage habe ich pro Jahr?») steht nirgends in der Wiki. Mit Regel antwortet das Modell «Ich finde dazu nichts.» Die Regel hat gewirkt.

Aber: Bei **«Wen rufe ich in der Nacht bei einem Ausfall an?»** sagt das Modell mit Regel ebenfalls «Ich finde dazu nichts», obwohl `04-bereitschaft.md` unter den Treffern liegt. Die Regel macht es hier zu streng. Und bei mehreren Antworten ist das Feld `quelle` leer, obwohl die Quelle im Text steht.

Das ist der **3-Punkte-Quellencheck**:

1. Steht die Aussage im Treffertext?
2. Stimmt die genannte Quelle?
3. Wurde etwas hinzugefügt, das nirgends steht?

**Merksatz:** RAG macht das Modell nicht unfehlbar. Es macht seine Antwort *prüfbar*, weil die Quelle dabei steht.

---

## 4. Ausblick (10 Minuten)

* **Tool Use (5 Min):** Statt dass wir die Suche vor dem Modell aufrufen, kann das Modell sie als *Werkzeug* selbst aufrufen («Suche in der Wiki»). Die Dozentin / der Dozent zeigt die Demo `05-beispiele/lektion-4/demo_tool_use.py` (Pydantic AI): Das Modell wählt selbst Suchbegriffe und sucht bei Bedarf noch einmal. Das ist ein Ausblick, nicht Stoff.
* **No-Code (5 Min):** Dasselbe Mini-RAG als Flow in Flowise oder Langflow. Die Dozentin / der Dozent zeigt die Demo; ihr installiert nichts.

---

## 5. Feedback (8 Minuten)

* Blitzrunde: «Ein Ding ist mir klar, eines ist unklar.»
* Handzeichen: War die Informationsmenge heute *zu viel, genau richtig oder zu wenig*?

Danach kündigen wir die **Nachbearbeitung** an: ein Mini-RAG über eure eigenen Texte. Daraus entsteht die Idee für das Abschlussprojekt in Modul 6.

---

**Zurück:** [Lektion 3](./lektion-3-vektorsuche.md) · **Zurück zum Modul:** [Modul 5](../README.md)
