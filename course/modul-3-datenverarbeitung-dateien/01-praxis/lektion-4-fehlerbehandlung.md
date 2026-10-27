# Lektion 4: Fehlerbehandlung und stabile Skripte

**Dauer:** 50 Minuten (21:00–21:50)  
**Ziel:** Fehler lesen, mit `try/except` gezielt abfangen und Skripte bauen, die bei kaputten Daten oder einer ausgefallenen API nicht abstürzen. Abschluss und Feedback zum Modul.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick** Lektion 3: Was lief, was hakt? | Plenum |
| 5–17 | **Input:** Traceback lesen, `try/except/else/finally`, spezifische Fehler, `requests`-Fehler | Demo + Mitmachen |
| 17–22 | **KI-Moment:** `/debug` auf einen `ValueError`-Traceback | Einzelarbeit + KI |
| 22–35 | **Übung 4:** Defekte CSV und API-Fehler robust behandeln | Einzelarbeit |
| 35–42 | **Kür** (freiwillig) oder Puffer | Einzelarbeit |
| 42–50 | **Abschluss:** Feedback-Blitzrunde, Ausblick auf Modul 4 | Plenum |

---

## 1. Rückblick (5 Minuten)

Gleiche Runde wie bisher. Wer eine Lektion verpasst hat, steigt mit dem Ordner `05-beispiele/lektion-4/` ein: Er enthält `wetter_defekt.csv` und `beispiel_fehler.json`, mehr braucht diese Lektion nicht.

Wir haben zwei Fehler schon gesehen:
- **Lektion 1:** `FileNotFoundError`, weil die Datei fehlte.
- **Lektion 3:** HTTP 400 mit `reason` bei einem falschen Variablennamen, und die API, die einen erfundenen Parameter stillschweigend ignorierte.

Heute lernen wir, solche Fehler **gezielt** zu behandeln.

---

## 2. Einen Traceback lesen

```text
Traceback (most recent call last):
  File "naiv.py", line 5, in <module>
    zeile["tmax"] = float(zeile["tmax"])
                    ~~~~~^^^^^^^^^^^^^^^
ValueError: could not convert string to float: ''
```

| Zeile | Was sie sagt |
| ----- | ------------ |
| letzte Zeile | **Fehlerart und Grund:** `ValueError`, ein leerer Text lässt sich nicht in eine Zahl umwandeln. |
| `File ..., line 5` | **Wo** es passiert ist. |
| die Code-Zeile darunter | **Welche** Anweisung. |

Lies den Traceback **von unten nach oben**: erst was, dann wo.

---

## 3. `try` und `except`

```python
try:
    tmax = float(zeile["tmax"])
except ValueError:
    print("tmax ist keine Zahl, Zeile wird übersprungen")
```

| Block | Wann er läuft |
| ----- | ------------- |
| `try` | Der Code, der schiefgehen kann. |
| `except Fehlerart` | Nur wenn genau diese Fehlerart auftritt. |
| `else` | Nur wenn im `try` **kein** Fehler auftrat. |
| `finally` | **Immer**, zum Beispiel zum Aufräumen. |

```python
try:
    tmax = float(zeile["tmax"])
except ValueError:
    uebersprungen += 1
else:
    gueltig.append(zeile)
```

### Häufige Fehlerarten in diesem Modul

| Fehler | Typische Ursache |
| ------ | ---------------- |
| `FileNotFoundError` | Datei existiert nicht oder Pfad falsch. |
| `ValueError` | Text lässt sich nicht umwandeln (`float("k.A.")`). |
| `KeyError` | Schlüssel fehlt im Dictionary. |
| `ZeroDivisionError` | Division durch 0, zum Beispiel Durchschnitt über eine leere Liste. |

### Mehrere `except`-Blöcke

```python
try:
    daten = lade_json("zusammenfassung.json")
except FileNotFoundError:
    print("Datei fehlt")
except json.JSONDecodeError:
    print("Datei ist kein gültiges JSON")
```

Python prüft die Blöcke **von oben nach unten** und nimmt den ersten passenden. Darum gilt: **Speziell zuerst, allgemein zuletzt.**

### Der Anti-Pattern: den Fehler verschlucken

```python
try:
    tmax = float(zeile["tmax"])
except:
    pass          # NICHT machen!
```

Das fängt **jeden** Fehler, auch Tippfehler im Code, und sagt nichts. Du merkst nicht, dass 5 von 24 Zeilen fehlen. Ein guter `except`-Block nennt die **konkrete Fehlerart** und **meldet** oder **zählt** das Problem.

---

## 4. Fehler bei API-Abrufen

`requests` kennt eigene Fehlerarten. Alle erben von `requests.exceptions.RequestException`:

| Fehler | Bedeutung |
| ------ | --------- |
| `HTTPError` | Die API hat mit einem Fehlerstatus geantwortet (4xx, 5xx). Kommt von `raise_for_status()`. |
| `ConnectionError` | Keine Verbindung (kein Netz, falsche Adresse). |
| `Timeout` | Die API hat zu langsam geantwortet. |
| `JSONDecodeError` | Die Antwort ist kein gültiges JSON (zum Beispiel leer). |
| `RequestException` | **Oberklasse** für alle obigen. |

```python
import requests

try:
    antwort = requests.get(url, params=parameter, timeout=5)
    antwort.raise_for_status()
    daten = antwort.json()
except requests.exceptions.HTTPError as fehler:
    print("Die API lehnt ab:", fehler.response.json()["reason"])
except requests.exceptions.JSONDecodeError:
    print("Leere oder ungültige Antwort")
except requests.exceptions.RequestException:
    print("Keine Verbindung")
```

Die Reihenfolge zählt: `HTTPError` und `JSONDecodeError` sind **Unterklassen** von `RequestException`. Stünde `RequestException` zuerst, würden die zwei spezifischen Blöcke nie erreicht.

**Aus Lektion 3:** Fehlen `latitude` und `longitude` ganz, antwortet die API mit HTTP 200 und einem leeren Body. `raise_for_status()` merkt nichts, erst `.json()` wirft den `JSONDecodeError`. Darum gehört `.json()` ins `try`.

Die API liefert bei HTTP-Fehlern einen Grund im Klartext, zum Beispiel:

```json
{"error": true, "reason": "Latitude must be in range of -90 to 90°. Given: 999.0."}
```

Er liegt als `beispiel_fehler.json` im Ordner, damit du auch ohne Netz damit arbeiten kannst.

---

## 5. KI-Moment: `/debug` (5 Minuten)

Dieser Code liest `wetter_defekt.csv` ohne Schutz:

```python
import csv

with open("wetter_defekt.csv", newline="", encoding="utf-8") as datei:
    for zeile in csv.DictReader(datei):
        zeile["tmax"] = float(zeile["tmax"])
```

Er bricht mit dem Traceback aus Abschnitt 2 ab (`ValueError: could not convert string to float: ''`).

**Mit Command** (im Repo):

```text
/debug <Code und Traceback hier einfügen>
```

**Ohne Command** (KI-Chat): Kopiere diesen Prompt und füge Code und Traceback an:

> Ich lerne Python (Level: Anfänger) und brauche Hilfe bei einem Fehler. Beantworte in dieser Reihenfolge: 1. Was bedeutet die Fehlermeldung in einem Satz? 2. Welche Zeile verursacht sie? 3. Was ist die Ursache? 4. Wie lässt sich der Fehler beheben? Erkläre die korrigierte Stelle. 5. Schlage 2–3 konkrete Korrekturen vor, nummeriert, und frage, welche ich anwenden soll.

**Beobachtungsaufgabe:** Wähle einen der Vorschläge und wende ihn an. Beurteile ihn danach:

- **`try/except ValueError` mit Überspringen oder Zählen:** Das ist, was wir wollen. Du verlierst keine Information, du siehst, wie viele Zeilen fehlen.
- **`except: pass`:** Das verschluckt jeden Fehler und sagt nichts. Besprich, warum das gefährlich ist.
- **Fehlende Werte durch `0.0` ersetzen:** Der Code läuft, aber dein Durchschnitt stimmt nicht mehr, weil `0.0` Grad kein «fehlt» ist. Der Fehler ist nur versteckt.

**Kontrolle:** Danach müssen **19 gültige** und **5 übersprungene** Zeilen herauskommen.

> **Vertrauen, aber prüfen:** 1. Ausführen. 2. Gegen einen Kontrollwert oder `assert` prüfen. 3. Erst dann übernehmen.

---

## 6. Übung 4 (13 Minuten)

Siehe `02-uebungen/ex-04-fehlerbehandlung.adoc`. Starte mit `lektion-4/start.py`. Teil 1: defekte CSV robust einlesen. Teil 2: API-Fehler abfangen.

---

## 7. Kür oder Puffer (7 Minuten)

Schreibe die übersprungenen Zeilen mit **Zeilennummer und Grund** in `uebersprungen.log`. Die Lösung steht in `lektion-4/loesung.py` (Parameter `logdatei` von `lese_robust`). Wer fertig ist, kann auch den Notfall testen: `hole_temperatur(None, None)` liefert eine leere Antwort.

---

## 8. Abschluss und Feedback (8 Minuten)

**Blitzrunde (ca. 6 Minuten):** Jede und jeder sagt in einem Satz:

1. **Ein Ding, das klar war.**
2. **Ein Ding, das unklar blieb.**

Dazu der Satz zum Mitnehmen: **Vertrauen, aber prüfen.** Das gilt für KI-Code, für Daten aus Dateien und für Antworten von APIs.

**Ausblick (ca. 1 Minute):** In Modul 4 (Agentic Coding) lassen wir die KI nicht mehr nur einzelne Funktionen schreiben, sondern grössere Aufgaben selbstständig bearbeiten. Was wir heute gelernt haben, nämlich Fehler lesen, Ergebnisse prüfen und Daten verstehen, ist dafür die Voraussetzung.

**Nach dem Unterricht:** Füllt den Reflexionsbogen in `03-nachbearbeitung/` in Ruhe aus. Er fragt auch: *Wo war die KI falsch oder hat etwas erfunden?*

---

## 9. Zusammenfassung des Moduls

| Lektion | Thema | Kernpunkt |
| ------- | ----- | --------- |
| 1 | Textdateien | `with open(...)`, `split`, `float`, Schreiben mit `"w"` |
| 2 | CSV | `DictReader`/`DictWriter`, Zahlen aus Text umwandeln |
| 3 | JSON & API | `json.dump`/`load`, `requests.get`, `raise_for_status` |
| 4 | Fehlerbehandlung | Gezielt abfangen, nie verschlucken, speziell zuerst |

Der rote Faden durch den Abend: Daten kommen **unsauber** an (Text, kaputte Zeilen, ausgefallene APIs). Wer sie liest, prüft und Fehler meldet, schreibt stabile Skripte.

---

## Hinweise für die Dozentin / den Dozenten

- **Streichreihenfolge L4 (bei Zeitnot):**
  1. Kür/Puffer entfällt (7 Minuten).
  2. Teil 2 der Übung (API-Fehler) wird zur reinen Demo, Teil 1 (CSV) bleibt Pflicht.
  3. `try/except` (Abschnitt 3) und die Feedback-Runde bleiben immer.
- **Feedback:** Wer nichts sagen möchte, darf pass sagen. Notieren Sie «unklar»-Antworten für den Start von Modul 4.
- **Typische Stolpersteine:** `except ValueError` zu weit oben im `try`-Block (fängt zu viel), `else` vergessen, `line_num` mit der Zeilennummer im Editor verwechseln (die Kopfzeile ist Zeile 1).
- **Ohne Netz oder bei API-Ausfall:** `OFFLINE = True` in `start.py` verwendet `beispiel_fehler.json`. Dasselbe Verhalten, andere Quelle.
- Musterlösung: `05-beispiele/lektion-4/loesung.py` (läuft mit `OFFLINE = True` immer gleich) nach der Übung freigeben.

---

**Zurück:** [Lektion 3](./lektion-3-json-api.md) · [Modul 3](../README.md) · **Weiter:** [Modul 4: Agentic Coding](../../modul-4-agentic-coding/)
