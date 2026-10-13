# 🚀 Skill Builder - Quick Start Guide

Build production-ready Claude Code Skills in minutes!

## Fastest Path to Success

### Step 1: Start Building

```bash
/build-skill
```

That's it! The system will guide you through everything.

## What Happens Next

### Phase 1: Requirements (2-3 minutes)

**skill-elicitation-agent** asks you questions:

```
Example conversation:

Agent: "What specific task or workflow should this skill help with?"
You: "Help me write conventional commit messages"

Agent: "When should Claude automatically use this skill?"
You: "When I'm about to commit code or ask about commit messages"

Agent: "Does this need to execute code or just provide instructions?"
You: "Just instructions, no code needed"

... a few more questions ...

Agent: "Here's the specification I've created..."
[Shows detailed spec]

Agent: "Does this look good? Should I proceed to generation?"
You: "Yes, looks perfect!"
```

### Phase 2: Generation (1-2 minutes)

**skill-generator-agent** builds your skill:

```
Creating skill structure...
✅ Created commit-helper/SKILL.md
✅ Added frontmatter with proper metadata
✅ Wrote clear instructions
✅ Included 3 examples
✅ Set up file structure

Location: ~/.claude/skills/commit-helper/
```

### Phase 3: Validation (30 seconds)

**skill-validator-agent** tests everything:

```
Running 10 validation checks...
✅ YAML frontmatter valid
✅ Description clear and discoverable
✅ File structure correct
✅ No security issues

Score: 9/10 ⭐⭐⭐⭐⭐
Status: PRODUCTION READY
```

### Phase 4: Documentation (1 minute)

**skill-documenter-agent** enhances docs:

```
Enhancing documentation...
✅ Added 5 comprehensive examples
✅ Created best practices section
✅ Added troubleshooting guide
✅ Included common pitfalls

Your skill is ready to use!
```

## First-Time Examples

### Example 1: Simple Instruction Skill (5 minutes)

**What**: Skill for commit messages

```bash
/build-skill
```

**Questions You'll Answer**:
- What format? → "Conventional Commits"
- When to use? → "When committing code"
- Any code needed? → "No, just instructions"

**What You Get**:
```
~/.claude/skills/commit-helper/
└── SKILL.md
```

**How to Use**:
```
"Help me write a commit message for my changes"
```

### Example 2: Multi-File Skill with Scripts (10 minutes)

**What**: PDF form filling skill

```bash
/build-skill
```

**Questions You'll Answer**:
- What operations? → "Fill forms, extract fields"
- Which libraries? → "pypdf, pdfplumber"
- Execute code? → "Yes, need Python scripts"

**What You Get**:
```
~/.claude/skills/pdf-form-filler/
├── SKILL.md
├── FORMS.md
├── REFERENCE.md
└── scripts/
    ├── fill_form.py
    └── validate.py
```

**How to Use**:
```
"Fill out this PDF form with my data"
```

### Example 3: Read-Only Safety Skill (7 minutes)

**What**: Security code analyzer

```bash
/build-skill
```

**Questions You'll Answer**:
- Analysis scope? → "OWASP Top 10"
- Modify files? → "No, read-only"
- Output format? → "Security report"

**What You Get**:
```
~/.claude/skills/security-analyzer/
├── SKILL.md (with tool restrictions)
├── PATTERNS.md
└── REFERENCE.md
```

**How to Use**:
```
"Analyze this code for security vulnerabilities"
```

## Common Questions

### Q: Where do skills get created?

**A**: By default in `~/.claude/skills/` (personal) or `.claude/skills/` (project).
The elicitation agent will ask which you prefer.

### Q: Can I edit a skill after creation?

**A**: Yes! Just edit the files directly. Use the validation script to check:
```bash
.claude/commands/skills/references/scripts/validate-skill.sh ~/.claude/skills/my-skill
```

### Q: How do I know if my skill will trigger?

**A**: Test it with:
```bash
.claude/commands/skills/references/scripts/test-skill-trigger.sh ~/.claude/skills/my-skill
```

### Q: What if validation fails?

**A**: The validator will tell you exactly what to fix. The generator agent can help make the changes.

### Q: Can I use templates directly?

**A**: Yes! Templates are in `../references/templates/`. But using `/build-skill` is recommended as it ensures quality.

## Tips for Success

### 1. Be Specific in Elicitation

❌ **Vague**: "I need help with files"

✅ **Specific**: "I need to extract text and tables from PDF files, and also fill out PDF forms"

### 2. Provide Examples

When asked, share:
- Example inputs
- Desired outputs
- Edge cases
- Existing workflows

### 3. Review the Specification

The elicitation agent shows you the plan before building. Read it carefully!

### 4. Test Immediately

After creation, test with:
```
"Use [skill-name] to [example task]"
```

### 5. Iterate Based on Usage

Skills can be refined over time. Keep the specification document for reference.

## Troubleshooting

### Skill Not Loading

**Check location**:
```bash
ls ~/.claude/skills/
ls .claude/skills/
```

**Check YAML**:
```bash
head -20 ~/.claude/skills/my-skill/SKILL.md
```

**Restart Claude Code** to reload skills

### Skill Not Triggering

**Test triggers**:
```bash
.claude/commands/skills/references/scripts/test-skill-trigger.sh ~/.claude/skills/my-skill
```

**Use explicit invocation**:
```
"Use the [skill-name] skill to [task]"
```

### Validation Errors

**Run validator**:
```bash
.claude/commands/skills/references/scripts/validate-skill.sh ~/.claude/skills/my-skill
```

**Fix issues** listed in the report, then re-validate

## Advanced Usage

### Creating Project-Wide Skills

When asked about location, choose **project** instead of personal:

```
Location: .claude/skills/

Then commit to git:
git add .claude/skills/my-skill
git commit -m "Add my-skill for team"
git push
```

Team members get the skill automatically on pull.

### Creating Plugin Skills

For distribution via plugins:

1. Create skill with `/build-skill`
2. Move to plugin structure
3. Publish plugin to marketplace

See: https://docs.anthropic.com/claude-code/plugins

### Using Templates Directly

For quick prototyping:

```bash
# Copy template
cp ../references/templates/simple-skill-template.md \
   ~/.claude/skills/my-skill/SKILL.md

# Replace placeholders
sed -i 's/{{SKILL_NAME}}/My Skill/g' ~/.claude/skills/my-skill/SKILL.md

# Validate
.claude/commands/skills/references/scripts/validate-skill.sh ~/.claude/skills/my-skill
```

But `/build-skill` is recommended for production use.

## What's Next?

### Learn More

- **Full Documentation**: See `.claude/commands/skills/README.md`
- **Agent Details**: See `.claude/agents/skill-builder/README.md`
- **Official Docs**: https://docs.anthropic.com/claude-code/skills

### Build Your First Skill

Ready? Let's go:

```bash
/build-skill
```

The agents will guide you through everything!

### Share Your Skills

Once created:
- Share with team via git
- Distribute as plugins
- Contribute to community repos

---

**Happy skill building! Transform your workflows into reusable expertise.** 🚀
