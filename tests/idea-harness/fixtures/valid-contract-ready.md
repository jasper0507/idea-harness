## Idea Control Status
State: Contract-Ready
Reason: The requirement contract can be drafted, but acceptance criteria still need confirmation.

## Evidence Ledger
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | Confirmed | "只给自己用的资料整理工具" | Low |
| Primary user | Confirmed | "只给自己用" | Low |
| Usage scenario | Confirmed | "粘贴一段文字" | Low |
| Core workflow | Confirmed | "粘贴一段文字，它帮我整理成标题、摘要和待办" | Low |
| MVP must-haves | Confirmed | "整理成标题、摘要和待办" | Low |
| Explicit non-goals | Confirmed | "不做登录、不保存历史、不上传文件" | Low |
| Data persistence | Confirmed | "不保存历史" | Low |
| Input/output | Confirmed | "粘贴一段文字" and "标题、摘要和待办" | Low |
| Acceptance criteria | Missing | None | High |

## Blocking Unknowns
- [NEEDS CLARIFICATION] Confirm how the user will judge the整理 result is usable.

## Assumption Firewall
AI 不得假设：
- Login, history storage, file upload, database, export, folders, tags, or deployment.

## Next Best Question
你会怎样判断整理结果已经可用？

## Requirement Contract
Goal: Build a personal material organizer.
Primary user: The user.
Core scenario: Paste text and receive title, summary, and todos.
MVP must-haves: Title, summary, and todos.
V1 non-goals: Login, history storage, and file upload.
Data behavior: No history storage.
Acceptance criteria: [NEEDS CLARIFICATION]
