# Beispiele: Modul 3: Datenverarbeitung & Dateien

Daten, Übungsgerüste und Musterlösungen. Jede Lektion hat einen **eigenen Startordner**, in dem alles liegt, was sie braucht.

## 📁 Inhalt

- [`check_setup.py`](./check_setup.py) – prüft Python und `requests`. Lauf: `uv run python 05-beispiele/check_setup.py`

| Ordner | Daten | Gerüst / Lösung |
| ------ | ----- | --------------- |
| [`lektion-1/`](./lektion-1/) | `wetter_zuerich.txt` | `start.py`, `loesung.py` |
| [`lektion-2/`](./lektion-2/) | `wetter_30tage.csv` | `start.py`, `loesung.py` |
| [`lektion-3/`](./lektion-3/) | `beispiel_antwort.json`, `beispiel_antwort_5_staedte.json` | `start.py`, `loesung.py` |
| [`lektion-4/`](./lektion-4/) | `wetter_defekt.csv`, `beispiel_fehler.json` | `start.py`, `loesung.py` |

## Szenario und Daten

Wetter von Zürich, Bern, Genf, Basel und Lugano vom 20. September bis 19. Oktober 2026. Die Daten sind ein eingefrorener Snapshot (Quelle: Weather data by Open-Meteo.com, CC BY 4.0). Die JSON-Antworten in `lektion-3/` und `lektion-4/` sind echte Antworten der API vom 20. Oktober 2026.

## So arbeitest du

1. Kopiere den Ordner der Lektion in dein Arbeitsverzeichnis.
2. Ergänze in `start.py` die Stellen mit `TODO`.
3. Vergleiche mit den Kontrollwerten in der Übung. Die `loesung.py` ist dein Vergleichspunkt **nach** der Übung.
4. `OFFLINE = True` (Lektion 3 und 4) liest gespeicherte Antworten statt live abzurufen.

---

**Zurück zum Modul:** [Modul 3: Datenverarbeitung & Dateien](../README.md)
