#!/usr/bin/env python3
"""
Lektion 2: Eingaben, Typumwandlung & Bedingungen – Demo-Code
"""

# =============================================================================
# 1. input() – immer str!
# =============================================================================

print("=== input() Grundlagen ===")
name = input("Wie heisst du? ")           # → str
alter_str = input("Wie alt bist du? ")  # → str (auch bei Zähleingabe!)
print(f"Typ von alter_str: {type(alter_str)}")
print(f"Du heisst {name} und dein Alter als Text: {alter_str}")

# =============================================================================
# 2. Typumwandlung (Casting) mit Fehlerbehandlung
# =============================================================================

print("\n=== Typumwandlung ===")

# Sicher: try/except
def sicher_int(eingabe: str) -> int | None:
    """Versucht String in int umzuwandeln. Gibt None bei Fehler."""
    try:
        return int(eingabe)
    except ValueError:
        return None

def sicher_float(eingabe: str) -> float | None:
    """Versucht String in float umzuwandeln. Gibt None bei Fehler."""
    try:
        return float(eingabe)
    except ValueError:
        return None

# Test
testwerte = ["42", "3.14", "abc", "-7", "0"]
for wert in testwerte:
    print(f"'{wert}' → int: {sicher_int(wert)}, float: {sicher_float(wert)}")

# =============================================================================
# 3. Vergleichsoperatoren
# =============================================================================

print("\n=== Vergleichsoperatoren ===")
alter = 20
print(f"alter = {alter}")
print(f"alter >= 18: {alter >= 18}")   # Volljährig?
print(f"alter < 18:  {alter < 18}")    # Minderjährig?
print(f"alter == 18: {alter == 18}")   # Genau 18?
print(f"alter != 18: {alter != 18}")   # Nicht 18?

# =============================================================================
# 4. Logische Operatoren
# =============================================================================

print("\n=== Logische Operatoren ===")
hat_ausweis = True
ist_mued = False

print(f"hat_ausweis = {hat_ausweis}, ist_mued = {ist_mued}")
print(f"hat_ausweis and not ist_mued: {hat_ausweis and not ist_mued}")  # Darf fahren
print(f"hat_ausweis or ist_mued:    {hat_ausweis or ist_mued}")         # Mindestens eins
print(f"not hat_ausweis:            {not hat_ausweis}")                 # Kein Ausweis

# Kurzschluss-Auswertung
print("\nKurzschluss:")
x = 10
print(f"x > 5 and print('ausgeführt')  → ", end="")
x > 5 and print("ausgeführt")
print(f"x < 5 and print('nicht ausgeführt') → ", end="")
x < 5 and print("nicht ausgeführt")

# =============================================================================
# 5. if / elif / else
# =============================================================================

print("\n=== if / elif / else ===")

# Einfache Verzweigung
note = 5.5
if note >= 4.0:
    print("Bestanden")
else:
    print("Nicht bestanden")

# Mehrfach-Verzweigung
note = 5.5
if note >= 5.5:
    bewertung = "Sehr gut"
elif note >= 4.5:
    bewertung = "Gut"
elif note >= 4.0:
    bewertung = "Genügend"
else:
    bewertung = "Ungenügend"
print(f"Note {note} → {bewertung}")

# Ternärer Operator (inline-if)
status = "Volljährig" if alter >= 18 else "Minderjährig"
print(f"Alter {alter} → {status}")

# =============================================================================
# 6. Praktisches Beispiel: BMI-Rechner
# =============================================================================

print("\n=== BMI-Rechner ===")

def bmi_berechnen(gewicht: float, groesse: float) -> float:
    """Berechnet BMI aus Gewicht (kg) und Grösse (m)."""
    return gewicht / (groesse ** 2)

def bmi_kategorie(bmi: float) -> str:
    """Gibt BMI-Kategorie zurück."""
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"

# Eingabe mit Validierung
gewicht_str = input("Gewicht (kg): ")
groesse_str = input("Grösse (m): ")

gewicht = sicher_float(gewicht_str)
groesse = sicher_float(groesse_str)

if gewicht is not None and groesse is not None and groesse > 0:
    bmi = bmi_berechnen(gewicht, groesse)
    kategorie = bmi_kategorie(bmi)
    print(f"BMI: {bmi:.1f} – {kategorie}")
else:
    print("Ungültige Eingabe! Bitte Zahlen > 0 eingeben.")

# =============================================================================
# 7. Beispiel: Einfacher Taschenrechner
# =============================================================================

print("\n=== Taschenrechner ===")

def rechne(a: float, op: str, b: float) -> float | None:
    """Führt Berechnung durch. None bei Fehler."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            print("Fehler: Division durch 0!")
            return None
        return a / b
    else:
        print(f"Unbekannter Operator: {op}")
        return None

# Interaktiv
a_str = input("Zahl 1: ")
op = input("Operator (+, -, *, /): ")
b_str = input("Zahl 2: ")

a = sicher_float(a_str)
b = sicher_float(b_str)

if a is not None and b is not None:
    ergebnis = rechne(a, op, b)
    if ergebnis is not None:
        print(f"Ergebnis: {ergebnis}")


if __name__ == "__main__":
    pass