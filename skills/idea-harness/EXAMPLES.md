# Examples

## Chinese: Fuzzy Idea

User:

```text
我想做一个学习管理网站。
```

Expected shape:

```markdown
## 当前结论
Status: Need More Info
Reason: “学习管理网站”还太宽，最容易跑偏的是先管理哪类学习内容。

## 已确认
- 你想做一个学习管理网站。

## 不能先假设
- 不能先假设它是任务管理器、课程表、笔记库、登录产品、数据库产品或图表看板。

## 下一步
你最想先管理哪一类学习内容？
A. 每天要做的学习任务
B. 作业和截止日期
C. 学习笔记或资料
D. 学习时间和打卡

推荐：如果你还不确定，先选 A，因为它最容易收成一个很小的第一版。
```

## English: Ready Small Tool

User:

```text
I want a simple browser tool for myself to run 25-minute focus sessions. I enter a task name, press start, see a countdown, and get a finished message when time is up. V1 must include a task name field, start button, countdown, and finished message. V1 should not include accounts, history, stats, notifications, sharing, mobile apps, or cloud sync. It does not need to keep anything after refresh. It is done when starting shows a 25-minute countdown and finishing shows the task is complete.
```

Expected shape:

```markdown
## Current Conclusion
Status: Ready
Reason: The goal, user, flow, V1 scope, non-goals, data behavior, and acceptance criteria are clear.

## Confirmed
- Goal: Build a personal 25-minute focus-session tool.
- User: The user, using it in a browser.
- Core flow: Enter a task name, press start, see a countdown, then see a finished message.
- V1 must include: task name, start button, countdown, finished message.
- V1 will not include: accounts, history, stats, notifications, sharing, mobile apps, or cloud sync.
- Data behavior: Nothing needs to remain after refresh.
- Acceptance criteria: Starting shows a 25-minute countdown; finishing shows the task is complete.

## Forbidden Assumptions
- Do not add accounts, storage, analytics, notifications, sharing, mobile apps, cloud sync, deployment, or a tech stack recommendation.

## Execution Prompt
Build a small app based only on the confirmed requirements below. Do not add unconfirmed features.

Confirmed requirements:
- Build a personal 25-minute focus-session browser tool.
- Let the user enter a task name, start a countdown, and see a completion message.
- Do not keep data after refresh.

Acceptance criteria:
- When the user enters a task name and starts, the page shows a 25-minute countdown.
- When the countdown ends, the page shows that the task is complete.

Forbidden assumptions:
- Do not add accounts, storage, analytics, notifications, sharing, mobile apps, cloud sync, deployment, or a tech stack recommendation.
```
