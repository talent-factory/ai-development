# Lektion 2: Test-Driven Development mit dem Agenten

**Dauer:** 50 Minuten (19:00–19:50)  
**Ziel:** Erst den Test, dann den Code: Das Verhalten des bestehenden Codes mit Tests festhalten und `vergleiche_staedte` test-first bauen.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–5 | **Rückblick** («Was lief, was hakt?»), Startstand holen | Gespräch |
| 5–15 | **Input:** rot-grün-Zyklus, Demo `tdd` | Vortrag + Demo |
| 15–20 | **KI-Moment:** derselbe Auftrag ohne und mit `tdd` | Demo + Mitmachen |
| 20–40 | **Übung 2:** Tests und `vergleiche_staedte` ([ex-02](../02-uebungen/ex-02-tdd.adoc)) | Einzelarbeit |
| 40–45 | **Kür** (freiwillig) | Einzelarbeit |
| 45–50 | **Puffer** | |

---

## 1. Rückblick und Startstand (5 Minuten)

Eine Runde: «Was lief, was hakt?» Keine Aufgabe.

**Startstand:** Kopiere `05-beispiele/lektion-1/loesung/` (Code, Daten und `plan.md`). Das gilt für alle, auch wenn du schon ein eigenes `plan.md` hast. So starten wir alle vom gleichen Stand.

---

## 2. Rot, grün, aufräumen (10 Minuten)

Test-Driven Development (TDD) in drei Schritten:

```text
ROT      Test schreiben, der fehlschlägt (die Funktion kann es noch nicht)
GRÜN     Gerade so viel Code schreiben, dass der Test besteht
AUFRÄUMEN  Code verbessern, Tests bleiben grün
```

Immer **ein** Test nach dem anderen. Ein Test, der nie rot war, beweist nichts.

Tests führen wir mit `pytest` aus:

```bash
uv run pytest
```

Wir testen nur **reine Funktionen** (`berechne_kennzahlen`, `beschreibe_wetter`, `vergleiche_staedte`). Datei-, Bildschirm- und Live-Abruf-Code bleibt ungetestet.

**Demo:** Wir bauen die ersten beiden Tests für `vergleiche_staedte` mit dem Skill `tdd`:

```text
Nutze den Skill `tdd`.
Kontext: Plan in `plan.md`, Funktion `vergleiche_staedte` gibt es noch nicht.
Aufgabe: Baue sie test-first, ein Test nach dem anderen: Test schreiben, rot zeigen, minimalen Code schreiben, grün zeigen. Ändere keine anderen Funktionen.
Format: nach jedem Schritt die Ausgabe von `pytest`.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

*Während die KI arbeitet:* Sage voraus, ob der nächste Test rot oder grün wird.

---

## 3. KI-Moment: Der Test, der nie rot wird (5 Minuten)

Derselbe Auftrag, einmal **ohne** Skill:

```text
Kontext: Projekt `wetter_bericht.py`, Datei `test_wetter_bericht.py` (pytest).
Aufgabe: Schreibe Tests für `berechne_kennzahlen`.
Format: eine Testdatei, nur der Code.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

Die KI schreibt viele Tests auf einmal, und sie sind **sofort grün**. Sie hat den Code gelesen und prüft, was er schon tut. Grün sagt dann wenig: Ein Test, der nie rot war, hat noch nie etwas bemerkt.

**Mutationsprobe (2 Minuten):** Verändere den Code absichtlich und schau, ob die Tests es merken. Ändere in `berechne_kennzahlen` bei den Regentagen `> 0` zu `>= 0`:

```python
"regentage": sum(1 for z in zeilen if z["niederschlag_mm"] >= 0),
```

Läuft `uv run pytest` jetzt rot? Dann hätte der Test den Fehler bemerkt. Bleibt er grün, taugt er nichts. (Danach die Änderung zurücknehmen.)

Zwei Dinge fallen oft auf:

- **Zu viel:** Die KI schreibt Tests für Fälle, die niemand bestellt hat (zum Beispiel `beschreibe_wetter(None)` oder einen `TypeError` bei einer Liste). Das schreibt Zufall als Vertrag fest. Streiche, was du nicht willst.
- **Ungeprüft:** Darf die KI `pytest` nicht ausführen, schreibt sie die Tests trotzdem und sagt, sie seien nicht getestet. Führe sie selbst aus.

Mit `tdd` ist die Reihenfolge umgekehrt: Der Test entsteht **vor** dem Code und muss zuerst rot sein. So kommt jeder Test mit seinem eigenen Beleg, dass er etwas prüft.

---

## 4. Übung 2 (20 Minuten)

Zwei Teile (siehe [ex-02-tdd.adoc](../02-uebungen/ex-02-tdd.adoc)):

1. **Ist-Verhalten festhalten:** Tests für `berechne_kennzahlen` und `beschreibe_wetter`. Auch ein Code ohne Klartext (zum Beispiel `1`) wird festgehalten, wie er **heute** ist (`"unbekannt"`).

```text
Kontext: Projekt `wetter_bericht.py`, Datei `test_wetter_bericht.py`.
Aufgabe: Schreibe Tests, die das heutige Verhalten von `beschreibe_wetter` festhalten, auch bei unbekannten Codes (heute «unbekannt»). Ändere den Code nicht.
Format: ein Test pro Fall, kurze Namen auf Deutsch.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

2. **`vergleiche_staedte` test-first** nach `plan.md`, mit dem Skill `tdd`.

Nach jedem Schritt der **3-Punkte-Check**: Läuft `pytest`? Passt es zum Plan? Was hat die KI sonst noch geändert?

**Wer nicht mitgekommen ist:** Kopiere `05-beispiele/lektion-2/loesung/`.

---

## 5. Kür (5 Minuten)

Schreibe einen Test für den Randfall `berechne_kennzahlen([])` (heute wirft die Funktion einen `ValueError`).

---

## Dozentenhinweise

- **Zeitnot:** Kür entfällt zuerst. `tdd` bleibt immer.
- **Freigabe:** Die KI fragt beim ersten `pytest`-Aufruf um Erlaubnis. Erlauben, für die Sitzung merken. Ohne Freigabe kann `tdd` nicht «rot zeigen» und hält an.
- **Probelauf (2026-10-27, Claude Code 2.1.311):** Tests ohne Skill: 14 Tests in ca. 45 s, sofort grün; die Mutationsprobe (`> 0` zu `>= 0`) färbt 3 Tests rot, sie taugen also. `tdd`: sechs saubere Zyklen (rot, grün) in ca. 80 s, nur `vergleiche_staedte` ergänzt, 19 Tests grün. Die KI rechnet die Durchschnitte selbst nach statt `berechne_kennzahlen` zu nutzen: typischer Fund für Lektion 3.
- **Rate-Limit:** Pair, Konserve zeigen: [`konserven/ki-moment-2-test-ohne-tdd.md`](../05-beispiele/konserven/ki-moment-2-test-ohne-tdd.md).
- **Musterlösung:** `05-beispiele/lektion-2/loesung/` (13 Tests grün).

---

*Datei: `01-praxis/lektion-2-tdd.md`*  
*Zurück zum Modul: [Modul 4](../README.md)*
