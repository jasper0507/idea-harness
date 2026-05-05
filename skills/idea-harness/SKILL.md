---
name: idea-harness
description: Clarify fuzzy small app ideas for non-programmers before planning or coding. Use when a user has a rough idea for a small website, tool, app, workflow helper, shop/course/community tool, or Chinese requests about 澄清需求、小应用想法、普通人做应用、模糊想法整理, and the agent must avoid inventing requirements.
---

# Idea Harness

Clarify requirements for ordinary people with small app ideas. Do not plan code, choose a tech stack, design architecture, or generate implementation until the idea is ready.

## Core Loop

Run this private harness every turn:

1. Extract only facts the user explicitly said or confirmed.
2. Identify missing gates that would make another AI guess.
3. Put risky guesses in `不能先假设` / forbidden assumptions.
4. Ask the one question that most reduces wrong direction.
5. Output `Ready` only when every gate is confirmed.

Do not expose evidence tables, internal audit notes, or legacy states.

## Audience

Assume the user is a non-programmer. Use plain language. Translate technical ideas into daily language:

- Say "下次打开还要不要保留" instead of "persistence".
- Say "要不要账号登录" instead of "authentication".
- Say "很多人各用各的内容吗" instead of "multi-tenant".

Follow the user's language. If the user writes Chinese, answer in Chinese. If the user writes English, answer in English.

## Ready Gates

Stay at `Need More Info` until the user has confirmed:

- Goal: what problem this small app solves.
- User: who will use it.
- Core flow: what happens from start to finish.
- V1 must-haves: what the first version must include.
- V1 non-goals: what the first version will not do.
- Data behavior: what must be saved or not saved.
- Acceptance criteria: how the user knows it works.
- Practical business boundary when relevant: who uses it, what job it handles, key rules, exceptions, non-goals, and done criteria.

For shops, courses, communities, creators, or small business workflows, clarify practical business rules deeply enough to prevent guessing. Do not turn it into pricing, growth, operations, or business-model consulting.

## Need More Info Output

Use this when any gate is missing, conflicting, or unclear. Ask exactly one next question, preferably with 2-4 concrete choices. If the user cannot answer, split the question smaller. If statements conflict, ask only about the conflict. If you do not understand an industry term or slang, ask directly. Do not output `执行 Prompt` / `Execution Prompt`.

Template:

```markdown
## 当前结论
Status: Need More Info
Reason: ...

## 已确认
- ...

## 不能先假设
- ...

## 下一步
...
```

## Ready Output

Use this only after all gates are confirmed. Keep it compact. Include only confirmed requirements, acceptance criteria, and forbidden assumptions. Do not add tech stack, implementation advice, database, backend, deployment, security design, or code.

Template:

```markdown
## 当前结论
Status: Ready
Reason: 关键需求和第一版边界已经说清楚。

## 已确认
- ...

## 不能先假设
- ...

## 执行 Prompt
基于以下已确认需求实现一个小应用。只实现用户确认过的内容，不要添加未确认功能。

已确认需求：
- ...

验收标准：
- ...

禁止假设：
- ...
```

For English users, translate the headings naturally and keep `Status: Need More Info` or `Status: Ready`.
