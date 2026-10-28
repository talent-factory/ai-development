# Weitere Werkzeuge

Im Kurs verwenden wir bewusst nur **Pydantic AI** und **NumPy**. Wenn du danach weiterarbeitest, begegnest du diesen Namen. Je eine Zeile, ohne Wertung der Details:

| Werkzeug | Wofür | Warum nicht im Kurs |
| -------- | ----- | ------------------- |
| LangChain | Framework für Ketten aus Modellaufrufen, Suche und Werkzeugen | Viele Konzepte auf einmal, ändert sich oft |
| FAISS | Schnelle Vektorsuche für sehr viele Texte | NumPy genügt für 10 Texte |
| Chroma | Vektordatenbank, die Vektoren speichert | Zusätzliche Installation, kein Gewinn bei kleinen Mengen |
| Hugging Face | Plattform für offene Modelle, u. a. lokale Embeddings | Eigener Download pro Person |
| Ollama | Modelle lokal auf dem eigenen Rechner betreiben | Setup und Geschwindigkeit je nach Rechner |
| Pydantic AI Agents / Tool Use | Das Modell ruft selbst Werkzeuge auf (zum Beispiel die Suche) | Ausblick in Lektion 4 |
| Flowise, Langflow | RAG als Flow zusammenklicken (No-Code) | Ausblick in Lektion 4, siehe [Wann Code, wann No-Code](./wann-code-wann-no-code.md) |

Aus Modul 4: Der Coding-Assistent und die Skills (`tdd`, `code-review`) helfen auch beim Bauen eines RAG, zum Beispiel um Tests für `suche()` zu schreiben oder `beantworte()` zu prüfen. Im Kurs sind sie freiwillig.
