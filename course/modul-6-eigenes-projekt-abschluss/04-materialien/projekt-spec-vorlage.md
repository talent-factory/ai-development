# Projekt-Spec: Vorlage und Grilling-Prompt

**Ziel des Abends:** Du schreibst für dein eigenes Projekt eine `SPEC.md`, mit der ein Coding-Agent (Claude Code oder OpenCode) in Etappen loslegen kann. Es entsteht noch kein fertiges Produkt. Wichtig ist, dass die Spec **klein genug** und **prüfbar** ist.

Der Ablauf ist derselbe wie in Modul 4: Plan → Test → Code → Review → Doku. Heute machst du den ersten Schritt für dein Projekt.

---

## Schritt 1: Idee in einem Satz (5 Minuten)

Fülle den Satz aus:

> Ich baue **[was]** für **[wen]**, damit **[Nutzen]**. Fertig ist es, wenn **[Beweis]**.

Beispiel: «Ich baue einen Chat über meine Kursunterlagen für mich selbst, damit ich Antworten mit Quelle finde. Fertig ist es, wenn 5 Testfragen richtig beantwortet werden und die Fallen-Frage «Ich finde dazu nichts» ergibt.»

### Schnelltest (3 Fragen)

1. **Daten:** Woher kommen sie, und darf ich sie verwenden? (Datei, offene API, selbst erfunden)
2. **Aufwand:** Läuft ein erster Prototyp in 3 Stunden? Wenn nein: Was streiche ich?
3. **Nutzen:** Wer würde es wirklich öffnen, und wozu?

---

## Schritt 2: Grilling-Prompt (15 Minuten)

Starte deinen Agenten im leeren Projektordner und gib ihm diesen Prompt (Skill `grilling`):

```text
Nutze den Skill grilling.

Kontext: Ich plane ein kleines KI-Projekt als Abschluss eines Python-Kurses
(Streamlit-Oberfläche, Python, Gemini über Pydantic AI, Bausteine aus dem Kurs:
Dateien/CSV/JSON/APIs, Tests, Embeddings, Mini-RAG).
Meine Idee in einem Satz: <DEIN SATZ>

Aufgabe: Stelle mir Fragen, EINE nach der anderen, bis die Spec eindeutig ist.
Hake nach, wenn eine Antwort vage ist. Frage insbesondere nach:
Datenquelle und Erlaubnis, was ausdrücklich NICHT zum Projekt gehört,
Randfällen, wie wir merken, dass es richtig funktioniert (Testfragen),
und was in 3 Stunden realistisch ist.
Schlage nichts vor, was ich nicht bestellt habe. Schreibe noch keinen Code.

Format: Wenn ich «fertig» sage, fasse alles in SPEC.md nach der Gliederung unten zusammen.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

**Danach prüfen (3-Punkte-Check):**

1. Steht in der Spec, was **ich** entschieden habe, und nicht, was die KI erfunden hat?
2. Sind Zahlen und Beispiele echt oder erfunden? Rechne eines nach.
3. Hat die KI etwas Ungefragtes dazugenommen? Streiche es.

---

## Schritt 3: Gliederung von `SPEC.md`

```markdown
# <Projektname>

## 1. Idee
Ein Satz: was, für wen, Nutzen, Fertig-Kriterium.

## 2. Nicht-Ziele
Was baue ich ausdrücklich nicht? (mindestens 3 Punkte)

## 3. Daten
Quelle, Format, Umfang, Erlaubnis/Lizenz. Mock-Daten klar als «Demo» kennzeichnen.

## 4. Architektur
Skizze in 5 Zeilen: Eingabe → Verarbeitung → Ausgabe. Welche Kursbausteine nutze ich?
(CSV/JSON/API · Embeddings/Suche · Mini-RAG `beantworte` · Streamlit)

## 5. Meilensteine
| # | Ergebnis | Woran erkenne ich, dass es fertig ist? |
|---|----------|----------------------------------------|
| 1 | Walking Skeleton: läuft lokal, noch ohne KI | Streamlit zeigt etwas an |
| 2 | ... | ... |
| 3 | ... | ... |

## 6. Testfragen
5 bis 10 Fragen mit erwarteter Antwort. Mindestens:
- eine Frage mit klarer Antwort,
- eine **Fallen-Frage**, die nicht beantwortbar sein darf,
- eine Frage, bei der die Technik scheitern könnte.

## 7. Risiken und Verantwortung
- Datenschutz: Welche Personendaten fliessen an ein Modell?
- Rechte: AGB der Quelle, Lizenz von Bildern/Texten.
- Halluzination: Wie zeige ich Quelle und Unsicherheit?
- Kosten und Schlüssel: `.env`, nie ins Repo.

## 8. Offene Fragen
Was weiss ich noch nicht?
```

---

## Beispiel für Abschnitt 7: Rechte und AGB (Too Good To Go)

> **Fall:** Eine App soll Überraschungspakete bei Too Good To Go automatisch finden.
>
> - **Offizielle API:** nicht gefunden. Es gibt nur inoffizielle Nachbauten der App-Schnittstelle (z. B. `tgtg-python`, Stand der Recherche: November 2026).
> - **Technisch fragil:** Der Bot-Schutz blockt immer wieder (403-Fehler, Login scheitert). Eine Spec, die davon abhängt, ist ein Risiko für den Zeitplan.
> - **AGB:** Die Nutzungsbedingungen verbieten laut Quellen automatisierten Zugriff und Scraping. Mögliche Folge: Sperre des Kontos. Den Wortlaut der deutschen und der Schweizer Fassung musst du selbst auf toogoodtogo.com unter «Legal» lesen. Das ist keine Rechtsberatung.
> - **Saubere Lösung für das Kursprojekt:** Eine eigene Mock-API (JSON-Datei oder kleines FastAPI) im gleichen Format, dahinter eine austauschbare Schnittstelle. Alternativ erfasst du die Abholzeiten von Hand und baust Benachrichtigungen (Telegram, ntfy) darauf.
> - **In die Spec gehört:** Die echte Anbindung steht unter «Nicht-Ziele» oder «Offene Fragen», mit dem Grund.
>
> **Übertrag auf dein Projekt:** Prüfe bei jeder Datenquelle: Gibt es eine offizielle Schnittstelle? Was sagen die AGB? Was passiert, wenn der Zugriff morgen blockiert wird?

---

## Schritt 4: Machbarkeits-Check (L3, Walking Skeleton)

Mit der Spec startest du Meilenstein 1:

```text
Lies SPEC.md. Setze NUR Meilenstein 1 um: eine minimale Streamlit-App ohne KI-Aufruf.
Schreibe zuerst einen Test für die Kernfunktion, dann den Code. Ändere nichts anderes.
Antworte auf Deutsch, Schweizer Rechtschreibung, ss statt ß.
```

Läuft `uv run streamlit run app.py`, ist die Spec nicht nur schön, sondern auch tragfähig.

---

## Schritt 5: Peer-Review (L4)

Pitch zu zweit, je 3 Minuten, dann 3 Minuten Gegenfragen. Die Partnerin oder der Partner prüft:

1. Verstehe ich in einem Satz, was gebaut wird?
2. Ist der Umfang in 3 Stunden machbar?
3. Welche Testfrage würde das Projekt am ehesten zum Scheitern bringen?
4. Welches Risiko aus Abschnitt 7 fehlt?
