# Lektion 4: Funktionen – Definieren, Parameter, Rückgabe, Docstrings

**Dauer:** 50 Minuten  
**Ziel:** Wiederverwendbare Bausteine bauen, Parameter & Rückgaben nutzen, KI als Code-Reviewer einsetzen.

---

## 1. Warum Funktionen?

- **DRY** – Don't Repeat Yourself
- **Lesbarkeit** – Namen erklären *was*, Code zeigt *wie*
- **Testbarkeit** – Kleine Einheiten isoliert prüfbar
- **Wiederverwendung** – Einmal schreiben, oft nutzen

---

## 2. Anatomie einer Funktion

```python
def quadrat(zahl: float) -> float:
    """Berechnet das Quadrat einer Zahl.
    
    Args:
        zahl: Die zu quadrierende Zahl.
    
    Returns:
        Das Quadrat (zahl * zahl).
    """
    return zahl * zahl


# Aufruf
ergebnis = quadrat(5)   # 25
print(quadrat(3.5))     # 12.25
```

**Bestandteile:**
| Teil | Beispiel | Pflicht? |
|------|----------|----------|
| `def` | `def quadrat(` | Ja |
| Name | `quadrat` | Ja |
| Parameter | `(zahl: float)` | Nein (kann leer sein) |
| Typ-Hinweis Parameter | `: float` | Nein (empfohlen) |
| `->` Rückgabetyp | `-> float` | Nein (empfohlen) |
| Docstring | `"""..."""` | Nein (empfohlen) |
| Körper | `return zahl * zahl` | Ja |
| `return` | `return ergebnis` | Nein (ohne → `None`) |

---

## 3. Parameter & Argumente

### Positions-Parameter
```python
def begruesse(name, gruesswort="Hallo"):
    print(f"{gruesswort}, {name}!")

begruesse("Alex")           # Hallo, Alex!
begruesse("Sam", "Hi")      # Hi, Sam!
begruesse(gruesswort="Hey", name="Pat")  # Hey, Pat! (Keyword-Argumente)
```

### Default-Werte (Standardparameter)
```python
def potenz(basis, exponent=2):
    return basis ** exponent

potenz(3)      # 9  (3²)
potenz(3, 3)   # 27 (3³)
```

**Warnung:** Mutable Defaults (`[]`, `{}`) vermeiden!
```python
# FALSCH – Liste wird geteilt!
def addiere(item, liste=[]):
    liste.append(item)
    return liste

# RICHTIG
def addiere(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

### Beliebig viele Argumente
```python
def summe(*zahlen):           # *args → Tupel
    return sum(zahlen)

def profil(**infos):          # **kwargs → Dict
    for k, v in infos.items():
        print(f"{k}: {v}")

summe(1, 2, 3, 4)             # 10
profil(name="Alex", alter=25, ort="Zürich")
```

---

## 4. Rückgabewerte

### Ein Wert
```python
def add(a, b):
    return a + b
```

### Mehrere Werte (Tupel)
```python
def min_max(zahlen):
    return min(zahlen), max(zahlen)

klein, gross = min_max([3, 1, 4, 1, 5])
print(klein, gross)  # 1 5
```

### Frühzeitiger Return (Guard Clauses)
```python
def teile(a, b):
    if b == 0:
        return None  # oder raise ValueError
    return a / b
```

### Kein `return` → `None`
```python
def drucke(text):
    print(text)

ergebnis = drucke("Hi")  # None
```

---

## 5. Docstrings – Dokumentation & KI-Kontext

```python
def bmi_rechner(gewicht: float, groesse: float) -> float:
    """Berechnet den Body-Mass-Index (BMI).
    
    Formel: BMI = Gewicht (kg) / Grösse (m)²
    
    Args:
        gewicht: Körpergewicht in Kilogramm.
        groesse: Körpergrösse in Metern.
    
    Returns:
        BMI-Wert als float.
    
    Raises:
        ValueError: Wenn gewicht <= 0 oder groesse <= 0.
    
    Example:
        >>> bmi_rechner(70, 1.75)
        22.86
    """
    if gewicht <= 0 or groesse <= 0:
        raise ValueError("Gewicht und Grösse müssen positiv sein.")
    return gewicht / (groesse ** 2)
```

**Abrufen:**
```python
help(bmi_rechner)
print(bmi_rechner.__doc__)
```

---

## 6. Typ-Hinweise (Type Hints) – PEP 484

```python
from typing import List, Tuple, Optional

def verarbeite(daten: List[int]) -> Tuple[int, Optional[float]]:
    """Gibt (Anzahl, Durchschnitt) zurück. Durchschnitt ist None bei leerer Liste."""
    if not daten:
        return 0, None
    return len(daten), sum(daten) / len(daten)
```

**Tools:** `mypy`, `pyright`, VS Code Pylance prüfen Typen statisch.

---

## 7. Praktische Beispiele

### Beispiel 1: Taschenrechner-Funktionen
```python
def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float | None:
    if b == 0:
        print("Fehler: Division durch 0")
        return None
    return a / b


def main():
    print("Taschenrechner")
    a = float(input("Zahl 1: "))
    op = input("Operator (+, -, *, /): ")
    b = float(input("Zahl 2: "))
    
    operationen = {"+": add, "-": sub, "*": mul, "/": div}
    
    if op in operationen:
        ergebnis = operationen[op](a, b)
        if ergebnis is not None:
            print(f"Ergebnis: {ergebnis}")
    else:
        print("Unbekannter Operator")


if __name__ == "__main__":
    main()
```

### Beispiel 2: Text-Analyse
```python
def analysiere_text(text: str) -> dict:
    """Analysiert Text: Zeichen, Wörter, Sätze."""
    return {
        "zeichen": len(text),
        "woerter": len(text.split()),
        "saetze": text.count(".") + text.count("!") + text.count("?"),
        "grossbuchstaben": sum(1 for c in text if c.isupper())
    }

ergebnis = analysiere_text("Hallo Welt! Wie geht's?")
print(ergebnis)
# {'zeichen': 22, 'woerter': 5, 'saetze': 2, 'grossbuchstaben': 2}
```

---

## 8. KI als Code-Reviewer – Prompts

| Prompt | Zweck |
|--------|-------|
| `"Prüfe diese Funktion auf: Typsicherheit, Docstring-Qualität, Edge-Cases."` | Review |
| `"Schreibe einen Docstring im Google-Style für diese Funktion."` | Docstring generieren |
| `"Meine Funktion wirft TypeError bei None. Wie baue ich Guard Clauses ein?"` | Robustheit |
| `"Vergleiche: Früher Return vs. einzelne Return-Anweisung am Ende."` | Style-Diskussion |
| `"Generiere 3 Testfälle für diese Funktion (Happy Path, Edge Case, Error)."` | Test-Ideen |

---

## 9. Mini-Projekt: Taschenrechner mit Menü (20 Min)

**Anforderungen:**
1. Funktionen: `add`, `sub`, `mul`, `div` (mit Zero-Check), `beenden`
2. `main()`-Schleife: Menü anzeigen, Eingabe, Funktion aufrufen, Ergebnis zeigen
3. Typ-Hinweise + Docstrings für alle Funktionen
4. KI-Review: `"Review meinen Taschenrechner-Code."`

**Struktur:**
```python
def add(a: float, b: float) -> float: ...
def sub(a: float, b: float) -> float: ...
def mul(a: float, b: float) -> float: ...
def div(a: float, b: float) -> float | None: ...

def zeige_menue() -> None: ...

def main() -> None:
    while True:
        zeige_menue()
        wahl = input("Wahl: ")
        # ...
```

---

## 10. Häufige Fehler & Lösungen

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| `TypeError: missing 1 required positional argument` | Aufruf ohne Argument | `func(wert)` nicht `func` |
| `UnboundLocalError` | Variable vor `return` nicht gesetzt | Alle Pfade prüfen, Default setzen |
| `None` statt Wert | `return` vergessen oder `print()` statt `return` | `return ergebnis` |
| Rekursion ohne Basis | Endlosrekursion | Basis-Fall (`if n <= 1: return 1`) |
| Mutable Default Argument | `def f(x=[]):` | `def f(x=None): if x is None: x = []` |

---

## 11. Weiterführende Links

- [Python Docs: Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [PEP 484 – Type Hints](https://peps.python.org/pep-0484/)
- [Real Python: Defining Your Own Function](https://realpython.com/defining-your-own-python-function/)

---

## 12. Reflexionsfragen (für Nachbearbeitung)

1. Welche Funktion aus dem Alltag würdest du in Code packen?
2. Was war der Unterschied zwischen `print()` und `return` in der Wirkung?
3. Wie hat das KI-Review deinen Code verbessert (konkrete Änderung)?

---

## 13. Ausblick Modul 3

- Funktionen in **Modulen** auslagern (`import`)
- Daten aus **Dateien** lesen → Funktionen wiederverwenden
- **Fehlerbehandlung** mit `try/except` vertiefen
- **Typ-Hinweise** mit `mypy` prüfen

---

*Datei: `01-praxis/lektion-4-funktionen.md`*  
*Zugehöriges Beispiel: `05-beispiele/04-funktionen_demo.py`*  
*Übung: `02-uebungen/ex-03-funktionen.adoc`*  
*Nachbearbeitung: `03-nachbearbeitung/reflexionsbogen.md`*