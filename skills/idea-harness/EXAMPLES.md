# Examples

三个完整对话示例，展示从一句模糊想法到 Ready（及执行 Prompt）的苏格拉底式澄清过程。

每个示例覆盖不同的状态路径和提问技法：

- 例1（中文）：gathering → needs-precision → ready
- 例2（English）：gathering → blocked → ready → 执行 Prompt
- 例3（中文）：gathering → ready → 回退 → blocked（"你决定"）→ ready

圆括号注释标注了当轮使用的问法，仅供 agent 学习参照——用户可见输出中不会出现这些标注。

---

## 例1：「我想做个背单词的工具」

路径：gathering → gathering → needs-precision → ready

### 用户原文

```text
我想做一个背单词的工具，每天背一点，不想用市面上那些太复杂的 App。
```

### 第1轮（gathering / 具象化）

```markdown
## 已确认
- 你想做一个背单词的工具。
- 你觉得市面上的背单词 App 太复杂。
- 你想每天背一点。

## 追问
上一次你用背单词 App 觉得"太复杂"的那个瞬间，具体是什么让你烦了？
```

### 用户回答

```text
就是打开以后一堆功能，什么打卡排行榜、AI 推荐、错题本……我就想翻翻我自己整理的词，看看哪些还记得、哪些忘了。
```

### 第2轮（gathering / 假设暴露）

```markdown
## 已确认
- 你的核心痛点是：背单词 App 功能太多，你只想翻自己整理的词。
- 主要动作是看一个词，判断自己记不记得。
- 词是你自己整理的，不是从词库里选。

## 追问
你说想看"哪些还记得、哪些忘了"——你是想让工具自动帮你安排今天该复习哪些词，还是自己翻着看就行？
```

### 用户回答

```text
自己翻就行。那些自动安排的反而让我有压力，我就想随便翻翻。
```

### 第3轮（needs-precision / 场景走查）

```markdown
## 已确认
- 你自己整理的词，自己翻着看，判断记没记住。
- 不需要工具自动安排复习计划。
- 第一版不做排行榜、错题本、AI 推荐。

## 追问
我走一遍你的使用场景确认一下：你打开工具 → 看到你的词表 → 翻一个词，心里判断记没记住 → 翻下一个。

等一下——你的词一开始怎么放进去？自己一个一个打字输入，还是从别的地方粘贴进来？
```

### 用户回答

```text
自己打字加进去。不多，每天加几个新词就行。加完以后就可以翻。在手机浏览器里用。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 市面上的背单词 App 功能太多，用户只想翻自己整理的词，判断记没记住。

用户：
- 自己。

场景：
- 每天在手机浏览器里打开，加几个新词，然后翻看已有的词判断是否记住。

第一版主动作：
- 手动添加单词，逐个翻看并自行判断是否记住。

数据行为：
- 单词保存在当前手机浏览器里；换设备或清除浏览器数据后会丢失。

不做事项：
- 不做智能复习算法 — 用户确认自己翻着看就行，自动安排"反而有压力"。
- 不做错题本 — 用户说这是让他觉得"太复杂"的功能之一。
- 不做打卡排行榜 — 用户明确不想要。
- 不做 AI 推荐 — 用户明确不想要。
- 不做词库选择 — 用户确认词是自己整理、手动输入的。
- 不做导入导出 — 用户确认一个一个打字输入，没有提到导入需求。
- 不做账号登录 — 只有用户自己使用。
- 不做云同步 — 用户没有提到换设备需求。

验收标准：
- 用户能输入一个新词并添加到词表。
- 用户能逐个翻看词表中的词。
- 翻看时能先看到词、再看到释义（或反过来），用于自测是否记住。
- 关闭手机浏览器后重新打开，词表仍然存在。
```

---

## Example 2: "I want a tool for my book club to vote on what to read next"

Path: gathering → blocked → gathering → ready, then user requests an execution prompt.

### User Message

```text
I run a small book club with friends. Every month we argue about what to read next. I want a simple tool where people can vote.
```

### Round 1 (gathering / negative definition)

```markdown
## Confirmed
- You run a monthly book club with friends.
- Choosing the next book causes arguments.
- You want a voting tool to settle it.

## Question
Imagine you built this and shared it with your book club, but after one month nobody used it again. What's the most likely reason?
```

### User Reply

```text
Probably too much hassle to use. People would just go back to arguing in the group chat. So it needs to be dead simple — open a link, vote, done.
```

### Round 2 (gathering / trade-off forcing)

```markdown
## Confirmed
- Must be very simple: open a link, vote, done.
- No accounts or sign-up.
- You want to avoid people falling back to the group chat.

## Question
Who decides which books are on the ballot?

A. You pick the options, everyone else just votes
B. Anyone in the club can suggest books, then everyone votes

Recommended: Start with A — you said "dead simple." If anyone can suggest, you also need a suggestion step, a deadline for suggestions, and a way to handle duplicates.
```

### User Reply

```text
Hmm, I want both actually. People should be able to suggest AND vote. It's not that complicated.
```

### Round 3 (blocked / trade-off forcing)

```markdown
## Confirmed
- You want both suggesting and voting.

## Question
You said the tool must be "dead simple — open a link, vote, done." But suggest-then-vote means two separate steps, a suggestion deadline, and handling duplicates or joke entries.

Voting on books you pre-pick: one screen, done in a minute.
Suggesting + voting: multiple steps, needs a cutoff, and you'll have to moderate.

For V1, which one?
```

### User Reply

```text
Fine, I'll pick the books myself for V1. I can always just ask in the group chat for suggestions and then put the shortlist in the tool.
```

### Round 4 (gathering / consequence projection)

```markdown
## Confirmed
- V1: you set the book options, friends vote.
- No suggestion feature in V1.
- No accounts — open a link and vote.

## Question
After everyone votes and there's a winner — then what? Do you just want to see which book won, or do you need to see how each person voted?
```

### User Reply

```text
Just which book won and how many votes each got. I don't need to know who voted for what. We're 8 people by the way, no more.
```

### Ready Output

```markdown
## Requirements Brief
Problem:
- A monthly book club of 8 friends argues about what to read next and needs a quick way to decide.

User:
- The organizer sets up the vote; 8 club members vote.

Scenario:
- Each month the organizer creates a vote with a shortlist of books, shares the link in the group chat. Members open the link and pick one book. The organizer checks the result.

V1 main action:
- Cast a vote on a shortlist of books and see which book won.

Data behavior:
- The organizer enters book titles when creating a vote. Votes are collected without requiring names or accounts. The result page shows vote counts per book and the winner.

Non-goals:
- No book suggestion feature — user confirmed they will collect suggestions in the group chat and enter the shortlist themselves.
- No per-person vote breakdown — user only wants to see totals and the winner.
- No accounts or login — user said "open a link, vote, done."
- No multiple rounds or runoff — user did not mention tie-breaking.
- No reminders or notifications — user did not ask for them.
- No history of past votes — user did not mention needing it.
- No comments or discussion — user wants to avoid recreating the group chat.

Acceptance criteria:
- Organizer can create a vote with 2 or more book titles.
- The tool generates a shareable link.
- A club member can open the link and cast one vote without signing in.
- After voting, the result page shows vote counts per book.
- The book with the most votes is visually marked as the winner.
```

### User Reply

```text
Looks good. Give me a prompt I can paste into Cursor to build it.
```

### Execution Prompt Output

```markdown
## Execution Prompt
You are implementing a small app. Only implement what is confirmed below. Do not add any unconfirmed features.

Current pain point:
- A monthly book club of 8 friends argues about what to read next and needs a quick way to decide.

Expected behavior:
- The organizer enters 2 or more book titles to create a vote.
- The tool produces a shareable link for that vote.
- Any club member opens the link and picks one book without signing in or giving a name.
- After picking, the member sees the current vote counts per book.
- The book with the most votes is visually marked as the winner.

Data behavior:
- Book titles are entered by the organizer when creating the vote.
- Votes are collected anonymously — no names, no sign-in.
- The result view shows the count per book and highlights the winner.

Must implement:
- Create a vote with 2 or more book titles.
- Generate a shareable link for that vote.
- Cast one vote per visit without sign-in.
- Show vote counts per book.
- Visually mark the book with the most votes as the winner.

Must not implement:
- No book suggestion feature — user confirmed they will collect suggestions in the group chat and enter the shortlist themselves.
- No per-person vote breakdown — user only wants to see totals and the winner.
- No accounts or login — user said "open a link, vote, done."
- No multiple rounds or runoff — user did not mention tie-breaking.
- No reminders or notifications — user did not ask for them.
- No history of past votes — user did not mention needing it.
- No comments or discussion — user wants to avoid recreating the group chat.

Forbidden assumptions:
- Do not add any feature not listed above.
- Do not implement anything listed under "Must not implement".

Acceptance criteria:
- Organizer can create a vote with 2 or more book titles.
- The tool generates a shareable link.
- A club member can open the link and cast one vote without signing in.
- After voting, the result page shows vote counts per book.
- The book with the most votes is visually marked as the winner.
```

---

## 例3：「我想做个记账的小工具」

路径：gathering → ready → gathering（回退）→ blocked（"你决定"）→ ready

### 用户原文

```text
我想做一个特别简单的记账工具，就记一下每天花了多少钱。
```

### 第1轮（gathering / 具象化 + 对比锚定）

```markdown
## 已确认
- 你想做一个记账工具。
- 只记每天花了多少钱。
- 你想要特别简单。

## 追问
你现在是怎么记的？用备忘录、Excel、还是脑子记？跟现在的方式比，你最想省掉的是哪一步？
```

### 用户回答

```text
现在用备忘录，每次要自己打日期，然后写金额和买了什么。我就想省掉打日期这步，打开直接输入金额和一句话备注就行。
```

### 第2轮（gathering / 后果推演）

```markdown
## 已确认
- 你现在用备忘录记账，痛点是每次要手动打日期。
- 主动作：打开 → 输入金额 + 一句话备注 → 完成。
- 日期由工具自动填。

## 追问
记了一个月以后，你会回头看这些记录吗？如果会，你想看到什么——一条一条翻，还是想看个总数？
```

### 用户回答

```text
会看。就想看这个月一共花了多少，不用太细。一条一条翻也行但主要是看总数。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 用备忘录记账每次要手动打日期，嫌麻烦。

用户：
- 自己。

场景：
- 每天花钱后打开工具，输入金额和一句话备注，日期自动填好。月底看一下这个月总共花了多少。

第一版主动作：
- 输入一笔支出（金额 + 备注），查看当月总支出。

数据行为：
- 每笔记录包含日期（自动）、金额、备注。保存在当前设备浏览器里。

不做事项：
- 不做分类标签 — 用户说只要金额和一句话备注，没提分类。
- 不做图表统计 — 用户说"就想看总数，不用太细"。
- 不做预算提醒 — 用户没有提到预算概念。
- 不做多设备同步 — 用户没有提到换设备需求。
- 不做账号登录 — 只有用户自己使用。
- 不做导出功能 — 用户没有提到导出需求。

验收标准：
- 用户能输入金额和一句话备注，提交后记录出现在列表中。
- 每条记录自动显示当天日期。
- 用户能看到当月所有记录的总金额。
- 关闭浏览器后重新打开，之前的记录仍然存在。
```

### 用户回答（Ready 后改主意）

```text
等等，我还想加一个功能：能按月份翻看之前的记录，不只是看当月。
```

### 第3轮（gathering / 回退后追问）

```markdown
## 已确认
- 你想增加按月份查看历史记录的功能。
- 之前确认的主动作不变：输入金额 + 备注。

## 追问
按月份翻看的时候，你想看到什么？每个月的总数就够了，还是要能展开看那个月每一笔？
```

### 用户回答

```text
看到每个月总数就行。点进去能看明细更好，但你决定吧，我不确定。
```

### 第4轮（blocked / "你决定"处理）

```markdown
## 已确认
- 你想按月份看历史，至少看到每月总数。

## 追问
我的建议是第一版只显示每月总数列表，不做点进去看明细。

你说过主要就是"看总数，不用太细"。如果以后发现光看总数不够，再加明细只是多一步，不影响已有功能。

这样可以吗？
```

### 用户回答

```text
行，就先只看每月总数。
```

### Ready 输出（更新后）

```markdown
## 需求简报
问题：
- 用备忘录记账每次要手动打日期，嫌麻烦。想回头看每月花了多少但备忘录翻起来不方便。

用户：
- 自己。

场景：
- 每天花钱后打开工具，输入金额和一句话备注，日期自动填好。想回顾时按月份查看每月总支出。

第一版主动作：
- 输入一笔支出（金额 + 备注），按月查看历史总支出。

数据行为：
- 每笔记录包含日期（自动）、金额、备注。保存在当前设备浏览器里。按月汇总显示总数。

不做事项：
- 不做月份明细展开 — 用户确认第一版只看每月总数。
- 不做分类标签 — 用户说只要金额和一句话备注，没提分类。
- 不做图表统计 — 用户说"就想看总数，不用太细"。
- 不做预算提醒 — 用户没有提到预算概念。
- 不做多设备同步 — 用户没有提到换设备需求。
- 不做账号登录 — 只有用户自己使用。
- 不做导出功能 — 用户没有提到导出需求。

验收标准：
- 用户能输入金额和一句话备注，提交后记录出现在列表中。
- 每条记录自动显示当天日期。
- 用户能看到当月所有记录的总金额。
- 用户能看到一个月份列表，每个月显示该月总支出。
- 关闭浏览器后重新打开，之前的记录仍然存在。
```
