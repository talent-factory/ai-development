# Plan: Städtevergleich `vergleiche_staedte`

## Ziel

`wetter_bericht.py` soll zwei Städte vergleichen können: Um wie viel Grad ist die eine im Schnitt wärmer, und welche war nässer?

## Signatur

```python
def vergleiche_staedte(zeilen_a: list[dict], zeilen_b: list[dict]) -> dict:
```

Die Zeilen kommen aus `lese_stadt(...)`. Die Funktion ist rein: keine Datei, kein Live-Abruf, kein `print`.

## Rückgabe

Ein Dictionary mit genau diesen Schlüsseln:

| Schlüssel | Bedeutung |
| --- | --- |
| `stadt_a` | Name der Stadt aus `zeilen_a` |
| `stadt_b` | Name der Stadt aus `zeilen_b` |
| `tmax_differenz` | Ø `tmax` von A minus Ø `tmax` von B, auf eine Dezimale gerundet (positiv: A ist wärmer) |
| `naessere_stadt` | Name der Stadt mit dem grösseren Gesamtniederschlag, bei Gleichstand `None` |

## Definition «nässer»

Nässer ist die Stadt mit dem grösseren **Gesamtniederschlag in mm** über alle Zeilen. Die Zahl der Regentage entscheidet nicht.

## Randfälle

- Leere Liste für eine der beiden Städte: `ValueError` (wie `berechne_kennzahlen`).
- Gleicher Gesamtniederschlag: `naessere_stadt` ist `None`.

## Nicht Teil des Features

- Kein Live-Wetter, keine Ausgabe auf dem Bildschirm, kein JSON-Bericht.
- Keine Änderung an den bestehenden Funktionen.
- Kein Vergleich von mehr als zwei Städten.
