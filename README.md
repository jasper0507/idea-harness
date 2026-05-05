# Idea Harness

> **Most vague ideas die in the AI's first round of guessing.**  
> Idea Harness puts a **harness on AI** right at this step.

**An ultra-focused Clarification Skill**: turns a non-programmer's vague "small app idea" into requirements that AI can safely execute — **without guessing**.

English | [简体中文](README.zh.md)

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

Andrej Karpathy has pointed out: **LLMs love to make assumptions without confirmation**. Idea Harness is built specifically to address this early-stage pain point.

---

## The Solution

**Idea Harness does one thing** — **requirements clarification**.

It takes Karpathy's "Think Before Coding" philosophy + Harness Engineering's control loop, and **laser-focuses** them into a lightweight Skill for the earliest stage.

Core mechanisms:
- Only acknowledge facts the user explicitly stated (evidence ledger)
- Strictly forbid dangerous assumptions
- Ask exactly **one most critical question** at a time
- Use `Status: Need More Info` / `Ready` gate control flow

---

## Key Differentiators

| Dimension | Idea Harness | Most Other Skills / Agents |
|-----------|--------------|---------------------------|
| **Scope** | **Ultra-narrow** — only does clarification | Full pipeline / execution / code generation |
| **Core Principle** | **No guessing**, only confirmed facts | Encourages creativity, proactively fills in features |
| **Stage** | **Step 0 when idea is most vague** | After some clarity is already established |
| **Risk Control** | Very strong (Status gates + boundary protection) | Weaker |
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
## Current Conclusion
Status: Need More Info
Reason: "Learning management website" is too broad — the most likely thing to get wrong is the core management target.

## Confirmed
- You want to build a learning management website.

## Forbidden Assumptions
- Cannot assume it needs login, database, course schedules, points system, etc.

## Next Step
What type of learning content do you want to manage first?
A. Daily learning tasks to complete
B. Assignments and deadlines
C. Study notes and materials
D. Study time and check-in records
```

Only after all key boundaries (goal, user, core flow, V1 scope, non-goals, etc.) are confirmed will it output `Status: Ready`.

---

## Design Philosophy

- **Narrow is more useful than all-in-one** — specialized for the clarification stage
- **Ask less, progress more**
- **Define boundaries first, then let AI implement**
- Combines **Harness Engineering** (putting reins on AI) + **Karpathy's philosophy** (Think Before Coding)

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
skills/
  idea-harness/
    SKILL.md          # Core Skill (minimal)
    EXAMPLES.md       # Real-world usage examples (continuously updated)
```

This is a **skill-only** project, kept extremely lightweight. No scripts, no frameworks, no unnecessary features.

---

## Contributing

Submit your **real vague ideas + clarification process**, and I'll add them to EXAMPLES.md to help more people.

---

**License**: MIT  
**Author**: jasper0507
