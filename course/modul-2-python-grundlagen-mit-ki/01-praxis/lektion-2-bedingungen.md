# Lektion 2: Eingaben, Typumwandlung & Bedingungen

**Dauer:** 50 Minuten  
**Ziel:** `input()` nutzen, Typen sicher umwandeln, `if`/`elif`/`else` strukturiert einsetzen.

---

## 1. Eingaben entgegennehmen – `input()`

```python
name = input("Wie heisst du? ")        # Gibt IMMER str zurück!
alter_str = input("Wie alt bist du? ") # Auch Zahlen als Text
```

**Wichtig:** `input()` liefert **immer** `str`. Für Rechnungen muss umgewandelt werden.

---

## 2. Typumwandlung (Casting)

| Funktion | Wandelt nach | Beispiel |
|----------|--------------|----------|
| `int(x)` | Ganzzahl | `int("42")` → `42` |
| `float(x)` | Kommazahl | `float("3.14")` → `3.14` |
| `str(x)` | Text | `str(42)` → `"42"` |
| `bool(x)` | Wahrheitswert | `bool(1)` → `True`, `bool("")` → `False` |

**Fehlerbehandlung (Vorschau):**
```python
try:
    alter = int(input("Alter: "))
except ValueError:
    print("Das war keine Zahl!")
    alter = 0
```

---

## 3. Vergleichsoperatoren (Rückgabe: `bool`)

| Operator | Bedeutung | Beispiel |
|----------|-----------|----------|
| `==` | gleich | `5 == 5` → `True` |
| `!=` | ungleich | `5 != 3` → `True` |
| `<` | kleiner | `3 < 5` → `True` |
| `>` | grösser | `5 > 3` → `True` |
| `<=` | kleiner/gleich | `5 <= 5` → `True` |
| `>=` | grösser/gleich | `5 >= 5` → `True` |

**Achtung:** `=` ist Zuweisung, `==` ist Vergleich!

---

## 4. Logische Operatoren

```python
alter = 20
hat_ausweis = True

# and: beide müssen True sein
if alter >= 18 and hat_ausweis:
    print("Darf fahren")

# or: mindestens einer True
if alter < 18 or not hat_ausweis:
    print("Darf nicht fahren")

# not: kehrt um
if not hat_ausweis:
    print("Kein Ausweis")
```

**Kurzschluss-Auswertung:** Bei `and` wird zweiter Teil nicht geprüft, wenn erster `False` ist.

---

## 5. Bedingte Anweisungen – `if`, `elif`, `else`

### Einfache Verzweigung
```python
alter = int(input("Alter: "))

if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

### Mehrfach-Verzweigung
```python
note = float(input("Note (1-6): "))

if note >= 5.5:
    print("Sehr gut")
elif note >= 4.5:
    print("Gut")
elif note >= 4.0:
    print("Genügend")
else:
    print("Ungenügend")
```

### Einrückung ist Pflicht! (4 Leerzeichen, kein Tab-Mix)

```python
if bedingung:
    tue_das()      # 4 Spaces
    und_auch_das() # 4 Spaces
print("Immer ausgeführt")  # Keine Einrückung = ausserhalb
```

---

## 6. Praktische Beispiele

### Beispiel 1: Alters-Check mit Eingabe
```python
alter_str = input("Dein Alter: ")

try:
    alter = int(alter_str)
    if alter < 0:
        print("Alter kann nicht negativ sein!")
    elif alter < 18:
        print("Noch nicht volljährig")
    elif alter < 65:
        print("Erwerbsalter")
    else:
        print("Rentenalter")
except ValueError:
    print("Bitte eine ganze Zahl eingeben.")
```

### Beispiel 2: Einfacher Taschenrechner
```python
a = float(input("Zahl 1: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Zahl 2: "))

if op == "+":
    ergebnis = a + b
elif op == "-":
    ergebnis = a - b
elif op == "*":
    ergebnis = a * b
elif op == "/":
    if b != 0:
        ergebnis = a / b
    else:
        print("Division durch 0 nicht erlaubt!")
        ergebnis = None
else:
    print("Unbekannter Operator")
    ergebnis = None

if ergebnis is not None:
    print(f"Ergebnis: {ergebnis}")
```

### Beispiel 3: BMI-Rechner (Mini-Projekt)
```python
gewicht = float(input("Gewicht (kg): "))
groesse = float(input("Grösse (m): "))

bmi = gewicht / (groesse ** 2)

if bmi < 18.5:
    kategorie = "Untergewicht"
elif bmi < 25:
    kategorie = "Normalgewicht"
elif bmi < 30:
    kategorie = "Übergewicht"
else:
    kategorie = "Adipositas"

print(f"BMI: {bmi:.1f} – {kategorie}")
```

---

## 7. KI-Pair-Programming – Prompts

| Prompt | Zweck |
|--------|-------|
| `"Schreibe ein Programm, das zwei Zahlen einliest und die größere ausgibt – mit Fehlerbehandlung für ungültige Eingaben."` | Vorlage generieren |
| `"Mein Code wirft ValueError bei Buchstaben. Wie fange ich das ab?"` | Debugging-Hilfe |
| `"Vergleiche: `if x:` vs `if x == True:` – was ist besser?"` | Best Practice |
| `"Erkläre mir den Unterschied zwischen `if`, `elif`, `else` an einem Alltagsbeispiel."` | Konzept vertiefen |

---

## 8. Mini-Übung: BMI-Rechner erweitern (15 Min)

Erweitere den BMI-Rechner:
1. Frage auch nach **Alter**
2. Für Unter-18-Jährige: Hinweis „BMI bei Jugendlichen anders interpretieren“
3. Gib **Idealgewichts-Bereich** aus (BMI 18.5–25 → Gewicht = BMI × Größe²)

**KI-Prompt:** `"Ergänze den BMI-Rechner: Idealgewicht-Bereich berechnen und ausgeben."`

---

## 9. Häufige Fehler & Lösungen

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| `ValueError: invalid literal for int()` | Buchstaben bei `int()` | `try/except` oder `.isdigit()` prüfen |
| `IndentationError` | Falsche Einrückung | 4 Spaces konsequent, VS Code: `Ctrl+Shift+P` → "Reindent" |
| `NameError` in `else`-Zweig | Variable nur in `if` definiert | Variable **vor** `if` initialisieren |
| Logikfehler: `if note = 6:` | Zuweisung statt Vergleich | `==` verwenden |
| `else` ohne `if` | Einrückung stimmt nicht | Prüfen: `else` auf gleicher Ebene wie `if` |

---

## 10. Weiterführende Links

- [Python Docs: input()](https://docs.python.org/3/library/functions.html#input)
- [Real Python: Conditional Statements](https://realpython.com/python-conditional-statements/)
- [Python Docs: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

---

## 11. Reflexionsfragen

1. Warum liefert `input()` immer einen String?
2. Wann nutzt du `elif` statt mehreren `if`?
3. Was passiert, wenn du `else` vergisst und keine Bedingung zutrifft?

---

*Datei: `01-praxis/lektion-2-bedingungen.md`*  
*Zugehöriges Beispiel: `05-beispiele/02-bedingungen_demo.py`*  
*Übung: `02-uebungen/ex-01-taschenrechner.adoc`*