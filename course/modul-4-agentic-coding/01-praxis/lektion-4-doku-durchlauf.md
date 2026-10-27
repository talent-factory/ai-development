# Lektion 4: Dokumentation und Durchlauf

**Dauer:** 50 Minuten (21:00–21:50)  
**Ziel:** Dokumentieren, was der Code wirklich tut, und den ganzen Durchlauf Plan → Test → Code → Review → Doku an einem kleinen Feature selbst ausführen.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick**, Startstand holen | Gespräch |
| 5–13 | **Input:** Docstring und README, **KI-Moment** (Doku gegen Code prüfen) | Vortrag + Demo |
| 13–33 | **Übung 4:** Mini-Durchlauf `finde_kaeltesten_tag` ([ex-04](../02-uebungen/ex-04-durchlauf.adoc)) | Einzelarbeit |
| 33–41 | **Feedback** (mündliche Blitzrunde) | Plenum |
| 41–50 | **Kür / Puffer** | |

---

## 1. Rückblick und Startstand (5 Minuten)

«Was lief, was hakt?» Alle kopieren `05-beispiele/lektion-3/loesung/` als Startstand.

---

## 2. Dokumentation (8 Minuten)

Zwei Arten von Doku, beide beschreiben **was ist**, nicht was geplant war:

| Art | Wo | Für wen |
| --- | -- | ------- |
| **Docstring** | in der Funktion | wer die Funktion aufruft |
| **README** | im Projektordner | wer das Projekt starten will |

```text
Kontext: Funktion `vergleiche_staedte` in `wetter_bericht.py`.
Aufgabe: Schreibe einen Docstring (Zweck, Parameter, Rückgabe, Randfälle) und einen Abschnitt in `README.md` (lege die Datei an, falls sie fehlt). Beschreibe nur, was der Code wirklich tut, nichts Geplantes oder Erfundenes.
Format: Docstring und Markdown-Abschnitt.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

### KI-Moment: Lügt der Docstring?

KI-Doku liest sich glatt. Genau deshalb muss man sie gegen den Code prüfen. Gehe jede Aussage durch:

- Stimmt der Rückgabetyp und stimmen die **Schlüssel**?
- Steht ein **Randfall** drin, den der Code gar nicht behandelt (oder umgekehrt)?
- Wird eine Funktion erwähnt, die es nicht gibt?

Auch eine insgesamt richtige Doku enthält oft Aussagen, die die KI **nicht ausgeführt** hat, zum Beispiel «fehlende Felder lösen einen `KeyError` aus». Prüfe solche Sätze mit einem Einzeiler in der Python-Konsole, bevor du sie stehen lässt. Und streiche, was länger ist als die Funktion selbst: Ein 25-zeiliger Docstring für eine 15-zeilige Funktion liest niemand.

Eine falsche Doku ist schlimmer als keine, weil man ihr glaubt.

---

## 3. Übung 4: Mini-Durchlauf (20 Minuten)

Du führst den ganzen Durchlauf allein aus, für eine neue Funktion `finde_kaeltesten_tag(zeilen)`. Die Aufgabe steht in [ex-04-durchlauf.adoc](../02-uebungen/ex-04-durchlauf.adoc):

1. **Plan** mit `grilling` (`plan.md` ergänzen)
2. **Test** zuerst, rot
3. **Code**, grün
4. **Review** mit dem 3-Punkte-Check
5. **Doku** (Docstring, README)

Wer fertig ist: Kür unten.

**Wer nicht mitgekommen ist:** Kopiere `05-beispiele/lektion-4/loesung/`. Das ist der Endstand des Abends.

---

## 4. Feedback (8 Minuten)

Blitzrunde, reihum, je ein Satz:

- **Ein Ding ist mir klar geworden.**
- **Ein Ding ist mir noch unklar.**

Den Reflexionsbogen füllst du später selbst aus. Der Durchlauf kommt im Abschlussprojekt in Modul 6 wieder.

---

## 5. Kür / Puffer (9 Minuten)

- Mit dem Skill `domain-modeling` ein `GLOSSARY.md` für den Wetterbericht erstellen:

```text
Nutze den Skill `domain-modeling`.
Kontext: Projekt Wetterbericht.
Aufgabe: Erstelle `GLOSSARY.md` mit den Begriffen des Projekts (Stadt, Wettercode, Regentag, …) und frage nach, wo Begriffe unscharf sind.
Format: Glossar im Format der Vorlage.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

- Oder ein eigenes Feature durch den Durchlauf schicken.

---

## Nachbearbeitung

Bis Modul 5: eigener Durchlauf an einem kleinen Feature und der Reflexionsbogen, siehe [03-nachbearbeitung](../03-nachbearbeitung/README.md).

## Dozentenhinweise

- **Zeitnot:** Zuerst Kür, dann der Doku-Schritt im Durchlauf (wird Nachbearbeitung). Feedback bleibt immer.
- **Probelauf (2026-10-27, Claude Code 2.1.311):** Doku (Docstring und neues `README.md`) in ca. 45 s; sie war im Lauf **inhaltlich korrekt** (anders als die Konserve), aber lang, und das README-Beispiel enthielt `...` statt Zahlen, weil die KI die Funktion nicht ausgeführt hatte. Nicht ausgeführte Aussagen (`KeyError`, `TypeError`) benennt sie selbst: gutes Material für den KI-Moment. Mini-Durchlauf: `grilling` ca. 28 s (5 Fragen), `plan.md` ergänzen ca. 20 s, `tdd` drei Zyklen in ca. 59 s (Gleichstand-Test sofort grün, von der KI als «kein TDD-Schritt» markiert), 20 Tests grün. Gesamt unter vier Minuten KI-Zeit für die fünf Schritte. Stolpern: Die KI schlug «kein eigener `plan.md` nötig» und «kein README-Eintrag» vor und fügte in den Plan unbestellt einen Abschnitt «Tests» ein. Wer den Durchlauf vollständig will, muss das ausdrücklich verlangen (3-Punkte-Check, Punkt 3).
- **Rate-Limit:** Pair, Konserve: [`konserven/ki-moment-4-docstring.md`](../05-beispiele/konserven/ki-moment-4-docstring.md).
- **Musterlösung:** `05-beispiele/lektion-4/loesung/` (20 Tests grün, `README.md`).

---

*Datei: `01-praxis/lektion-4-doku-durchlauf.md`*  
*Zurück zum Modul: [Modul 4](../README.md)*
