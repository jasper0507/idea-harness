## Idea Control Status
State: Execution-Ready
Reason: All execution gates have user evidence.

## Evidence Ledger
| Field | Status | User Evidence | Risk |
|---|---|---|---|
| Goal | Confirmed | "个人番茄钟小工具" | Low |
| Primary user | Confirmed | "给我自己在电脑浏览器里用" | Low |
| Core workflow | Confirmed | "输入任务名，点击开始，倒计时 25 分钟，结束后显示完成提示" | Low |
| MVP must-haves | Confirmed | "任务名、开始按钮、倒计时和结束提示" | Low |
| Explicit non-goals | Confirmed | "不做登录、统计、云同步、多人协作、手机 App" | Low |
| Data persistence | Confirmed | "刷新页面后不需要保留记录" | Low |
| Acceptance criteria | Confirmed | "页面显示 25 分钟倒计时；倒计时结束时显示这个任务完成" | Low |

## Blocking Unknowns
- None.

## Assumption Firewall
AI 不得假设：
- Login, statistics, cloud sync, collaboration, mobile app, storage, analytics, notifications, or deployment.

## Requirement Contract
Goal: Build a personal Pomodoro tool.
Primary user: The user, on a computer browser.
Core scenario: Enter a task name, start a 25-minute countdown, and see a completion message.
MVP must-haves: Task name, start button, countdown, and completion message.
V1 non-goals: Login, statistics, cloud sync, collaboration, mobile app, and history storage.
Data behavior: Refreshing the page does not need to preserve records.
Acceptance criteria: Starting with a task name shows a 25-minute countdown; when it ends, the task completion is shown.

## Final AI Execution Prompt
已确认需求：
- Goal: Build a personal Pomodoro tool.
- Primary user: The user, on a computer browser.
- Core workflow: Enter a task name, click start, show a 25-minute countdown, then show a completion message.
