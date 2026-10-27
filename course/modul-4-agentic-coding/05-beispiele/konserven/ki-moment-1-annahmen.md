# Konserve 1: `grilling` fragt nach Annahmen

*Echte Ausgabe von Claude Code 2.1.311 (2026-10-27) auf einer Kopie des Wetterberichts, Runde 1 von 2, leicht gekürzt. Prompt wie in Lektion 1.*

❓ **Q1 – Reine Funktion oder mit Ein-/Ausgabe?** Soll `vergleiche_staedte` wie `berechne_kennzahlen` nur ein Ergebnis zurückgeben oder auch ausgeben oder speichern?

➡️ Rein. Die Funktion gibt ein `dict` zurück, kein `print`, kein Schreiben.

❓ **Q2 – Wie sind Stadtnamen im Ergebnis bekannt?** Aus `zeilen_a[0]["stadt"]` lesen oder zusätzliche Parameter?

➡️ Namen aus den Zeilen lesen, die Signatur bleibt.

❓ **Q3 – Welche Temperatur wird verglichen?** a) nur `tmax_durchschnitt`, b) `tmin` und `tmax` getrennt, c) Mittel aus beiden pro Tag.

➡️ a) Eine Zahl, A minus B, auf eine Nachkommastelle gerundet.

❓ **Q4 – Was bedeutet «nässer»?** Gesamtniederschlag in mm oder Anzahl Regentage? Und was gilt bei Gleichstand?

➡️ `niederschlag_gesamt_mm`; bei Gleichstand `None`.

❓ **Q5 – Ungültige oder ungleiche Eingaben:** leere Listen, unterschiedlich viele Tage, unterschiedliche Datumsbereiche. Soll die Funktion das prüfen?

➡️ Leere Liste: `ValueError` mit verständlicher Meldung. Rest nicht prüfen.

❓ **Q6 – Berechnung wiederverwenden?** `berechne_kennzahlen` zweimal aufrufen oder neu rechnen?

➡️ Wiederverwenden.

*(Runde 2 fragte danach nach den Schlüsseln des Ergebnisses, dem Ort der Prüfung auf leere Listen, der Anbindung an `main` und nach Tests.)*

---

**Auswertung:**

- Q3 und Q4 kann der Code nicht beantworten. Das sind *deine* Entscheidungen. Hätte die KI sie still getroffen, hättest du es erst im Ergebnis gemerkt.
- In Runde 2 schlug die KI unbestellt einen Schlüssel `waermere_stadt`, Tests und die Anbindung an `main` vor. Prüfe immer: **Gehört das zu meinem Plan?**
- Im ersten `plan.md` stand ein Beispiel `Zürich`/`Lugano` mit `tmax_differenz: -2.3` und Lugano als nässerer Stadt. Die echten CSV-Werte sind `-1.2` und Zürich. Die KI hat das Beispiel erfunden. **Rechne Beispielwerte nach.**
