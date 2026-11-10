# Lektion 2: Spec fertigstellen

**Dauer:** 50 Minuten (19:00–19:50)  
**Ziel:** Aus dem `plan.md` eine vollständige `SPEC.md` machen: Architektur, Meilensteine, Testfragen, Risiken.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Rückblick, Stand der Pläne | Gespräch |
| 5–15 | **Input:** Architektur aus Kursbausteinen, Meilensteine, gute Testfragen | Vortrag |
| 15–40 | **Schritt 3:** `SPEC.md` nach der Gliederung der [Vorlage](../04-materialien/projekt-spec-vorlage.md) | Einzelarbeit |
| 40–47 | **KI-Moment:** Abschnitt 7 Risiken und Rechte | Gespräch |
| 47–50 | Puffer | |

---

## 1. Input (10 Minuten)

- **Architektur in 5 Zeilen:** Eingabe → Verarbeitung → Ausgabe. Welche Kursbausteine kommen vor? (CSV/JSON/API, Embeddings und Suche, `beantworte` aus Modul 5, Streamlit)
- **Meilensteine:** Meilenstein 1 ist immer ein Walking Skeleton ohne KI.
- **Testfragen:** eine mit klarer Antwort, eine Fallen-Frage (darf nicht beantwortbar sein), eine, bei der die Technik scheitern könnte.

> TODO Dozent: Beispiel einer Fallen-Frage aus Modul 5 («Wie viele Ferientage habe ich pro Jahr?») als Brücke nutzen.

## 2. Spec schreiben (25 Minuten)

Die Gliederung steht in der Vorlage. Mindestziel: Abschnitte 1 bis 6 ausgefüllt.

Nach dem Schreiben der 3-Punkte-Check: Steht drin, was **ich** entschieden habe? Sind Zahlen echt? Hat die KI etwas Ungefragtes ergänzt?

## 3. Risiken und Verantwortung (7 Minuten)

Der Kasten «Too Good To Go» in der Vorlage dient als Beispiel für Rechte und AGB. Jede und jeder prüft die eigene Datenquelle mit drei Fragen:

1. Gibt es eine offizielle Schnittstelle?
2. Was sagen die AGB?
3. Was passiert, wenn der Zugriff morgen blockiert wird?

> TODO Dozent: Datenschutz kurz ansprechen (welche Personendaten fliessen an ein Modell?).

## 4. Mindestziel

`SPEC.md` mit Abschnitten 1 bis 7 und mindestens 5 Testfragen.
