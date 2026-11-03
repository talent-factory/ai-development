# Plan: Städtevergleich `vergleiche_staedte`

## Ziel

`wetter_bericht.py` soll zwei Städte vergleichen können: Um wie viel Grad ist die eine im Schnitt wärmer, und welche war nässer?

## Signatur

```python
def vergleiche_staedte(zeilen_a: list[dict], zeilen_b: list[dict]) -> dict:
```

Die Zeilen kommen aus `lese_stadt(...)`. Die Funktion ist rein: keine Datei, kein Netzwerk, kein `print`.

## Rückgabe

Ein Dictionary mit genau diesen vier Schlüsseln:

| Schlüssel | Bedeutung |
| --- | --- |
| `stadt_a` | Name der Stadt aus `zeilen_a` (aus `zeilen_a[0]["stadt"]`) |
| `stadt_b` | Name der Stadt aus `zeilen_b` (aus `zeilen_b[0]["stadt"]`) |
| `tmax_differenz` | `tmax_durchschnitt` von A minus `tmax_durchschnitt` von B, eine Dezimale (positiv: A ist wärmer) |
| `naessere_stadt` | Name der Stadt mit dem grösseren `niederschlag_gesamt_mm`, bei Gleichstand `None` |

Es gibt keinen Schlüssel `waermere_stadt`: Das Vorzeichen von `tmax_differenz` sagt es schon.

## Berechnung

- Verglichen wird nur die Temperatur `tmax` (Durchschnitt), nicht `tmin`.
- `berechne_kennzahlen` wird für beide Städte wiederverwendet. Die Formeln für Durchschnitt und Gesamtniederschlag stehen nur dort.
- Folge: Die Differenz entsteht aus bereits auf 0.1 gerundeten Durchschnitten. Sie kann deshalb um 0.1 von der Differenz der ungerundeten Durchschnitte abweichen. Das ist bewusst so entschieden: Die Werte im Vergleich stimmen mit denen im Bericht überein.
- Der Gleichstand wird auf den gerundeten Gesamtniederschlägen (0.1 mm) geprüft.

## Definition «nässer»

Nässer ist die Stadt mit dem grösseren **Gesamtniederschlag in mm** über alle Zeilen. Die Zahl der Regentage entscheidet nicht.

## Randfälle

- Leere Liste für eine der beiden Städte: `ValueError("Keine Wetterdaten vorhanden.")`. Die Prüfung steht in `vergleiche_staedte` selbst: `berechne_kennzahlen` würde bei einer leeren Liste nur `max() iterable argument is empty` werfen.
- Gleicher (gerundeter) Gesamtniederschlag: `naessere_stadt` ist `None`.
- Bewusst nicht geprüft: unterschiedlich viele Tage, abweichende Datumsbereiche, dieselbe Stadt in beiden Listen.

## Beispiel (aus `wetter_30tage.csv` nachgerechnet)

| Stadt | Tage | Ø `tmax` | Gesamtniederschlag |
| --- | --- | --- | --- |
| Zürich | 30 | 20.7 °C | 36.3 mm |
| Lugano | 30 | 21.8 °C | 35.2 mm |

`vergleiche_staedte(zürich, lugano)` gibt `tmax_differenz = -1.1` und `naessere_stadt = "Zürich"` zurück.

Zum Vergleich: Die Differenz der ungerundeten Durchschnitte (20.69 und 21.8467) ist -1.1567, gerundet -1.2. Das ist die oben festgehaltene Abweichung durch das Wiederverwenden von `berechne_kennzahlen`.

## Nicht Teil des Features

- Keine Anbindung an `main`, keine Bildschirmausgabe, kein JSON-Bericht, kein Live-Wetter.
- Keine Änderung an den bestehenden Funktionen.
- Kein Vergleich von mehr als zwei Städten.

## Tests (Lektion 2, test-first)

In `test_wetter_bericht.py`, mit kleinen von Hand gebauten Zeilenlisten (je 2 bis 3 Tage), erwartete Werte selbst nachgerechnet:

- A wärmer als B (positive Differenz)
- A kälter als B (negative Differenz)
- A nässer
- B nässer
- mehr Gesamtniederschlag schlägt mehr Regentage (A: 1 Regentag, 10 mm; B: 3 Regentage, 4 mm)
- Gleichstand: `naessere_stadt` ist `None`
- Gleichstand auf gerundeten Werten (5.04 mm gegen 5.0 mm)
- leere Liste A: `ValueError`
- leere Liste B: `ValueError`
- Rundung auf eine Dezimale

## Zusätzliche Tests und Coverage

Für die Vorgabe «mindestens 90 % Abdeckung» (Zweigabdeckung) enthält `test_wetter_bericht.py` auch Tests für die Bestandsfunktionen und `main`. Dafür kommen `pytest-cov` und die Coverage-Konfiguration (`fail_under = 90`, `branch = true`) in `pyproject.toml`. Die Schwelle gilt repo-weit, gemessen wird mit `uv run pytest <pfad> --cov=<pfad>`.
