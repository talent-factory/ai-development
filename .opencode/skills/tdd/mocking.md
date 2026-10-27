# Wann mocken?

Nur an **Systemgrenzen** ersetzen:

- Externe APIs (Zahlung, E-Mail, LLM-Aufrufe usw.)
- Datenbanken (meist besser eine echte Test-DB: SQLite in-memory oder `testcontainers`)
- Zeit und Zufall
- Dateisystem: meist **nicht** mocken, sondern die Fixture `tmp_path` verwenden

Nicht mocken:

- Eigene Klassen und Module
- Interne Kollaborateure
- Alles, was du selbst kontrollierst

## Fakes vor Mocks

Ein **Fake** ist eine kleine, funktionierende Ersatz-Implementierung (z. B. In-Memory). Er ersetzt die Grenze, ohne Aufrufe zu protokollieren, und prüft dadurch Verhalten statt Interaktion. Mocks mit `assert_called_with` koppeln den Test an die Implementierung.

```python
class FakeZahlungsdienst:
    def __init__(self) -> None:
        self.belastungen: list[Decimal] = []

    def belasten(self, betrag: Decimal) -> Quittung:
        self.belastungen.append(betrag)
        return Quittung(betrag=betrag, status="bezahlt")
```

Auch den Fake nur dort prüfen, wo die Wirkung selbst das Verhalten ist (z. B. «es wurde genau einmal belastet»), nicht den Aufrufweg.

## Für Mockbarkeit entwerfen

**1. Abhängigkeiten injizieren**

Externe Abhängigkeiten werden übergeben, nicht intern erzeugt. Die Schnittstelle wird mit `typing.Protocol` beschrieben, dann ist jeder passende Fake ohne Vererbung austauschbar und der Typchecker prüft ihn.

```python
from typing import Protocol


class Zahlungsdienst(Protocol):
    def belasten(self, betrag: Decimal) -> Quittung: ...


# Leicht testbar
def bezahle(bestellung: Bestellung, dienst: Zahlungsdienst) -> Quittung:
    return dienst.belasten(bestellung.summe)


# Schwer testbar
def bezahle(bestellung: Bestellung) -> Quittung:
    dienst = StripeClient(os.environ["STRIPE_KEY"])
    return dienst.belasten(bestellung.summe)
```

**2. Spezifische Methoden statt generischer Fetcher**

Pro externer Operation eine eigene Methode statt einer generischen mit Fallunterscheidung:

```python
# GUT: jede Methode ist einzeln ersetzbar
class ApiClient(Protocol):
    def benutzer_holen(self, benutzer_id: int) -> Benutzer: ...
    def bestellungen_holen(self, benutzer_id: int) -> list[Bestellung]: ...
    def bestellung_anlegen(self, daten: BestellDaten) -> Bestellung: ...


# SCHLECHT: der Ersatz braucht Fallunterscheidungen
class ApiClient(Protocol):
    def anfrage(self, pfad: str, **optionen) -> dict: ...
```

Vorteile:

- Jeder Ersatz liefert genau eine Form
- Keine Fallunterscheidung im Test-Setup
- Man sieht, welche Endpunkte ein Test nutzt
- Typsicherheit pro Endpunkt

## Wenn doch gemockt wird

- **`autospec` verwenden**: `mocker.patch("modul.funktion", autospec=True)` oder `create_autospec(Klasse, spec_set=True)`. Ein blankes `MagicMock` akzeptiert jeden Tippfehler und jede falsche Signatur stillschweigend.
- **Dort patchen, wo nachgeschlagen wird**: `patch("meinmodul.requests.get")`, nicht `patch("requests.get")`.
- **Möglichst `monkeypatch`** für Umgebungsvariablen und einfache Attribute: `monkeypatch.setenv("API_KEY", "test")`.

## Werkzeuge an Systemgrenzen

| Grenze | Werkzeug |
|---|---|
| HTTP (`httpx`) | `respx` |
| HTTP (`requests`) | `responses` |
| Zeit | `time-machine` (schneller und robuster als `freezegun`), oder `Clock` injizieren |
| Zufall | `random.Random(seed)` injizieren |
| Datenbank | SQLite in-memory oder `testcontainers` |
| Dateisystem | `tmp_path` |
| LLM-API | Client als `Protocol` injizieren, Fake mit festen Antworten. Nie echte API-Aufrufe im Test |
