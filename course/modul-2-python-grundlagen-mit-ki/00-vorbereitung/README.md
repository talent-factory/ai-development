# Vorbereitung: Modul 2: Python-Grundlagen mit KI verstehen

**Zeitaufwand:** 2–3 Stunden vor dem Präsenztag

---

## 1. Modul 1 wiederholen (30 Min)

- [ ] Setup prüfen: `python --version`, `uv --version`, `opencode --version`
- [ ] `hello-world.py` aus Modul 1 nochmals ausführen
- [ ] Eine KI-Frage zu Python stellen, Antwort reflektieren (Was war hilfreich? Was ungenau?)

---

## 2. Leseauftrag: Python-Basics (60–90 Min)

Lesen & **ausprobieren** in der Python-REPL (`python` im Terminal):

| Thema | Quelle | Was du können solltest |
|-------|--------|------------------------|
| Variablen & Datentypen | [Python Tutorial: Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator) | `int`, `float`, `str`, `bool` unterscheiden, `type()` nutzen |
| Operatoren | [Python Docs: Expressions](https://docs.python.org/3/reference/expressions.html) | `+ - * / // % **` anwenden, f-Strings formatieren |
| `input()` & Casting | [Real Python: input()](https://realpython.com/python-input-output/) | `input()` → `str`, `int()`, `float()` umwandeln |
| `if`/`elif`/`else` | [Python Tutorial: Control Flow](https://docs.python.org/3/tutorial/controlflow.html#if-statements) | Bedingungen schreiben, Einrückung beachten |
| `while` / `for` / `range` | [Python Tutorial: Loops](https://docs.python.org/3/tutorial/controlflow.html#for-statements) | Schleifen schreiben, `break`/`continue` kennen |
| Funktionen | [Python Tutorial: Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) | `def`, Parameter, `return`, Docstring verstehen |

**Tipp:** Nutze KI als Lernpartner:
> `"Erkläre mir den Unterschied zwischen // und / mit 3 Beispielen."`
> `"Zeige mir 5 typische Anfängerfehler bei if-Bedingungen."`

---

## 3. Erste REPL-Experimente (30 Min)

Öffne Terminal → `python` → probiere:

```python
# 1. Typen erkunden
type(42)
type(3.14)
type("Hallo")
type(True)

# 2. Rechnen
7 / 2
7 // 2
7 % 2
2 ** 10

# 3. Strings
name = "Alex"
f"Hallo, {name}!"
"Ha " * 3

# 4. Bedingungen
alter = 20
alter >= 18
"Volljährig" if alter >= 18 else "Minderjährig"

# 5. Schleifen
for i in range(3):
    print(i)

# 6. Funktion
def quadrat(x):
    return x * x
quadrat(5)
help(quadrat)
```

**Ziel:** Du hast alles **mindestens einmal selbst getippt** und die Ausgabe gesehen.

---

## 4. KI-Vorbereitung (15 Min)

- [ ] Claude (Browser oder Claude Code) und OpenCode bereit haben
- [ ] Repo-Root im Terminal öffnen, `claude` starten und `/erklaere` testen (bzw. `opencode` mit `/erklaere`)
- [ ] Teste Prompt: `"Ich lerne Python. Erkläre mir Variablen wie einem 12-Jährigen."`
- [ ] Notiere: Was war gut? Was war zu komplex?

---

## 5. Checkliste für den Präsenztag

- [ ] Laptop geladen
- [ ] VS Code, Python, uv, OpenCode funktionieren
- [ ] Browser-Tabs: Claude, OpenCode-Docs
- [ ] Dieses Dokument (digital oder gedruckt) dabei
- [ ] Fragen aus der Vorbereitung notiert

---

## 6. Bei Problemen

| Problem | Lösung |
|---------|--------|
| `python` nicht gefunden | Neuinstallation, "Add to PATH" prüfen, Terminal neu starten |
| `uv` nicht gefunden | `curl -LsSf https://astral.sh/uv/install.sh \| sh` (Mac/Linux) oder `pip install uv` |
| OpenCode startet nicht | `opencode auth login`, API-Key prüfen |
| REPL schließt sofort | `python -i` oder `python -c "..."` nutzen |

---

*Datei: `00-vorbereitung/README.md`*  
*Zurück zum Modul: [Modul 2: Python-Grundlagen mit KI verstehen](../README.md)*