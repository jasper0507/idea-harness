# Idea Harness

[![CI](https://github.com/jasper0507/idea-harness/actions/workflows/verify.yml/badge.svg)](https://github.com/jasper0507/idea-harness/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/jasper0507/idea-harness)](https://github.com/jasper0507/idea-harness/releases)

> **Most vague ideas die in the AI's first round of guessing.**
> Idea Harness puts a **harness on AI** right at this step.

Turns a non-programmer's vague "small app idea" into requirements that AI can safely execute — **without guessing**.

[简体中文](README.md) | English

---

## The Problem

AI Coding Agents encounter "I want to build an expense tracking app" and immediately start guessing — accounts, databases, push notifications… You get something you didn't want.

The core issue: **when requirements are unclear, LLMs tend to fill in unconfirmed assumptions.**

## The Solution

**Idea Harness does one thing — requirements clarification.**

- Only acknowledge facts the user explicitly stated or confirmed
- Seven clarification gates as a decision tree, not a linear checklist
- Four precision checks catch requirements that look complete but aren't precise enough
- Hard state machine: `gathering` → `needs-precision` → `blocked` → `ready`
- Ask exactly one critical question by default
- Output a requirements brief only when Ready; generate an execution prompt only on explicit request

---

## Quick Start

### 1. Get the skill

```bash
git clone https://github.com/jasper0507/idea-harness.git
```

### 2. Load into your AI tool

**Claude Code**
```bash
cp -r idea-harness/skills/idea-harness ~/.claude/skills/
```

**Cursor**
```bash
cp -r idea-harness/skills/idea-harness .cursor/skills/
```

**Codex (OpenAI)**
```bash
# Reference in your project's AGENTS.md
echo "Read and follow skills/idea-harness/SKILL.md when clarifying app ideas." >> AGENTS.md
```

**Hermes Agent**
```bash
cp -r idea-harness/skills/idea-harness ~/.hermes/skills/
```

**OpenClaw**
```bash
cp -r idea-harness/skills/idea-harness ~/.openclaw/skills/
```

### 3. Start chatting

```text
Use idea-harness to clarify my small app idea first.
I want to build [your vague idea].
```

---

## Output Example

**Need More Info stage**:

```markdown
## Confirmed
- You want to build a learning management website.

## Question
"Learning management website" is not a clear problem yet. Which learning problem do you want to remove first?

A. Not knowing what to study today
B. Forgetting assignments or deadlines
C. Notes and materials are too scattered
D. Not knowing how long you studied or whether you stayed consistent

Recommended: Start with A. It is the easiest to turn into a tiny V1: open the page and see what to study today.
```

Only after all seven gates are confirmed and precision checks pass will it output a Requirements Brief. An execution prompt is generated only when you explicitly ask.

---

## Design Philosophy

- **Narrow is more useful than all-in-one** — specialized for the clarification stage
- **Ask less, progress more**
- **Define boundaries first, then let AI implement**

---

## When to Use

**Recommended**: You only have a vague idea · Non-technical person turning idea into requirements · Want a tiny but correct V1 · Afraid AI will add unwanted features

**Not suitable**: You already have a clear PRD · Need to write code now · Need business model planning

---

## Project Structure

```text
skills/idea-harness/
  SKILL.md             # Core entry
  STATE-MACHINE.md     # State machine
  PRECISION-GATE.md    # Precision checks
  OUTPUTS.md           # Output templates
  VOCABULARY.md        # Language conventions
  EXAMPLES.md          # Full conversation examples
CLAUDE.md              # Repo context for AI agents
scripts/verify.sh      # Static smoke checks
```

Skill-only project: no dependencies — just Markdown + one verification script.

---

## Contributing

Submit your **real vague ideas + clarification process** — just open a PR updating `skills/idea-harness/EXAMPLES.md`.

---

**License**: MIT　·　**Author**: jasper0507
