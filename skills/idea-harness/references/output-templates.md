# Output Templates

Use these templates exactly enough to keep the structure stable. Keep the wording plain and short.

## Non-Execution Template

Use this when State is `Blocked`, `Draftable`, or `Contract-Ready`.

```markdown
## Idea Control Status
State: Blocked / Draftable / Contract-Ready
Reason: ...

## Evidence Ledger
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | ... | "..." | ... |
| Primary user | ... | ... | ... |
| Usage scenario | ... | ... | ... |
| Core workflow | ... | ... | ... |
| MVP must-haves | ... | ... | ... |
| Explicit non-goals | ... | ... | ... |
| Data persistence | ... | ... | ... |
| Input/output | ... | ... | ... |
| Acceptance criteria | ... | ... | ... |

## Blocking Unknowns
- [NEEDS CLARIFICATION] ...

## Assumption Firewall
AI 不得假设：
- ...

## Next Best Question
...

## Requirement Contract
Goal:
Primary user:
Core scenario:
MVP must-haves:
V1 non-goals:
Data behavior:
Acceptance criteria:
```

Do not include the `Final AI Execution Prompt` heading in non-execution states.

## Execution-Ready Template

Use this only when every blocking gate is `Confirmed`.

```markdown
## Idea Control Status
State: Execution-Ready
Reason: 所有执行门禁都有用户证据。

## Evidence Ledger
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | Confirmed | "..." | Low |

## Blocking Unknowns
- None.

## Assumption Firewall
AI 不得假设：
- ...

## Requirement Contract
Goal:
Primary user:
Core scenario:
MVP must-haves:
V1 non-goals:
Data behavior:
Acceptance criteria:

## Final AI Execution Prompt
你将基于以下已确认需求实现一个小网站/小工具/小应用。只实现用户确认过的内容，不要加入 Assumption Firewall 中禁止的功能。

已确认需求：
- ...

验收标准：
- 当 ... 时，系统应该 ...
- 如果 ...，系统应该 ...

禁止假设：
- ...
```

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
