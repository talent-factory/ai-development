# Lektion 2: Texte in Zahlen verwandeln

**Dauer:** 50 Minuten (19:00–19:50)  
**Ziel:** Einen Text in einen Vektor verwandeln und die Ähnlichkeit zweier Texte messen. Du erkennst, was die Zahl aussagt und was nicht.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick:** Was lief, was hakt? | Gespräch |
| 5–15 | **Input:** Text → 3072 Zahlen, Ähnlichkeit mit `np.dot`; **KI-Moment** | Live-Coding |
| 15–40 | **Übung 2:** `embed()`, `aehnlichkeit()`, drei Satzpaare ([ex-02](../02-uebungen/ex-02-embeddings.adoc)) | Einzelarbeit |
| 40–45 | **Kür** (freiwillig) | Einzelarbeit |
| 45–50 | **Puffer** | |

---

## 1. Rückblick (5 Minuten)

Gleiches Muster in jeder Lektion: «Was lief, was hakt?» Kein Stoff, keine Aufgabe. Wer `pruefe.py 1` nicht grün hat, nimmt `lektion-1/loesung/rag.py` als Startstand.

---

## 2. Input: Embeddings (10 Minuten)

Du hast die Begriffe in der Vorbereitung gelesen. Jetzt sehen wir sie im Code:

```python
from hilfen import embed

vektoren = embed(["Deployments laufen donnerstags."])
print(vektoren.shape)  # (1, 3072)
```

Der Satz ist eine Liste von 3072 Zahlen. Die Vektoren haben die Länge 1. Deshalb ist die Ähnlichkeit zweier Texte einfach ihr **Skalarprodukt**:

```python
float(np.dot(vektor_a, vektor_b))  # 1.0 = gleiche Bedeutung
```

Die Datei `hilfen.py` nimmt dir die technischen Details ab (zum Beispiel das asynchrone Warten auf das Modell). Wir öffnen sie kurz und schauen hinein, erklären sie aber nicht.

### KI-Moment: Ähnlich ist nicht wahr

Wir vergleichen «Deployments sind erlaubt» und «Deployments sind verboten»: Ähnlichkeit etwa **0.93**. Zwei Sätze mit gegenteiliger Aussage sind für das Modell fast gleich, denn beide handeln von Deployments. Zwei unverwandte Sätze erreichen immer noch etwa 0.70. Die Werte liegen meist zwischen 0.6 und 0.9.

**Merksatz:** Ähnlichkeit misst das **Thema**, nicht die Wahrheit. Und wir lesen sie im Vergleich, nicht als absolute Zahl.

---

## 3. Übung 2 (25 Minuten)

[ex-02-embeddings.adoc](../02-uebungen/ex-02-embeddings.adoc): `aehnlichkeit(a, b) -> float` und drei Satzpaare vergleichen. Mindestziel: `uv run python pruefe.py 2` meldet «Mindestziel erreicht».

---

**Zurück:** [Lektion 1](./lektion-1-modell-befragen.md) · **Weiter:** [Lektion 3: Die passende Textstelle finden](./lektion-3-vektorsuche.md)
