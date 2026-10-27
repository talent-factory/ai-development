# Nachbearbeitung: Modul 3: Datenverarbeitung & Dateien

**Zeitaufwand:** 3–4 Stunden bis Modul 4

---

## 1. Pflicht-Aufgabe (ca. 2–3 Std)

### A) Wetterbericht `wetter_bericht.py`

Schreibe ein Skript, das alle Techniken des Abends kombiniert: Datei lesen, auswerten, API abrufen, Fehler abfangen, Ergebnis als JSON speichern.

Das Skript:

1. Fragt mit `input()` nach einer **Stadt** (Zürich, Bern, Genf, Basel oder Lugano). Eine unbekannte Stadt führt zu einer freundlichen Meldung, nicht zum Absturz.
2. Liest `wetter_30tage.csv` (aus `05-beispiele/lektion-2/`) und berechnet **für diese Stadt**:
   - Durchschnitt von `tmin` und `tmax`
   - höchste `tmax` mit Datum
   - Anzahl Regentage (`niederschlag_mm > 0`)
   - Gesamtniederschlag in mm
3. Ruft die **aktuelle Temperatur** und den Wettercode der Stadt bei Open-Meteo ab und übersetzt den Code in Klartext (Dictionary mit mindestens den Codes 0, 3, 45, 61, 80, 95).
4. **Fängt Fehler ab:** Datei fehlt, API nicht erreichbar, API lehnt ab, Antwort leer. Das Skript schreibt dann «Live-Wetter nicht verfügbar» in den Bericht, statt abzubrechen.
5. Speichert alles in `bericht_<stadt>.json` (Kennzahlen und Live-Wetter) und gibt eine lesbare Zusammenfassung auf dem Bildschirm aus. Die Ausgabe nennt die Quelle: *Weather data by Open-Meteo.com*.
6. Ist in **Funktionen** gegliedert (Typ-Hinweise und Docstrings), `main()` mit `if __name__ == "__main__":`.

**Kontrollwerte (aus der CSV):**

| Stadt | Ø `tmax` | Tage über 20 °C |
| ----- | -------- | --------------- |
| Bern | 19.9 | 17 |
| Lugano | 21.8 | 22 |

Die Live-Werte (aktuelle Temperatur, Wettercode) ändern sich. Prüfe dort nur, ob eine sinnvolle Zahl und ein Klartext erscheinen.

**Koordinaten:**

| Stadt | latitude | longitude |
| ----- | -------- | --------- |
| Zürich | 47.3769 | 8.5417 |
| Bern | 46.948 | 7.4474 |
| Genf | 46.2044 | 6.1432 |
| Basel | 47.5596 | 7.5886 |
| Lugano | 46.0037 | 8.9511 |

**KI-Nutzung:** Nutze die KI mindestens einmal (zum Beispiel als Erklärer, Testdaten-Generator oder Debug-Partner). Halte fest, was du gefragt hast und wie du das Ergebnis geprüft hast. Das fliesst in die Reflexion ein.

---

### B) Reflexionsbogen (30 Min)

Fülle den [Reflexionsbogen](./reflexionsbogen.md) aus. Er enthält die Frage: *Wo war die KI falsch oder hat etwas erfunden?*

---

## 2. Zusatz-Aufgaben (freiwillig, +1–2 Std)

### C) Städtevergleich

Vergleiche zwei Städte nebeneinander: Differenz der Durchschnitte, welche Stadt hatte mehr Regentage, in welcher war der heisseste Tag.

### D) Mit defekten Daten umgehen

Lass dein Skript auch mit `wetter_defekt.csv` aus `05-beispiele/lektion-4/` laufen. Zähle die übersprungenen Zeilen und schreibe sie ins Log.

### E) Eigene Idee

Setze eine eigene Datenidee um, die mindestens zwei der drei Formate (TXT, CSV, JSON) nutzt.

---

## 3. Vorbereitung Modul 4 (Agentic Coding)

- [ ] Lies dein eigenes Skript noch einmal durch und notiere drei Stellen, an denen du dir eine KI als Hilfe gewünscht hättest.
- [ ] Überlege: Welche Teile deines Skripts würdest du **einer KI selbstständig überlassen**, und wie würdest du ihr Ergebnis prüfen?

---

## 4. Abgabe

**Bis Modul 4 (nächster Kurstag):**

1. `wetter_bericht.py` in `03-nachbearbeitung/`
2. `bericht_<stadt>.json` für **eine** Stadt
3. Reflexionsbogen als `reflexion.md` in `03-nachbearbeitung/`
4. Optional: Zusatz-Aufgaben

**Format:** Dateien per GitHub Classroom / Moodle / E-Mail (laut Dozent)

---

## 5. Bewertungskriterien (für Dozent)

| Kriterium | Gewichtung |
| --------- | ---------- |
| Funktionalität (läuft, Kontrollwerte stimmen) | 35 % |
| Fehlerbehandlung (gezielte `except`-Blöcke, nichts verschluckt) | 25 % |
| Struktur (Funktionen, Typ-Hinweise, Docstrings, `main()`) | 20 % |
| KI-Nutzung dokumentiert und reflektiert | 20 % |

---

*Datei: `03-nachbearbeitung/README.md`*  
*Zurück zum Modul: [Modul 3: Datenverarbeitung & Dateien](../README.md)*
