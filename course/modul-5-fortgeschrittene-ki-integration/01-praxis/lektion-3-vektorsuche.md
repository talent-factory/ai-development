# Lektion 3: Die passende Textstelle finden

**Dauer:** 50 Minuten (20:00–20:50)  
**Ziel:** Mit NumPy die ähnlichsten Texte zu einer Frage finden (Top-k) und die Treffer prüfen, statt sie blind zu übernehmen.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick** | Gespräch |
| 5–15 | **Input:** Top-k mit NumPy | Live-Coding |
| 15–35 | **Übung 3, Teil 1:** `suche(frage, k=3)` ([ex-03](../02-uebungen/ex-03-vektorsuche.adoc)) | Einzelarbeit |
| 35–45 | **Prüf-Handgriff:** Treffer lesen, **KI-Moment** (falscher Top-1) | Einzelarbeit + Gespräch |
| 45–50 | **Puffer** | |

---

## 1. Input: Top-k mit NumPy (10 Minuten)

Eine Suche ist nichts anderes als: Frage in einen Vektor verwandeln und mit allen Textvektoren vergleichen.

```python
werte = vektoren @ frage_vektor          # Ähnlichkeit zu allen Texten auf einmal
beste = np.argsort(-werte)[:3]           # die drei besten
```

* `embed(..., ist_frage=True)` sagt dem Modell, dass es um eine Suchfrage geht.
* Die Vektoren der Wiki berechnen wir **einmal** und merken sie uns (`functools.cache`).
* *Top-k* heisst: die `k` besten Treffer, nicht nur den besten.

---

## 2. Der Prüf-Handgriff (10 Minuten)

Ab jetzt gilt bei jeder Suche: **den Treffertext lesen**, nicht nur den Dateinamen. Das ist der Anfang des 3-Punkte-Quellenchecks, den wir in Lektion 4 vollständig anwenden.

### KI-Moment: Der falsche Top-1

Bei der Frage **«Wen rufe ich in der Nacht bei einem Ausfall an?»** liegt `06-incident.md` (0.68) knapp vor `04-bereitschaft.md` (0.67). Der erste Treffer ist nicht die beste Quelle. Der richtige Text ist aber unter den Top-3, deshalb nehmen wir mehrere Treffer.

Bei **«Wann darf ich veröffentlichen?»** liegt der Freeze (0.67) vor dem Deployment (0.65). Welcher Text beantwortet die Frage besser? Die Suche kann das nicht entscheiden, du schon.

**Merksatz:** Die Suche findet *ähnliche* Texte, nicht *die richtige Antwort*. Treffer prüfen, nicht blind übernehmen.

---

## 3. Übung 3 (20 Minuten)

[ex-03-vektorsuche.adoc](../02-uebungen/ex-03-vektorsuche.adoc): `suche(frage, k=3)`. Mindestziel: `uv run python pruefe.py 3`. Die fünf Testfragen müssen ihren Text unter den besten drei haben.

---

**Zurück:** [Lektion 2](./lektion-2-embeddings.md) · **Weiter:** [Lektion 4: Suche und Modell verbinden](./lektion-4-mini-rag.md)
