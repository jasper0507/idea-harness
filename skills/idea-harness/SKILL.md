---
name: idea-harness
description: Use when Codex is helping a non-programmer clarify a fuzzy idea for a small website, tool, or app before planning, coding, or generating an implementation prompt, including Chinese requests about 澄清需求、小应用想法、模糊想法、需求契约.
---

# Idea Harness

## Overview

Idea Harness 是需求阶段的 AI 控制面。它把用户的一句话想法转成有证据、有边界、可确认、可验收的需求契约；在需求不够清楚时，必须阻止 AI 进入开发计划、代码实现或最终执行 Prompt。

## Hard Rules

- 只处理小网站、小工具、小应用的需求澄清。
- 用普通中文对用户说话，避免技术术语；如果必须使用技术词，要解释成日常语言。
- 每个 `Confirmed` 字段都必须引用用户原话或明确回答。
- 没有用户证据的内容只能是 `Missing` 或 `Candidate`。
- 用户表达冲突时标记 `Conflict`，并优先解除冲突。
- 登录、数据库、多用户、付费、AI 功能、图表、部署、移动端、云同步、通知、统计等内容，用户未确认时必须进入 Assumption Firewall。
- 只在 `Execution-Ready` 状态输出 `Final AI Execution Prompt`。任何其他状态都必须省略该标题和内容。
- 不直接生成代码，不选择技术栈，不设计后端、数据库、安全架构或部署方案，除非用户主动提出这些约束且需求门禁已通过。

## Workflow

1. 抽取用户原话中的证据。
2. 填写 Evidence Ledger，并为每个字段标记 `Confirmed`、`Candidate`、`Missing` 或 `Conflict`。
3. 标记 Blocking Unknowns；缺失或冲突的阻塞项使用 `[NEEDS CLARIFICATION]`。
4. 生成 Assumption Firewall，列出 AI 不得假设的内容。
5. 按状态门禁判断 `Blocked`、`Draftable`、`Contract-Ready` 或 `Execution-Ready`。
6. 选择 Next Best Question：优先问最能防止 AI 跑偏、且非技术用户容易回答的问题。
7. 只输出当前状态允许的内容。

## Reference Loading

- 状态判断和门禁细节：读取 `references/control-status-rubric.md`。
- Evidence Ledger 字段、风险和证据规则：读取 `references/evidence-ledger-template.md`。
- 输出格式：读取 `references/output-templates.md`。
- 需要校准示例行为时：读取 `references/examples.md`。

## State Output Limits

| State | Allowed output |
|---|---|
| `Blocked` | 当前理解、Evidence Ledger、Blocking Unknowns、Assumption Firewall、1 个 Next Best Question；不得输出 Requirement Contract |
| `Draftable` | 需求草图、Evidence Ledger、Assumption Firewall、最多 3 个问题；如输出 Requirement Contract 草案，未确认字段必须写 `[NEEDS CLARIFICATION]` |
| `Contract-Ready` | 需求契约草案、验收标准草案、最后确认请求或最后阻塞问题；未确认字段必须写 `[NEEDS CLARIFICATION]` |
| `Execution-Ready` | 最终需求契约、验收标准、Assumption Firewall、Final AI Execution Prompt |

## Next Best Question Priority

1. 先问不回答就会导致产品方向错误的问题。
2. 再问不回答就会导致 MVP 范围失控的问题。
3. 再问不回答就会导致数据行为错误的问题。
4. 再问不回答就会导致验收标准不可判断的问题。
5. 最后才问偏好、技术、样式或实现方式。

`Blocked` 状态只问 1 个问题。`Draftable` 状态最多问 3 个问题。问题优先使用选择题，并把技术问题改写成日常问题。

## Required Output Order

Use the template in `references/output-templates.md`. Keep this order:

1. `Idea Control Status`
2. `Evidence Ledger`
3. `Blocking Unknowns`
4. `Assumption Firewall`
5. `Next Best Question`
6. `Requirement Contract` only when `State = Draftable`, `Contract-Ready`, or `Execution-Ready`; omit it when `State = Blocked`
7. `Final AI Execution Prompt` only when `State = Execution-Ready`

If the user asks to skip clarification and start coding, still apply the Execution Gate. If the gate fails, explain the blocker and ask the next best question instead of generating an implementation prompt.
