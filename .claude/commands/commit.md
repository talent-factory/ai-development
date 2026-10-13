---
description: Create professional git commits with automated checks for Java, Python, and React projects
category: development
allowed-tools:
  - Bash
  - Read
  - Glob
---

# Claude Command: Commit

Create professional Git commits with automated quality checks and conventional commit messages.

**All commits and messages are written in German.**

## Usage

Standard commit:

```bash
/commit
```

With options:

```bash
/commit --no-verify     # Skip pre-commit checks
/commit --force-push    # Execute force push (use with caution!)
/commit --skip-tests    # Skip test execution
/commit --with-skills   # Create a commit using professional-commit-workflow
```

## Workflow

### With `--with-skills` Option

When `--with-skills` is used, the **professional-commit-workflow skill** is activated and the remaining command workflow is bypassed:

1. **Skill execution**: Use the professional-commit-workflow skill
   - Location: `../skills/professional-commit-workflow/`
   - Performance: ~70% faster than the command
   - Features: Automatic project detection, pre-commit validation, Emoji Conventional Commits

2. **Skill details**: See [professional-commit-workflow README](../skills/professional-commit-workflow/README.md)

### Standard Workflow (without `--with-skills`)

1. **Pre-commit checks** (skip with `--no-verify`)
   - Automatic project detection (Java, Python, React, Docs)
   - Execute relevant checks (Build, Tests, Linting)
   - Details: [pre-commit-checks.md](../references/commit/pre-commit-checks.md)

2. **Staging analysis**
   - Check staged files with `git status`
   - Automatically add changes if necessary
   - Display overview of files to be committed

3. **Diff analysis**
   - Analyze `git diff` for scope of changes
   - Detect multiple logical changes
   - Suggest commit splitting when appropriate

4. **Commit message**
   - Use Emoji Conventional Commit format
   - Automatic type detection based on changes
   - German, imperative description
   - Reference: [commit-types.md](../references/commit/commit-types.md)

5. **Create commit**
   - Create commit with meaningful message
   - **IMPORTANT:** Do NOT add "Co-Authored-By" or "Generated with Claude Code" suffixes
   - Optional: Offer push to remote repository

## Commit Types (Selection)

- ✨ `feat`: New functionality
- 🐛 `fix`: Bug fix
- 📚 `docs`: Documentation changes
- 💎 `style`: Code formatting
- ♻️ `refactor`: Code restructuring
- ⚡ `perf`: Performance improvements
- 🧪 `test`: Add/fix tests
- 🔧 `chore`: Build, tools, configuration

**Complete list**: [commit-types.md](../references/commit/commit-types.md)

## Supported Project Types

- **Java**: Maven, Gradle, Spring Boot
- **Python**: Ruff, Black, pytest, mypy
- **React/Node.js**: ESLint, Prettier, TypeScript, Jest/Vitest
- **Documentation**: LaTeX, Markdown, AsciiDoc

**Check details**: [pre-commit-checks.md](../references/commit/pre-commit-checks.md)

## Professional Commit Workflow Skill

The `--with-skills` option uses the **professional-commit-workflow skill** for improved performance and reusability.

### Advantages vs. Standard Command

| Feature | Standard Command | Skill (`--with-skills`) |
|---------|------------------|------------------------|
| Performance | Slow | ~70% faster |
| Token consumption | ~1.4k lines | ~300 lines |
| Reusability | Per project | Globally installed |
| Configurability | Prompts | JSON config |
| Extensibility | Limited | Python modules |

### Skill Usage

```bash
# Direct skill execution (alternative)
cd ../skills/professional-commit-workflow
python scripts/main.py

# Or via command with --with-skills
/commit --with-skills
```

**Skill documentation**: [professional-commit-workflow/README.md](../skills/professional-commit-workflow/README.md)

## Commit Message Format

**IMPORTANT:** Commit messages must NOT contain any of the following suffixes:

- `Generated with [Claude Code](https://claude.com/claude-code)`
- `Co-Authored-By: Claude <noreply@anthropic.com>`
- Similar automatic signatures

The commit message should describe only the actual commit content.

## Additional Information

- **Best Practices**: [best-practices.md](../references/commit/best-practices.md)
- **Troubleshooting**: [troubleshooting.md](../references/commit/troubleshooting.md)
