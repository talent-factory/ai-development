#!/usr/bin/env python3
"""
Lektion 3: Schleifen – while, for, range() – Demo-Code
"""

import random

# =============================================================================
# 1. while-Schleife
# =============================================================================

print("=== while-Schleife ===")

# Countdown
print("Countdown:")
n = 5
while n > 0:
    print(f"  {n}")
    n -= 1
print("  Start!")

# Eingabe-Schleife mit Sentinel
print("\nEingabe bis 'quit':")
# while True:
#     cmd = input("> ")
#     if cmd == "quit":
#         break
#     print(f"  Echo: {cmd}")

# Demo ohne Blockierung:
demo_eingaben = ["hallo", "welt", "quit"]
for cmd in demo_eingaben:
    if cmd == "quit":
        print("  Beendet")
        break
    print(f"  Echo: {cmd}")

# =============================================================================
# 2. for-Schleife mit range()
# =============================================================================

print("\n=== for mit range() ===")

print("range(5):")
for i in range(5):
    print(f"  {i}", end=" ")
print()

print("range(1, 6):")
for i in range(1, 6):
    print(f"  {i}", end=" ")
print()

print("range(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}", end=" ")
print()

print("range(5, 0, -1) – Countdown:")
for i in range(5, 0, -1):
    print(f"  {i}", end=" ")
print()

# =============================================================================
# 3. for über Sequenzen
# =============================================================================

print("\n=== for über Sequenzen ===")

farben = ["rot", "grün", "blau", "gelb"]
print("Liste:")
for farbe in farben:
    print(f"  {farbe}")

print("\nString:")
for buchstabe in "Python":
    print(f"  {buchstabe}", end=" ")
print()

print("\nenumerate() – mit Index:")
for idx, farbe in enumerate(farben):
    print(f"  {idx}: {farbe}")

print("\nenumerate(start=1):")
for idx, farbe in enumerate(farben, start=1):
    print(f"  {idx}. {farbe}")

# =============================================================================
# 4. break & continue
# =============================================================================

print("\n=== break & continue ===")

print("break bei 5:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}", end=" ")
print()

print("continue – überspringt gerade Zahlen:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"  {i}", end=" ")
print()

print("else-Block (kein break):")
for i in range(3):
    print(f"  {i}", end=" ")
else:
    print("→ fertig ohne break")
print()

print("else-Block (mit break):")
for i in range(3):
    if i == 1:
        break
    print(f"  {i}", end=" ")
else:
    print("→ fertig ohne break")
print("→ fertig MIT break (else nicht ausgeführt)")

# =============================================================================
# 5. Verschachtelte Schleifen
# =============================================================================

print("\n=== Verschachtelte Schleifen: Multiplikationstabelle ===")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end="")
    print()

# =============================================================================
# 6. Praktisches Beispiel: Zahlenraten-Spiel
# =============================================================================

print("\n=== Zahlenraten-Spiel ===")

def zahlenraten(max_zahl: int = 100) -> int:
    """Spielt eine Runde Zahlenraten. Gibt Anzahl Versuche zurück."""
    geheim = random.randint(1, max_zahl)
    versuche = 0
    geraten = False
    
    print(f"Rate die Zahl zwischen 1 und {max_zahl}!")
    
    while not geraten:
        versuche += 1
        # Demo: simulierte Eingaben
        if versuche == 1:
            tipp = geheim // 2
        elif versuche == 2:
            tipp = geheim + 10
        else:
            tipp = geheim
        
        print(f"  Versuch {versuche}: {tipp}")
        
        if tipp < geheim:
            print("  → Zu klein!")
        elif tipp > geheim:
            print("  → Zu gross!")
        else:
            print(f"  → Richtig! Versuche: {versuche}")
            geraten = True
    
    return versuche

# Demo-Runde
versuche = zahlenraten(50)

# =============================================================================
# 7. Beispiel: Summe 1 bis n (Gauß)
# =============================================================================

print("\n=== Summe 1 bis n ===")

n = 100

# Mit for-Schleife
summe_for = 0
for i in range(1, n + 1):
    summe_for += i

# Gauß-Formel
summe_gauss = n * (n + 1) // 2

print(f"Schleife: 1+2+...+{n} = {summe_for}")
print(f"Gauß:     1+2+...+{n} = {summe_gauss}")
print(f"Identisch: {summe_for == summe_gauss}")

# =============================================================================
# 8. Beispiel: FizzBuzz
# =============================================================================

print("\n=== FizzBuzz (1-20) ===")
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# =============================================================================
# 9. while vs. for – Zusammenfassung
# =============================================================================

print("\n=== while vs. for ===")
print("""
FOR-Schleife:
  ✓ Anzahl Durchläufe bekannt
  ✓ Über Sequenzen iterieren (Liste, String, range, ...)
  ✓ Einfacher, weniger Fehlerquellen

WHILE-Schleife:
  ✓ Bedingung hängt von Eingabe/Event ab
  ✓ Unbekannte Anzahl Durchläufe
  ✓ Endlosschleife mit break
  ⚠ Initialisierung & Aktualisierung nicht vergessen!
""")


if __name__ == "__main__":
    pass