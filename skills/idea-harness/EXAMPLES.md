# Examples

这些例子展示普通人在没有技术背景的情况下，如何把一句模糊的小应用想法，一步一步确认成可交给 AI 执行的清楚需求。

v0.4.0 的默认输出保持极简：

- 澄清阶段只展示 `已确认` 和 `下一步`。
- Ready 阶段只展示 `需求简报`。
- 只有用户明确要求时，才额外输出 `执行 Prompt`。

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

## 下一步
你说的“记一下”，记完之后你最想拿这些记录做什么？

A. 就是存着，偶尔翻翻这个月花了多少
B. 看每个类别分别花了多少
C. 设置每月预算，快超了时提醒
D. 先不想那么多，能记一笔、看到列表就行

推荐：先选 D。它最容易收成一个很小的第一版：只做“记一笔”和“看记录列表”。
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

## 下一步
下次打开时，还要不要看到之前记过的账？

A. 要，保存在当前这个浏览器里
B. 不用，每次打开都是空的也可以
C. 要，换手机或换电脑也能看到

推荐：先选 A。它能满足“下次还在”，但不需要账号登录或云同步。
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
- 不做账号登录、云同步、统计图表、预算提醒、导出、自定义分类、多设备同步。

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

## 下一步
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

## 下一步
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
- 不做购物车、支付、订单系统、账号登录、后台管理、买家留言、库存管理、发货跟踪、会员体系。

验收标准：
- 页面能展示多件作品。
- 每件作品有照片和文字介绍。
- 页面展示微信二维码，买家可以扫码联系。
- 页面风格温暖、有手作感觉。
```

---

## 例3：学习相关 - 「我想做个背单词的工具」

### 用户原文

```text
我想做个背单词的工具，每天学几个新词，有复习提醒的那种。
```

### 第1轮：Need More Info

```markdown
## 已确认
- 你想做一个背单词工具。
- 使用场景是每天学几个新词。
- 你在意复习效果。

## 下一步
第一版里的单词从哪里来？

A. 你自己手动输入单词和意思
B. 使用现成词库，比如四六级、考研、雅思
C. 读文章或看剧遇到生词时，随手加入自己的单词本

推荐：如果你是日常积累，先选 C。它能收成一个很小的第一版：自己添加生词，再复习自己的单词本。
```

### 用户回答

```text
选 C，我平时看英文文章遇到不认识的词就想记下来，积累自己的单词本。
```

### 第2轮：Need More Info

```markdown
## 已确认
- 你想做一个自己用的单词本工具。
- 单词来源是平时阅读遇到的生词。
- 你要自己添加英文单词和中文意思。

## 下一步
复习时第一版用哪种方式？

A. 翻卡片：先看英文，点一下看中文意思
B. 小测验：给一个单词，从几个选项里选意思
C. 两种都要

推荐：先选 A。翻卡片最接近纸质单词卡，第一版也最小。
```

### 用户回答

```text
选 A，翻卡片就行。但我希望下次打开的时候，之前加过的单词还在，不用重新加。
```

### 第3轮：Need More Info

```markdown
## 已确认
- 第一版主动作是添加生词并用翻卡片复习。
- 复习时先看英文，点一下后看到中文意思。
- 下次打开时，之前加过的单词需要还在。

## 下一步
复习时单词按什么顺序出现？

A. 最新添加的先出现
B. 随机出现
C. 没记住的多出现几次，记住的少出现

推荐：先选 A。它最简单，不需要记忆算法，也方便先复习最近添加的词。
```

### 用户回答

```text
选 A 就行。在电脑上用，手机以后再说。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 平时阅读遇到生词后容易散落，想积累成自己的单词本并复习。

用户：
- 自己，在电脑浏览器里使用。

场景：
- 阅读时遇到生词后打开工具添加；复习时打开翻卡片模式。

第一版主动作：
- 添加英文单词和中文意思，并用翻卡片方式复习。

数据行为：
- 单词保存在当前电脑浏览器里；下次打开仍在，清除浏览器数据后会丢失。

不做事项：
- 不做账号登录、现成词库、自动发音、图片联想、间隔重复算法、测验模式、手机适配、多设备同步、导入导出。

验收标准：
- 能添加英文单词和中文意思。
- 添加后能在单词列表里看到。
- 复习模式显示英文，点击后显示中文意思。
- 最新添加的单词先出现。
- 关闭并重新打开同一浏览器后，之前添加的单词仍然存在。
```

---

## 例4：社交/社群 - 「我想做个粉丝群管理」

### 用户原文

```text
我是一个小主播，粉丝越来越多了，想做个东西管理一下我的粉丝群，比如发个通知大家都能看到。
```

### 第1轮：Need More Info

```markdown
## 已确认
- 你是小主播，粉丝越来越多。
- 你想有一个地方管理粉丝相关信息。
- 你提到一个明确需求：发内容让粉丝看到。

## 下一步
你的粉丝现在主要在哪里？

A. 微信群里
B. 抖音、小红书、B 站等平台上
C. 还没有固定地方，想自己建一个

推荐：如果粉丝主要在平台上，先确认平台来源。这样第一版可以先解决“让粉丝在平台之外看到你的内容”。
```

### 用户回答

```text
选 B，我的粉丝主要在抖音，但我不想他们只在抖音看我，想有自己的地方发内容。
```

### 第2轮：Need More Info

```markdown
## 已确认
- 粉丝主要来自抖音。
- 你想建立一个抖音之外的内容发布地方。
- 第一版重点是你发内容，粉丝能看到。

## 下一步
你第一版想发布什么内容形式？

A. 文字公告
B. 文字加图片
C. 文字加图片加视频
D. 付费内容

推荐：先选 B。图文比纯文字更丰富，比视频和付费内容简单，适合第一版。
```

### 用户回答

```text
选 B，文字加图片就行，付费的以后再说。但我想让粉丝关注一下，这样我发新内容他们能收到提醒。
```

### 第3轮：Need More Info

```markdown
## 已确认
- 第一版是你自己的图文内容发布页。
- 内容形式是文字加图片。
- 付费内容以后再说。
- 你希望粉丝能知道你发了新内容。

## 下一步
你说的“提醒”，第一版具体指哪一种？

A. 粉丝收藏页面，之后自己打开查看新内容
B. 浏览器或手机主动推送通知
C. 发到微信群或公众号里

推荐：先选 A。它不需要账号、推送权限或公众号对接，第一版只要把内容页做好。
```

### 用户回答

```text
没有大群，选 A 吧，他们收藏页面，有新内容就来看。关注就是收藏页面的意思。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 想把抖音粉丝沉淀到自己的内容页面，减少只依赖平台发布的限制。

用户：
- 主播作为发布者；粉丝作为浏览者。

场景：
- 主播发布图文内容；粉丝打开收藏的链接，查看内容列表和详情。

第一版主动作：
- 发布并展示图文内容。

数据行为：
- 主播发布的图文内容保存在页面服务里；粉丝不需要登录即可浏览。

不做事项：
- 不做粉丝注册登录、评论、点赞、打赏、付费内容、推送通知、私信、直播、视频内容、关注体系。

验收标准：
- 主播能发布文字加图片内容。
- 粉丝打开链接能看到内容列表。
- 粉丝能点进内容详情查看图文。
- 粉丝不登录也能浏览。
```

---

## 例5：生活服务 - 「我想做个小区团购」

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

## 下一步
微信群接龙最让你头疼的是什么？

A. 不知道谁买了什么、买了多少份
B. 算账和收钱很麻烦
C. 参团的人不知道进度
D. 以上都要

推荐：先选 A。它最聚焦，第一版先解决“统计谁买了什么”这个最具体的问题。
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

## 下一步
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
- 不做支付收款、配送管理、商品库、多团长体系、参团登录、历史团购记录、自动截团、通知提醒。

验收标准：
- 团长能创建一个团购，填写商品名和描述。
- 工具能生成可分享链接。
- 邻居打开链接能填写姓名和份数。
- 团长能看到所有参团记录和总份数。
```

---

## 例6：English Example - A Personal Productivity Tool

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

## Next Step
After you cross something off, what should happen to it?

A. It stays visible, crossed out
B. It disappears from the list
C. It moves to a separate done section

Recommendation: Start with A. It is the smallest version that still lets you see what you finished.
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

## Next Step
Should the list still be there after you close the browser and come back tomorrow?

A. Yes, keep the tasks and done state in the same browser
B. No, start fresh every time
C. Yes, and keep it synced across devices

Recommendation: Start with A. It keeps your daily list without needing accounts or sync.
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
- No categories, due dates, priorities, tags, accounts, login, sharing, collaboration, reminders, notifications, phone app, multiple lists, import, or export.

Acceptance criteria:
- User can type and add a task.
- User can cross off a task.
- Crossed-off tasks stay visible and visually marked as done.
- Closing and reopening the same browser shows the same tasks and states.
```

---

## 例7：生活服务 - 「我想做个宠物寄养预约」

### 用户原文

```text
我在小区开了一个小小的宠物寄养，每次有人问能不能寄养，我都得在微信上一条条问、一条条记，太乱了，想做个简单的预约工具。
```

### 第1轮：Need More Info

```markdown
## 已确认
- 你在小区做宠物寄养。
- 现在靠微信一条条问、一条条记，很乱。
- 你想做一个简单预约工具。

## 下一步
第一版预约时，最需要记清楚哪些信息？

A. 主人是谁、什么时候送来、什么时候接走
B. 以上信息，加上宠物品种和特殊注意事项
C. 以上信息，再自动计算费用

推荐：先选 B。它能解决“信息记不清”的核心问题，费用仍可以你自己算。
```

### 用户回答

```text
选 B 吧，主人信息、时间、宠物情况都要记。费用我自己算就行。
```

### 第2轮：Need More Info

```markdown
## 已确认
- 第一版要记录主人信息、寄养时间、宠物信息和特殊注意事项。
- 不需要自动计算费用。
- 核心问题是替代微信聊天里的混乱记录。

## 下一步
这个工具第一版由谁来填写预约记录？

A. 只有你自己填写，主人仍然在微信告诉你信息
B. 主人打开链接自己填写，你在后台查看
C. 主人和你都可以填写

推荐：先选 A。它最小，不要求宠物主人多做一步，也不需要公开预约表单。
```

### 用户回答

```text
选 A，我来填，主人在微信上说就行，我整理进去。但我想能看现在有哪些宠物在寄养，哪些快到期了。
```

### Ready 输出

```markdown
## 需求简报
问题：
- 宠物寄养信息散落在微信聊天里，容易漏记或查找困难。

用户：
- 寄养服务提供者自己。

场景：
- 主人在微信告知寄养信息后，服务提供者打开工具录入，并查看当前寄养状态。

第一版主动作：
- 新增寄养记录，并查看当前寄养列表和即将到期记录。

数据行为：
- 寄养记录保存在工具里；下次打开仍能看到。

不做事项：
- 不做宠物主人自行预约、在线支付、费用计算、日历视图、短信提醒、宠物主人账号、历史统计。

验收标准：
- 能填写主人姓名、联系方式、宠物品种、特殊注意事项、送来日期、接走日期。
- 能看到当前寄养中的记录列表。
- 能看出哪些记录临近接走日期。
```

---

## 例8：英文例子 - A Family Chore Tracker

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

## Next Step
What happens after a kid checks off a chore?

A. Nothing extra; you just see it is done
B. They earn points or rewards
C. The chore resets on a daily or weekly rotation

Recommendation: Start with A. It solves the referee problem without adding rewards or scheduling rules.
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

## Next Step
How will your kids see their chores?

A. One shared list on a family device, with names next to each chore
B. Each kid gets a separate link or page
C. Each kid logs into their own account

Recommendation: Start with A. A shared list is simplest for a family device and avoids accounts or separate links.
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
- No separate kid accounts, login, points, rewards, weekly rotation, calendar, push notifications, phone app, history, or stats.

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
- 不做账号登录、云同步、统计图表、预算提醒、导出、自定义分类、多设备同步。

验收标准：
- 能选固定分类、填写金额并记一笔。
- 记完后能看到已记录的账目列表。

## 执行 Prompt
你要实现一个小应用。只能实现下面确认过的内容，不要添加任何未确认功能。

问题：
- 做一个自己用的手机浏览器记账工具，避免花了钱之后没有清楚记录。

用户：
- 自己。

核心流程：
- 打开页面 -> 选择固定分类 -> 填写金额 -> 点击“记一笔” -> 看到记录列表。

数据行为：
- 记录保存在当前手机浏览器里；换设备或清除浏览器数据后会丢失。

必须实现：
- 固定分类选择。
- 金额输入。
- “记一笔”按钮。
- 记账记录列表。
- 当前浏览器本地保存。

不得实现：
- 账号登录。
- 云同步。
- 统计图表。
- 预算提醒。
- 导出。
- 自定义分类。
- 多设备同步。

禁止假设：
- 不要添加后端、数据库、支付、AI、通知、分享、多人权限或移动 App 打包。

验收标准：
- 能选固定分类、填写金额并记一笔。
- 记完后能看到已记录的账目列表。
- 关闭并重新打开同一手机浏览器后，记录仍然存在。
```
