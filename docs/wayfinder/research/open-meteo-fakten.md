# Open-Meteo-API: Fakten für Modul 3 (Lektion 3 und 4)

Stand: 2026-10-20. Ticket: `.wayfinder/modul-3/tickets/02-open-meteo-fakten.md`.
Quellen: https://open-meteo.com/en/docs, /en/terms, /en/licence (Primärquellen) sowie echte Testaufrufe mit curl und urllib am 2026-10-20.
Kennzeichnung: **[Doku]** aus Primärdokumentation, **[Test]** selbst per Aufruf geprüft.

## 1. Endpoint und minimale Parameter

- Endpoint **[Doku]**: `https://api.open-meteo.com/v1/forecast`. Kein API-Key nötig (`apikey` ist nur für kommerzielle Nutzung).
- Pflicht: `latitude`, `longitude`. Für `daily` ist `timezone` Pflicht **[Doku]**.
- `current=temperature_2m,weather_code,wind_speed_10m` liefert den aktuellen Wert, `daily=temperature_2m_max,temperature_2m_min,precipitation_sum` die Tageswerte.
- `timezone=Europe/Zurich` (URL-kodiert `Europe%2FZurich`), `forecast_days` 0-16, Default 7 **[Doku]**.
- Mehrere Orte: Kommaliste in `latitude`/`longitude`, Antwort wird dann eine JSON-Liste **[Doku, Test]**.

Koordinaten (WGS84; Open-Meteo gibt die Mitte der Gitterzelle zurück, Abweichung ist normal):

| Stadt | latitude | longitude | Antwort-Koordinaten **[Test]** | Höhe (m) |
|---|---|---|---|---|
| Zürich | 47.3769 | 8.5417 | 47.376667 / 8.543693 | 409 |
| Bern | 46.9481 | 7.4474 | 46.951378 / 7.4586725 | 554 |
| Genf | 46.2044 | 6.1432 | 46.203693 / 6.145807 | 368 |
| Basel | 47.5584 | 7.5733 | 47.55629 / 7.5667233 | 283 |
| Lugano | 46.0037 | 8.9511 | 45.99724 / 8.945581 | 286 |

(Stadtkoordinaten sind gerundete Allgemeinwerte, keine Primärquelle von Open-Meteo.)

Einzelaufruf:

```
curl "https://api.open-meteo.com/v1/forecast?latitude=47.3769&longitude=8.5417&current=temperature_2m,weather_code,wind_speed_10m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FZurich&forecast_days=3"
```

Alle fünf Städte in einem Request (Test: HTTP 200, Liste mit 5 Objekten, Reihenfolge wie die Koordinaten):

```
...forecast?latitude=47.3769,46.9481,46.2044,47.5584,46.0037&longitude=8.5417,7.4474,6.1432,7.5733,8.9511&current=temperature_2m&timezone=Europe%2FZurich
```

Tipp für Anfänger: `requests.get(url, params={...})` bzw. `urllib.parse.urlencode` kodiert das `/` selbst.

## 2. Antwortformat (echte Antwort, Zürich, 2026-10-20 09:15 Ortszeit)

Header **[Test]**: `HTTP/1.1 200 OK`, `Content-Type: application/json; charset=utf-8`.

```json
{
  "latitude": 47.376667, "longitude": 8.543693,
  "generationtime_ms": 0.31375885009765625,
  "utc_offset_seconds": 7200,
  "timezone": "Europe/Zurich", "timezone_abbreviation": "GMT+2",
  "elevation": 409.0,
  "current_units": {"time": "iso8601", "interval": "seconds", "temperature_2m": "°C", "weather_code": "wmo code", "wind_speed_10m": "km/h"},
  "current": {"time": "2026-10-20T09:15", "interval": 900, "temperature_2m": 10.8, "weather_code": 3, "wind_speed_10m": 4.2},
  "daily_units": {"time": "iso8601", "temperature_2m_max": "°C", "temperature_2m_min": "°C", "precipitation_sum": "mm"},
  "daily": {
    "time": ["2026-10-20", "2026-10-21", "2026-10-22"],
    "temperature_2m_max": [17.5, 12.4, 14.0],
    "temperature_2m_min": [10.6, 9.1, 7.3],
    "precipitation_sum": [0.00, 15.70, 0.00]
  }
}
```

Hinweise für den Unterricht:

- `daily` ist ein Dict von **parallelen Listen** (Index i gehört zu `time[i]`), nicht eine Liste von Objekten. Gut für `zip(...)`.
- Einheiten stehen in `*_units`. Default: °C, km/h, mm **[Doku]**.
- `weather_code` ist ein numerischer WMO-Code, Klartext muss selbst gemappt werden **[Doku]**: 0 klar, 1 überwiegend klar, 2 teils bewölkt, 3 bedeckt, 45/48 Nebel, 51-55 Niesel, 61-65 Regen, 71-75 Schnee, 80-82 Schauer, 95 Gewitter, 96/99 Gewitter mit Hagel (nur bei bestimmten Modellen).
- Zeitstempel in `current.time` sind lokale Zeit ohne Offset (bei `timezone=Europe/Zurich`). Der UTC-Offset wird zum Anfragezeitpunkt fixiert **[Doku]**.
- Bei mehreren Orten ist die Antwort eine **Liste** von obigen Objekten (`type == list`, Länge 5 **[Test]**). Achtung: Struktur unterscheidet sich vom Einzelaufruf (Dict).
- `current` wird in 15-Minuten-Intervallen aktualisiert (`interval: 900`).

## 3. Rate-Limits und Lizenz

Limits der kostenlosen, nicht-kommerziellen Nutzung **[Doku, /en/terms]**: "Less than 10'000 API calls per day, 5'000 per hour and 600 per minute" (Monatswert in der Tabelle: 300'000). Zählung "per IP address and application".

Nutzungsbedingung **[Doku]**: Gratis-API nur für nicht-kommerzielle Zwecke. Als nicht-kommerziell genannt sind u. a. "educational content" und öffentliche Forschung an öffentlichen Institutionen. Open-Meteo behält sich vor, missbräuchliche Anwendungen/IPs ohne Vorwarnung zu blocken; keine Garantie für Verfügbarkeit oder Genauigkeit.

Realismus für ca. 20 Studierende im selben Netz: **ja**. Alle teilen sich vermutlich eine öffentliche IP (NAT). Selbst wenn jede Person 10 Aufrufe pro Minute macht, sind das 200/min (Limit 600/min), und 5'000/h sind bei einer Unterrichtsstunde kaum erreichbar. Risiko entsteht nur bei Schleifen ohne Pause, Retry-Stürmen oder wenn mehrere Kurse am selben Netz laufen. Empfehlung: Fünf Städte in einem Request abfragen oder pro Stadt nur ein Aufruf; Retries mit Pause. **Nicht geprüft**: wie Multi-Location-Requests gezählt werden (ein Aufruf oder fünf) und das genaue Verhalten bei Überschreitung (Statuscode, vermutlich 429). Die Primärseiten /en/docs und /en/licence nennen dazu nichts. Ein 429 wurde nicht provoziert (würde die Klassen-IP gefährden).

Lizenz und Quellenangabe **[Doku, /en/licence]**: Daten unter CC BY 4.0. Pflicht: "appropriate credit, link to the licence, indicate if changes were made". Ein Link muss "next to any location Open-Meteo data are displayed" stehen. Vorgeschlagenes Markup: `<a href="https://open-meteo.com/">Weather data by Open-Meteo.com</a>`. Für Folien/Material reicht entsprechend: "Wetterdaten: Open-Meteo.com (CC BY 4.0)" mit Link. Quellcode von Open-Meteo steht unter AGPLv3 (betrifft den Unterricht nicht). Hinweis: `/en/license` leitet auf `/en/licence` weiter.

## 4. HTTP-Bibliothek im Projekt

Befund aus `/Users/daniel/GitRepository/ai-development/pyproject.toml` und `uv.lock`:

- `requests` und `httpx` sind **nicht** direkt in `[project].dependencies` deklariert.
- Beide sind **transitiv** in `uv.lock` vorhanden (`requests 2.33.1`, z. B. über `google-search-results`; `httpx 0.28.1`, z. B. über `anthropic`/`langchain`) und im Haupt-`.venv` installiert (geprüft: `site-packages` enthält `requests`, `httpx`).
- Im frischen Worktree ohne `.venv` schlug `import requests` fehl; ein `uv sync` im Hauptverzeichnis hat sie.
- `requires-python >= 3.13.1`; lokal Python 3.13.11. `urllib` ist Standardbibliothek und immer da.

Empfehlung: Für Anfänger `requests` (lesbarer, `.json()`, `.raise_for_status()`, `timeout=`), da im Projekt-venv verfügbar. Risiko: Es ist nur transitiv; falls Studierende eine eigene Umgebung bauen, vorher `uv add requests` (oder in pyproject.toml aufnehmen). Als Fallback funktioniert `urllib.request` + `json` ohne Installation.

## 5. Fehlerfälle (echte Antworten, [Test])

Open-Meteo-Fehler sind **HTTP 400** mit JSON `{"error": true, "reason": "..."}` **[Doku, Test]**. Die Schlüsselreihenfolge variiert (curl vs. urllib lieferten `error` bzw. `reason` zuerst).

| Fall | Aufruf (Kurzform) | Ergebnis |
|---|---|---|
| Breitengrad ungültig | `latitude=999&longitude=8.5&current=temperature_2m` | `400` `{"error":true,"reason":"Latitude must be in range of -90 to 90°. Given: 999.0."}` |
| Längengrad fehlt | `latitude=47.37&current=temperature_2m` | `400` `{"error":true,"reason":"Parameter 'latitude' and 'longitude' must have the same number of elements"}` |
| Unbekannte Variable | `current=foo` | `400` `{"error":true,"reason":"Invalid value: Cannot initialize SurfacePressureAndHeightVariable<...> from invalid St...` (lange, interne Meldung, für Anfänger kaum lesbar; hier abgeschnitten) |
| Ungültige Zeitzone | `timezone=Mars/Base` | `400` `{"error":true,"reason":"Invalid timezone"}` |
| Offline / DNS-Fehler | Host `api.open-meteo.invalid` | curl: Exit 6. urllib: `URLError` mit `reason` = `gaierror [Errno 8] nodename nor servname provided, or not known` |
| Timeout | `timeout=0.001` | curl: Exit 28. urllib: `URLError: <urlopen error timed out>` |

Python-Verhalten für Lektion 4:

- **[Test, urllib]** HTTP 400 löst `urllib.error.HTTPError` aus; Body lesbar mit `e.read().decode()`, Code in `e.code`.
- **[Test, urllib]** Offline und Timeout sind beide `URLError` (Unterscheidung über `e.reason`). `HTTPError` ist Unterklasse von `URLError`, die `except`-Reihenfolge ist also wichtig (Lehrstoff).
- **[nicht ausgeführt, requests-Standardverhalten]** `requests` wirft bei 400 nicht automatisch; erst `response.raise_for_status()` wirft `requests.HTTPError`, der JSON-Body mit `reason` bleibt über `response.json()` lesbar. Weitere Klassen: `requests.exceptions.ConnectionError`, `requests.exceptions.Timeout`. Im Worktree war requests nicht installiert; vor der Lektion kurz im Projekt-venv verifizieren.
- Ohne `timeout=` wartet `requests` unbegrenzt: immer `timeout` setzen (Lehrpunkt).
- Gutes Lektion-4-Muster: `reason` aus dem 400-Body an Benutzer ausgeben statt nur "Fehler".
- Zum Offline-Testen im Raum: Hostnamen verfälschen (`.invalid` ist reserviert und löst nie auf) oder WLAN aus; kein echter Netzausfall nötig.

## Offene Risiken

1. Netz am Abend: Ein Live-Ausfall von api.open-meteo.com oder eine gesperrte Klassen-IP trifft alle gleichzeitig. Fallback: obige JSON-Antwort als lokale Datei (z. B. `zuerich.json`) bereitstellen.
2. Zählung von Multi-Location-Anfragen und 429-Verhalten nicht verifiziert (siehe 3).
3. `requests` nur transitiv vorhanden, requests-Fehlerklassen nicht live getestet (siehe 4 und 5).
4. Werte (Temperaturen, Datum) im Beispiel sind Momentaufnahmen vom 2026-10-20; im Unterricht ändern sie sich, Folien nicht auf konkrete Zahlen stützen.
5. Quellenangabe in Folien nicht vergessen (CC BY 4.0, Link auf open-meteo.com).
