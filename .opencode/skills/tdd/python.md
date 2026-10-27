# TDD mit Python: Werkzeuge und Muster

## Setup

- `pytest` ist Standard, nicht `unittest`. Ausführung: `uv run pytest`.
- Tests als flache Funktionen, keine `TestCase`-Klassen.
- Layout: `tests/` neben `src/`, Dateien `test_<modul>.py`.
- Konfiguration in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers --strict-config -W error"
```

Die Coverage-Konfiguration (Pflicht: 90 %) steht im Abschnitt «Qualität der Suite messen». `pytest-cov` als Dev-Abhängigkeit installieren (`uv add --dev pytest pytest-cov`).

`-W error` macht Warnungen (z. B. Deprecations) zu Fehlern, `--strict-markers` fängt Tippfehler bei Markern ab.

Typisierung: Testfunktionen und Fixtures mit Type Hints versehen. `mypy` oder `pyright` auch über `tests/` laufen lassen.

## Nützliche Kommandos im Zyklus

```bash
uv run pytest tests/test_x.py::test_name   # einzelnen Test (Rot/Grün prüfen)
uv run pytest -x --lf                      # beim ersten Fehler stoppen, zuletzt gescheiterte zuerst
uv run pytest                              # ganze Suite am Ende jedes Durchlaufs
```

## Fixtures

- Klein halten und eine Sache einrichten. Aufräumen per `yield`.
- `conftest.py` nur für wirklich geteilte Fixtures. Alles andere neben dem Test.
- Eingebaute Fixtures nutzen: `tmp_path` (Dateien), `monkeypatch` (Env, Attribute), `capsys` (Ausgabe), `caplog` (Logging).

```python
@pytest.fixture
def zahlungs_fake() -> FakeZahlungsdienst:
    return FakeZahlungsdienst()
```

## Parametrisieren

`@pytest.mark.parametrize` mit `ids=` für lesbare Testnamen statt kopierter Tests. Beispiele siehe [tests.md](tests.md).

## Testdaten

Kleine Builder-Funktionen oder `polyfactory` statt langer Literal-Blöcke in jedem Test. Nur die Felder angeben, die für das Verhalten relevant sind:

```python
def bestellung(**felder) -> Bestellung:
    return Bestellung(**{"kunde": "Alice", "positionen": [BUCH], **felder})
```

## Async

`pytest-asyncio` (mit explizit gesetztem `asyncio_mode`) oder `anyio`. Kein manuelles `asyncio.run` in Tests.

## Property-Based Testing mit Hypothesis

Ergänzt Beispieltests, wenn sich Eigenschaften formulieren lassen (Parser, Berechnungen, Roundtrips). Es ist eine direkte Antwort auf tautologische Tests: Statt den Wert nachzurechnen, wird eine Invariante geprüft.

```python
from hypothesis import given, strategies as st


@given(st.text())
def test_serialisierung_roundtrip(text):
    assert laden(speichern(text)) == text
```

Gefundene Gegenbeispiele als feste Regressionstests mit `@example(...)` festhalten.

## Snapshot-Tests

`syrupy` nur bewusst einsetzen, bei grossen, stabilen Strukturen. Snapshots nie blind mit `--snapshot-update` übernehmen, sonst entsteht ein tautologischer Test.

## Determinismus und Isolation

- Keine Abhängigkeit von Reihenfolge, Uhrzeit, Netzwerk oder globalem Zustand.
- Optional `pytest-randomly`, um Reihenfolgeabhängigkeiten aufzudecken.
- Keine echten Netzwerk-, LLM- oder Zahlungsaufrufe in Tests.

## Qualität der Suite messen

- **Coverage (Pflicht: mindestens 90 %)** mit `pytest-cov`, als Zweigabdeckung gemessen. Die Schwelle steht in `pyproject.toml`, damit `pytest` bei Unterschreitung fehlschlägt:

```toml
[tool.pytest.ini_options]
addopts = "-ra --strict-markers --strict-config -W error --cov --cov-report=term-missing"

[tool.coverage.run]
branch = true
source = ["src"]          # bzw. das Paket oder Verzeichnis der Übung

[tool.coverage.report]
fail_under = 90
show_missing = true
exclude_also = [
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
    "raise NotImplementedError",
    "\\.\\.\\.",              # Protocol-Methodenkörper
]
```

  Im Zyklus: `uv run pytest` zeigt unter «Missing» die ungedeckten Zeilen. Für jede ein Verhalten benennen und dafür einen Test schreiben (Rot, Grün), nicht die Zeile künstlich «anfassen».
  - Ungedeckte `except`-Zweige und Fehlerpfade sind meist echte fehlende Tests (siehe [tests.md](tests.md), Fehlerfälle).
  - `# pragma: no cover` nur für Code, der sich sinnvoll nicht testen lässt (z. B. `main()`-Einstieg), und immer mit kurzer Begründung. Nie, um die Schwelle zu erreichen.
  - Die Schwelle gilt je Projekt bzw. Übung. Soll sie je Datei gelten, nach `coverage json` pro Datei in `files[*].summary.percent_covered` prüfen.
  - Abdeckung ist ein Minimum: Sie zeigt, welcher Code nie ausgeführt wird, nicht ob die Tests etwas prüfen.
- **Mutation Testing** (`mutmut`) zeigt, ob Tests Änderungen am Code tatsächlich bemerken. Stichprobenartig für kritische Module einsetzen.
- Pro Seam mindestens ein Test für Fehler- und Randfälle: leere Eingabe, `None`, Grenzwerte.
