# Gute und schlechte Tests

## Gute Tests

**Integrationsnah**: Über echte Schnittstellen testen, nicht über Mocks interner Teile.

```python
# GUT: prüft beobachtbares Verhalten
def test_checkout_mit_gueltigem_warenkorb_wird_bestaetigt(zahlungs_fake):
    warenkorb = Warenkorb()
    warenkorb.hinzufuegen(BUCH)

    ergebnis = checkout(warenkorb, zahlungs_fake)

    assert ergebnis.status == "bestaetigt"
```

Merkmale:

- Prüft Verhalten, das Aufrufer interessiert
- Nutzt nur die öffentliche API
- Übersteht interne Refactorings
- Beschreibt WAS, nicht WIE
- Ein Verhalten pro Test (mehrere `assert`s auf demselben Ergebnisobjekt sind in Ordnung)
- Klare Struktur: Arrange, Act, Assert, getrennt durch Leerzeilen
- Name als Satz über das Verhalten, z. B. `test_leerer_warenkorb_kann_nicht_bezahlt_werden`

## Schlechte Tests

**Implementierungsdetail-Tests**: Gekoppelt an die interne Struktur.

```python
# SCHLECHT: prüft, wie intern gearbeitet wird
def test_checkout_ruft_zahlungsdienst_belasten_auf(mocker):
    dienst = mocker.Mock()
    checkout(warenkorb, dienst)
    dienst.belasten.assert_called_once_with(warenkorb.summe)
```

Warnsignale:

- Interne Kollaborateure werden gemockt
- Private Methoden (`_name`) werden getestet
- Assertions auf Aufrufanzahl oder -reihenfolge (`assert_called_once`, `call_args_list`)
- Test bricht beim Refactoring ohne Verhaltensänderung
- Testname beschreibt WIE statt WAS
- Prüfung über Umwege statt über die Schnittstelle

```python
# SCHLECHT: umgeht die Schnittstelle zur Prüfung
def test_benutzer_anlegen_speichert_in_datenbank(db):
    benutzer_anlegen(db, name="Alice")
    zeile = db.execute("SELECT * FROM benutzer WHERE name = ?", ("Alice",)).fetchone()
    assert zeile is not None


# GUT: prüft über die Schnittstelle
def test_angelegter_benutzer_ist_abrufbar(db):
    benutzer = benutzer_anlegen(db, name="Alice")

    abgerufen = benutzer_holen(db, benutzer.id)

    assert abgerufen.name == "Alice"
```

**Tautologische Tests**: Der erwartete Wert wiederholt die Implementierung, der Test besteht per Konstruktion.

```python
# SCHLECHT: erwarteter Wert wird so berechnet wie im Code
def test_gesamtsumme_addiert_positionen():
    positionen = [Position(preis=10), Position(preis=5)]
    erwartet = sum(p.preis for p in positionen)
    assert gesamtsumme(positionen) == erwartet


# GUT: erwarteter Wert ist ein unabhängiges, bekanntes Literal
def test_gesamtsumme_addiert_positionen():
    assert gesamtsumme([Position(preis=10), Position(preis=5)]) == 15
```

## Tabellentests statt Kopien

Mehrere Beispiele für dasselbe Verhalten gehören in `parametrize`, nicht in kopierte Tests. Die erwarteten Werte bleiben unabhängige Literale (Kontrollwerte).

```python
@pytest.mark.parametrize(
    ("celsius", "fahrenheit"),
    [(0, 32), (100, 212), (-40, -40)],
    ids=["gefrierpunkt", "siedepunkt", "gleichstand"],
)
def test_celsius_in_fahrenheit(celsius, fahrenheit):
    assert celsius_zu_fahrenheit(celsius) == fahrenheit
```

## Fehlerfälle

```python
def test_negative_menge_wird_abgelehnt():
    with pytest.raises(ValueError, match="Menge muss positiv sein"):
        Position(preis=10, menge=-1)
```

`match=` ist Pflicht: Ohne es besteht der Test bei jedem beliebigen `ValueError`.

## Gleitkommazahlen

```python
def test_mehrwertsteuer():
    assert mehrwertsteuer(19.99) == pytest.approx(1.54, abs=0.005)
```

Niemals `==` auf Floats. Für Geldbeträge besser `Decimal`.
