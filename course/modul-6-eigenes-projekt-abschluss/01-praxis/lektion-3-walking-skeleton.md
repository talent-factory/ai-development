# Lektion 3: Walking Skeleton

**Dauer:** 50 Minuten (20:00–20:50)  
**Ziel:** Mit Meilenstein 1 zeigen, dass die Spec tragfähig ist: eine minimale Streamlit-App mit erstem Test.

---

## Ablauf

| Zeit | Aktivität | Methode |
| ---- | --------- | ------- |
| 0–10 | **Input:** Streamlit in 10 Minuten (`st.title`, `st.text_input`, `st.session_state`) | Live-Demo |
| 10–40 | **Schritt 4:** Meilenstein 1 mit dem Agenten, test-first | Einzelarbeit |
| 40–47 | **KI-Moment:** Läuft es? Passt es zur Spec? Wurde Ungefragtes geändert? | Gespräch |
| 47–50 | Puffer | |

---

## 1. Streamlit in 10 Minuten

Kein neues Thema, sondern das Werkzeug für die Oberfläche. Grundlage ist [streamlit.adoc](./archive/streamlit.adoc) und der Anschluss an die `Antwort` aus Modul 5 (`text`, `sicherheit`, `quelle`).

> TODO Dozent: kleines Live-Beispiel wählen, das zu den drei Archetypen passt. `05-beispiele/archive/chatbot.py` ist veraltet (LangChain, OpenAI) und taugt nicht als Vorlage.

## 2. Meilenstein 1 (30 Minuten)

Prompt aus Schritt 4 der [Vorlage](../04-materialien/projekt-spec-vorlage.md). Start mit `uv run streamlit run app.py`.

Mindestziel: Die App läuft lokal, es gibt mindestens einen grünen Test für die Kernfunktion, und die KI hat nur Meilenstein 1 angefasst (`git status` und Diff prüfen).

> TODO Dozent: Fallback festlegen für Teilnehmende, die nicht bis zur lauffähigen App kommen: Abschnitt «Offene Fragen» der Spec ergänzen statt Code erzwingen.

## 3. Wenn es nicht läuft

Das ist ein Befund über die Spec, kein Misserfolg. Notiere, was fehlte, und passe `SPEC.md` an.
