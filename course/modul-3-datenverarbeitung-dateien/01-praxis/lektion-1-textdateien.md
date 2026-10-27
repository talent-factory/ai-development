# Lektion 1: Textdateien lesen und schreiben

**Dauer:** 50 Minuten (18:00–18:50)  
**Ziel:** Daten aus einer Textdatei einlesen, zerlegen, auswerten und das Ergebnis wieder in eine Datei schreiben. KI dient als Erklärer.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Begrüssung, Tagesüberblick, Szenario «Wetter Schweizer Städte» | Kurzvortrag |
| 5–10 | Startdateien holen, `check_setup.py` ausführen, **Check Listen & Dicts** | Einzelarbeit |
| 10–25 | **Live-Coding:** `open()`, `with`, Zeilen lesen, `split`, schreiben | Demo + Mitmachen |
| 25–30 | **KI-Moment:** `/erklaere` auf ein `open()`-Snippet | Einzelarbeit + KI |
| 30–45 | **Übung 1:** Wetterdaten Zürich auswerten | Einzelarbeit |
| 45–50 | **Kür** (freiwillig) oder Sicherung des Ergebnisses | Einzelarbeit |

---

## 1. Das Szenario für den ganzen Tag

Wir arbeiten heute mit **einem** Datensatz: dem Wetter von fünf Schweizer Städten (Zürich, Bern, Genf, Basel, Lugano) vom 20. September bis 19. Oktober 2026. Die Daten sind eingefroren, alle haben dieselben Zahlen.

| Lektion | Datei | Thema |
| ------- | ----- | ----- |
| 1 | `wetter_zuerich.txt` | Textdateien |
| 2 | `wetter_30tage.csv` | CSV |
| 3 | `zusammenfassung.json` + Open-Meteo-API | JSON und HTTP |
| 4 | `wetter_defekt.csv` | Fehlerbehandlung |

Jede Lektion hat einen **eigenen Ordner** in `05-beispiele/lektion-N/`. Wer eine Lektion verpasst hat, steigt mit dem Ordner der nächsten ein.

---

## 2. Startdateien und Setup (5 Minuten)

1. Kopiere den Ordner `05-beispiele/lektion-1/` in dein Arbeitsverzeichnis.
2. Prüfe dein Setup:

```bash
uv run python 05-beispiele/check_setup.py
```

Erwartet: zweimal `OK`. Bei `FEHLER: requests fehlt` hilft `uv add requests` (wir brauchen es in Lektion 3).

### Check: Listen und Dictionaries

Beantworte kurz für dich, bevor wir weitermachen:

```python
temperaturen = [12.5, 18.0, 9.3]
tag = {"datum": "2026-09-20", "tmax": 25.4}
```

1. Was ergibt `temperaturen[1]`? → `18.0` (Zählung beginnt bei 0)
2. Was ergibt `len(temperaturen)`? → `3`
3. Wie liest du `tmax` aus `tag`? → `tag["tmax"]` (ergibt `25.4`)

> Unsicher? Das ist kein Problem, wir benutzen Listen und Dicts gleich in jedem Beispiel.

---

## 3. Live-Coding: Eine Textdatei lesen

### Der Aufbau der Datei

`wetter_zuerich.txt` hat eine Zeile pro Tag, die Felder sind mit `;` getrennt:

```text
2026-09-20;Zürich;13.8;25.4;0.0
```

Reihenfolge: `datum;stadt;tmin;tmax;niederschlag`.

### Öffnen mit `with`

```python
with open("wetter_zuerich.txt", encoding="utf-8") as datei:
    for zeile in datei:
        print(zeile.strip())
```

| Teil | Bedeutung |
| ---- | --------- |
| `open(...)` | Öffnet die Datei. Der Standardmodus ist Lesen (`"r"`). |
| `encoding="utf-8"` | Wichtig für Umlaute wie «Zürich». Immer angeben. |
| `with ... as datei` | Schliesst die Datei am Ende automatisch, auch bei einem Fehler. |
| `for zeile in datei` | Geht Zeile für Zeile durch die Datei. |
| `.strip()` | Entfernt den Zeilenumbruch `\n` am Ende. |

### Zeile zerlegen und umwandeln

```python
zeile = "2026-09-20;Zürich;13.8;25.4;0.0"
teile = zeile.split(";")      # ['2026-09-20', 'Zürich', '13.8', '25.4', '0.0']
tmax = float(teile[3])         # 25.4  (aus Text wird eine Zahl)
```

**Wichtig:** Alles, was aus einer Datei kommt, ist zuerst **Text** (`str`). Zahlen musst du selbst mit `float()` umwandeln.

### Alle Tage in eine Liste von Dictionaries

```python
tage = []
with open("wetter_zuerich.txt", encoding="utf-8") as datei:
    for zeile in datei:
        datum, stadt, tmin, tmax, niederschlag = zeile.strip().split(";")
        tage.append({"datum": datum, "tmax": float(tmax)})

print(len(tage))          # Anzahl Tage
print(tage[0]["tmax"])    # tmax des ersten Tages
```

### Schreiben

```python
with open("ergebnis.txt", "w", encoding="utf-8") as datei:
    datei.write("Erste Zeile\n")
    datei.write(f"Anzahl Tage: {len(tage)}\n")
```

| Modus | Bedeutung |
| ----- | --------- |
| `"r"` | Lesen (Standard). Datei muss existieren. |
| `"w"` | Schreiben. **Überschreibt** eine vorhandene Datei! |
| `"a"` | Anhängen am Ende. |

`write()` fügt **keinen** Zeilenumbruch ein, `\n` musst du selbst setzen.

### Pfade mit `pathlib`

Damit dein Skript auch aus einem anderen Ordner funktioniert, baust du den Pfad relativ zum Skript:

```python
from pathlib import Path

DATEI = Path(__file__).parent / "wetter_zuerich.txt"
```

---

## 4. KI-Moment: `/erklaere` (5 Minuten)

Lass dir dieses Snippet erklären:

```python
with open("wetter_zuerich.txt", encoding="utf-8") as datei:
    zeilen = datei.readlines()
print(len(zeilen))
```

**Mit Command** (im Repo):

```text
/erklaere <Snippet hier einfügen>
```

**Ohne Command** (KI-Chat): Kopiere diesen Prompt:

> Ich lerne Python (Level: Anfänger). Erkläre mir den folgenden Code Zeile für Zeile, wie einem Anfänger. Verwende einfache Sprache. Gehe am Ende auf einen typischen Fehler ein, der bei diesem Code passieren kann.

**Beobachtungsaufgabe:** Die KI nennt am Ende einen typischen Fehler, meist **«Datei nicht gefunden»**. Löse ihn selbst aus: Ändere den Dateinamen in `wetter_zuerich.tx` und starte das Skript. Lies die Meldung `FileNotFoundError`. Wir sehen sie in Lektion 4 wieder.

> **Vertrauen, aber prüfen:** 1. Ausführen. 2. Gegen einen Kontrollwert oder `assert` prüfen. 3. Erst dann übernehmen.

---

## 5. Übung 1 (15 Minuten)

Siehe `02-uebungen/ex-01-textdatei.adoc`. Starte mit `lektion-1/start.py`. Kontrollwerte stehen in der Übung.

---

## 6. Kür (5 Minuten, freiwillig)

Liste die **Regentage** (`niederschlag > 0`) mit Datum auf, zum Beispiel `2026-10-01: 3.8 mm`. Die Lösung steht in `lektion-1/loesung.py` (Funktion `liste_regentage`).

---

## 7. Zusammenfassung

| Konzept | Merksatz |
| ------- | -------- |
| `with open(...)` | Öffnet und schliesst die Datei sicher. |
| `encoding="utf-8"` | Immer angeben, sonst gehen Umlaute kaputt. |
| `.strip().split(";")` | Zeile säubern und in Felder zerlegen. |
| `float(...)` | Text aus der Datei in eine Zahl umwandeln. |
| `"w"` | Überschreibt. Wer anhängen will, nimmt `"a"`. |

---

## Hinweise für die Dozentin / den Dozenten

- **Streichreihenfolge L1:** Kür entfällt zuerst. Der Check Listen/Dicts darf auf 3 Minuten schrumpfen.
- Wer `check_setup.py` mit `FEHLER` abbricht, bekommt `uv add requests`. Das Problem betrifft erst Lektion 3, es muss jetzt nicht gelöst werden.
- Typische Stolpersteine: vergessenes `strip()` (Zahlen mit `\n`), `float()` vergessen (Textvergleich statt Zahl), `"w"` überschreibt die Eingabedatei, falls beide Dateinamen gleich sind.
- Musterlösung: `05-beispiele/lektion-1/loesung.py` nach der Übung freigeben.

---

**Weiter:** [Lektion 2: CSV-Dateien](./lektion-2-csv.md) · **Zurück:** [Modul 3](../README.md)
