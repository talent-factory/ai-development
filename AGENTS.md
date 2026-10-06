# AGENTS.md — OpenCode Guide for ki-development

## Project snapshot

- Python educational repo for an AI/ML course. Mostly standalone example scripts and Streamlit apps.
- Package manager: `uv`. Lockfile: `uv.lock`. Python: `3.13.1` (`.python-version`, `pyproject.toml`).
- Default git branch is `develop`; `main` and `develop` are protected and require PR review and linear history (no merge commits). See `CONTRIBUTING.md`.

## Setup

- `uv sync` — install dependencies from `uv.lock`.
  - The README mentions `uv pip install -r requirements.txt`, but there is **no root `requirements.txt`**.
- `uv pip install -e .` — add `src/` to `PYTHONPATH` so local packages (`utils`, etc.) are importable.
  - Do **not** import `ai_development`; the distribution name in `pyproject.toml` is `ai-development`, but no top-level package with either name exists. Import the packages under `src/` directly.
- Copy `.env.example` to `.env` and fill API keys. `src/utils/project_utils.load_environment()` loads from the project root.

## Running code

- Python script: `uv run python <path>`
- Streamlit app: `uv run streamlit run streamlit/<app>.py` (port 8501)
- Some folders have their own `requirements.txt` (e.g., `streamlit/requirements.txt`, `scripts/rag-praxis/requirements.txt`). The root `uv` env usually covers them, but if a script fails on a missing package, install that folder's requirements.

## Package / import layout

- `src/` becomes the package root only after `uv pip install -e .`. Top-level importable package currently: `utils`.
- `src/pydantic/` and `src/rag/` are folders of standalone scripts **without `__init__.py`**; do not treat them as packages.
- Beware: adding `__init__.py` to `src/pydantic/` would shadow the installed `pydantic` library.

## Code style

- See `.windsurfrules` for the full guide. Key points:
  - Imports: standard-library → third-party → local, grouped.
  - `snake_case` functions/variables; `PascalCase` classes.
  - Use `if __name__ == "__main__":` in executable scripts.
  - Cache Streamlit functions with `@st.cache_data` / `@st.cache_resource`.
  - Comments and user-facing strings are in German.

## Tests & linting

- There is **no root test suite**. `uv run pytest` is not configured and currently collects non-test files under `docs/solutions/`; do not treat it as a green check.
- `ruff` is available on PATH but is **not a pinned project dependency** and has no project config. It flags files in `docs/` and `scripts/`. Use it only if you add project-level config and dev dependencies.

## Taskmaster / AI workflow

- The repo is configured for `task-master-ai`. Root task data lives in `.taskmaster/`.
- For commands and workflow, see `CLAUDE.md` and `.cursor/rules/taskmaster/`.
- CLI fallback: `npx -y task-master-ai <command>` (e.g., `npx -y task-master-ai list`).

## Subprojects

- `rag-system/` is a self-contained project with its own `pyproject.toml`, `.venv`, `AGENTS.md`, and Taskmaster setup. Use its instructions and commands there, not the root ones.
- `streamlit/`, `scripts/rag-praxis/`, and `docs/solutions/` are collections of examples/solutions; each may have its own README or `requirements.txt`.

## Commits

- Use Conventional Commits (`feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`) per `CONTRIBUTING.md`.
