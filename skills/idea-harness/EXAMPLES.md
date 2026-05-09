# Examples

两个完整对话示例，展示从一句模糊想法到 Ready 的苏格拉底式澄清过程。

每个示例覆盖不同的状态路径和提问技法。圆括号注释标注了当轮使用的问法，仅供 agent 学习参照——用户可见输出中不会出现这些标注。

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

Path: gathering → blocked → gathering → ready

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
