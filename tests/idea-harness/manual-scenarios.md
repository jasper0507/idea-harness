# Idea Harness Manual Scenarios

Use these scenarios to manually pressure-test `$idea-harness`. The expected behavior is intentionally narrow: the skill should control requirement readiness, not expand the idea into product design or code.

## Scenario 1: Learning Management

**Input**

```text
我想做一个学习管理网站。
```

**Expected**

- State is `Blocked`.
- `Goal` is at most `Candidate`, not `Confirmed`, because "学习管理" is too broad.
- `Core workflow`, `MVP must-haves`, `Explicit non-goals`, and `Acceptance criteria` are `Missing`.
- Assumption Firewall forbids assuming task manager, course schedule, note app, login, database, charts, AI features, or deployment.
- Asks exactly one next question, preferably about what learning content the user wants to manage first.
- Does not output `Final AI Execution Prompt`.

## Scenario 2: Expense Tracker

**Input**

```text
我想做一个记账工具，记录每天花了多少钱。
```

**Expected**

- State is `Blocked` because `Primary user` is not confirmed.
- `Goal` can be `Confirmed` from "记录每天花了多少钱".
- The skill exposes missing user, workflow, data retention, MVP boundary, non-goals, and acceptance criteria instead of assuming them.
- Assumption Firewall forbids assuming login, database, charts, budget alerts, multi-user sharing, payment integration, mobile app, or cloud sync.
- Does not output `Final AI Execution Prompt`.

## Scenario 3: Material Organizer Without Persistence

**Input**

```text
我想做一个帮我整理资料的小应用。我会粘贴一段资料，它帮我分成标题、摘要和待办。只有我自己用，第一版只要能整理一次文本，不需要账号，也不需要保存历史。
```

**Expected**

- State is at most `Contract-Ready` when only acceptance criteria remain unconfirmed; if core workflow is incomplete, state is at most `Draftable`.
- Confirmed fields must quote user evidence such as "粘贴一段资料" and "不需要保存历史".
- Data persistence is `Confirmed` as no history needed.
- The skill must not assume file upload, database, AI model choice, folders, tags, collaboration, or export formats.
- Does not output `Final AI Execution Prompt` unless acceptance criteria and all blocking gates are also confirmed by the user.

## Scenario 4: Diary Website Missing Non-Goals

**Input**

```text
我想做一个日记网站，自己每天写一篇日记，下次打开还能看到以前写的内容。完成标准是我能新增一篇、看到列表、点开旧日记。
```

**Expected**

- State is at most `Draftable` because `Explicit non-goals` is missing.
- Data persistence can be `Confirmed` from "下次打开还能看到以前写的内容".
- Acceptance criteria can be `Confirmed` from "新增一篇、看到列表、点开旧日记".
- The skill should ask about what V1 explicitly will not do, not about framework or deployment.
- Does not output `Final AI Execution Prompt`.

## Scenario 5: Execution-Ready Small Tool

**Input**

```text
我想做一个个人番茄钟小工具，主要给我自己在电脑浏览器里用。流程是输入任务名，点击开始，倒计时 25 分钟，结束后显示完成提示。我第一版必须有任务名、开始按钮、倒计时和结束提示。第一版不做登录、统计、云同步、多人协作、手机 App，也不保存历史。完成标准是：当我输入任务名并点击开始时，页面显示 25 分钟倒计时；倒计时结束时显示这个任务完成；刷新页面后不需要保留记录。
```

**Expected**

- State is `Execution-Ready`.
- All blocking gates are `Confirmed` with direct user evidence.
- Final requirement contract only includes confirmed requirements.
- `Final AI Execution Prompt` is allowed and must include acceptance criteria plus Assumption Firewall.
- The prompt must not add login, storage, analytics, sound, notifications, task lists, or deployment unless user evidence exists.

## Scenario 6: Conflicting Request

**Input**

```text
我想做一个日记网站，只给我自己离线用，不要保存任何数据。但我也希望下次打开还能看到所有以前的日记。
```

**Expected**

- State is `Blocked`.
- Data persistence is `Conflict`.
- Blocking Unknowns explicitly mention the conflict between "不要保存任何数据" and "下次打开还能看到所有以前的日记".
- Next Best Question asks the user to choose whether diary content should be kept after closing.
- Does not output `Final AI Execution Prompt`.
