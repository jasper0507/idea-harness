# Idea Harness

> A deliberately narrow agent skill: turn a non-programmer's one-line "small app idea" into something clear enough for AI to continue, before it starts inventing requirements.

Most small apps do not fail at the code. They fail in the first round of guessing.

The user says:

```text
I want to build a learning management website.
```

An agent can easily add accounts, schedules, task boards, databases, charts, reminders, permissions, and deployment plans, then start building something the user never asked for.

Idea Harness does very little: before planning or coding, it forces the agent to clarify the goal, user, first-version scope, and acceptance criteria.

## What It Solves

Idea Harness is for people who do not have a requirements document yet. It is not for teams that already have a PRD, technical plan, or product roadmap.

It helps the agent:

- Record only facts the user explicitly said or confirmed.
- Put risky guesses into `Forbidden Assumptions`.
- Ask one question at a time, choosing the question that best reduces wrong direction.
- Stay at `Need More Info` until the scope is clear.
- Output an `Execution Prompt` only when the first-version boundary is clear enough for the next agent to act on.

## Quick Start

Give this skill directory to an agent that supports `SKILL.md`:

```text
skills/idea-harness/SKILL.md
```

Then start like this:

```text
Use idea-harness to clarify my small app idea first.
I want to build a learning management website.
```

You will not immediately get a heavy requirements document. You will first get a judgment: whether the idea is already clear enough to continue.

## What Output Looks Like

If the information is not enough, it stays at `Need More Info`:

```markdown
## Current Conclusion
Status: Need More Info
Reason: "Learning management website" is still too broad. The easiest place to go wrong is deciding what kind of learning content it manages first.

## Confirmed
- You want to build a learning management website.

## Forbidden Assumptions
- Do not assume it is a task manager, class schedule, notes library, login product, database product, or analytics dashboard.

## Next Step
What kind of learning content do you want to manage first?
A. Daily study tasks
B. Assignments and deadlines
C. Study notes or resources
D. Study time and check-ins
```

Only after the goal, user, core flow, V1 must-haves, V1 non-goals, data behavior, and acceptance criteria are confirmed will it move to `Ready` and output an `Execution Prompt` containing only confirmed requirements.

## When To Use It

Use it when:

- The user has a fuzzy one-line idea, such as "I want to build a booking mini app."
- The user is not a programmer and does not know how to write requirements.
- The user wants a very small first version, not a full product.
- The agent must avoid adding unconfirmed login, databases, admin panels, AI features, dashboards, deployment, or other heavy assumptions.

Do not use it when:

- There is already a clear PRD and the next step is task breakdown or coding.
- The job is to choose a tech stack, design architecture, build a database, or plan deployment.
- The user needs business model, growth, operations, pricing, or full product consulting.
- The goal is to inflate a simple idea into a heavy product plan.

## How It Works

Idea Harness runs a lightweight harness loop internally:

```text
User idea
  -> Extract confirmed facts
  -> Find missing boundaries
  -> Block risky assumptions
  -> Ask one key question
  -> Repeat until Ready
  -> Output Execution Prompt
```

It does not expand the user's idea like a product manager, and it does not jump into engineering. Its value is blocking the places where an agent could guess and surfacing the places where it must ask.

## Repository Shape

```text
README.md
README.en.md
LICENSE
skills/
  idea-harness/
    SKILL.md
    EXAMPLES.md
```

This is a skill-only repository. It has no runtime, test project, platform manifest, or installer.

## Design Principles

- Narrow is more useful than universal.
- Fewer questions are easier to answer than exhaustive questionnaires.
- Define the first-version boundary before asking AI to build.
- Unconfirmed features are not inspiration. They are risk.
