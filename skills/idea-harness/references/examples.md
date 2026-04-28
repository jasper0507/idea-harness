# Examples

Use these examples to calibrate behavior. They are not scripts; adapt them to the user's exact wording.

## Example 1: Blocked Learning Website

**User**

```text
我想做一个管理学习的网站。
```

**Expected response shape**

```markdown
## Idea Control Status
State: Blocked
Reason: 目标过宽，用户想管理的学习对象尚未确认。

## Evidence Ledger
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | Candidate | "管理学习"；可能是任务、作业、资料或时间管理，但用户未确认 | High |
| Primary user | Missing | None | High |
| Usage scenario | Missing | None | Medium |
| Core workflow | Missing | None | High |
| MVP must-haves | Missing | None | High |
| Explicit non-goals | Missing | None | High |
| Data persistence | Missing | None | Medium |
| Input/output | Missing | None | Medium |
| Acceptance criteria | Missing | None | High |

## Blocking Unknowns
- [NEEDS CLARIFICATION] 先确认用户最想管理哪类学习内容。
- [NEEDS CLARIFICATION] 主要使用者还不明确。
- [NEEDS CLARIFICATION] 第一版必须做什么和不做什么还不明确。

## Assumption Firewall
AI 不得假设：
- 它是任务管理器、课程表、背单词工具、资料库或打卡工具。
- 它需要登录、数据库、图表、AI 功能、移动端或部署方案。

## Next Best Question
你最想先管理哪一类学习内容？
A. 每天要做的学习任务
B. 作业和截止日期
C. 学习笔记或资料
D. 学习时间和打卡

```

Do not include `Requirement Contract` or `Final AI Execution Prompt`.

## Example 2: Contract-Ready But Missing Acceptance

**User**

```text
我想做一个只给自己用的资料整理工具。我粘贴一段文字，它帮我整理成标题、摘要和待办。第一版不做登录、不保存历史、不上传文件。
```

**Expected behavior**

- Confirm `Primary user`, `Input/output`, `Data persistence`, and several non-goals.
- State is at most `Contract-Ready` because acceptance criteria are not confirmed.
- Ask how the user will judge the result is usable.
- Do not include `Final AI Execution Prompt`.

## Example 3: Execution-Ready Pomodoro

**User**

```text
我想做一个个人番茄钟小工具，主要给我自己在电脑浏览器里用。流程是输入任务名，点击开始，倒计时 25 分钟，结束后显示完成提示。我第一版必须有任务名、开始按钮、倒计时和结束提示。第一版不做登录、统计、云同步、多人协作、手机 App，也不保存历史。完成标准是：当我输入任务名并点击开始时，页面显示 25 分钟倒计时；倒计时结束时显示这个任务完成；刷新页面后不需要保留记录。
```

**Expected behavior**

- State is `Execution-Ready`.
- Every hard requirement in the final prompt maps to user evidence.
- Assumption Firewall forbids login, statistics, sync, collaboration, mobile app, storage, analytics, notifications, and deployment assumptions.
- `Final AI Execution Prompt` is allowed.

## Example 4: Conflict

**User**

```text
我想做一个日记网站，只给我自己离线用，不要保存任何数据。但我也希望下次打开还能看到所有以前的日记。
```

**Expected behavior**

- State is `Blocked`.
- Mark Data persistence as `Conflict`.
- Ask the user to choose whether diary content should be kept after closing.
- Do not include `Final AI Execution Prompt`.
