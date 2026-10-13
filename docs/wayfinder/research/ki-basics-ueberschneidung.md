# Ticket 10: KI-Basics-Überschneidung für Modul 2

**Frage:** Was haben die KI-Basics (Sabine Jungk, KI Professional, Modul 1) zu Prompting, KI-Antworten prüfen und Halluzinationen schon vermittelt? Was darf Modul 2 (Python lesen/verstehen, KI Code erklären lassen) voraussetzen, was muss es neu oder anders vertiefen?

**Stand:** 2026-10-09

## Quellen und Kürzel

| Kürzel | Datei in `bibliography/` | Seiten |
|---|---|---|
| **PB** | `Prompting-Basics_Handout_2026.pdf` (Übungsunterlage zu Hause, Ausgabe Sept. 2026) | 5, komplett gelesen |
| **KB2** | `KI Professional - Modul 1 KI Basics 22.09.26_2HT.V1.Handout.pdf` (2. Halbtag, Folien) | 74, Text komplett durchsucht, Kernfolien (3, 13, 38-50, 57-60, 64) gelesen |
| **KB1** | `KI Professional - Modul 1 KI Basics 15.09.26.V1.Handout.pdf` (1. Halbtag, Folien) | 53, Text komplett durchsucht, Treffer gelesen |

Seitenzahlen sind PDF-Seiten (nicht die aufgedruckten Foliennummern). Nicht ausgewertet: `You & AI ...pdf` (Buch) und `ki-grundlagen-quiz.html`, weil das Ticket nur Handouts nennt.

## Kurzfazit

1. Die KI-Basics vermitteln **Prompting allgemein und branchenneutral** (Business-Texte, Berichte, E-Mails). Sie vermitteln **kein** Prompting für Code.
2. Prüfen von KI-Antworten ist nur **als Haltung** vorhanden («Verifikations-Check», Mensch trägt Verantwortung). Es gibt **keine Methode, wie man Code prüft** (ausführen, testen, Fehlermeldung lesen).
3. Halluzinationen sind **als Begriff eingeführt und als Risiko benannt**, aber nur sehr knapp: eine Erwähnung in PB und eine Folie zu Agenten in KB1.
4. **Python, Programmieren und Code kommen in keinem der drei Dokumente vor** (Volltextsuche nach «Python», «Programm», «Code»: nur Treffer ausserhalb des Themas, siehe unten). Modul 2 kann also keinerlei Code-Vorwissen aus den KI-Basics ableiten.
5. Die Zielgruppe ist Business-Weiterbildung (IBAW, «Lehrgang KI Professional - Business», KB2 S. 1, S. 74). Ob dieselben Teilnehmenden Modul 2 besuchen, ist aus den Handouts nicht ersichtlich und im Ticket nicht geklärt (siehe offene Punkte).

## 1. Prompting: was vermittelt wurde

### Grundprinzipien (PB)
- Fünf Kernprinzipien: klar und deutlich sein, Kontext und Motivation liefern, spezifisch sein, mit Beispielen arbeiten (Zero-/One-/Few-Shot), Unsicherheit zulassen (PB S. 1-2).
- Fortgeschrittene Techniken: Prefilling, Chain-of-Thought («Denke Schritt für Schritt»), Ausgabeformat steuern, Prompt Chaining (Entwurf, Kritik, Überarbeitung) (PB S. 2-3).
- «Was heute weniger wichtig ist»: XML-Tags und starre Rollenvorgaben (PB S. 3).
- Exkurs mit Begriffen aus dem Google-Whitepaper: System-Prompting, Self-Consistency, ReAct, Prompt-Journal (PB S. 3).
- Fehlerbehebungstabelle und «Häufige Fehler» (PB S. 3-4); sechs Übungen mit Prompt-Journal (PB S. 4-5). Alle Übungsbeispiele sind Alltag/Business (Dashboard, Projektplan ITSM, Kunden-E-Mail, Social-Media-Post, Break-even-Rechnung, interne Ankündigung). Das einzige quasi-technische Beispiel ist JSON-Prefilling (PB S. 2).

### Folien (KB2)
- «Was sich beim Prompten geändert hat»: weg von langen Rollenbeschreibungen und Prompt-Formeln, hin zu Auftrag und Erfolgskriterien; «Kontext schlägt Formulierung»; «Weniger Prompt = besser» (KB2 S. 41).
- Sieben Regeln: Ergebnis statt Ablauf, Kontext statt Adjektive, Begründen statt verbieten, positiv formulieren, Struktur sichtbar machen (XML-Tags bei Claude, Überschriften bei ChatGPT), Beispiele statt Stilbeschreibungen, Widersprüche entfernen (KB2 S. 42-43). Schlusssatz: «Weglassen ist 2026 die wichtigste Prompt-Technik.»
- Sieben Bausteine eines Masterprompts: Rolle und Kontext, Auftrag, Erfolgskriterien, Leitplanken, Material, Ausgabeformat, Rückfrage-Regel; Meta-Prompt («Stelle mir fünf Fragen ...») (KB2 S. 45); Beispiel Masterprompt (KB2 S. 46).
- Modellvergleich ChatGPT vs. Claude (KB2 S. 47), Übungen Prompt-Diät, Masterprompt, Kopf an Kopf (KB2 S. 48), Checkliste vor dem Absenden (KB2 S. 49).
- Modellvergleich als Aufgabe: gleicher Prompt in mehreren Modellen, Antworten vergleichen und bewerten (KB2 S. 38).

### Hinweis auf Unstimmigkeiten zwischen den Unterlagen
PB und KB2 sind nicht deckungsgleich: PB empfiehlt Chain-of-Thought und Few-Shot als Techniken und nennt starre Rollen «weniger wichtig» (PB S. 2-3). KB2 setzt «Rolle und Kontext» als ersten Baustein und «Rolle und Erfolgskriterien nennen» für ChatGPT (KB2 S. 45, 47) und sagt «weniger Prompt = besser» (KB2 S. 41). Teilnehmende haben also zwei leicht verschiedene Prompt-Rezepte gesehen. Modul 2 sollte sich auf **eine** Grundregel beziehen, die in beiden steht: «Auftrag klar, Kontext und Begründung liefern, Beispiele geben, Überflüssiges weglassen».

## 2. KI-Antworten prüfen und Halluzinationen: was vermittelt wurde

| Thema | Was die Unterlagen sagen | Quelle |
|---|---|---|
| Halluzination als Begriff | «erfundene Antworten (sogenannte Halluzinationen)», Gegenmittel: der KI erlauben «ich weiss es nicht» zu sagen; Beispielsatz «Wenn die vorliegenden Daten nicht ausreichen, ..., sage das explizit, statt zu raten.» | PB S. 2 |
| Fehlerbehebung | Zeile «KI erfindet Informationen»: «Sage, wenn du es nicht weisst, statt zu raten.» | PB S. 3 |
| Halluzination bei Agenten | «Agenten können plausibel klingende, aber falsche Ergebnisse produzieren.» Merksatz: je mehr ein Agent darf, desto wichtiger Kontrolle, Zugriffsrechte, Governance | KB1 S. 29 |
| Grundmechanismus | «Stochastischer Papagei»: Modell setzt Muster nach Wahrscheinlichkeit fort, «der Schein von Kompetenz» bleibt gültig | KB2 S. 13 |
| Verifikations-Check | «Kann ich das Ergebnis unabhängig prüfen, ohne der Maschine blind zu glauben?» (Teil der 5 Leitfragen: Daten, Impact, Verifikation, Transparenz, Human) | KB2 S. 64 |
| Verantwortung | KI gilt juristisch als Werkzeug; «Die KI hat das entschieden» ist keine zulässige Ausrede; Human-in-the-Loop, namentlich zuständige Person | KB2 S. 59-60 |
| Bilder prüfen | Quelle prüfen, Rückwärtssuche (Google Lens, TinEye), Beispiel «Explosion beim Pentagon» | KB1 S. 40 |
| Bias | Modelle schwer erklärbar, unerkannte Verzerrungen | KB1 S. 42 |
| Kognitive Auslagerung | MIT-Studie 2025 (Preprint): wer KI schreiben lässt, behält weniger; Tipp «Zuerst selbst denken, dann KI nutzen» | KB2 S. 3; Diskussionsfolie KB1 S. 53 |
| Tipps ohne Fachbezug | Checkliste vor dem Absenden enthält nur Prompt-Qualität und Datenschutz, keine Prüfschritte für die Antwort | KB2 S. 49 |

**Was fehlt:** Es gibt keine Folie und keinen Absatz, der erklärt, *wie* man eine Antwort prüft (Gegenrecherche, Quellen verlangen, Stichproben, Plausibilitätscheck). Halluzination wird nirgends definiert oder mit einem echten Fehlerbeispiel gezeigt. Der Lösungshinweis zu Übung 5 (Break-even) ist der einzige Ort, an dem ein Resultat nachgerechnet wird (PB S. 5). Das ist sinngemäss der einzige «Prüf»-Moment in den Übungen.

## 3. Code und Python: was nicht vermittelt wurde

- Volltextsuche in beiden grossen Handouts nach «Python», «Programmier», «Quellcode»: nur drei irrelevante Treffer («programmiert zu werden» in KB2, «Quellcode» im Zusammenhang mit Erklärbarkeit nach DSG, `XAI` in KB2 S. 57). Kein Code-Beispiel, kein Hinweis auf Coding-Assistenten, kein Code-Block.
- Einzige technische Berührungspunkte: JSON-Prefilling als Format-Trick (PB S. 2), «ReAct»/Werkzeugaufruf als Agenten-Prinzip (PB S. 3; KB1 S. 27-29), Token/Kontextfenster (KB2 S. 16-18), Maschinelles Lernen (KB2 S. 21-24). Alles Konzeptebene.
- Agenten werden als Konzept und Risiko behandelt (KB1 S. 25-29), nicht als Werkzeug, mit dem man Code schreibt.

## 4. Konsequenzen für Modul 2

### Darf Modul 2 voraussetzen
- Begriffe: Prompt, Kontext, Beispiel (One-/Few-Shot), Prompt Chaining, Chain-of-Thought, Token/Kontextfenster, Halluzination (Begriff), Modell-Vergleich ChatGPT/Claude/Gemini.
- Haltung: «Ich bin verantwortlich, nicht die KI» (KB2 S. 59-60) und «nicht blind glauben» (KB2 S. 64). Daran kann Modul 2 anknüpfen («Das gilt für Code genauso»), muss es aber nicht neu begründen.
- Praxis: Teilnehmende haben mindestens ein KI-Tool aktiv genutzt und eigene Prompts verglichen (KB2 S. 32, 38, 48; PB S. 4-5). Zugang zu mindestens einem Chatbot-Konto ist plausibel, aber nicht bestätigt.
- Erwartung: Prompts dürfen kurz und zielorientiert sein; Prompt-Journal als Lernform ist bekannt (PB S. 3-4).
- Datenschutz-Grundregel: keine Personendaten und Geschäftsgeheimnisse in Prompts (KB2 S. 48-49). Relevant, sobald Teilnehmende Code oder Daten in ein Chatfenster kopieren.

### Muss Modul 2 neu oder anders vertiefen
1. **Code prüfen statt Text prüfen.** KI-Code lässt sich (anders als Fliesstext) ausführen: Programm starten, Fehlermeldung lesen, mit bekannten Eingaben testen. Das ist die konkrete Umsetzung des «Verifikations-Checks» (KB2 S. 64), die in den KI-Basics fehlt. Der Break-even-Nachrechnen-Moment (PB S. 5) ist ein guter Anknüpfungspunkt (Ergebnis erwartbar, also prüfbar).
2. **Halluzination bei Code konkret zeigen.** Erfundene Funktionen/Bibliotheken, veraltete Syntax, Code, der sauber aussieht und falsch rechnet. Die KI-Basics geben den Begriff, nicht das Gefühl dafür.
3. **Code erklären lassen als eigene Prompt-Technik.** «Erkläre Zeile für Zeile», «Was passiert bei Eingabe X?», Rückfragen an die KI. Die sieben Bausteine (KB2 S. 45) lassen sich übertragen (Kontext = Vorwissen des Lernenden; Ausgabeformat = Schritt für Schritt; Rückfrage-Regel), aber das muss gezeigt werden, die Teilnehmenden werden es nicht selbst übertragen.
4. **Lesen vor Prompten.** Die KI-Basics lehren Schreiben des Prompts. Modul 2 braucht die umgekehrte Fähigkeit: Code lesen, verstehen, Erklärungen der KI gegen den Code abgleichen. Dafür gibt es kein Vorwissen.
5. **Fachbegriffe im Prompt.** Business-Prompting kommt ohne Programmiersprache aus. Teilnehmende wissen nicht, wie man Fehlermeldung, Python-Version oder Codeausschnitt sinnvoll in einen Prompt gibt (Material nach oben, Frage ans Ende, KB2 S. 43/47 als Startpunkt).
6. **Eigene Lernkontrolle trotz KI.** Die MIT-Studie (KB2 S. 3, KB1 S. 53) liefert das Argument «erst selbst denken, dann KI»; Modul 2 sollte es für Code ausspielen (Vorhersage, was der Code tut, bevor man die KI fragt), da Code zum Verstehen, nicht zum Abgeben gedacht ist.

### Auf was Modul 2 verzichten kann
- Eine eigene Einführung «Was ist ein Prompt, Zero/One/Few-Shot, Chain-of-Thought»: nur verlinken.
- Eine erneute Begründung von Verantwortung und Human-in-the-Loop: kurz verweisen.

### Empfohlene Formulierung im Modul-2-Material
Wo Modul 2 auf KI-Basics verweist, jeweils konkret nennen: «Prompting-Basics_Handout (Prinzipien 1-5)», «KI-Basics Halbtag 2 (sieben Bausteine)», «Verifikations-Check». So lassen sich Doppelungen vermeiden und Lücken sichtbar halten.

## Offene Punkte
- Ist die Zielgruppe von Modul 2 dieselbe wie die der KI-Professional-Kohorte (IBAW, Business)? Die Handouts richten sich an Business-Lernende; ob sie Voraussetzung für Modul 2 sind, steht in keinem Dokument.
- Das Handout «15.09.26» (KB1) trägt auf der Titelfolie das Datum 22.09.26 (KB1 S. 2) und ist daher vermutlich ein Revisionsstand, nicht zwingend der Stand des tatsächlichen Halbtags. Für die Auswertung unerheblich.
- Nicht gelesen wurden die Seiten 5-40 von KB2 im Detail (Technik/Funktionsweise); Volltextsuche nach Prompting-, Prüf- und Halluzinationsbegriffen hat dort keine weiteren relevanten Treffer ergeben, aber Folieninhalte, die nur als Bild vorliegen, würden dabei fehlen (die Textextraktion enthielt auf einigen Folien nur Fragmente, z. B. KB2 S. 44, 50, 52, 53).
- Das gesprochene Wort der Dozentin (z. B. mündliche Hinweise auf Halluzinationen) ist aus den Handouts nicht erkennbar.
