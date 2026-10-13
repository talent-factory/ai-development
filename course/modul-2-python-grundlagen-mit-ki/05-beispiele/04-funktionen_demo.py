#!/usr/bin/env python3
"""
Lektion 4: Funktionen – Definieren, Parameter, Rückgabe, Docstrings – Demo-Code
"""

from typing import List, Tuple, Optional

# =============================================================================
# 1. Grundlagen: def, Parameter, return
# =============================================================================

print("=== Funktions-Grundlagen ===")

def quadrat(zahl: float) -> float:
    """Berechnet das Quadrat einer Zahl.
    
    Args:
        zahl: Die zu quadrierende Zahl.
    
    Returns:
        Das Quadrat (zahl * zahl).
    """
    return zahl * zahl

# Aufruf
print(f"quadrat(5) = {quadrat(5)}")
print(f"quadrat(3.5) = {quadrat(3.5)}")

# =============================================================================
# 2. Parameter-Varianten
# =============================================================================

print("\n=== Parameter-Varianten ===")

# Default-Parameter
def begruesse(name: str, gruesswort: str = "Hallo") -> None:
    """Gibt Gruss aus."""
    print(f"{gruesswort}, {name}!")

begruesse("Alex")              # Hallo, Alex!
begruesse("Sam", "Hi")         # Hi, Sam!
begruesse(gruesswort="Hey", name="Pat")  # Hey, Pat! (Keyword-Args)

# *args – beliebig viele Positions-Argumente
def summe(*zahlen: float) -> float:
    """Summiert alle übergebenen Zahlen."""
    return sum(zahlen)

print(f"summe(1, 2, 3) = {summe(1, 2, 3)}")
print(f"summe(10, 20, 30, 40) = {summe(10, 20, 30, 40)}")

# **kwargs – beliebig viele Keyword-Argumente
def profil(**infos: str) -> None:
    """Gibt Profil-Informationen aus."""
    for k, v in infos.items():
        print(f"  {k}: {v}")

profil(name="Alex", alter="25", ort="Zürich", hobby="Python")

# Kombiniert
def flexibel(pflicht: str, default: int = 1, *args, key_only: str, **kwargs) -> None:
    print(f"pflicht={pflicht}, default={default}, args={args}, key_only={key_only}, kwargs={kwargs}")

flexibel("muss", 2, "extra1", "extra2", key_only="nur_keyword", extra="value")

# =============================================================================
# 3. Rückgabewerte
# =============================================================================

print("\n=== Rückgabewerte ===")

# Ein Wert
def add(a: float, b: float) -> float:
    return a + b

# Mehrere Werte → Tupel
def min_max(zahlen: List[float]) -> Tuple[float, float]:
    """Gibt (Minimum, Maximum) zurück."""
    return min(zahlen), max(zahlen)

daten = [3, 1, 4, 1, 5, 9, 2]
klein, gross = min_max(daten)
print(f"Daten: {daten}")
print(f"Min: {klein}, Max: {gross}")

# Kein return → None
def nur_drucken(text: str) -> None:
    print(text)

ergebnis = nur_drucken("Test")
print(f"Rückgabe von nur_drucken: {ergebnis}")  # None

# Guard Clauses (früher Return)
def teile(a: float, b: float) -> Optional[float]:
    """Teilt a durch b. None bei Division durch 0."""
    if b == 0:
        return None
    return a / b

print(f"teile(10, 2) = {teile(10, 2)}")
print(f"teile(10, 0) = {teile(10, 0)}")

# =============================================================================
# 4. Docstrings & help()
# =============================================================================

print("\n=== Docstrings ===")

def bmi_rechner(gewicht: float, groesse: float) -> float:
    """Berechnet den Body-Mass-Index (BMI).
    
    Formel: BMI = Gewicht (kg) / Grösse (m)²
    
    Args:
        gewicht: Körpergewicht in Kilogramm (> 0).
        groesse: Körpergrösse in Metern (> 0).
    
    Returns:
        BMI-Wert als float.
    
    Raises:
        ValueError: Wenn gewicht <= 0 oder groesse <= 0.
    
    Example:
        >>> bmi_rechner(70, 1.75)
        22.857...
    """
    if gewicht <= 0 or groesse <= 0:
        raise ValueError("Gewicht und Grösse müssen positiv sein.")
    return gewicht / (groesse ** 2)

# Docstring anzeigen
print(bmi_rechner.__doc__)
print("\n--- help(bmi_rechner) ---")
help(bmi_rechner)

# =============================================================================
# 5. Typ-Hinweise (Type Hints)
# =============================================================================

print("\n=== Typ-Hinweise ===")

from typing import List, Dict, Optional, Union

# Moderne Syntax (Python 3.10+)
def moderne_funktion(wert: int | float) -> str | None:
    if wert > 0:
        return "positiv"
    return None

# Kompatible Syntax (Python 3.9+)
def kompatibel(wert: Union[int, float]) -> Optional[str]:
    if wert > 0:
        return "positiv"
    return None

# Container-Typen
def verarbeite_liste(zahlen: List[int]) -> Dict[str, float]:
    """Gibt Statistiken zurück."""
    if not zahlen:
        return {"count": 0, "avg": 0.0}
    return {
        "count": float(len(zahlen)),
        "avg": sum(zahlen) / len(zahlen)
    }

print(f"verarbeite_liste([1,2,3,4,5]) = {verarbeite_liste([1, 2, 3, 4, 5])}")
print(f"verarbeite_liste([]) = {verarbeite_liste([])}")

# =============================================================================
# 6. Scoping (Gültigkeitsbereiche)
# =============================================================================

print("\n=== Scoping ===")

global_var = "global"

def outer():
    outer_var = "outer"
    
    def inner():
        nonlocal outer_var
        outer_var = "changed by inner"
        global global_var
        global_var = "changed by inner (global)"
        print(f"  inner: outer_var = {outer_var}")
    
    print(f"  outer vor inner: {outer_var}")
    inner()
    print(f"  outer nach inner: {outer_var}")

print(f"global vor outer: {global_var}")
outer()
print(f"global nach outer: {global_var}")

# =============================================================================
# 7. Lambda-Funktionen
# =============================================================================

print("\n=== Lambda-Funktionen ===")

quadrat_lambda = lambda x: x * x
print(f"quadrat_lambda(7) = {quadrat_lambda(7)}")

# Bei Higher-Order Functions
zahlen = [1, 2, 3, 4, 5]
quadrate = list(map(lambda x: x ** 2, zahlen))
gerade = list(filter(lambda x: x % 2 == 0, zahlen))
print(f"quadrate: {quadrate}")
print(f"gerade: {gerade}")

# Sortieren mit Key
punkte = [("Alex", 10), ("Sam", 5), ("Pat", 15)]
punkte.sort(key=lambda p: p[1])  # Nach Punkten sortieren
print(f"sortiert nach Punkten: {punkte}")

# =============================================================================
# 8. Praktisches Beispiel: Modularer Taschenrechner
# =============================================================================

print("\n=== Modularer Taschenrechner ===")

def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> Optional[float]:
    if b == 0:
        print("Fehler: Division durch 0!")
        return None
    return a / b

# Operationen als Dictionary (Dispatcher-Pattern)
OPERATIONEN = {
    "1": ("Addition", "+", add),
    "2": ("Subtraktion", "-", sub),
    "3": ("Multiplikation", "*", mul),
    "4": ("Division", "/", div),
}

def zeige_menue() -> None:
    print("\n=== TASCHENRECHNER ===")
    for key, (name, symbol, _) in OPERATIONEN.items():
        print(f"  {key}. {name} ({symbol})")
    print("  5. Beenden")

def zahl_einlesen(prompt: str) -> Optional[float]:
    try:
        return float(input(prompt))
    except ValueError:
        print("Ungültige Zahl!")
        return None

def main() -> None:
    while True:
        zeige_menue()
        wahl = input("Wahl (1-5): ").strip()
        
        if wahl == "5":
            print("Auf Wiedersehen!")
            break
        
        if wahl not in OPERATIONEN:
            print("Ungültige Wahl!")
            continue
        
        name, symbol, func = OPERATIONEN[wahl]
        
        a = zahl_einlesen("Zahl 1: ")
        if a is None:
            continue
        b = zahl_einlesen("Zahl 2: ")
        if b is None:
            continue
        
        ergebnis = func(a, b)
        if ergebnis is not None:
            print(f"Ergebnis: {a} {symbol} {b} = {ergebnis}")

# =============================================================================
# 9. Beispiel: Text-Analyse
# =============================================================================

print("\n=== Text-Analyse ===")

from collections import Counter

def analysiere_text(text: str) -> dict:
    """Analysiert Text und gibt Statistiken zurück."""
    woerter = text.split()
    saetze = text.count(".") + text.count("!") + text.count("?")
    haeufig = Counter(w.lower().strip(".,!?") for w in woerter)
    
    return {
        "zeichen_gesamt": len(text),
        "zeichen_ohne_leerzeichen": len(text.replace(" ", "")),
        "woerter": len(woerter),
        "saetze": saetze,
        "haeufigste_woerter": haeufig.most_common(3)
    }

beispiel = "Python ist toll! Python macht Spass. Programmieren mit Python ist super."
ergebnis = analysiere_text(beispiel)
for k, v in ergebnis.items():
    print(f"  {k}: {v}")

# =============================================================================
# 10. Best Practices Zusammenfassung
# =============================================================================

print("\n=== Best Practices ===")
print("""
1. EINE Aufgabe pro Funktion
2. Max. 3-4 Parameter (sonst Dataclass/Objekt)
3. KEINE mutable Defaults: def f(x=[]) → def f(x=None): if x is None: x = []
4. Typ-Hinweise + Google-Docstring für jede öffentliche Funktion
5. Guard Clauses: if not valid: return early
6. if __name__ == "__main__": main() – importierbar ohne Ausführung
7. Funktionen kurz halten (< 20 Zeilen ideal)
8. Sprechende Namen: berechne_bmi() statt calc()
""")

# Demo-Aufruf (nur bei direktem Start)
if __name__ == "__main__":
    # main()  # Entkommentieren für interaktiven Taschenrechner
    pass