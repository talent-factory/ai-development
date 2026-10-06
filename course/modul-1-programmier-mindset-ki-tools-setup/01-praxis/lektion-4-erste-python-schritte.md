# Lektion 4: Erste Python-Schritte mit KI

**Dauer:** 50 Minuten  
**Ziel:** Erstes Python-Script ausführen, KI als Erklär-Partner nutzen und ethische Grundregeln kennenlernen.

---

## 🎯 Lernziele

Nach dieser Lektion können die Teilnehmenden:

- Ein Python-Script in VS Code ausführen.
- KI gezielt bitten, Code zu erklären oder kleine Änderungen vorzuschlagen.
- Den Unterschied zwischen menschlich geschriebenem und KI-generiertem Code diskutieren.
- Die wichtigsten ethischen und rechtlichen Grundregeln beim Einsatz von KI nennen.

---

## ⏱️ Zeitplan

| Zeit      | Phase                  | Inhalt                                              |
| --------- | ---------------------- | --------------------------------------------------- |
| 0–10 min  | Erstes Script          | `hello-world.py` öffnen und ausführen               |
| 10–25 min | KI als Erklär-Partner  | Code in ChatGPT/Claude einfügen und erklären lassen |
| 25–40 min | Kleine Änderung mit KI | Prompt formulieren, Ergebnis testen, korrigieren    |
| 40–50 min | Ethik & Regeln         | Datenschutz, Urheberrecht, Transparenz              |

---

## 💻 Erstes Python-Script (10 Min)

**Datei:** `05-beispiele/hello-world.py`

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")
st.write("Dies ist meine erste Streamlit-App.")
```

**Ausführung:**

```bash
uv run streamlit run course/modul-1-programmier-mindset-ki-tools-setup/05-beispiele/hello-world.py
```

**Was passiert?**

- Ein Webserver startet lokal.
- Der Browser öffnet eine einfache Seite mit Titel und Text.

---

## 🤖 KI als Erklär-Partner (15 Min)

### Prompt-Beispiel

```text
Erkläre mir diesen Python-Code Zeile für Zeile, als wäre ich Anfänger:

import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello World")
st.write("Dies ist meine erste Streamlit-App.")
```

**Diskussion:**

- Was hat die KI gut erklärt?
- Was war unklar?
- Welche Frage stellt man als Nachfolge?

### Weiterer Prompt

```text
Wozu dienen die Imports `pandas` und `numpy` in diesem Beispiel?
Werden sie hier bereits verwendet?
```

**Erkenntnis:** KI kann helfen, aber der Mensch muss den Code verstehen und überflüssige Teile erkennen.

---

## ✍️ Kleine Änderung mit KI (15 Min)

**Aufgabe:** Füge eine zweite Zeile hinzu, die den aktuellen Wochentag anzeigt.

**Möglicher Prompt:**

```text
Erweitere diesen Code so, dass unter dem Text der aktuelle Wochentag angezeigt wird.
Gib mir nur den geänderten Code zurück.

[Code einfügen]
```

**Vorgehen:**

1. Prompt formulieren.
2. KI-Antwort in VS Code einfügen.
3. Script ausführen.
4. Bei Fehlern: Fehlermeldung an die KI weitergeben und Lösung anfordern.

**Diskussion:**

- Hat die KI richtig verstanden, was wir wollten?
- Welche Probleme sind aufgetreten?
- Wie gehen wir mit Fehlern um?

---

## ⚖️ Ethik & Regeln (10 Min)

### Wichtige Grundsätze

1. **Nicht alles mit KI teilen**
   - Keine Passwörter, API-Keys, persönliche Daten oder interne Firmengeheimnisse in öffentliche KI-Tools eingeben.

2. **Urheberrecht beachten**
   - KI-generierter Code ist kein Freifahrtschein. Lizenzbedingungen prüfen.

3. **Transparenz**
   - Dokumentieren, wenn KI bei der Erstellung unterstützt hat.

4. **Verantwortung**
   - Der Mensch trägt die Verantwortung für den eingesetzten Code.

5. **Kritisch prüfen**
   - KI halluziniert manchmal. Ergebnisse nicht blind übernehmen.

### Diskussionsfrage

> «Du sollst für ein Unternehmen ein Script schreiben, das Kundendaten verarbeitet. Darfst du den Code an eine öffentliche KI weitergeben? Was wäre eine sichere Alternative?»

---

## 📚 Materialien

- `05-beispiele/hello-world.py`
- Browser mit ChatGPT/Claude
- `01-praxis/01-introduction.adoc` (rechtliche/ethische Hintergründe)

---

## 🏠 Hausaufgabe (Nachbereitung)

- Passe `hello-world.py` mit KI-Unterstützung so an, dass dein Name und ein persönlicher Gruß angezeigt werden.
- Dokumentiere in 2–3 Sätzen, welche Prompts du verwendet hast und was gut bzw. schwierig war.
- Lies den ethischen Hintergrund in `01-praxis/01-introduction.adoc` nach.
