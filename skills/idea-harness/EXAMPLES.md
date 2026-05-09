# Examples

完整对话示例，展示从一句模糊想法到 Ready 的澄清过程。

---

## 例1：个人工具 - 「我想做个记账的东西」

### 用户原文

```text
我想做一个记账的东西，平时花了钱就想记一下，不想太麻烦。
```

### 第1轮：Need More Info

```markdown
## 已确认
- 你想做一个记账的小工具。
- 使用场景是平时花了钱后随手记一下。
- 你希望第一版不要太麻烦。

## 追问
你说的"记一下"，记完之后你最想拿这些记录做什么？

A. 就是存着，偶尔翻翻这个月花了多少
B. 看每个类别分别花了多少
C. 设置每月预算，快超了时提醒
D. 先不想那么多，能记一笔、看到列表就行

推荐：先选 D。它最容易收成一个很小的第一版：只做"记一笔"和"看记录列表"。
```

### 用户回答

```text
选 D 吧，先能记就行。但我希望能选一下是花了什么类别的钱，比如吃饭还是交通。
```

### 第2轮：Need More Info

```markdown
## 已确认
- 你想做一个自己用的简单记账工具。
- 第一版主动作是选分类、填金额、记一笔。
- 第一版要能看到记过的账目列表。
- 需要固定分类，比如吃饭、交通。

## 追问
下次打开时，还要不要看到之前记过的账？

A. 要，保存在当前这个浏览器里
B. 不用，每次打开都是空的也可以
C. 要，换手机或换电脑也能看到

推荐：先选 A。它能满足"下次还在"，但不需要账号登录或云同步。
```

### 用户回答

```text
选 A。手机浏览器里用就行，分类固定几个，不用自己加。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 平时花钱后没有清楚记录，想用一个简单工具随手记账。

用户：
- 自己。

场景：
- 花钱后打开手机浏览器，选分类并记录一笔支出。

第一版主动作：
- 选择固定分类，填写金额，记一笔，并看到记录列表。

数据行为：
- 记录保存在当前手机浏览器里；换设备或清除浏览器数据后会丢失。

不做事项：
- 不做账号登录 — 只有用户自己使用，不需要区分身份。
- 不做云同步 — 用户确认只在一台手机浏览器使用。
- 不做统计图表 — 用户说"先能记就行"，统计以后再说。
- 不做预算提醒 — 用户没有提到预算需求。
- 不做导出 — 第一版只需本地查看。
- 不做自定义分类 — 用户确认使用固定分类。
- 不做多设备同步 — 用户确认只在一台手机使用。

验收标准：
- 能选固定分类、填写金额并记一笔。
- 记完后能看到已记录的账目列表。
- 关闭并重新打开同一手机浏览器后，记录仍然存在。
```

---

## 例2：小生意 - 「我想开个网店卖手工」

### 用户原文

```text
我想开个网店，卖我自己做的手工饰品，之前朋友都说好看，想试试在网上卖。
```

### 第1轮：Need More Info

```markdown
## 已确认
- 你想在网上展示并售卖自己做的手工饰品。
- 现在还处在刚开始尝试的阶段。
- 你的第一目标是看看有没有人想买。

## 追问
第一版里，买家看到作品后要怎么购买？

A. 看作品展示页，然后通过微信或手机号联系你
B. 直接在页面里下单付款
C. 先跳到小红书、闲鱼等平台再购买

推荐：先选 A。它最小，不需要购物车、支付和订单系统，适合先验证有没有人想买。
```

### 用户回答

```text
选 A 吧，先做个展示页，放我的微信二维码，有人喜欢就联系我。但我想能放很多作品，每个作品有自己的照片和介绍。
```

### 第2轮：Need More Info

```markdown
## 已确认
- 第一版是手工饰品展示页。
- 买家看作品后通过微信二维码联系你。
- 每个作品需要照片和文字介绍。
- 第一版不需要购物车、支付或订单系统。

## 追问
作品资料第一版怎么放进去？

A. 你把作品照片和介绍给制作页面的人，由对方写进页面
B. 你自己登录后台，上传照片和介绍
C. 买家也可以上传作品或留言

推荐：先选 A。现在作品不多时，这样最简单，不需要后台、账号或上传系统。
```

### 用户回答

```text
选 A，现在就几件作品，你帮我加进去。以后多了再说。但页面希望有手作的温暖感觉。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 想把手工饰品展示给潜在买家，减少只靠聊天介绍作品的麻烦。

用户：
- 买家通过手机或电脑浏览器访问页面；作者提供作品资料。

场景：
- 买家打开链接，浏览作品列表，查看作品照片和介绍，再通过微信二维码联系作者。

第一版主动作：
- 展示多件作品，并让买家看到联系方式。

数据行为：
- 作品照片和介绍由制作者手动写入页面；作者不需要自己登录管理。

不做事项：
- 不做购物车和支付 — 第一版只做展示，验证有没有人想买。
- 不做订单系统 — 交易通过微信直接完成。
- 不做账号登录 — 买家无需注册，作者无需后台。
- 不做后台管理 — 现在作品少，手动写入页面即可。
- 不做买家留言 — 用户没有提到留言需求。
- 不做库存管理 — 第一版不涉及订单和库存追踪。
- 不做发货跟踪 — 用户没有提到物流需求。
- 不做会员体系 — 第一版只做展示和联系。

验收标准：
- 页面能展示多件作品。
- 每件作品有照片和文字介绍。
- 页面展示微信二维码，买家可以扫码联系。
- 页面风格温暖、有手作感觉。
```

---

## 例3：社群服务 - 「我想做个小区团购」

### 用户原文

```text
我们小区经常有人组织团购，但每次都在微信群里接龙，乱七八糟的，想做个工具来管理团购。
```

### 第1轮：Need More Info

```markdown
## 已确认
- 场景是小区团购。
- 现在用微信群接龙，信息很乱。
- 你想做一个工具管理团购。

## 追问
微信群接龙最让你头疼的是什么？

A. 不知道谁买了什么、买了多少份
B. 算账和收钱很麻烦
C. 参团的人不知道进度
D. 以上都要

推荐：先选 A。它最聚焦，第一版先解决"统计谁买了什么"这个最具体的问题。
```

### 用户回答

```text
选 A，主要是统计很麻烦，谁买了什么、几份，一条条翻聊天记录太累了。
```

### 第2轮：Need More Info

```markdown
## 已确认
- 第一版重点是解决团购统计混乱。
- 团长需要清楚看到谁买了什么、买了几份。
- 暂时不处理收款和进度。

## 追问
第一版的团购一般怎么组织？

A. 每次只团一个商品，邻居填姓名和份数
B. 每次有多个商品，邻居从商品列表里选择
C. 多个团长都能各自开团

推荐：先选 A。单商品开团最小，能直接替代微信群接龙。
```

### 用户回答

```text
选 A，一般就一个商品，比如今天团水果，明天团鸡蛋。参团的人不用登录，填名字和份数就行。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 小区团购用微信群接龙统计很乱，团长需要清楚知道谁买了什么和买了几份。

用户：
- 团长作为组织者；邻居作为参团者。

场景：
- 团长开一个单商品团购，把链接发到群里；邻居打开链接填写姓名和份数；团长查看统计。

第一版主动作：
- 单商品开团并收集参团记录。

数据行为：
- 团购和参团记录保存在工具里；邻居不需要登录，只填写姓名和份数。

不做事项：
- 不做支付收款 — 用户说暂时不处理收款。
- 不做配送管理 — 用户没有提到配送需求。
- 不做商品库 — 每次只团一个商品，不需要商品列表。
- 不做多团长体系 — 第一版只有一个团长组织。
- 不做参团登录 — 用户确认邻居只填名字和份数。
- 不做历史团购记录 — 用户没有提到查看历史需求。
- 不做自动截团 — 用户没有提到截止时间需求。
- 不做通知提醒 — 用户没有提到通知需求。

验收标准：
- 团长能创建一个团购，填写商品名和描述。
- 工具能生成可分享链接。
- 邻居打开链接能填写姓名和份数。
- 团长能看到所有参团记录和总份数。
```

---

## Example 4: Personal Tool — "A Minimal To-Do List"

### User Message

```text
I want to make a to-do list but not like the ones you see everywhere. I want something really minimal. Just type what I need to do, and cross it off when done. No categories, no due dates, no fancy stuff.
```

### Round 1: Need More Info

```markdown
## Confirmed
- You want a very minimal to-do list.
- Core action: type a task and cross it off when done.
- You do not want categories, due dates, or extra features.

## Question
After you cross something off, what should happen to it?

A. It stays visible, crossed out
B. It disappears from the list
C. It moves to a separate done section

Recommended: Start with A. It is the smallest version that still lets you see what you finished.
```

### User Reply

```text
A, definitely. I like seeing a long list of crossed-out stuff at the end of the day. Makes me feel productive.
```

### Round 2: Need More Info

```markdown
## Confirmed
- You want a minimal personal to-do list.
- Tasks stay visible after completion, marked as done.
- V1 does not need categories, due dates, priorities, sharing, or reminders.

## Question
Should the list still be there after you close the browser and come back tomorrow?

A. Yes, keep the tasks and done state in the same browser
B. No, start fresh every time
C. Yes, and keep it synced across devices

Recommended: Start with A. It keeps your daily list without needing accounts or sync.
```

### User Reply

```text
Yeah, I need it to survive. I'll use it in my browser on my laptop. No need for a phone version.
```

### Ready Output

```markdown
## Requirements Brief
Problem:
- Daily tasks are easy to lose track of, and existing to-do apps feel too heavy.

User:
- The user, in a laptop browser.

Scenario:
- During the workday, the user opens the browser list, adds tasks, and crosses them off.

V1 main action:
- Add a task and mark it done while keeping done tasks visible.

Data behavior:
- Tasks and done state persist in the same browser. Clearing browser data removes them.

Non-goals:
- No categories — user explicitly does not want them.
- No due dates — user explicitly does not want them.
- No priorities or tags — user wants it minimal.
- No accounts or login — single user on one device.
- No sharing or collaboration — personal use only.
- No reminders or notifications — user did not ask for them.
- No phone app — user confirmed laptop-only.
- No multiple lists — user wants one simple list.
- No import or export — user did not ask for them.

Acceptance criteria:
- User can type and add a task.
- User can cross off a task.
- Crossed-off tasks stay visible and visually marked as done.
- Closing and reopening the same browser shows the same tasks and states.
```

---

## Example 5: Family Tool — "A Chore Tracker for My Kids"

### User Message

```text
I need something to track chores for my kids. They never remember whose turn it is to do what, and I'm tired of being the referee. I want to assign chores and they can check them off.
```

### Round 1: Need More Info

```markdown
## Confirmed
- You want a chore tracker for your kids.
- Problem: they do not remember whose turn it is.
- You want to assign chores and let kids check them off.

## Question
What happens after a kid checks off a chore?

A. Nothing extra; you just see it is done
B. They earn points or rewards
C. The chore resets on a daily or weekly rotation

Recommended: Start with A. It solves the referee problem without adding rewards or scheduling rules.
```

### User Reply

```text
A is fine for now. I just want to see who's done what without nagging.
```

### Round 2: Need More Info

```markdown
## Confirmed
- V1 is a simple family chore tracker.
- Parent assigns chores.
- Kids check chores off.
- No points, rewards, or rotation for V1.

## Question
How will your kids see their chores?

A. One shared list on a family device, with names next to each chore
B. Each kid gets a separate link or page
C. Each kid logs into their own account

Recommended: Start with A. A shared list is simplest for a family device and avoids accounts or separate links.
```

### User Reply

```text
Two kids, ages 10 and 12. They'll use the family iPad. A shared list with names works fine.
```

### Ready Output

```markdown
## Requirements Brief
Problem:
- The parent has to remind kids whose turn it is to do chores.

User:
- Parent assigns chores; two kids, ages 10 and 12, check them off on the family iPad.

Scenario:
- Parent adds chores with a kid's name. Kids open the shared list on the iPad and check off finished chores.

V1 main action:
- Assign a chore to a kid and mark it done.

Data behavior:
- Chores and done state persist in the same browser on the family iPad. Clearing browser data removes them.

Non-goals:
- No separate kid accounts or login — shared device, shared list.
- No points or rewards — user says "fine for now" without them.
- No weekly rotation — user did not ask for scheduling.
- No calendar view — user did not ask for date-based tracking.
- No push notifications — user did not ask for reminders.
- No phone app — family iPad only.
- No history or stats — user just wants current status.

Acceptance criteria:
- Parent can add a chore and assign it to a specific kid.
- The shared page shows chores with assigned kid names.
- Kids can check off chores.
- Done and not-done chores are visually distinct.
```

---

## 按需执行 Prompt 示例

### 用户追加要求

```text
现在生成可以交给 Codex 的执行 Prompt。
```

### 输出

```markdown
## 需求简报
问题：
- 做一个自己用的手机浏览器记账工具，避免花了钱之后没有清楚记录。

用户：
- 自己。

场景：
- 平时花钱后打开手机浏览器随手记录。

第一版主动作：
- 选择固定分类，填写金额，记一笔，并看到记录列表。

数据行为：
- 记录保存在当前手机浏览器里；换设备或清除浏览器数据后会丢失。

不做事项：
- 不做账号登录 — 只有用户自己使用，不需要区分身份。
- 不做云同步 — 用户确认只在一台手机浏览器使用。
- 不做统计图表 — 用户说"先能记就行"，统计以后再说。
- 不做预算提醒 — 用户没有提到预算需求。
- 不做导出 — 第一版只需本地查看。
- 不做自定义分类 — 用户确认使用固定分类。
- 不做多设备同步 — 用户确认只在一台手机使用。

验收标准：
- 能选固定分类、填写金额并记一笔。
- 记完后能看到已记录的账目列表。
- 关闭并重新打开同一手机浏览器后，记录仍然存在。

## 执行 Prompt
你要实现一个小应用。只能实现下面确认过的内容，不要添加任何未确认功能。

当前痛点：
- 做一个自己用的手机浏览器记账工具，避免花了钱之后没有清楚记录。

期望行为：
- 打开页面后，用户选择固定分类，填写金额，点击记录。
- 记录完成后，用户在列表中看到这笔记录。
- 关闭页面后重新打开，之前的记录仍然存在。

数据行为：
- 记录保存在当前手机浏览器里；换设备或清除浏览器数据后会丢失。

必须实现：
- 固定分类选择。
- 金额输入。
- 记录提交。
- 记账记录列表。
- 当前浏览器本地保存。

不得实现：
- 账号登录 — 只有用户自己使用，不需要区分身份。
- 云同步 — 用户确认只在一台手机浏览器使用。
- 统计图表 — 用户说"先能记就行"，统计以后再说。
- 预算提醒 — 用户没有提到预算需求。
- 导出 — 第一版只需本地查看。
- 自定义分类 — 用户确认使用固定分类。
- 多设备同步 — 用户确认只在一台手机使用。

禁止假设：
- 不要添加任何上面没有确认的功能。
- 不要添加后端、数据库、支付、AI、通知、分享、多人权限或移动 App 打包。

验收标准：
- 能选固定分类、填写金额并记一笔。
- 记完后能看到已记录的账目列表。
- 关闭并重新打开同一手机浏览器后，记录仍然存在。
```
