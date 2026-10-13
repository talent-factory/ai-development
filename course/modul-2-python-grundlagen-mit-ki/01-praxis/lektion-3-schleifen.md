# Lektion 3: Schleifen – `while`, `for`, `range()`

**Dauer:** 50 Minuten  
**Ziel:** Wiederholungen automatisieren, Schleifenarten unterscheiden, KI als Debugging-Partner nutzen.

---

## 1. Warum Schleifen?

Statt Code zu kopieren:
```python
print(1)
print(2)
print(3)
# ...
```

Schreibe einmal:
```python
for i in range(1, 4):
    print(i)
```

---

## 2. Die `while`-Schleife

**Solange Bedingung `True` → wiederholen.**

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler = zaehler + 1  # oder: zaehler += 1
print("Fertig")
```

### Wichtige Regeln
1. **Initialisierung** vor der Schleife
2. **Bedingung** wird **vor** jedem Durchlauf geprüft
3. **Aktualisierung** im Körper (sonst Endlosschleife!)

### Endlosschleife vermeiden
```python
# FALSCH – läuft ewig
while True:
    print("Hilfe!")

# RICHTIG – Abbruchbedingung
while eingabe != "quit":
    eingabe = input("Befehl: ")
```

### `break` und `continue`
```python
# break: Schleife sofort verlassen
while True:
    cmd = input("> ")
    if cmd == "exit":
        break
    print(f"Echo: {cmd}")

# continue: aktuellen Durchlauf abbrechen, nächsten starten
for i in range(10):
    if i % 2 == 0:
        continue  # überspringt gerade Zahlen
    print(i)      # nur ungerade: 1, 3, 5, 7, 9
```

---

## 3. Die `for`-Schleife

**Iteriert über Sequenzen** (range, Listen, Strings, ...).

### `range()` – Zahlenfolgen erzeugen

| Aufruf | Erzeugt | Beispiel |
|--------|---------|----------|
| `range(n)` | 0 bis n-1 | `range(3)` → 0, 1, 2 |
| `range(start, stop)` | start bis stop-1 | `range(1, 5)` → 1, 2, 3, 4 |
| `range(start, stop, step)` | Schrittweite | `range(0, 10, 2)` → 0, 2, 4, 6, 8 |

```python
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

for i in range(10, 0, -1):
    print(i)  # 10, 9, ..., 1 (Countdown)
```

### Über Listen & Strings iterieren
```python
farben = ["rot", "grün", "blau"]
for farbe in farben:
    print(farbe)

for buchstabe in "Python":
    print(buchstabe)
```

### `enumerate()` – Index & Wert
```python
for idx, farbe in enumerate(farben):
    print(f"{idx}: {farbe}")
# 0: rot
# 1: grün
# 2: blau
```

---

## 4. Verschachtelte Schleifen

```python
# Multiplikationstabelle 1-3
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="  ")
    print()  # neue Zeile
```

---

## 5. Praktische Beispiele

### Beispiel 1: Zahlenraten-Spiel (`while`)
```python
import random

geheim = random.randint(1, 100)
versuche = 0
geraten = False

print("Rate die Zahl (1-100)!")

while not geraten:
    tipp = int(input("Dein Tipp: "))
    versuche += 1
    
    if tipp < geheim:
        print("Zu klein!")
    elif tipp > geheim:
        print("Zu gross!")
    else:
        print(f"Richtig! Du brauchtest {versuche} Versuche.")
        geraten = True
```

### Beispiel 2: Summe 1 bis n (`for`)
```python
n = int(input("Bis zu welcher Zahl summieren? "))
summe = 0

for i in range(1, n + 1):
    summe += i

print(f"1 + 2 + ... + {n} = {summe}")
# Formel: n * (n + 1) / 2
print(f"Prüfung (Gauß): {n * (n + 1) // 2}")
```

### Beispiel 3: FizzBuzz (Klassiker)
```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

## 6. `while` vs. `for` – Wann was?

| Situation | Empfehlung |
|-----------|------------|
| Anzahl Durchläufe **bekannt** | `for` + `range()` |
| Über **Liste/String** iterieren | `for` |
| Bedingung **abhängig von Eingabe/Event** | `while` |
| Unbekannte Anzahl, bis Ereignis eintritt | `while` |
| Endlosschleife mit `break` | `while True:` |

---

## 7. KI-Debugging – Prompts

| Prompt | Zweck |
|--------|-------|
| `"Mein Code hat eine Endlosschleife. Finde den Fehler: [Code]"` | Bug finden |
| `"Was ist der Unterschied zwischen `range(10)` und `range(1, 11)`?"` | Off-by-One verstehen |
| `"Erkläre mir `enumerate()` an einem Beispiel."` | Neues Konzept |
| `"Wie baue ich eine Countdown-Schleife von 10 bis 1?"` | `range` mit negativem Step |

---

## 8. Mini-Übung: FizzBuzz erweitern (10 Min)

1. Erweitere FizzBuzz: Bei 7 → „Bazz“, bei 3×7 → „FizzBazz“, bei 5×7 → „BuzzBazz“, bei 3×5×7 → „FizzBuzzBazz“
2. Teste mit KI: `"Prüfe meinen FizzBuzz-Code auf Vollständigkeit."`

---

## 9. Häufige Fehler & Lösungen

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| Endlosschleife | Variable nicht aktualisiert | `zaehler += 1` im Körper prüfen |
| Off-by-One | `range(1, 10)` gibt 1-9 | `range(1, 11)` für 1-10 |
| `TypeError: 'int' object is not iterable` | `for i in 5:` | `for i in range(5):` |
| `UnboundLocalError` | Variable nur in Schleife gesetzt | Vorher initialisieren: `summe = 0` |
| Einrückungsfehler nach `break` | Code nach `break` eingerückt | `break` auf Schleifen-Ebene |

---

## 10. Weiterführende Links

- [Python Docs: for Statements](https://docs.python.org/3/reference/compound_stmts.html#for)
- [Python Docs: while Statements](https://docs.python.org/3/reference/compound_stmts.html#while)
- [Real Python: Python Loops](https://realpython.com/python-for-loop/)

---

## 11. Reflexionsfragen

1. Wann hast du `while` vermisst, weil `for` nicht passte?
2. Was war dein erster Endlosschleifen-Bug – wie hast du ihn gefunden?
3. Wie hat KI beim Debugging geholfen (oder nicht)?

---

*Datei: `01-praxis/lektion-3-schleifen.md`*  
*Zugehöriges Beispiel: `05-beispiele/03-schleifen_demo.py`*  
*Übung: `02-uebungen/ex-02-zahlenraten.adoc`*