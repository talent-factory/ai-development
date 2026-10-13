#!/usr/bin/env python3
"""
Lektion 1: Variablen, Datentypen & Operatoren – Demo-Code
"""

# =============================================================================
# 1. Variablen anlegen & Datentypen
# =============================================================================

# Ganze Zahlen (int)
alter = 25
jahr = 2026
temperatur = -10

# Kommazahlen (float)
groesse = 1.78
pi = 3.14159
wissenschaftlich = 1.5e6  # 1.500.000

# Text (str)
name = "Alex"
farbe = 'blau'
mehrzeilig = """Das ist ein
mehrzeiliger
String."""

# Wahrheitswerte (bool)
ist_student = True
hat_fuehrerschein = False

# None (kein Wert)
nichts = None

# Typ anzeigen
print("=== Datentypen ===")
print(f"alter: {alter} → {type(alter)}")
print(f"groesse: {groesse} → {type(groesse)}")
print(f"name: {name} → {type(name)}")
print(f"ist_student: {ist_student} → {type(ist_student)}")
print(f"nichts: {nichts} → {type(nichts)}")

# =============================================================================
# 2. Rechenoperatoren
# =============================================================================

print("\n=== Rechenoperatoren ===")
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")   # Addition
print(f"a - b  = {a - b}")   # Subtraktion
print(f"a * b  = {a * b}")   # Multiplikation
print(f"a / b  = {a / b}")   # Division (immer float!)
print(f"a // b = {a // b}")  # Ganzzahldivision
print(f"a % b  = {a % b}")   # Modulo (Rest)
print(f"a ** b = {a ** b}")  # Potenz

# =============================================================================
# 3. String-Operationen
# =============================================================================

print("\n=== String-Operationen ===")
vorname = "Alex"
nachname = "Mueller"

# Konkatenation
voller_name = vorname + " " + nachname
print(f"Konkatenation: {voller_name}")

# f-Strings (empfohlen)
print(f"f-String: Hallo, {vorname} {nachname}!")

# Formatierung
preis = 19.99
print(f"Preis: {preis:.2f} CHF")        # 2 Nachkommastellen
print(f"Preis: {preis:>10.2f} CHF")     # Rechtsbündig, Breite 10
print(f"Prozent: {0.25:.0%}")           # 25%

# String-Methoden
text = "  Python Rocks!  "
print(f"strip(): '{text.strip()}'")
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.lower()}'")
print(f"replace(): '{text.replace('Python', 'Java')}'")

# =============================================================================
# 4. Vergleichsoperatoren
# =============================================================================

print("\n=== Vergleichsoperatoren ===")
x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y:  {x < y}")
print(f"x > y:  {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# =============================================================================
# 5. Praktisches Beispiel: Kreisberechnung
# =============================================================================

print("\n=== Beispiel: Kreisberechnung ===")
radius = float(input("Radius eingeben: "))  # Eingabe → float
pi = 3.14159

flaeche = pi * radius ** 2
umfang = 2 * pi * radius

print(f"Kreis (r = {radius}):")
print(f"  Fläche = {flaeche:.2f}")
print(f"  Umfang = {umfang:.2f}")

# =============================================================================
# 6. Typumwandlung (Casting) – Vorschau Lektion 2
# =============================================================================

print("\n=== Typumwandlung ===")
zahl_str = "42"
zahl_int = int(zahl_str)
zahl_float = float(zahl_str)

print(f"'{zahl_str}' → int: {zahl_int} ({type(zahl_int)})")
print(f"'{zahl_str}' → float: {zahl_float} ({type(zahl_float)})")

# Fehlerbehandlung (try/except) – kommt in Lektion 2
try:
    int("keine_zahl")
except ValueError as e:
    print(f"Fehler abgefangen: {e}")


if __name__ == "__main__":
    # Dieser Block wird nur ausgeführt, wenn das Script direkt gestartet wird
    # (nicht bei Import)
    pass