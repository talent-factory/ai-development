# Konserve 4: Docstring gegen den Code prüfen

*Beispielausgabe, nicht live erzeugt (vom Dozenten konstruiert, damit der Moment sichtbar wird).* Im echten Probelauf mit Claude Code war die Doku inhaltlich richtig, siehe unten.

```python
def vergleiche_staedte(zeilen_a: list[dict], zeilen_b: list[dict]) -> dict:
    """Vergleicht zwei Städte.

    Returns:
        Dictionary mit ``stadt_a``, ``stadt_b``, ``tmax_differenz``,
        ``waermere_stadt`` und ``naessere_stadt``. Bei leeren Listen wird
        ``None`` zurückgegeben.
    """
```

**Prüfung gegen den Code:**

| Aussage | Stimmt? |
| ------- | ------- |
| Schlüssel `stadt_a`, `stadt_b`, `tmax_differenz`, `naessere_stadt` | ✅ |
| Schlüssel `waermere_stadt` | ❌ gibt es nicht, der Code liefert ihn nie |
| Bei leeren Listen wird `None` zurückgegeben | ❌ der Code wirft einen `ValueError` |
| Gleichstand beim Niederschlag | ⚠️ fehlt, `naessere_stadt` ist dann `None` |

**Lehre:** Der Docstring klingt plausibel und ist an zwei Stellen falsch. Wer ihm glaubt, ruft die Funktion falsch auf. Die Prompt-Zeile «Beschreibe nur, was der Code wirklich tut» hilft, ersetzt die Prüfung aber nicht.

---

## Was im echten Probelauf geschah (Claude Code 2.1.311, 2026-10-27)

Der Auftrag «Beschreibe nur, was der Code wirklich tut» ergab einen Docstring und ein `README.md`, die zum Code **passten**: Schlüssel, `ValueError` bei leerer Liste, Rundung der Differenz erst nach dem Abziehen, Gleichstand `None`. Trotzdem gab es drei Dinge zu prüfen:

| Auffälligkeit | Prüfung |
| ------------- | ------- |
| «Fehlende Felder lösen einen `KeyError` aus, nicht-numerische Werte einen `TypeError`.» Die KI schrieb dazu selbst: «Das habe ich nicht ausgeführt.» | Einzeiler in der Konsole: Stimmt es? (Ja.) |
| Das README-Beispiel zeigt `...` statt Zahlen. | Die KI hat die Funktion nicht ausgeführt. Setze die echten Werte selbst ein. |
| Der Docstring ist rund 25 Zeilen lang, die Funktion 15. | Kürzen auf das, was ein Aufrufer wissen muss. |

**Lehre:** Auch eine richtige Doku braucht die Prüfung, vor allem bei Aussagen, die die KI nicht ausgeführt hat.
