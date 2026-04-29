# Idea Harness Manual Scenarios

Use these scenarios to manually pressure-test `$idea-harness`. The expected behavior is intentionally light: the skill should control requirement readiness without exposing an audit report.

## Scenario 1: Learning Management

**Input**

```text
我想做一个学习管理网站。
```

**Expected**

- Public status is `Need More Info`.
- The response has `当前结论`, `已确认`, `不能先假设`, and `下一步`.
- `已确认` says only that the user wants a learning management site; it does not pretend the product type is known.
- `不能先假设` forbids task manager, course schedule, note app, login, database, charts, AI features, or deployment.
- Asks exactly one next question, preferably about what learning content the user wants to manage first.
- Does not output `执行 Prompt`.

## Scenario 2: Expense Tracker

**Input**

```text
我想做一个记账工具，记录每天花了多少钱。
```

**Expected**

- Public status is `Need More Info` because the primary user and first-version boundary are not confirmed.
- `已确认` can mention "记录每天花了多少钱".
- The skill exposes missing decisions through one next question instead of assuming login, database, charts, budget alerts, sharing, payment integration, mobile app, or cloud sync.
- Does not output `执行 Prompt`.

## Scenario 3: Material Organizer Without Persistence

**Input**

```text
我想做一个帮我整理资料的小应用。我会粘贴一段资料，它帮我分成标题、摘要和待办。只有我自己用，第一版只要能整理一次文本，不需要账号，也不需要保存历史。
```

**Expected**

- Public status is `Need More Info` if acceptance criteria remain unconfirmed.
- `已确认` quotes or paraphrases only confirmed facts such as paste text, output title/summary/todos, personal use, no account, no history.
- `不能先假设` forbids file upload, folders, tags, collaboration, export formats, database, or AI model choice unless confirmed.
- Does not output `执行 Prompt` unless acceptance criteria and all blocking gates are also confirmed by the user.

## Scenario 4: Diary Website Missing Non-Goals

**Input**

```text
我想做一个日记网站，自己每天写一篇日记，下次打开还能看到以前写的内容。完成标准是我能新增一篇、看到列表、点开旧日记。
```

**Expected**

- Public status is `Need More Info` because first-version non-goals are missing.
- `已确认` can mention daily diary writing, persistence, and acceptance criteria.
- The next question asks what V1 explicitly will not do, not framework or deployment.
- Does not output `执行 Prompt`.

## Scenario 5: Ready Small Tool

**Input**

```text
我想做一个个人番茄钟小工具，主要给我自己在电脑浏览器里用。流程是输入任务名，点击开始，倒计时 25 分钟，结束后显示完成提示。我第一版必须有任务名、开始按钮、倒计时和结束提示。第一版不做登录、统计、云同步、多人协作、手机 App，也不保存历史。完成标准是：当我输入任务名并点击开始时，页面显示 25 分钟倒计时；倒计时结束时显示这个任务完成；刷新页面后不需要保留记录。
```

**Expected**

- Public status is `Ready`.
- `已确认` includes goal, user, workflow, must-haves, non-goals, data behavior, and acceptance criteria.
- `执行 Prompt` is allowed and must include acceptance criteria plus forbidden assumptions.
- The prompt must not add login, storage, analytics, sound, notifications, task lists, or deployment unless user evidence exists.

## Scenario 6: Conflicting Request

**Input**

```text
我想做一个日记网站，只给我自己离线用，不要保存任何数据。但我也希望下次打开还能看到所有以前的日记。
```

**Expected**

- Public status is `Need More Info`.
- `当前结论` names the conflict between "不要保存任何数据" and "下次打开还能看到所有以前的日记".
- `下一步` asks the user to choose whether diary content should be kept after closing.
- Does not output `执行 Prompt`.
