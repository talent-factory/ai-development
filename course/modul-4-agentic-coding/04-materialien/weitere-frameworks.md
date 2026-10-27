# Weitere Frameworks

Im Kurs nutzen wir die Skills aus `mattpocock/skills`. Es gibt andere Sammlungen mit einem anderen Ansatz. Stand der Recherche: 2026-10-21.

## superpowers (`obra/superpowers`)

Eine Sammlung von rund 15 Skills mit einem festen Ablauf (Idee klären, Plan schreiben, Test-first umsetzen, Review). Anders als bei den Pocock-Skills laufen sie **automatisch**: Ein Startskript prüft vor jeder Aufgabe, ob ein Skill passt.

- Claude Code: `/plugin install superpowers@claude-plugins-official`
- OpenCode: natives Plugin über `opencode.json` (OpenCode 2: Schlüssel `plugins`, ab 2.0.4)

Vor dem Einsatz bedenken: Der Ablauf ist verbindlich und kann bei kleinen Aufgaben schwerfällig wirken. Lange Läufe mit mehreren Subagenten verbrauchen viele Token. Ein optionaler Begleitdienst sendet Telemetrie, abschaltbar mit `SUPERPOWERS_DISABLE_TELEMETRY`.

## Und sonst?

- [`cli-comparison.md`](./cli-comparison.md): ein älterer Vergleich von vier Coding-CLIs (ohne OpenCode, nur zur Orientierung).
- Die Recherche mit Quellen und Wortzahlen liegt in `.wayfinder/modul-4/research/framework-recherche.md`.

## Faustregel

Kleine, gezielte Skills (wie im Kurs) lernst du schneller und kontrollierst du besser. Ein vollautomatischer Ablauf lohnt sich erst, wenn du den Durchlauf von Hand beherrschst.
