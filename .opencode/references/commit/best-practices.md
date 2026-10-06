# Best Practices für Commits

## Commit-Grösse

- Ein Commit sollte **eine logische Einheit** darstellen.
- Vermische nicht Feature, Bugfix und Refactoring in einem Commit.
- Bei grossen Änderungen: Aufteilen in mehrere kleine Commits.

## Commit-Nachricht

- **Sprache**: Deutsch
- **Form**: Imperativ, Präsens
- **Erste Zeile**: Maximal 72 Zeichen
- **Kein Punkt** am Ende der ersten Zeile
- **Keine automatischen Suffixe** wie `Generated with Claude Code` oder `Co-Authored-By`

## Beispiele für gute Nachrichten

```text
✨ feat(api): Endpunkt für Benutzerregistrierung hinzufügen
```

```text
🐛 fix(parser): Leerzeichen in CSV-Zeilen korrekt behandeln
```

```text
📚 docs(readme): Installationsanleitung aktualisieren
```

```text
♻️ refactor(service): Validierung in eigene Methode auslagern
```

## Body verwenden

Bei komplexen Änderungen sollte der Commit einen Body enthalten:

```text
✨ feat(auth): Zwei-Faktor-Authentifizierung hinzufügen

Implementiert TOTP-basierte 2FA für lokale Benutzer.
Fügt Endpunkte für Aktivierung und Validierung hinzu.
Aktualisiert die Dokumentation mit Einrichtungsschritten.
```

## Was vermeiden

- ❌ `Update file.txt`
- ❌ `Fix stuff`
- ❌ `WIP`
- ❌ Automatisch generierte Signaturen
- ❌ Gemischte Änderungen ohne klaren Fokus

## Staging

- Prüfe vor dem Commit mit `git status`, was gestaged wird.
- Nutze `git add -p`, um nur relevante Teile einer Datei zu stagen.
- Vermische keine Formatierungsänderungen mit inhaltlichen Änderungen.
