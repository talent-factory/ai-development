# Lektion 3: JSON verarbeiten und eine Wetter-API abrufen

**Dauer:** 50 Minuten (20:00–20:50)  
**Ziel:** JSON-Dateien speichern und laden, die Struktur einer API-Antwort lesen und einen HTTP-Abruf mit `requests` auswerten. KI schreibt den Aufruf, wir prüfen ihn gegen die Doku.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick** Lektion 2: Was lief, was hakt? | Plenum |
| 5–15 | **JSON:** `json.dump`, `json.load`, verschachtelte Strukturen | Demo + Mitmachen |
| 15–25 | **Geführte API-Demo:** `requests.get`, Parameter, Antwortstruktur | Dozentin / Dozent |
| 25–30 | **KI-Moment:** API-Aufruf ohne Doku schreiben lassen, gegen die Doku prüfen | Einzelarbeit + KI |
| 30–45 | **Übung 3:** JSON speichern/laden, Wettercode-Dict, Bern abrufen | Einzelarbeit |
| 45–50 | **Kür** (freiwillig): alle fünf Städte in einem Request | Einzelarbeit |

> **Zeitrisiko:** Diese Lektion ist die dichteste des Tages. Die Streichreihenfolge steht unten bei den Hinweisen.

---

## 1. Rückblick (5 Minuten)

Gleiche Runde wie bisher: Was lief in Lektion 2, was hakt? Wer eine Lektion verpasst hat, steigt mit dem Ordner `05-beispiele/lektion-3/` ein. Er enthält das Ergebnis aus Lektion 2 (Durchschnitt `tmax` je Stadt) bereits im Code.

---

## 2. JSON

**JSON** (*JavaScript Object Notation*) ist ein Textformat für **verschachtelte** Daten. Fast jede Web-API spricht JSON. Es sieht aus wie Python-Dictionaries und -Listen:

```json
{
  "Zürich": 20.7,
  "Bern": 19.9
}
```

| Python | JSON |
| ------ | ---- |
| `dict` | Objekt `{...}` |
| `list` | Array `[...]` |
| `str`, `int`, `float` | Text, Zahl |
| `True` / `False` | `true` / `false` |
| `None` | `null` |

### Speichern und laden

```python
import json

durchschnitt = {"Zürich": 20.7, "Bern": 19.9}

with open("zusammenfassung.json", "w", encoding="utf-8") as datei:
    json.dump(durchschnitt, datei, indent=2, ensure_ascii=False)

with open("zusammenfassung.json", encoding="utf-8") as datei:
    geladen = json.load(datei)

print(geladen["Bern"])   # 19.9
```

| Teil | Bedeutung |
| ---- | --------- |
| `json.dump(daten, datei)` | Schreibt Python-Daten als JSON in eine Datei. |
| `json.load(datei)` | Liest JSON und gibt Dicts und Listen zurück. |
| `indent=2` | Macht die Datei lesbar (eingerückt). |
| `ensure_ascii=False` | Behält Umlaute: `"Zürich"` statt `"Zürich"`. |

**Zum Merken:** `dump`/`load` arbeiten mit **Dateien**. `dumps`/`loads` (mit `s`) arbeiten mit **Text** (*string*).

### CSV oder JSON?

| | CSV | JSON |
| - | --- | ---- |
| Struktur | flache Tabelle | verschachtelt |
| Typen | alles Text | Zahlen, Text, Listen, `null` |
| Typisch für | Tabellenkalkulation, Exporte | Web-APIs, Konfiguration |

---

## 3. Geführte API-Demo (10 Minuten)

Eine **API** (Programmierschnittstelle) liefert Daten über das Netz. Wir fragen **Open-Meteo** nach dem Wetter. Der Dienst braucht keinen Schlüssel.

> Datenquelle: **Weather data by Open-Meteo.com** (Lizenz CC BY 4.0). Bei Veröffentlichungen ist diese Quellenangabe Pflicht.

### Der Aufruf

```python
import requests

antwort = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": 46.948,
        "longitude": 7.4474,
        "current": "temperature_2m,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,weather_code",
        "forecast_days": 3,
        "timezone": "Europe/Zurich",
    },
    timeout=10,
)
antwort.raise_for_status()
daten = antwort.json()
```

| Teil | Bedeutung |
| ---- | --------- |
| `params={...}` | Werden als `?latitude=...&longitude=...` an die URL gehängt. |
| `timeout=10` | Gibt nach 10 Sekunden auf, statt ewig zu warten. **Immer angeben.** |
| `raise_for_status()` | Löst bei HTTP-Fehlern (4xx, 5xx) einen `HTTPError` aus. |
| `.json()` | Wandelt den Antworttext in Dicts und Listen um. |

### Die Antwort lesen

Die wichtigen Teile von `daten`:

```text
daten["current"]["temperature_2m"]      → aktuelle Temperatur
daten["daily"]["time"]                  → ['2026-10-20', '2026-10-21', '2026-10-22']
daten["daily"]["temperature_2m_max"]    → [14.4, 13.5, 12.9]
daten["daily"]["weather_code"]          → [61, 80, 45]
```

`daily` ist ein Dictionary aus **parallelen Listen**: Index 0 ist heute in jeder Liste. Den Tag 0 liest du so:

```python
heute_tmax = daten["daily"]["temperature_2m_max"][0]
heute_code = daten["daily"]["weather_code"][0]
```

### Wettercodes

Die API liefert **WMO-Codes**, also Zahlen. Den Klartext übersetzen wir selbst mit einem Dictionary:

| Code | Bedeutung | Code | Bedeutung |
| ---- | --------- | ---- | --------- |
| 0 | klar | 61 | leichter Regen |
| 3 | bedeckt | 80 | leichte Regenschauer |
| 45 | Nebel | 95 | Gewitter |

```python
WETTERCODES = {0: "klar", 3: "bedeckt", 45: "Nebel"}
WETTERCODES.get(61, "unbekannt")   # 'unbekannt', weil der Code fehlt
```

`.get(code, "unbekannt")` verhindert einen `KeyError` bei Codes, die wir nicht eingetragen haben.

### Wenn das Netz oder die API nicht mitspielt

In `start.py` steht oben `OFFLINE = False`. Mit `OFFLINE = True` liest das Programm die gespeicherte Antwort `beispiel_antwort.json` statt live abzurufen. Du arbeitest dann mit denselben Zahlen wie die ganze Klasse.

---

## 4. KI-Moment: API-Aufruf ohne Doku (5 Minuten)

Eine KI kann einen API-Aufruf in Sekunden schreiben. Aber stimmt er?

**Prompt** (in den KI-Chat kopieren, bewusst **ohne** Dokumentation):

> Schreibe mir einen Python-Aufruf mit `requests` für die Open-Meteo-API, der die Tageshöchsttemperatur und den Niederschlag für Bern der nächsten drei Tage liefert.

**Prüfe den Aufruf gegen diesen Doku-Ausschnitt:**

| Parameter | Bedeutung | Beispiel |
| --------- | --------- | -------- |
| `latitude`, `longitude` | Koordinaten (Pflicht) | `46.948`, `7.4474` |
| `daily` | Tageswerte, kommagetrennt | `temperature_2m_max,precipitation_sum` |
| `current` | aktuelle Werte | `temperature_2m,weather_code` |
| `forecast_days` | Anzahl Tage | `3` |
| `timezone` | Zeitzone | `Europe/Zurich` |

**Beobachtungsaufgabe:** Führe den Aufruf aus und vergleiche die Namen mit der Tabelle. Drei Dinge können passieren:

1. **Alles stimmt:** Du bekommst die Daten. Prüfe trotzdem `len(daten["daily"]["time"])`, es muss `3` sein.
2. **Falscher Variablenname** (zum Beispiel `daily=temp_max`): Die API antwortet mit HTTP 400 und einer lesbaren Begründung im Feld `reason`.
3. **Erfundener zusätzlicher Parameter** (zum Beispiel `temperature=true`): Die API **ignoriert** ihn stillschweigend. Du bekommst HTTP 200, aber ohne den erhofften Wert. Fehlermeldung gibt es keine.

Der dritte Fall ist der gefährlichste: Kein Fehler heisst nicht, dass das Ergebnis stimmt.

> **Vertrauen, aber prüfen:** 1. Ausführen. 2. Gegen einen Kontrollwert oder `assert` prüfen. 3. Erst dann übernehmen.

---

## 5. Übung 3 (15 Minuten)

Siehe `02-uebungen/ex-03-json-api.adoc`. Starte mit `lektion-3/start.py`. Die Übung hat drei Teile: JSON speichern und laden, ein eigenes Wettercode-Dict bauen, Wetter von Bern abrufen.

---

## 6. Kür (5 Minuten, freiwillig)

Hole **alle fünf Städte in einem einzigen Request**: Gib `latitude` und `longitude` als kommagetrennte Listen mit. Die Antwort ist dann eine **Liste** mit einem Dictionary pro Stadt (nicht mehr ein Dictionary). Die Lösung steht in `lektion-3/loesung.py` (Funktion `hole_wetter_alle_staedte`).

---

## 7. Zusammenfassung

| Konzept | Merksatz |
| ------- | -------- |
| `json.dump` / `json.load` | Dateien schreiben und lesen. Mit `indent=2, ensure_ascii=False`. |
| `requests.get(url, params=..., timeout=...)` | Ruft eine API ab. `timeout` nie vergessen. |
| `raise_for_status()` | Macht aus HTTP-Fehlern eine Exception. |
| `daily` als parallele Listen | Index 0 ist heute in jeder Liste. |
| `.get(code, "unbekannt")` | Dict-Zugriff ohne `KeyError`. |
| KI und APIs | Erfundene Parameter ignoriert die API manchmal still. Immer gegen die Doku prüfen. |

---

## Hinweise für die Dozentin / den Dozenten

- **Streichreihenfolge L3 (bei Zeitnot, in dieser Reihenfolge):**
  1. Kür entfällt.
  2. Wettercode-Eigenbau: Die Studierenden nehmen `WETTERCODES_VOLL` aus `start.py`.
  3. Live-API wird zur reinen Demo: Alle setzen `OFFLINE = True`.
  4. Der Rückblick schrumpft auf 2 Minuten.
- **API-Last:** Die Gratisgrenze liegt bei 600 Aufrufen pro Minute und IP. 20 Studierende im selben Netz sind unkritisch, solange nicht in einer Schleife abgerufen wird. Bei einem Ausfall: `OFFLINE = True` ansagen und den Ausfall als Brücke zu Lektion 4 nutzen.
- **Live-Werte ändern sich.** Die Kontrollwerte der Übung gelten deshalb nur für `OFFLINE = True`. Live prüft man die Struktur (drei Tage, `daily` vorhanden).
- **Heute beobachtet (20.10.2026), vor dem Unterricht kurz erneut prüfen:** Fehlen `latitude` und `longitude` ganz, antwortet die API mit HTTP 200 und leerem Body. Erst `.json()` wirft dann einen `JSONDecodeError`. Das nehmen wir in Lektion 4 auf.
- `requests` sollte installiert sein (`uv add requests`, siehe Vorbereitung). Fehlt es, funktioniert `OFFLINE = True` trotzdem: `requests` wird erst im Live-Zweig von `hole_wetter()` importiert. Nachinstallieren kann man später.
- Musterlösung: `05-beispiele/lektion-3/loesung.py` (läuft mit `OFFLINE = True` immer gleich) nach der Übung freigeben.

---

**Weiter:** [Lektion 4: Fehlerbehandlung](./lektion-4-fehlerbehandlung.md) · **Zurück:** [Lektion 2](./lektion-2-csv.md) · [Modul 3](../README.md)
