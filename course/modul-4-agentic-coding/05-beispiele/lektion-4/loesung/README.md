# Wetterbericht

Kleines Python-Programm: wertet 30 Tage Wetterdaten (CSV) von fünf Schweizer Städten aus, holt das aktuelle Wetter bei Open-Meteo und speichert einen Bericht als JSON.

## Starten

```bash
uv run python wetter_bericht.py
```

Das Programm fragt nach einer Stadt (Zürich, Bern, Genf, Basel, Lugano) und schreibt `bericht_<stadt>.json`. Ohne Netz erscheint «Live-Wetter nicht verfügbar», der Rest funktioniert.

## Tests

```bash
uv run pytest
```

Die Tests prüfen nur reine Funktionen mit kleinen Beispieldaten, nie die CSV-Datei und nie den Live-Abruf.

## Funktionen (Auswahl)

| Funktion | Zweck |
| --- | --- |
| `berechne_kennzahlen(zeilen)` | Durchschnitte, heissester Tag, Regentage, Gesamtniederschlag |
| `vergleiche_staedte(zeilen_a, zeilen_b)` | Differenz der Ø `tmax` und nässere Stadt |
| `finde_kaeltesten_tag(zeilen)` | Datum und `tmin` des kältesten Tages |
| `bereite_live_wetter_auf(antwort)` | Temperatur und Klartext aus der API-Antwort |

### Beispiel: Städtevergleich

```python
zuerich = lese_stadt(CSV_DATEI, "Zürich")
bern = lese_stadt(CSV_DATEI, "Bern")
vergleiche_staedte(zuerich, bern)
# {'stadt_a': 'Zürich', 'stadt_b': 'Bern', 'tmax_differenz': 0.8, 'naessere_stadt': 'Zürich'}
```

Nässer ist die Stadt mit dem grösseren Gesamtniederschlag. Bei Gleichstand ist `naessere_stadt` `None`. Eine leere Liste löst einen `ValueError` aus.

Weather data by Open-Meteo.com (CC BY 4.0).
