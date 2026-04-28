## Idea Control Status
State: Blocked
Reason: Data persistence has conflicting user evidence.

## Evidence Ledger
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | Confirmed | "做一个日记网站" | Low |
| Primary user | Confirmed | "只给我自己离线用" | Low |
| Usage scenario | Confirmed | "写日记" | Medium |
| Core workflow | Missing | None | High |
| MVP must-haves | Missing | None | High |
| Explicit non-goals | Confirmed | "不要保存任何数据" | High |
| Data persistence | Conflict | "不要保存任何数据" conflicts with "下次打开还能看到所有以前的日记" | High |
| Input/output | Candidate | Diary text is likely entered, but exact input and output are not confirmed | Medium |
| Acceptance criteria | Missing | None | High |

## Blocking Unknowns
- [NEEDS CLARIFICATION] Resolve whether diary content should remain after closing.

## Assumption Firewall
AI 不得假设：
- It stores diary content, deletes diary content, uses a database, syncs to cloud, or has accounts.

## Next Best Question
关闭页面后，下次打开时日记还需要保留吗？
