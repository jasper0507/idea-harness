# Idea Harness

A requirements-clarification skill for non-programmers with small app ideas.

Idea Harness helps ordinary people turn a fuzzy idea for a small website, tool, or app into a clear enough scope for an AI agent to continue without inventing requirements. It is not a PRD generator, prompt optimizer, technical planner, or coding skill.

Its differentiation is intentionally narrow: **early requirement clarification for non-programmers**.

## Use It When

- The user has a rough idea like "I want a learning management website."
- The user is not a programmer and does not know how to write requirements.
- The user wants a small first version, not a full product plan.
- The agent must avoid adding unconfirmed login, databases, dashboards, AI features, deployment, or other heavy assumptions.

## Do Not Use It For

- Choosing a tech stack.
- Designing databases, backends, deployment, or security architecture.
- Writing code.
- Generating a heavy PRD.
- Turning a simple idea into a full startup plan.

## Usage

Use the plain skill directory:

```text
skills/idea-harness/SKILL.md
```

Example:

```text
Use idea-harness to clarify my small app idea first.
I want to build a personal study planning tool.
```

The skill keeps a lightweight harness loop internally: collect evidence, find missing gates, block risky assumptions, ask one useful question, and only become `Ready` when the idea is clear enough.

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

This is a skill-only repository. It has no runtime, validator, test suite, platform manifest, or installer.
