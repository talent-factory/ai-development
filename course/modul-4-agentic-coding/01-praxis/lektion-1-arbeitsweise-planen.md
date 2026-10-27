# Lektion 1: Arbeitsweise und Planen

**Dauer:** 50 Minuten (18:00–18:50)  
**Ziel:** Mit einem Coding-Agenten arbeiten, ohne ihn blind machen zu lassen: Code erklären lassen, eine Änderung mit `grilling` klären und als `plan.md` festhalten.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | Begrüssung, Tagesüberblick, **Start-Check** (`check_setup.py`) | Kurzvortrag + Einzelarbeit |
| 5–15 | **Input:** Prompt-Handwerk, Skills, 3-Punkte-Check | Vortrag |
| 15–25 | **Live-Demo:** `grilling` auf `wetter_bericht.py`, **KI-Moment** (Annahmen) | Demo + Mitmachen |
| 25–40 | **Übung 1:** `plan.md` für `vergleiche_staedte` ([ex-01](../02-uebungen/ex-01-plan.adoc)) | Einzelarbeit |
| 40–45 | **Kür** (freiwillig) | Einzelarbeit |
| 45–50 | **Puffer** | |

---

## 1. Der Abend im Überblick

Heute arbeiten wir mit einem Coding-Agenten (OpenCode oder Claude Code) an **einem** Projekt, dem Wetterbericht aus Modul 3. Der rote Faden ist der **Durchlauf**:

```text
Plan  →  Test  →  Code  →  Review  →  Doku
 L1       L2       L2       L3         L4
```

| Lektion | Schritt | Skill |
| ------- | ------- | ----- |
| 1 | Plan | `grilling` |
| 2 | Test, Code | `tdd` |
| 3 | Review, Refactoring, Diagnose | `code-review` (Demo), `diagnosing-bugs` |
| 4 | Doku, ganzer Durchlauf | (Kür: `domain-modeling`) |

In Lektion 4 führst du den ganzen Durchlauf selbst an einem kleinen Feature aus. Das Feature, an dem wir bis dahin üben, ist ein **Städtevergleich**.

---

## 2. Start-Check (2–3 Minuten)

Kopiere den Startpunkt in dein Arbeitsverzeichnis (`05-beispiele/wetter_bericht/`) und prüfe dein Setup:

```bash
uv run python 05-beispiele/check_setup.py
```

Heb die Hand, wenn eine Zeile `FEHLER` zeigt. Wir lösen das **nicht im Plenum**: Arbeite mit deiner Sitznachbarin oder deinem Sitznachbarn, wir klären es in der Pause.

---

## 3. Prompt-Handwerk (10 Minuten)

Ein Coding-Agent liest deine Dateien und kann sie ändern. Gute Ergebnisse hängen weniger vom Modell als von der Anweisung ab. Jeder Prompt heute hat drei Teile:

| Teil | Frage |
| ---- | ----- |
| **Kontext** | Woran arbeite ich, welche Datei, welcher Plan? |
| **Aufgabe** | Was genau soll die KI tun, und was ausdrücklich nicht? |
| **Format** | Wie soll die Antwort aussehen? |

Dazu eine feste **Schlusszeile**, immer wortgleich:

> Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.

Ohne sie schreibt die KI «ß». Mehr dazu im [Prompt-Cheatsheet](../04-materialien/cheatsheet-prompts.adoc).

### Skills

Ein **Skill** ist eine kurze Anweisung, die eine Arbeitsweise vorgibt, zum Beispiel «erst Fragen stellen» (`grilling`) oder «erst den Test schreiben» (`tdd`). Du hast sie in der Vorbereitung installiert. Aufruf:

- **OpenCode:** im Prompt «Nutze den Skill `grilling`.»
- **Claude Code:** `/mattpocock-skills:grilling` (oder dieselbe Formulierung)

Die Slash-Commands aus Modul 2 und 3 (`/erklaere`, `/debug`, `/verbessere`) kennst du schon. Skills sind die nächste Stufe davon: weniger ein Befehl, mehr eine Arbeitsweise.

### Der 3-Punkte-Check

Nach **jedem** KI-Schritt, bevor du weitermachst («Vertrauen, aber prüfen»):

1. **Läuft es?** Programm und Tests ausführen.
2. **Passt es zu `plan.md`?** Signatur, Rückgabe, Randfälle.
3. **Wurde etwas Ungefragtes geändert?** Diff ansehen.

---

## 4. Live-Demo: `grilling` auf dem Wetterbericht (10 Minuten)

Wir wollen den Wetterbericht um einen Städtevergleich erweitern: `vergleiche_staedte(zeilen_a, zeilen_b)` (Temperaturdifferenz, nässere Stadt). Bevor die KI Code schreibt, klären wir, was genau gemeint ist.

**Schritt 1: Code erklären lassen** (ändert nichts)

```text
Kontext: Ich arbeite im Projekt `wetter_bericht.py` (Wetterbericht für Schweizer Städte, CSV und Open-Meteo).
Aufgabe: Erkläre mir den Aufbau der Datei: Welche Funktionen gibt es, wer ruft wen auf, was ist reine Berechnung und was Ein-/Ausgabe? Ändere nichts.
Format: Liste mit einem Satz pro Funktion.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

*Während die KI arbeitet:* Lies mit. Welche Funktionen sind «rein» (nur Rechnung)? Das wird heute wichtig.

**Schritt 2: Mit `grilling` befragen lassen**

```text
Nutze den Skill `grilling`.
Kontext: Ich will `wetter_bericht.py` um `vergleiche_staedte(zeilen_a, zeilen_b)` erweitern (Temperaturdifferenz, nässere Stadt).
Aufgabe: Befrage mich, bis jede Annahme geklärt ist. Stelle die Fragen runde um Runde, ändere nichts am Code.
Format: nummerierte Fragen, je mit deiner empfohlenen Antwort.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

*Während die KI arbeitet:* Sage voraus, welche Frage als Nächstes kommt.

---

## 5. KI-Moment: Was die KI nicht wissen kann

Die KI stellt Fragen, die der Code **nicht beantwortet**. Zum Beispiel: «Was heisst *nässer*: mehr Regentage oder mehr Millimeter?» Das kann sie aus `wetter_bericht.py` nicht ablesen. Sie schlägt eine Antwort vor, **du entscheidest**.

Das ist der Kern von Planen mit einem Agenten: Die Entscheidungen, die nur du treffen kannst, gehören in den Plan, bevor Code entsteht. Sonst entscheidet die KI still für dich.

---

## 6. Übung 1 (15 Minuten)

Gehe das `grilling`-Gespräch selbst durch und halte das Ergebnis in `plan.md` fest. Die Aufgabe steht in [ex-01-plan.adoc](../02-uebungen/ex-01-plan.adoc).

Danach der Prompt, der den Plan festhält:

```text
Kontext: Wir haben `vergleiche_staedte` besprochen.
Aufgabe: Fasse das Ergebnis in `plan.md` zusammen: Ziel, Signatur, Rückgabe-Schlüssel, Definition von «nässer», Randfälle, was nicht zum Feature gehört. Ändere keinen Code.
Format: Markdown mit kurzen Abschnitten.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

Wende danach den **3-Punkte-Check** auf `plan.md` an. Besonders Punkt 3: Hat die KI Code angefasst?

**Wer nicht mitgekommen ist:** Kopiere `05-beispiele/lektion-1/loesung/` und lies `plan.md`. Das ist der Startstand für Lektion 2.

---

## 7. Kür (5 Minuten)

Schärfe dein `plan.md` nach: Welche Annahme steht noch nicht drin? Oder plane ein zweites Feature (zum Beispiel «die drei regenreichsten Tage»).

---

## Dozentenhinweise

- **Zeitnot:** Zuerst entfällt die Kür. `grilling` mit `plan.md` bleibt immer.
- **Probelauf (2026-10-27, Claude Code 2.1.311, Wetterbericht-Kopie):** Code erklären, `grilling` (zwei Runden, 10 Fragen) und `plan.md` laufen durch, je Schritt ca. 20 Sekunden, der Code blieb unverändert. Beobachtungen: Die KI stellt die «nässer»-Frage von selbst (KI-Moment trägt). Sie schlägt unbestellt `waermere_stadt`, Tests und eine Anbindung an `main` vor; im Plan landete ausserdem ein erfundenes Beispiel (`Zürich`/`Lugano`: `-2.3`, Lugano nässer; echt sind `-1.2` und Zürich). Das ist ein zweiter, ungeplanter KI-Moment: Beispielwerte gegen die CSV prüfen. Geprüft nur in Claude Code, nicht in OpenCode.
- **Zeit:** Zehn Fragen in zwei Runden sind für 15 Minuten knapp. Bei Bedarf im Prompt ergänzen: «Höchstens 6 Fragen insgesamt.»
- **Rate-Limit:** Ab dem zweiten Limit-Fehler im Pair arbeiten, Konserve zeigen: [`konserven/ki-moment-1-annahmen.md`](../05-beispiele/konserven/ki-moment-1-annahmen.md).
- **Musterlösung:** `05-beispiele/lektion-1/loesung/` (enthält `plan.md`).

---

*Datei: `01-praxis/lektion-1-arbeitsweise-planen.md`*  
*Zurück zum Modul: [Modul 4](../README.md)*
