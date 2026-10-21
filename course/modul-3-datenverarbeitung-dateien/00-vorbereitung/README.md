# Vorbereitung: Modul 3 – Datenverarbeitung & Dateien

**Zeitaufwand:** ca. 30 Minuten, vor dem Unterricht  
**Ziel:** Setup prüfen und Listen sowie Dictionaries sicher anwenden. Beides brauchen wir heute in jeder Lektion.

---

## Überblick

| Teil | Dauer | Inhalt |
| ---- | ----- | ------ |
| 1 | 5 Min. | Setup: `requests` installieren und prüfen |
| 2 | 10 Min. | Leseauftrag: Listen und Dictionaries |
| 3 | 10–15 Min. | Selbsttest mit 7 Aufgaben |
| 4 | 5 Min. | Überblick: Was wir heute machen |

Wer die Vorbereitung nicht schafft, kommt trotzdem mit: Lektion 1 beginnt mit einem 5-Minuten-Check zu Listen und Dicts.

---

## 1. Setup (5 Minuten)

Im Projektordner:

```bash
uv add requests
uv run python course/modul-3-datenverarbeitung-dateien/05-beispiele/check_setup.py
```

Erwartet:

```text
OK: Python 3.13
OK: requests 2.33.1
```

Die Versionsnummern dürfen abweichen. Kommt eine Zeile mit `FEHLER`, folge der Anweisung darin. Funktioniert `uv` bei dir nicht mehr, hilft als Notlösung `pip install requests`. Melde dich in diesem Fall vorher, damit wir es nicht im Unterricht klären müssen.

---

## 2. Leseauftrag: Listen und Dictionaries (10 Minuten)

Dateien liefern uns viele Werte auf einmal. Dafür brauchen wir zwei Datentypen.

### Liste: geordnete Werte

```python
temperaturen = [12.5, 18.0, 9.3, 21.7]

temperaturen[0]            # 12.5  (erstes Element, Zählung beginnt bei 0)
temperaturen[-1]           # 21.7  (letztes Element)
len(temperaturen)          # 4
temperaturen.append(15.2)  # hängt einen Wert hinten an

for t in temperaturen:     # jedes Element einzeln
    print(t)
```

### Dictionary: Werte mit Namen

```python
tag = {"datum": "2026-09-20", "tmax": 25.4, "niederschlag": 0.0}

tag["tmax"]                # 25.4
tag["wind"] = 12.0         # neuen Eintrag hinzufügen
tag.get("sonne")           # None, weil der Schlüssel fehlt (kein Fehler)
tag["sonne"]               # KeyError! Der Schlüssel fehlt.

for schluessel, wert in tag.items():
    print(schluessel, wert)
```

### Beides kombiniert: Liste von Dictionaries

Genau so sehen unsere Wetterdaten aus:

```python
tage = [
    {"datum": "2026-09-20", "tmax": 25.4},
    {"datum": "2026-09-21", "tmax": 20.9},
]

tage[1]["datum"]           # '2026-09-21'
for tag in tage:
    print(tag["datum"], tag["tmax"])
```

### Text zerlegen und umwandeln

Aus einer Datei kommt jede Zeile als Text:

```python
zeile = "2026-09-20;Zürich;13.8;25.4;0.0"
teile = zeile.split(";")   # ['2026-09-20', 'Zürich', '13.8', '25.4', '0.0']
tmax = float(teile[3])     # 25.4  (jetzt eine Zahl)
```

---

## 3. Selbsttest (10–15 Minuten)

Löse die Aufgaben im Kopf oder in einer Python-Shell (`uv run python`). Die Lösungen stehen unten, schau erst nach, wenn du eine eigene Antwort hast.

Gegeben:

```python
temperaturen = [12.5, 18.0, 9.3, 21.7]
tag = {"datum": "2026-09-20", "tmax": 25.4, "niederschlag": 0.0}
tage = [
    {"datum": "2026-09-20", "tmax": 25.4},
    {"datum": "2026-09-21", "tmax": 20.9},
]
zeile = "2026-09-20;Zürich;13.8;25.4;0.0"
```

1. Was ergibt `temperaturen[2]`?
2. Was ergibt `len(temperaturen)` nach `temperaturen.append(15.2)`? (Ab Aufgabe 3 gilt wieder die ursprüngliche Liste mit vier Werten.)
3. Wie viele Werte in `temperaturen` sind grösser als 15? (Schreibe eine `for`-Schleife mit Zähler.)
4. Wie berechnest du den Durchschnitt von `temperaturen`?
5. Was ergibt `tag["niederschlag"]`, und was passiert bei `tag["wind"]`?
6. Wie gibst du das Datum des zweiten Eintrags in `tage` aus?
7. Wie holst du die Maximaltemperatur aus `zeile` als **Zahl**?

<details>
<summary>Lösungen</summary>

1. `9.3` (Index 2 ist das dritte Element)
2. `5`
3. `2` (18.0 und 21.7):

   ```python
   anzahl = 0
   for t in temperaturen:
       if t > 15:
           anzahl += 1
   ```

4. `sum(temperaturen) / len(temperaturen)` → `15.375`
5. `0.0`. Bei `tag["wind"]` gibt es einen `KeyError`, weil der Schlüssel fehlt.
6. `print(tage[1]["datum"])` → `2026-09-21`
7. `float(zeile.split(";")[3])` → `25.4`

</details>

Hakt es bei mehr als zwei Aufgaben, lies Teil 2 noch einmal. Wir klären Offenes in der ersten Viertelstunde von Lektion 1.

---

## 4. Überblick: Was wir heute machen

Wir arbeiten den ganzen Abend mit **einem Szenario**: dem Wetter von fünf Schweizer Städten (Zürich, Bern, Genf, Basel, Lugano) vom 20. September bis 19. Oktober 2026.

| Lektion | Zeit | Thema | Datei |
| ------- | ---- | ----- | ----- |
| 1 | 18:00–18:50 | Textdateien lesen und schreiben | `wetter_zuerich.txt` |
| 2 | 19:00–19:50 | CSV-Dateien | `wetter_30tage.csv` |
| 3 | 20:00–20:50 | JSON und eine Wetter-API | `zusammenfassung.json` |
| 4 | 21:00–21:50 | Fehlerbehandlung und Abschluss | `wetter_defekt.csv` |

In jeder Lektion setzen wir die KI an einer Stelle ein: als Erklärer, als Testdaten-Generator, als Doku-Leser und als Fehlerberater. Regel für den ganzen Abend: **Vertrauen, aber prüfen.**

Du brauchst am Unterrichtstag: Laptop mit Projektordner, Editor, Internetzugang und Zugang zu einem KI-Chat oder Claude Code.

---

**Zurück zum Modul:** [Modul 3: Datenverarbeitung & Dateien](../README.md)
