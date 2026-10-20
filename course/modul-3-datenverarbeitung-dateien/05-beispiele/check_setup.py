"""Prüft, ob die Umgebung für Modul 3 bereit ist (Python und `requests`)."""

import sys


def main() -> None:
    """Gibt für jede Voraussetzung OK oder eine Anleitung zur Behebung aus."""
    print(f"OK: Python {sys.version_info.major}.{sys.version_info.minor}")

    try:
        import requests
    except ImportError:
        print("FEHLER: `requests` fehlt. Installiere es mit:  uv add requests")
        return
    print(f"OK: requests {requests.__version__}")


if __name__ == "__main__":
    main()
