"""Prüft, dass sich in Python-Dateien gegenüber `git HEAD` nur Docstrings und Kommentare geändert haben.

Aufruf: python3 -I check_nur_doku.py DATEI [DATEI ...]
Exit-Code 0: nur Dokumentation geändert. Exit-Code 1: Code hat sich verändert oder die Datei ist nicht parsebar.
"""

import ast
import subprocess
import sys


def _ohne_docstrings(quelltext: str) -> str:
    """Parst den Quelltext und liefert den AST-Dump ohne Docstrings.

    Args:
        quelltext: Python-Quelltext.

    Returns:
        Textdarstellung des AST, in der Docstrings entfernt sind.
    """
    baum = ast.parse(quelltext)
    for knoten in ast.walk(baum):
        if not isinstance(knoten, ast.Module | ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef):
            continue
        if ast.get_docstring(knoten, clean=False) is not None:
            knoten.body = knoten.body[1:] or [ast.Pass()]
    return ast.dump(baum)


def _pruefe(pfad: str) -> str | None:
    """Vergleicht eine Datei mit ihrer Version in HEAD.

    Args:
        pfad: Pfad der Python-Datei.

    Returns:
        Fehlermeldung oder `None`, wenn nur Dokumentation geändert wurde.
    """
    alt = subprocess.run(["git", "show", f"HEAD:./{pfad}"], capture_output=True, text=True)
    if alt.returncode != 0:
        return "nicht in HEAD vorhanden (neue Datei), kann nicht verglichen werden"
    try:
        with open(pfad, encoding="utf-8") as datei:
            neu = datei.read()
        if _ohne_docstrings(alt.stdout) != _ohne_docstrings(neu):
            return "Code wurde verändert, nicht nur Dokumentation"
    except SyntaxError as fehler:
        return f"Syntaxfehler: {fehler}"
    return None


def main() -> int:
    """Prüft alle übergebenen Dateien und gibt das Ergebnis aus.

    Returns:
        Exit-Code: 0 bei Erfolg, 1 sobald eine Datei auffällt.
    """
    fehler = {pfad: grund for pfad in sys.argv[1:] if (grund := _pruefe(pfad))}
    for pfad, grund in fehler.items():
        print(f"FEHLER {pfad}: {grund}")
    if not fehler:
        print(f"OK: {len(sys.argv) - 1} Datei(en), nur Dokumentation geändert.")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
