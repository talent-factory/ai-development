"""Sanity-Tests für Projekt-Hilfsfunktionen."""

from pathlib import Path

from utils.project_utils import find_project_root


def test_find_project_root_returns_path():
    """Das Projektstammverzeichnis sollte als Path zurückgegeben werden."""
    root = find_project_root()
    assert isinstance(root, Path)
    assert (root / "pyproject.toml").exists()
