# Evidence Ledger Template

The Evidence Ledger is the internal source of truth. Use it to reason, but do not expose the table to ordinary users unless they explicitly ask for the audit view. Do not let plausible guesses become confirmed requirements.

## Fields

| Field | Meaning | Blocking? |
|---|---|---|
| Goal | What problem the website, tool, or app solves. | Yes |
| Primary user | Who will use it. | Yes |
| Usage scenario | When and why the user uses it. | No |
| Core workflow | The main flow from start to finish. | Yes |
| MVP must-haves | What V1 must include to be useful. | Yes |
| Explicit non-goals | What V1 explicitly will not do. | Yes |
| Data persistence | Whether user-entered content must remain after closing or refreshing. | Conditional |
| Input/output | What the user enters and what the system returns. | No |
| Acceptance criteria | How the user judges that it works. | Yes |

Data persistence blocks only when the idea involves user-entered content, records, notes, tasks, files, journal entries, expenses, or other content that may need to remain available later.

## Row Format

```markdown
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | Confirmed | "..." | Low |
```

## Status Rules

- Use `Confirmed` only with a direct quote or explicit answer.
- Use `Candidate` for a reasonable inference that still needs confirmation.
- Use `Missing` when no evidence exists.
- Use `Conflict` when user statements cannot both be true.
- Write `None` in User Evidence for `Missing`.
- For `Candidate`, say what was inferred and why it cannot be treated as confirmed.

## Evidence Examples

| User text | Field | Correct status |
|---|---|---|
| "我想做一个学习管理网站" | Goal | `Candidate`, because "学习管理" is broad |
| "只有我自己用" | Primary user | `Confirmed` |
| "第一版不做登录" | Explicit non-goals | `Confirmed` |
| "下次打开还能看到" | Data persistence | `Confirmed` |
| "不要保存任何数据" and "下次打开还能看到所有日记" | Data persistence | `Conflict` |

## Public Confirmed Fields

When enough evidence exists, map ledger fields into the public `已确认` section:

```markdown
- 目标：...
- 使用者：...
- 核心流程：...
- 第一版必须有：...
- 第一版不做：...
- 数据保存：...
- 验收标准：...
```

Only confirmed fields can be stated as hard requirements. If a field is not confirmed, keep the public status as `Need More Info` and ask one next question instead of showing a partially filled contract.
