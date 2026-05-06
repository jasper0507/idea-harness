# Idea Harness

> **Most vague ideas die in the AI's first round of guessing.**
> Idea Harness puts a **harness on AI** right at this step.

**An ultra-focused Clarification Skill**: turns a non-programmer's vague "small app idea" into requirements that AI can safely execute — **without guessing**.

[简体中文](README.md) | English

---

## The Problem

Most AI Coding Agents (Claude Code, Cursor, Codex, etc.) encounter inputs like:

```text
I want to build a learning management website.
I want to make an expense tracking app.
I want to create a family chore tracker.
```

They immediately start **guessing**:
- Account systems, databases, push notifications, analytics dashboards, admin panels...
- Features and complex architectures you never asked for

Result: **You get something you didn't want**, or the project collapses entirely.

The core issue is simple: **when requirements are unclear, LLMs tend to fill in unconfirmed assumptions**. Idea Harness is built specifically to address this early-stage pain point.

---

## The Solution

**Idea Harness does one thing** — **requirements clarification**.

It takes a "clarify before implementation" workflow + Harness Engineering's control loop, and **laser-focuses** them into a lightweight Skill for the earliest stage.

Core mechanisms:
- Only acknowledge facts the user explicitly stated or confirmed
- Maintain seven clarification gates as a decision tree, not a linear checklist
- Four precision checks catch requirements that look complete but aren't precise enough
- Hard state machine: `gathering` → `needs-precision` → `blocked` → `ready`
- Ask exactly one critical question by default
- In `Need More Info`, show only `Confirmed` and `Question`
- In `Ready`, show only the `Requirements Brief` by default
- Generate a behavior-contract-style execution prompt only when the user explicitly asks

---

## Key Differentiators

| Dimension | Idea Harness | Most Other Skills / Agents |
|-----------|--------------|---------------------------|
| **Scope** | **Ultra-narrow** — only does clarification | Full pipeline / execution / code generation |
| **Core Principle** | **No guessing**, only confirmed facts | Encourages creativity, proactively fills in features |
| **Stage** | **Step 0 when idea is most vague** | After some clarity is already established |
| **Risk Control** | Very strong (seven gates + precision checks + state machine) | Weaker |
| **Lightweight** | **Pure Skill**, extremely minimal | Often includes frameworks, tests, multi-file |

**One-line summary**:
Others teach AI **how to do it**. Idea Harness teaches AI to **ask first, then do**.

---

## Quick Start (30 seconds)

1. Load `skills/idea-harness/SKILL.md` into your Agent (Claude Code, Cursor, or any tool that supports Skills)
2. Start chatting:

```text
Use idea-harness to clarify my small app idea first.
I want to build [your vague idea].
```

---

## Output Example

**Need More Info stage** (typical output):

```markdown
## Confirmed
- You want to build a learning management website.

## Question
"Learning management website" is not a clear problem yet. Which learning problem do you want to remove first?

A. Not knowing what to study today
B. Forgetting assignments or deadlines
C. Notes and materials are too scattered
D. Not knowing how long you studied or whether you stayed consistent

Recommendation: Start with A. It is the easiest to turn into a tiny V1: open the page and see what to study today.
```

Only after all seven gates are confirmed and precision checks pass will it output a `Requirements Brief`. If you explicitly ask for an execution prompt, it can then generate a behavior-contract-style prompt for Codex, Claude Code, or Cursor.

---

## Design Philosophy

- **Narrow is more useful than all-in-one** — specialized for the clarification stage
- **Ask less, progress more**
- **Define boundaries first, then let AI implement**
- Combines **Harness Engineering** (putting reins on AI) + a **clarify before implementation** workflow

---

## When to Use

**Recommended**:
- You only have a vague idea
- You're a non-technical person who doesn't know how to turn an idea into requirements
- You want to build a **tiny but correct** first version
- You're afraid AI will take over and add unwanted features

**Not suitable**:
- You already have a clear PRD
- You need to immediately write code or choose a tech stack
- You need business model planning or full product roadmapping

---

## Project Structure

```text
README.md
README.en.md
LICENSE
docs/
  designs/
    v0.4.0-socratic-harness-design.md
skills/
  idea-harness/
    SKILL.md             # Core entry (~95 lines)
    STATE-MACHINE.md     # State definitions, transitions, decision tree priority
    PRECISION-GATE.md    # Four precision checks
    OUTPUTS.md           # All output templates
    VOCABULARY.md        # Internal terms, user-facing language conventions
    EXAMPLES.md          # Full Chinese/English conversation examples
    SMOKE_TESTS.md       # v0.5.0 smoke test checklist
```

This is a **skill-only** project, kept extremely lightweight. No scripts, no frameworks, no unnecessary features.

---

## Contributing

Submit your **real vague ideas + clarification process**, and I'll add them to EXAMPLES.md to help more people.

---

**License**: MIT
**Author**: jasper0507
