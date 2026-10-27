# Konserve 2: Tests ohne `tdd` werden nie rot

*Zusammenfassung eines echten Laufs von Claude Code 2.1.311 (2026-10-27), Kopie des Wetterberichts. Der Testcode ist gekürzt.*

**Auftrag (ohne Skill):** «Schreibe Tests für `berechne_kennzahlen`.»

Die KI schrieb in rund 45 Sekunden **14 Tests**, unter anderem:

```python
def test_durchschnitte(drei_tage): ...
def test_heissester_tag_bei_gleichstand_ist_der_erste(): ...
def test_regentage_zaehlt_nur_niederschlag_ueber_null(drei_tage): ...
def test_niederschlag_gesamt_ist_gerundet(): ...
def test_leere_liste_wirft_value_error(): ...
```

Sie durfte `pytest` nicht ausführen und schrieb deshalb: «Die Tests sind ungetestet.» Beim eigenen Lauf: **14 passed**, alle sofort grün.

**Mutationsprobe:** Im Code `z["niederschlag_mm"] > 0` zu `>= 0` geändert. Ergebnis: **3 failed, 11 passed** (`test_regentage_zaehlt_nur_niederschlag_ueber_null`, `test_kleinster_niederschlag_zaehlt_als_regentag`, `test_ohne_niederschlag_keine_regentage`). Diese Tests hätten den Fehler bemerkt.

**Ein zweiter Auftrag** («Tests, die das heutige Verhalten von `beschreibe_wetter` festhalten») ergab 13 Tests. Darunter standen auch diese:

```python
def test_code_als_text_ist_unbekannt():      beschreibe_wetter("3") == "unbekannt"
def test_none_ist_unbekannt():               beschreibe_wetter(None) == "unbekannt"
def test_unhashbarer_code_wirft_typeerror(): beschreibe_wetter([3]) wirft TypeError
```

Die KI merkte selbst an: «Die letzten vier Tests halten Verhalten fest, das wohl eher zufällig entsteht.»

**Auswertung:**

- Tests nach dem Code sind immer grün. Ob sie etwas taugen, zeigt erst die Mutationsprobe.
- Die KI schreibt gern mehr, als bestellt war. Zufälliges Verhalten gehört nicht in einen Vertrag. Streiche, was du nicht willst.
- Ohne ausgeführtes `pytest` ist «Tests geschrieben» keine Aussage. Selbst ausführen.
- Mit `tdd` entstand jeder Test vor dem Code und war zuerst rot (sechs Zyklen, 19 Tests grün). Die KI liess einen Test sogar bewusst weg: Er wäre sofort grün gewesen und damit kein TDD-Schritt.
