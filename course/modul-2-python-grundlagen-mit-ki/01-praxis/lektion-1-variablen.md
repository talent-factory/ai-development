# Lektion 1: Variablen, Datentypen & Operatoren

**Dauer:** 50 Minuten  
**Ziel:** Variablen anlegen, Datentypen unterscheiden, Operatoren anwenden, KI als Erklär-Partner nutzen.

---

## 1. Was ist eine Variable?

Eine Variable ist ein **benannter Speicherplatz** für einen Wert.

```python
# Syntax: name = wert
alter = 25
name = "Alex"
groesse = 1.78
ist_student = True
```

**Wichtige Regeln:**
- Namen: Buchstaben, Zahlen, `_` – **nicht** mit Zahl beginnen
- Case-sensitive: `alter` ≠ `Alter`
- Keine Schlüsselwörter (`if`, `for`, `class`, …)

---

## 2. Die vier Basis-Datentypen

| Typ | Erklärung | Beispiel | `type()` |
|-----|-----------|----------|----------|
| `int` | Ganze Zahlen | `42`, `-7`, `0` | `<class 'int'>` |
| `float` | Kommazahlen | `3.14`, `-0.5`, `2.0` | `<class 'float'>` |
| `str` | Text (Zeichenkette) | `"Hallo"`, `'Welt'`, `""` | `<class 'str'>` |
| `bool` | Wahrheitswerte | `True`, `False` | `<class 'bool'>` |

**Prüfen:** `type(variable)` zeigt den Typ an.

---

## 3. Operatoren

### Rechenoperatoren (Zahlen)

| Operator | Name | Beispiel | Ergebnis |
|----------|------|----------|----------|
| `+` | Addition | `3 + 2` | `5` |
| `-` | Subtraktion | `5 - 3` | `2` |
| `*` | Multiplikation | `4 * 3` | `12` |
| `/` | Division (float) | `7 / 2` | `3.5` |
| `//` | Ganzzahldivision | `7 // 2` | `3` |
| `%` | Modulo (Rest) | `7 % 2` | `1` |
| `**` | Potenz | `2 ** 3` | `8` |

### String-Operatoren

```python
vorname = "Alex"
nachname = "Mueller"
name = vorname + " " + nachname      # Konkatenation
begruessung = f"Hallo, {name}!"       # f-String (empfohlen)
wiederholung = "Ha " * 3              # "Ha Ha Ha "
```

### Vergleichsoperatoren (liefern `bool`)

```python
5 > 3      # True
10 == 10   # True
7 != 5     # True
3.14 <= 3  # False
```

---

## 4. Praktische Beispiele

### Beispiel 1: Variablen anzeigen
```python
alter = 25
name = "Sam"
groesse = 1.80
ist_student = True

print(f"Name: {name}")
print(f"Alter: {alter}, Typ: {type(alter)}")
print(f"Grösse: {groesse}, Typ: {type(groesse)}")
print(f"Student: {ist_student}, Typ: {type(ist_student)}")
```

### Beispiel 2: Rechnen mit Variablen
```python
radius = 5
pi = 3.14159
flaeche = pi * radius ** 2
umfang = 2 * pi * radius

print(f"Kreis (r={radius}): Fläche = {flaeche:.2f}, Umfang = {umfang:.2f}")
```

### Beispiel 3: Typumwandlung (Vorschau Lektion 2)
```python
zahl_str = "42"
zahl_int = int(zahl_str)      # str → int
zahl_float = float(zahl_str)  # str → float
print(type(zahl_int), zahl_int * 2)
```

---

## 5. KI als Erklär-Partner – Prompts zum Ausprobieren

> **Tipp:** Kopiere deinen Code in den Chat und frage:

| Prompt | Zweck |
|--------|-------|
| `"Erkläre mir diesen Code Zeile für Zeile wie einem Anfänger."` | Verständnis sichern |
| `"Was passiert, wenn ich hier einen String statt einer Zahl eingebe?"` | Fehlersuche |
| `"Zeige mir 3 alternative Schreibweisen für diese Berechnung."` | Varianten vergleichen |
| `"Warum gibt `7 / 2` einen float zurück, aber `7 // 2` einen int?"` | Konzepte vertiefen |

---

## 6. Mini-Übung (10 Min)

Erstelle ein Script `meine_daten.py`:

1. Lege Variablen für dich an: `name`, `alter`, `groesse_m`, `lieblingsfarbe`, `mag_python`
2. Gib alles mit **einem** `print()` und f-Strings aus
3. Berechne: `alter_in_monaten = alter * 12`
4. Frage KI: „Wie formatiere ich die Grösse auf 2 Nachkommastellen?“

**Erwartete Ausgabe:**
```
Ich heisse Alex, bin 25 Jahre alt (300 Monate), 1.78 m gross,
meine Lieblingsfarbe ist blau und ich mag Python: True
```

---

## 7. Häufige Fehler & Lösungen

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| `SyntaxError: invalid syntax` bei `2name = "x"` | Name beginnt mit Zahl | `name2 = "x"` |
| `NameError: name 'alter' is not defined` | Variable vor Nutzung nicht gesetzt | Erst zuweisen, dann lesen |
| `TypeError: can only concatenate str to str` | `print("Alter: " + 25)` | `print("Alter: " + str(25))` oder f-String |
| `ZeroDivisionError` | Division durch 0 | Prüfen: `if b != 0:` |

---

## 8. Weiterführende Links

- [Python Docs: Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Real Python: Variables](https://realpython.com/python-variables/)
- [PEP 8 – Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

---

## 9. Reflexionsfragen (für Nachbearbeitung)

1. Welcher Datentyp war neu für dich?
2. Bei welchem Operator warst du unsicher (`//`, `%`, `**`)?
3. Wie hat dir die KI-Erklärung geholfen – war sie präzise genug?

---

*Datei: `01-praxis/lektion-1-variablen.md`*  
*Zugehöriges Beispiel: `05-beispiele/01-variablen_demo.py`*