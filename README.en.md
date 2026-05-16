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

### 3. Start chatting

```text
Use idea-harness to clarify my small app idea first.
I want to build [your vague idea].
```

---

## Output Example

**Socratic questioning** — not a multiple-choice survey, but helping you see what you haven't thought through:

```markdown
## Confirmed
- You run a monthly book club with friends.
- Choosing the next book causes arguments.
- You want a voting tool to settle it.

## Question
Imagine you built this and shared it with your book club, but after one month nobody used it again. What's the most likely reason?
```

When a user's answer hides an untested assumption, the skill calls it out:

```markdown
## Question
You said the tool must be "dead simple — open a link, vote, done." But suggest-then-vote means two separate steps, a suggestion deadline, and handling duplicates.

Voting on books you pre-pick: one screen, done in a minute.
Suggesting + voting: multiple steps, needs a cutoff, and you'll have to moderate.

For V1, which one?
```

Only after all seven gates are confirmed and precision checks pass will it output a Requirements Brief. An execution prompt is generated only when you explicitly ask.

---

## Design Philosophy

- **Narrow is more useful than all-in-one** — specialized for the clarification stage
- **Ask less, progress more**
- **Define boundaries first, then let AI implement**
- **Clarify for the machine, enlighten the human** — constrain the downstream agent while helping the user discover what they actually want

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
LICENSE                # MIT
CHANGELOG.md           # Version history
.github/workflows/verify.yml
scripts/verify.sh      # Static smoke checks
```

Skill-only project: no runtime dependencies — skill markdown, one verify script, license, changelog, and minimal CI only.

---

## Contributing

Submit your **real vague ideas + clarification process** — just open a PR updating `skills/idea-harness/EXAMPLES.md`.

---

**License**: MIT　·　**Author**: jasper0507
