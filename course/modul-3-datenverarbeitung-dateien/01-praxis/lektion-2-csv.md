# Lektion 2: CSV-Dateien importieren, filtern und exportieren

**Dauer:** 50 Minuten (19:00–19:50)  
**Ziel:** Eine CSV-Datei mit `csv.DictReader` einlesen, auswerten, filtern und das Ergebnis mit `csv.DictWriter` exportieren. KI erzeugt Testdaten, die wir prüfen.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick** Lektion 1: Was lief, was hakt? | Plenum |
| 5–20 | **Live-Coding:** `csv.DictReader`, Typumwandlung, `DictWriter` | Demo + Mitmachen |
| 20–25 | **KI-Moment:** Testdaten erzeugen und mit `assert` prüfen | Einzelarbeit + KI |
| 25–45 | **Übung 2:** Durchschnitt, Filter, Export | Einzelarbeit |
| 45–50 | **Kür** (freiwillig) oder Sicherung des Ergebnisses | Einzelarbeit |

---

## 1. Rückblick (5 Minuten)

Kurze Runde, ohne Aufgabe: Was hat in Lektion 1 geklappt, was hakt noch? Typische Antworten: `strip()` vergessen, `float()` vergessen, Datei nicht gefunden.

Wer Lektion 1 verpasst hat, nimmt den Ordner `05-beispiele/lektion-2/` und steigt hier ein.

---

## 2. Was ist CSV?

**CSV** (*Comma-Separated Values*) ist eine Textdatei in Tabellenform: eine Zeile pro Datensatz, die Felder sind durch ein Trennzeichen getrennt. Die **erste Zeile** enthält die Spaltennamen.

```text
stadt,datum,tmin,tmax,niederschlag_mm,wettercode
Zürich,2026-09-20,13.8,25.4,0.0,45
Zürich,2026-09-21,13.9,20.9,0.0,3
```

Unsere Datei `wetter_30tage.csv` enthält 150 Datenzeilen: 5 Städte × 30 Tage.

**Warum nicht einfach `split(",")`?** Das funktioniert, bis ein Feld selbst ein Komma enthält (`"Zürich, Stadt"`) oder Anführungszeichen vorkommen. Das `csv`-Modul behandelt diese Fälle richtig.

---

## 3. Live-Coding: CSV lesen

### Mit `DictReader`

```python
import csv

with open("wetter_30tage.csv", newline="", encoding="utf-8") as datei:
    leser = csv.DictReader(datei)
    for zeile in leser:
        print(zeile["stadt"], zeile["tmax"])
```

| Teil | Bedeutung |
| ---- | --------- |
| `newline=""` | Pflicht beim `csv`-Modul. Sonst gibt es unter Windows leere Zeilen. |
| `encoding="utf-8"` | Wieder für die Umlaute. |
| `csv.DictReader(datei)` | Liest die Kopfzeile und liefert **pro Zeile ein Dictionary**. |
| `zeile["tmax"]` | Zugriff über den Spaltennamen. Kein Zählen von Positionen. |

### Alles ist Text

```python
zeile = {"stadt": "Zürich", "tmax": "25.4"}
zeile["tmax"] > 20          # TypeError! Text lässt sich nicht mit einer Zahl vergleichen
float(zeile["tmax"]) > 20   # True
```

Darum wandeln wir die Zahlenfelder beim Einlesen **einmal** um:

```python
for feld in ("tmin", "tmax", "niederschlag_mm"):
    zeile[feld] = float(zeile[feld])
```

### Auswerten: Durchschnitt je Stadt

```python
werte = {}                                       # Stadt → Liste von tmax-Werten
for zeile in zeilen:
    werte.setdefault(zeile["stadt"], []).append(zeile["tmax"])

for stadt, liste in werte.items():
    print(stadt, round(sum(liste) / len(liste), 1))
```

`setdefault(schluessel, [])` legt eine leere Liste an, falls der Schlüssel noch fehlt, und gibt die Liste zurück.

### Filtern

```python
warm = []
for zeile in zeilen:
    if zeile["tmax"] > 20:
        warm.append(zeile)
```

### Schreiben mit `DictWriter`

```python
with open("warme_tage.csv", "w", newline="", encoding="utf-8") as datei:
    schreiber = csv.DictWriter(datei, fieldnames=["stadt", "datum", "tmin", "tmax", "niederschlag_mm", "wettercode"])
    schreiber.writeheader()      # schreibt die Kopfzeile
    schreiber.writerows(warm)    # schreibt alle Zeilen auf einmal
```

---

## 4. KI-Moment: Testdaten erzeugen (5 Minuten)

Eine KI kann in Sekunden Testdaten liefern, mit denen du deine Funktionen ausprobierst, bevor du sie auf den echten Daten laufen lässt.

**Prompt** (in den KI-Chat kopieren):

> Erzeuge 10 CSV-Zeilen mit der Kopfzeile `stadt,datum,tmin,tmax,niederschlag_mm,wettercode`. Städte: Zürich, Bern, Genf. Datum im Format 2026-10-01. Temperaturen in °C mit Dezimalpunkt, tmin immer kleiner als tmax. Gib nur das CSV aus, ohne Erklärung.

Speichere die Antwort als `testdaten.csv` und prüfe sie mit deinem Code:

```python
zeilen = lese_csv(Path("testdaten.csv"))

for zeile in zeilen:
    assert list(zeile) == ["stadt", "datum", "tmin", "tmax", "niederschlag_mm", "wettercode"]
    assert zeile["tmin"] < zeile["tmax"], f"tmin >= tmax: {zeile}"
print("Testdaten OK:", len(zeilen), "Zeilen")
```

**Was du beobachtest:** Oft stimmt etwas nicht, zum Beispiel ein Komma als Dezimaltrenner (`13,8`), zusätzliche Anführungszeichen oder `tmin > tmax`. Dann bricht `float()` mit einem `ValueError` ab oder `assert` schlägt an. So findest du Fehler **bevor** sie die echten Daten treffen.

**Wichtig:** Die KI-Daten sind nur zum Testen. Die Auswertung in der Übung läuft auf `wetter_30tage.csv`, weil nur dort die Kontrollwerte gelten.

> **Vertrauen, aber prüfen:** 1. Ausführen. 2. Gegen einen Kontrollwert oder `assert` prüfen. 3. Erst dann übernehmen.

---

## 5. Übung 2 (20 Minuten)

Siehe `02-uebungen/ex-02-csv.adoc`. Starte mit `lektion-2/start.py`. Kontrollwerte stehen in der Übung.

---

## 6. Kür (5 Minuten, freiwillig)

Lass die Benutzerin oder den Benutzer die **Stadt mit `input()` wählen** und gib nur deren Tage über 20 °C aus. Die Hilfsfunktion `filtere_stadt` steht in `lektion-2/loesung.py`.

---

## 7. Zusammenfassung

| Konzept | Merksatz |
| ------- | -------- |
| `csv.DictReader` | Liefert pro Zeile ein Dictionary, Zugriff über den Spaltennamen. |
| `newline=""` | Beim `csv`-Modul immer angeben. |
| `float(...)` | CSV liefert nur Text. Zahlen einmal beim Einlesen umwandeln. |
| `setdefault` | Legt bei Bedarf eine leere Liste für einen neuen Schlüssel an. |
| `csv.DictWriter` | `writeheader()` für die Kopfzeile, `writerows()` für alle Zeilen. |
| KI-Testdaten | Erst mit `assert` prüfen, dann benutzen. |

---

## Hinweise für die Dozentin / den Dozenten

- **Streichreihenfolge L2:** Kür entfällt zuerst. Der Rückblick darf auf 3 Minuten schrumpfen.
- Typische Stolpersteine: `float()` vergessen (`TypeError` beim Vergleich), `newline=""` vergessen, `fieldnames` nicht passend zu den Zeilen (`ValueError` bei `writerows`), Durchschnitt durch falsche Zählerstände.
- Der KI-Moment funktioniert auch ohne KI-Zugang: Dozentin oder Dozent zeigt eine vorbereitete, absichtlich fehlerhafte Antwort (`13,8` statt `13.8`).
- Musterlösung: `05-beispiele/lektion-2/loesung.py` nach der Übung freigeben.

---

**Weiter:** [Lektion 3: JSON und APIs](./lektion-3-json-api.md) · **Zurück:** [Lektion 1](./lektion-1-textdateien.md) · [Modul 3](../README.md)
