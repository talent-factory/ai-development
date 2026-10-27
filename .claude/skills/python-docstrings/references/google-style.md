# Google-Style-Docstrings (Deutsch)

Referenz zu `SKILL.md`. Grundlage: PEP 257 und der Google Python Style Guide, Abschnitt «Comments and Docstrings».

## Modul

```python
"""Wetterbericht für eine Schweizer Stadt: CSV auswerten, Live-Wetter abrufen, Bericht speichern.

Weather data by Open-Meteo.com (CC BY 4.0).
"""
```

Lizenz- und Quellenhinweise im bestehenden Modul-Docstring bleiben erhalten.

## Funktion

```python
def berechne_durchschnitt(werte: list[float], *, runden: int = 1) -> float:
    """Berechnet den Mittelwert einer Messreihe.

    Args:
        werte: Messwerte, mindestens ein Eintrag.
        runden: Anzahl Nachkommastellen im Ergebnis.

    Returns:
        Der gerundete Mittelwert.

    Raises:
        ValueError: Wenn `werte` leer ist.
    """
```

- Zusammenfassung im Indikativ («Berechnet …», «Lädt …»), nicht im Imperativ und ohne den Funktionsnamen zu wiederholen.
- `Args`: ein Eintrag je Parameter, `*args` und `**kwargs` mit Stern. Standardwerte nur nennen, wenn sie nicht aus der Signatur hervorgehen.
- `Returns` entfällt, wenn die Funktion `None` zurückgibt. Bei Generatoren `Yields` statt `Returns`.
- Mehrere Rückgabewerte (Tupel): jeden Wert beschreiben.

## Klasse

```python
class Messreihe:
    """Eine geordnete Reihe von Temperaturmessungen.

    Attributes:
        stadt: Name der Messstation.
        werte: Messwerte in Grad Celsius, älteste zuerst.
    """
```

`__init__` bekommt keinen eigenen Docstring, die Parameter stehen im Klassen-Docstring (`Args`), wenn sie nicht den Attributen entsprechen.

## Property und dünne Methoden

Properties: eine Zeile, die beschreibt, **was** das Attribut ist («Anzahl Messwerte.»), nicht «Gibt … zurück».
Selbsterklärende Dunder-Methoden (`__repr__`, `__len__`) brauchen keinen Docstring.

## Kommentare

| Gut | Schlecht |
|---|---|
| `# API liefert km/h, intern rechnen wir in m/s` | `# Wert in Variable speichern` |
| `# Open-Meteo erlaubt max. 10 000 Abrufe/Tag` | `# Schleife über alle Städte` |

TODO-Kommentare nicht entfernen und nicht erfinden.

## Häufige Fehler, die zu korrigieren sind

- Typen doppelt im Text: `werte (list[float]): …` → `werte: …`
- Docstring beschreibt altes Verhalten oder nicht mehr vorhandene Parameter.
- `Raises` für Ausnahmen, die nirgends ausgelöst werden.
- Zusammenfassung über mehrere Zeilen oder ohne Punkt.
- Docstring wiederholt den Funktionsnamen: `def lade_csv(): """Lädt CSV."""`
