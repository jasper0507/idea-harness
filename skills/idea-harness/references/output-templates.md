# Output Templates

Use these templates for user-facing responses. Keep the wording short, plain, and non-technical.

Do not expose internal audit headings such as `Evidence Ledger`, `Blocking Unknowns`, `Assumption Firewall`, `Requirement Contract`, or `Final AI Execution Prompt` unless the user explicitly asks for the internal audit view.

## Need More Info Template

Use this whenever the idea is not internally `Execution-Ready`. Ask exactly one next question.

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

Rules:

- Do not include `执行 Prompt`.
- Keep `已确认` limited to direct user evidence.
- Put risky guesses in `不能先假设`, not in requirements.
- Ask one question only. Prefer 2-4 concrete choices when helpful.

## Ready Template

Use this only when every execution gate is confirmed by user evidence.

```markdown
## 当前结论
Status: Ready
Reason: 目标、使用者、流程、第一版范围、不做内容、数据行为和验收标准都已确认。

## 已确认
- 目标：...
- 使用者：...
- 核心流程：...
- 第一版必须有：...
- 第一版不做：...
- 数据保存：...
- 验收标准：...

## 不能先假设
- ...

## 执行 Prompt
你将基于以下已确认需求实现一个小网站/小工具/小应用。只实现用户确认过的内容，不要加入“不能先假设”中的功能。

已确认需求：
- 目标：...
- 使用者：...
- 核心流程：...
- 第一版必须有：...
- 第一版不做：...
- 数据保存：...

验收标准：
- 当 ... 时，系统应该 ...
- 如果 ...，系统应该 ...

禁止假设：
- ...
```

Rules:

- Every item in `执行 Prompt` must map to a confirmed user statement.
- Include acceptance criteria under `验收标准`.
- Include forbidden assumptions under `禁止假设`.
- Do not include `[NEEDS CLARIFICATION]`, `待确认`, or `未确认` in `Ready` output.

## Question Style

Prefer everyday language:

| Avoid | Use instead |
|---|---|
| 是否需要持久化存储？ | 关闭页面后，下次打开时这些内容还需要保留吗？ |
| 是否需要鉴权？ | 第一版需要账号登录吗，还是只给你自己直接用？ |
| 是否需要多租户？ | 会有很多人各自管理自己的内容，还是只有你自己用？ |
| 是否需要数据可视化？ | 第一版需要图表，还是只要能看到文字/列表就够了？ |

## Acceptance Criteria Style

Use observable behavior:

- 当 [用户行为] 时，系统应该 [可观察结果]。
- 如果 [条件]，系统应该 [处理方式]。
- 第一版不应包含 [明确非目标]。

Avoid vague standards:

- 界面要好看。
- 工具要智能。
- 应用要完整。
