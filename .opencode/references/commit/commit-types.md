# Commit-Typen

Übersicht über die unterstützten Emoji Conventional Commit-Typen.

Alle Commit-Nachrichten sind auf Deutsch verfasst und verwenden das imperative Präsens.

## Haupttypen

| Emoji | Typ | Beschreibung | Beispiel |
|-------|-----|--------------|----------|
| ✨ | `feat` | Neue Funktionalität | `✨ feat(api): Benutzerregistrierung hinzufügen` |
| 🐛 | `fix` | Bugfix | `🐛 fix(parser): Null-Pointer bei leerer Eingabe vermeiden` |
| 📚 | `docs` | Dokumentation | `📚 docs(readme): Installationsanleitung aktualisieren` |
| 💎 | `style` | Code-Formatierung ohne Logikänderung | `💎 style(formatter): Einrückung korrigieren` |
| ♻️ | `refactor` | Code-Restrukturierung | `♻️ refactor(service): Validierung in eigene Methode auslagern` |
| ⚡ | `perf` | Performance-Verbesserung | `⚡ perf(db): Index für Abfragen hinzufügen` |
| 🧪 | `test` | Tests hinzufügen oder fixen | `🧪 test(auth): Login-Fälle ergänzen` |
| 🔧 | `chore` | Build, Tools, Konfiguration | `🔧 chore(ci): Pipeline für Release erstellen` |

## Zusätzliche Typen

| Emoji | Typ | Beschreibung | Beispiel |
|-------|-----|--------------|----------|
| 🚀 | `ci` | CI/CD-Änderungen | `🚀 ci(github): Deployment-Workflow anpassen` |
| 🔒 | `security` | Sicherheitsrelevante Änderungen | `🔒 security(auth): Passwort-Hash aktualisieren` |
| 🗑️ | `remove` | Code oder Dateien entfernen | `🗑️ remove(legacy): Alten Endpunkt löschen` |
| 🐎 | `build` | Build-System oder externe Abhängigkeiten | `🐎 build(deps): TypeScript auf 5.5 aktualisieren` |
| 🌐 | `i18n` | Übersetzungen / Internationalisierung | `🌐 i18n(de): Fehlermeldungen übersetzen` |
| 📦 | `deps` | Abhängigkeiten aktualisieren | `📦 deps: axios auf Version 1.7 aktualisieren` |
| 🏷️ | `release` | Release-Version | `🏷️ release: Version 1.2.0` |
| 🔀 | `merge` | Merge-Commit | `🔀 merge: develop in main überführen` |
| 🚑 | `hotfix` | Kritischer Hotfix | `🚑 hotfix(payment): Zahlungsabruf reparieren` |
| 📊 | `analytics` | Tracking oder Analytics | `📊 analytics(ui): Klick-Event hinzufügen` |

## Auswahlhilfe

1. Fügt der Commit neue Funktionalität für den Nutzer hinzu? → `feat`
2. Behebt er einen Fehler? → `fix`
3. Ändert er nur Formatierung? → `style`
4. Restrukturiert er Code ohne neues Verhalten? → `refactor`
5. Verbessert er die Geschwindigkeit? → `perf`
6. Betrifft er Tests? → `test`
7. Betrifft er Build, CI oder reine Konfiguration? → `chore`, `ci` oder `build`
8. Entfernt er Code/Dateien? → `remove`
9. Ist er sicherheitsrelevant? → `security`
