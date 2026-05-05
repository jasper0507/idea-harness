# Examples

这些例子展示普通人在没有技术背景的情况下，如何描述一个模糊的小应用想法，以及 Idea Harness 如何一步步把想法变成可以动手做的需求。

每个例子都从一句模糊的话开始，经过两三轮澄清，最终到达 Ready 状态。例子之间没有先后关系，可以根据实际场景参考。

---

## 例1：个人工具 —— 「我想做个记账的东西」

### 用户原文

```text
我想做一个记账的东西，平时花了钱就想记一下，不想太麻烦。
```

### 第1轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: "记账"有很多方向，最容易跑偏的是做成一个功能太多、太复杂的记账 App。

## 已确认
- 你想做一个记账的小工具。
- 使用场景：平时花了钱随手记一下。
- 核心诉求：不想太麻烦，要简单。

## 不能先假设
- 不能先假设它需要账号登录。
- 不能先假设它需要统计图表。
- 不能先假设它需要预算提醒。
- 不能先假设它需要支持多个人使用。

## 下一步
你说的"记一下"，记完之后你最想拿这些记录做什么？

A. 就是存着，偶尔翻翻这个月花了多少
B. 想看看每个类别（吃饭、交通、买东西）分别花了多少
C. 想设定一个每月预算，快超了的时候提醒我
D. 先不想那么多，能记就行

推荐：如果你只是想随手记、偶尔看看，选 D 最简单，第一版只做"记一笔、看列表"就够了。
```

### 用户回答

```text
选 D 吧，先能记就行。但我希望能选一下是花了什么类别的钱，比如吃饭还是交通。
```

### 第2轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 分类记账的方向已确认，但还需要确认数据是否需要保留、用什么设备。

## 已确认
- 你想做一个简单的个人记账工具。
- 核心流程：选分类、填金额、记一笔。
- 有分类：吃饭、交通等。
- 第一版不需要统计图表、预算提醒、多人使用。

## 不能先假设
- 不能先假设它需要注册账号。
- 不能先假设换设备后数据还在。
- 不能先假设需要自定义分类。

## 下一步
你现在打算在什么设备上用？

A. 手机浏览器
B. 电脑浏览器
C. 两个都要，数据要同步

还有，分类是用固定的几个（吃饭、交通、日用品、娱乐），还是要自己随便加？

推荐：如果你只是自己用，先用固定分类、在手机浏览器上用最简单，后面再加功能也不迟。
```

### 用户回答

```text
手机浏览器吧。分类就固定的那几个，不用自己加。
```

### Ready 输出

```markdown
## 当前结论
Status: Ready
Reason: 目标用户、核心流程、功能范围、数据行为和验收标准都已确认。

## 已确认
- 目标：做一个自己用的手机浏览器记账工具。
- 用户：自己，在手机浏览器里使用。
- 核心流程：打开页面 → 选分类（吃饭、交通、日用品、娱乐）→ 填金额 → 点"记一笔" → 看到自己的记账列表。
- V1 必须包含：固定分类选择、金额输入、记一笔按钮、记账记录列表。
- V1 不做：自定义分类、统计图表、预算提醒、账号登录、多人使用、导出功能。
- 数据行为：数据存在手机本地，换设备或清除浏览器后数据会丢失。
- 验收标准：能选分类、填金额、记一笔；能看到自己记过的所有账。

## 不能先假设
- 不能添加账号登录、云同步、统计图表、预算提醒、导出、自定义分类、多设备同步。

## 验收标准
- 打开页面能选分类（吃饭、交通、日用品、娱乐）、填金额、点"记一笔"。
- 记完后能看到自己记过的账目列表。
```

---

## 例2：小生意 —— 「我想开个网店卖手工」

### 用户原文

```text
我想开个网店，卖我自己做的手工饰品，之前朋友都说好看，想试试在网上卖。
```

### 第1轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: "网上卖手工"涉及很多环节，最容易跑偏的是直接做成一个完整的电商平台。

## 已确认
- 你想在网上卖自己做的手工饰品。
- 起因：朋友觉得好看，想试试看。
- 阶段：刚开始尝试，还没确定能不能卖出去。

## 不能先假设
- 不能先假设需要购物车、订单系统、支付对接。
- 不能先假设需要会员体系、积分、优惠券。
- 不能先假设需要库存管理、发货跟踪。
- 不能先假设需要多商家入驻。

## 下一步
你打算怎么让买家来买？

A. 把作品展示出来，放个联系方式（微信/手机号），让买家直接联系我下单
B. 做一个能直接下单付款的店铺，买家自己选、自己付
C. 先在一个平台（比如小红书、闲鱼）上卖，自己再做一个展示页

推荐：如果你刚开始试，选 A 最简单——做一个展示页，放作品照片和联系方式，不用处理支付和订单，先验证有没有人想买。
```

### 用户回答

```text
选 A 吧，先做个展示页，放我的微信二维码，有人喜欢就联系我。但我想能放很多作品，每个作品有自己的照片和介绍。
```

### 第2轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 展示页方向已确认，还需确认访问方式和是否需要后台管理。

## 已确认
- 你想做一个手工饰品展示页。
- 核心流程：放作品照片、介绍、微信二维码，买家看到喜欢的直接联系你下单。
- 每个作品有自己的照片和文字介绍。
- 不需要购物车、支付、订单系统。

## 不能先假设
- 不能先假设需要注册登录。
- 不能先假设需要后台管理界面。
- 不能先假设需要买家留言功能。

## 下一步
作品的资料（照片、介绍）你想怎么加进去？

A. 你把资料给我，我帮你写进页面里（每次要改就再找我）
B. 有一个后台页面，你自己登录后上传照片、写介绍，不用找别人

推荐：如果作品还不多（比如 10 件以内），选 A 最简单，不用多做一个后台管理页面。等作品多了再升级也可以。
```

### 用户回答

```text
现在就几件作品，选 A 吧，你帮我加进去。以后多了再说。但我希望页面好看一点，有那种手作的温暖感觉。
```

### Ready 输出

```markdown
## 当前结论
Status: Ready
Reason: 目标、核心流程、功能范围、数据行为和验收标准都已确认。

## 已确认
- 目标：做一个手工饰品展示页，用来吸引买家联系你下单。
- 用户：买家（在手机或电脑浏览器打开链接）。
- 核心流程：买家打开页面 → 看到作品列表 → 点进每个作品看照片和介绍 → 看到底部微信二维码 → 扫码联系你。
- V1 必须包含：作品展示列表（每个作品有照片和文字介绍）、作品详情页、微信二维码展示。
- V1 不做：购物车、支付、订单系统、账号登录、后台管理、买家留言、会员体系、库存管理。
- 页面风格：有手作温暖感，用柔和的颜色和自然的感觉。
- 数据行为：作品内容由作者手动添加，不需要用户自己管理。
- 验收标准：能展示多件作品，每件作品有照片和介绍，底部有微信二维码，买家可以扫码联系。

## 不能先假设
- 不能添加购物车、支付、订单、账号登录、后台管理、买家留言、库存、发货、会员体系。

## 验收标准
- 页面上有作品列表，点进去能看到每件作品的照片和介绍。
- 页面底部有微信二维码，买家可以扫码联系。
- 页面风格温暖、有手作感觉。
```

---

## 例3：学习相关 —— 「我想做个背单词的工具」

### 用户原文

```text
我想做个背单词的工具，每天学几个新词，有复习提醒的那种。
```

### 第1轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: "背单词"有很多实现方式，最容易跑偏的是做成一个完整的学习平台。

## 已确认
- 你想做一个背单词的工具。
- 使用场景：每天学几个新词。
- 你提到了"复习提醒"，说明你在意复习效果。

## 不能先假设
- 不能先假设需要词库导入功能。
- 不能先假设需要发音播放。
- 不能先假设需要多人排行榜。
- 不能先假设需要复杂的记忆算法。

## 下一步
你的单词来源是什么？

A. 我自己手动输入想背的单词和意思
B. 用一个现成的词库（比如四六级、考研、雅思）
C. 读书、看剧的时候遇到不认识的词，想随手加进去

推荐：如果你有明确的考试目标（比如四六级），选 B 最方便；如果只是平时积累，选 C 更灵活。
```

### 用户回答

```text
选 C，我平时看英文文章遇到不认识的词就想记下来，积累自己的单词本。
```

### 第2轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 单词来源已确认，还需要确认复习方式和数据保存。

## 已确认
- 你想做一个自己用的单词本工具。
- 单词来源：自己手动添加，来自平时阅读遇到的生词。
- 每个单词包含：英文单词和中文意思。
- 目标：积累自己的单词库，方便复习。

## 不能先假设
- 不能先假设需要注册账号。
- 不能先假设需要自动发音。
- 不能先假设需要间隔重复算法。
- 不能先假设需要手机 App。

## 下一步
复习的时候你希望怎么用？

A. 打开页面，看到一个单词，想一下意思，点一下翻面看答案（简单的翻卡片）
B. 做个小测验，给一个单词，从四个选项里选正确的意思
C. 两种都要

推荐：如果你只是想快速复习，选 A（翻卡片）最简单，也最接近"翻单词卡"的直觉。
```

### 用户回答

```text
选 A，翻卡片就行。但我希望下次打开的时候，之前加过的单词还在，不用重新加。
```

### 第3轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 翻卡片复习已确认，还需确认使用设备和复习顺序。

## 已确认
- 你想做一个自己用的单词本工具。
- 核心流程：添加单词（英文+中文）→ 复习时翻卡片。
- 复习方式：看到英文 → 点一下 → 翻面看到中文意思。
- 数据要求：下次打开时之前添加的单词还在。

## 不能先假设
- 不能先假设需要注册账号。
- 不能先假设需要自动发音、图片联想。
- 不能先假设需要间隔重复算法。

## 下一步
复习的时候，单词按什么顺序出现？

A. 最新加的先复习
B. 随机顺序
C. 没记住的多出现几次，记住的少出现

推荐：选 A 最简单，新加的排在最前面，复习完一遍再从头开始。
```

### 用户回答

```text
选 A 就行。在电脑上用，手机以后再说。
```

### Ready 输出

```markdown
## 当前结论
Status: Ready
Reason: 目标、核心流程、功能范围、数据行为和验收标准都已确认。

## 已确认
- 目标：做一个自己用的网页单词本，方便积累和复习平时遇到的生词。
- 用户：自己，在电脑浏览器里使用。
- 核心流程：添加单词（输入英文和中文意思）→ 进入复习模式 → 看到英文 → 点击翻面看到中文 → 继续下一个。
- V1 必须包含：单词添加功能（英文+中文输入）、单词列表、复习翻卡片模式（点一下翻面）、数据在浏览器保存（下次打开还在）。
- V1 不做：注册登录、自动发音、图片联想、间隔重复算法、测验模式、手机适配、多设备同步、导入导出。
- 数据行为：单词数据保存在浏览器本地，下次打开还在；清除浏览器数据后会丢失。
- 复习顺序：最新添加的排在最前面。
- 验收标准：能添加单词并保存；复习时能看到英文、点一下看到中文意思；下次打开页面之前添加的单词还在。

## 不能先假设
- 不能添加注册登录、自动发音、间隔重复算法、测验模式、手机适配、多设备同步、导入导出。

## 验收标准
- 能添加单词（英文+中文），添加后出现在单词列表里。
- 复习模式：显示英文，点击后翻面显示中文意思。
- 下次打开页面，之前添加的单词还在。
```

---

## 例4：社交/社群 —— 「我想做个粉丝群管理」

### 用户原文

```text
我是一个小主播，粉丝越来越多了，想做个东西管理一下我的粉丝群，比如发个通知大家都能看到。
```

### 第1轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: "粉丝群管理"范围很广，最容易跑偏的是做成一个完整的社区平台。

## 已确认
- 你是一个小主播，粉丝越来越多。
- 你想做一个东西来管理粉丝群。
- 一个明确的需求：发通知让粉丝都能看到。

## 不能先假设
- 不能先假设需要论坛、帖子、评论功能。
- 不能先假设需要粉丝分等级、打赏系统。
- 不能先假设需要私信功能。
- 不能先假设需要直播功能。

## 下一步
你说的"粉丝群"，现在粉丝主要在哪里？

A. 微信群，粉丝加你微信进群
B. 抖音/小红书/B站等平台的粉丝
C. 还没有固定的群，想自己建一个

推荐：如果你已经有微信群，选 A——做一个公告板工具，你发公告，粉丝扫码或点链接就能看到，不用把所有粉丝加到一个大群里。
```

### 用户回答

```text
选 B，我的粉丝主要在抖音，但我不想他们只在抖音看我，想有自己的地方发内容。
```

### 第2轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 想建立自己的内容发布渠道，但还需要确认内容形式和互动需求。

## 已确认
- 你是小主播，粉丝主要在抖音。
- 想建立自己的渠道，不完全依赖抖音。
- 一个核心需求：发内容，粉丝能看到。

## 不能先假设
- 不能先假设需要粉丝注册账号。
- 不能先假设需要评论、点赞功能。
- 不能先假设需要付费内容、打赏功能。
- 不能先假设需要直播功能。

## 下一步
你想在自己的地方发什么类型的内容？

A. 主要是文字公告（比如活动通知、直播时间、动态分享）
B. 文字 + 图片（图文内容）
C. 文字 + 图片 + 视频
D. 还有付费内容（只有付费的粉丝才能看）

推荐：选 B（文字 + 图片）最实用，既能发公告通知，也能发图文动态，比纯文字丰富，比视频简单。
```

### 用户回答

```text
选 B，文字加图片就行，付费的以后再说。但我想让粉丝关注一下，这样我发新内容他们能收到提醒。
```

### 第3轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 图文发布已确认，还需要确认"关注"和"提醒"的具体含义。

## 已确认
- 你想做一个自己的图文内容发布页。
- 内容形式：文字 + 图片。
- 你发内容，粉丝能看到。
- 想让粉丝"关注"，有新内容时收到提醒。

## 不能先假设
- 不能先假设需要推送通知（浏览器通知、短信等）。
- 不能先假设需要粉丝之间互动。
- 不能先假设需要复杂的关注体系。

## 下一步
你说的"提醒"，你希望粉丝怎么收到？

A. 粉丝加到一个微信群里，你在工具里发内容，自动转发到群里
B. 粉丝收藏这个页面，你发了新内容，他们下次打开就能看到
C. 做一个微信公众号，发内容自动推送

推荐：如果你已经有微信群，选 A 最直接——你在一个地方发内容，自动同步到群里，粉丝在微信里就能看到。
```

### 用户回答

```text
没有大群，选 B 吧，他们收藏页面，有新内容就来看。关注就是收藏页面的意思。
```

### Ready 输出

```markdown
## 当前结论
Status: Ready
Reason: 目标、核心流程、功能范围、数据行为和验收标准都已确认。

## 已确认
- 目标：做一个小主播自己的图文内容发布页，用来沉淀抖音以外的粉丝。
- 用户：主播（发布者）+ 粉丝（浏览者），通过链接访问，手机或电脑浏览器。
- 核心流程：主播发布内容（文字+图片）→ 粉丝打开链接看到内容列表 → 点进去看详情。
- V1 必须包含：内容发布功能（文字+图片，主播在后台发布）、内容列表页（粉丝打开链接看到所有内容）、内容详情页。
- V1 不做：粉丝注册登录、评论互动、点赞打赏、付费内容、推送提醒、私信、直播、视频内容、关注体系。
- 数据行为：内容由主播发布后保存在服务器，粉丝随时可以查看；不需要粉丝账号。
- 验收标准：主播能发布图文内容；粉丝打开链接能看到内容列表并点进去看详情。

## 不能先假设
- 不能添加粉丝注册登录、评论互动、点赞打赏、付费内容、推送通知、私信、直播、关注体系、视频内容。

## 验收标准
- 主播能在后台发布图文内容（文字+图片）。
- 粉丝打开链接能看到内容列表，点进去看详情。
- 不需要粉丝登录就能浏览内容。
```

---

## 例5：生活服务 —— 「我想做个小区团购」

### 用户原文

```text
我们小区经常有人组织团购，但每次都在微信群里接龙，乱七八糟的，想做个工具来管理团购。
```

### 第1轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: "管理团购"有很多环节，最容易跑偏的是做成一个完整的电商系统。

## 已确认
- 场景：小区团购，经常有人组织。
- 现在的方式：微信群接龙，比较混乱。
- 想做一个工具来管理团购。

## 不能先假设
- 不能先假设需要支付功能。
- 不能先假设需要商品库、库存管理。
- 不能先假设需要配送管理。
- 不能先假设需要多个团长各自开团。

## 下一步
微信群接龙最让你头疼的是什么？

A. 不知道谁买了什么、买了多少份
B. 买完之后算账、收钱很麻烦
C. 参团的人不知道团购的进度（成团了没、什么时候到货）
D. 以上都有

推荐：选 A 最聚焦——先解决"统计谁买了什么"这个最痛的问题，算账和进度后面再加。
```

### 用户回答

```text
选 A，主要是统计很麻烦，谁买了什么、几份，一条条翻聊天记录太累了。
```

### 第2轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 统计需求已确认，还需要确认使用流程和角色。

## 已确认
- 场景：小区团购，目前用微信群接龙。
- 核心痛点：统计谁买了什么、几份很麻烦。
- 第一版重点：解决统计混乱的问题。

## 不能先假设
- 不能先假设需要支付、收款功能。
- 不能先假设需要配送跟踪。
- 不能先假设需要多个团长。
- 不能先假设需要商品库。

## 下一步
团购一般怎么组织的？

A. 你（团长）选好一个商品（比如水果、鸡蛋），发出来让大家选要不要、要几份
B. 有好几个商品，大家从列表里自己选
C. 有时候是水果，有时候是日用品，品类不固定

还有，参团的人需要登录吗？还是用链接就能参加？

推荐：如果每次团购就一两个商品，选 A（单个商品开团）最简单；参团的人不需要登录，用链接就能填，最方便。
```

### 用户回答

```text
选 A，一般就一个商品，比如今天团水果，明天团鸡蛋。参团的人不用登录，填名字和份数就行。
```

### Ready 输出

```markdown
## 当前结论
Status: Ready
Reason: 目标、核心流程、功能范围、数据行为和验收标准都已确认。

## 已确认
- 目标：做一个小区团购统计工具，替代微信群接龙，让团长能清楚看到谁买了什么。
- 用户：团长（组织者）+ 参团的邻居们，用手机浏览器。
- 核心流程：团长开团（填商品名、描述、截团时间）→ 生成一个链接/二维码发到群里 → 邻居点链接填姓名和份数 → 团长在后台看到所有参团记录和汇总。
- V1 必须包含：开团功能（团长填商品信息）、参团页面（邻居填姓名和份数）、参团记录列表（团长看谁买了什么、汇总总份数）。
- V1 不做：支付收款、配送管理、商品库、多团长体系、参团登录、历史团购记录、自动截团、通知提醒。
- 数据行为：团购数据在服务器保存，参团的人不需要登录，填姓名和份数即可；团长在后台能看到当次团购的所有记录。
- 验收标准：团长能开团并生成链接；邻居点链接能参团填写；团长能看到所有人的参团记录和总份数汇总。

## 不能先假设
- 不能添加支付、配送、商品库、多团长、登录、历史记录、自动截团、通知提醒。

## 验收标准
- 团长能开一个团（填商品名、描述）并生成分享链接。
- 邻居打开链接能填写姓名和份数。
- 团长后台能看到所有参团记录，以及总份数汇总。
```

---

## 例6：English Example —— A Personal Productivity Tool

### User Message

```text
I want to make a to-do list but not like the ones you see everywhere. I want something really minimal. Just type what I need to do, and cross it off when done. No categories, no due dates, no fancy stuff.
```

### Round 1: Need More Info

```markdown
## Current Conclusion
Status: Need More Info
Reason: "A minimal to-do list" is clear in spirit, but the details around saving and device would most likely cause guessing.

## Confirmed
- You want a minimal to-do list tool.
- Core flow: type a task, cross it off when done.
- No categories, no due dates, no fancy stuff.

## Forbidden Assumptions
- Cannot assume it needs user accounts.
- Cannot assume it needs priority levels, tags, or categories.
- Cannot assume it needs due dates, reminders, or notifications.
- Cannot assume it needs sharing or collaboration.
- Cannot assume it needs a mobile app.

## Next Step
When you cross something off, should it disappear from the list, or stay visible but crossed out?

A. It stays on the list, crossed out — so I can see what I've done today
B. It gets removed from the list — I only want to see what's left
C. It moves to a separate "done" section

Recommendation: If you want to feel a sense of progress, A (stay crossed out) is the simplest and most satisfying — no extra sections or pages needed.
```

### User Reply

```text
A, definitely. I like seeing a long list of crossed-out stuff at the end of the day. Makes me feel productive.
```

### Round 2: Need More Info

```markdown
## Current Conclusion
Status: Need More Info
Reason: Cross-out behavior is confirmed. Still need to confirm data saving and device.

## Confirmed
- You want a minimal to-do list tool.
- Core flow: type a task → it appears on the list → cross it off when done → it stays visible but crossed out.
- No categories, due dates, priorities, tags, accounts, sharing, or collaboration.

## Forbidden Assumptions
- Cannot assume it needs user accounts or login.
- Cannot assume it needs to sync across devices.
- Cannot assume it needs reminders or notifications.

## Next Step
Should the list survive if you close the browser and come back tomorrow?

A. Yes — I want my tasks and crossed-out items to still be there next time I open it
B. No — a fresh start every time I open the page is fine

Also, where will you use it?

Recommendation: If this is your daily work tool, you probably want it to survive (A). And using it in a browser on your computer is the simplest setup.
```

### User Reply

```text
Yeah, I need it to survive. I'll use it in my browser on my laptop. No need for a phone version.
```

### Ready Output

```markdown
## Current Conclusion
Status: Ready
Reason: Goal, user, core flow, V1 scope, non-goals, data behavior, and acceptance criteria are all confirmed.

## Confirmed
- Goal: Build a personal minimal to-do list for daily use.
- User: The user, in a browser on a laptop.
- Core flow: Type a task → it appears on the list → cross it off when done → it stays visible but marked as done.
- V1 must include: task input field, task list, cross-off action (stays visible but crossed out), data persistence across sessions.
- V1 will not include: categories, due dates, priorities, tags, accounts, login, sharing, collaboration, reminders, notifications, mobile version, multiple lists, import/export.
- Data behavior: Tasks persist across browser sessions (close and reopen, tasks are still there). Data is stored in the browser; clearing browser data removes the tasks.
- Acceptance criteria: Can add a task; can cross off a task (stays visible, marked as done); closing and reopening the browser shows the same list.

## Forbidden Assumptions
- Do not add accounts, login, categories, due dates, priorities, tags, sharing, reminders, notifications, mobile version, multiple lists, import/export, or a tech stack recommendation.

## Acceptance Criteria
- User can type a task and add it to the list.
- User can cross off a task; the task stays on the list, visually marked as done.
- Closing and reopening the browser shows the same tasks and their status.
```

---

## 例7：生活服务 —— 「我想做个宠物寄养预约」

### 用户原文

```text
我在小区开了一个小小的宠物寄养，每次有人问能不能寄养，我都得在微信上一条条问、一条条记，太乱了，想做个简单的预约工具。
```

### 第1轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: "预约工具"的范围很广，最容易跑偏的是做成一个带日历、支付、客服的完整预约系统。

## 已确认
- 你在小区做宠物寄养。
- 现在的方式：微信一条条问、一条条记，很乱。
- 想做一个简单的预约工具。

## 不能先假设
- 不能先假设需要在线支付。
- 不能先假设需要日历排期视图。
- 不能先假设需要宠物主人注册账号。
- 不能先假设需要多种宠物类型。
- 不能先假设需要价格计算器。

## 下一步
寄养预约的时候，你最需要记清楚的信息是什么？

A. 谁的宠物、什么时候送来、什么时候接走
B. 以上 + 宠物的品种、特殊注意事项（比如吃什么、怕什么）
C. 以上 + 自动算费用

推荐：先选 B，把主人信息、寄养时间和宠物特殊情况记清楚，费用可以自己算，这样第一版最实用。
```

### 用户回答

```text
选 B 吧，主人信息、时间、宠物情况都要记。费用我自己算就行。
```

### 第2轮：Need More Info

```markdown
## 当前结论
Status: Need More Info
Reason: 记录内容已确认，还需要确认使用流程。

## 已确认
- 你想做一个宠物寄养记录工具。
- 记录内容：主人信息（名字、联系方式）、寄养时间（送来日期、接走日期）、宠物信息（品种、特殊注意事项）。
- 不需要在线支付、费用计算。

## 不能先假设
- 不能先假设需要宠物主人自己填写。
- 不能先假设需要日历视图。
- 不能先假设需要短信提醒。

## 下一步
这个工具谁来用？

A. 只有你自己用——主人在微信上告诉你信息，你自己填进去
B. 主人自己打开链接填写预约，你在后台看

推荐：选 A 最简单——你把微信上的信息整理填进去就行，主人不需要多做一个操作，也不会填错。
```

### 用户回答

```text
选 A，我来填，主人在微信上说就行，我整理进去。但我想能看现在有哪些宠物在寄养，哪些快到期了。
```

### Ready 输出

```markdown
## 当前结论
Status: Ready
Reason: 目标、核心流程、功能范围、数据行为和验收标准都已确认。

## 已确认
- 目标：做一个个人用的宠物寄养记录工具，替代微信聊天记录里的混乱信息。
- 用户：自己，在手机或电脑浏览器里使用。
- 核心流程：主人在微信告诉你信息 → 你在工具里填写预约记录（主人姓名、联系方式、宠物品种、特殊注意事项、送来日期、接走日期）→ 查看当前寄养列表和即将到期的记录。
- V1 必须包含：新增寄养记录表单（主人信息、宠物信息、寄养时间、特殊注意事项）、当前寄养记录列表、即将到期记录高亮显示。
- V1 不做：宠物主人自己预约、在线支付、日历视图、短信提醒、宠物主人账号、历史记录统计。
- 数据行为：记录保存在工具里，下次打开还在。
- 验收标准：能填写寄养记录；能看到当前寄养列表；能看出来哪些快到期了。

## 不能先假设
- 不能添加宠物主人自行预约、在线支付、日历视图、短信提醒、账号登录、历史统计。

## 验收标准
- 能填写新的寄养记录（主人姓名、联系方式、宠物品种、特殊注意事项、送来日期、接走日期）。
- 能看到当前寄养中的记录列表。
- 能看出来哪些寄养快到期了（比如临近接走日期的高亮显示）。
```

---

## 例8：英文例子 —— A Family Chore Tracker

### User Message

```text
I need something to track chores for my kids. They never remember whose turn it is to do what, and I'm tired of being the referee. I want to assign chores and they can check them off.
```

### Round 1: Need More Info

```markdown
## Current Conclusion
Status: Need More Info
Reason: "Track chores for kids" can go many directions — from a simple checklist to a reward system with points and allowance.

## Confirmed
- You want a chore tracker for your kids.
- Problem: kids don't remember whose turn it is.
- You want to assign chores and let kids check them off.

## Forbidden Assumptions
- Cannot assume it needs points, rewards, or allowance tracking.
- Cannot assume it needs multiple kids with separate logins.
- Cannot assume it needs a weekly schedule or calendar.
- Cannot assume it needs a mobile app.

## Next Step
What happens after a kid checks off a chore?

A. Nothing — I just want to see that it's done, so I don't have to ask
B. I want to give them points or a reward for finishing
C. It should reset for the next day or week, so the same chores rotate

Recommendation: If your main goal is just to stop being the referee, A is enough for V1 — assign chores, kids check them off, you see what's done. Points and rotation can come later.
```

### User Reply

```text
A is fine for now. I just want to see who's done what without nagging.
```

### Round 2: Need More Info

```markdown
## Current Conclusion
Status: Need More Info
Reason: The "assign and check off" flow is clear. Need to confirm how kids interact with it.

## Confirmed
- You want a simple chore tracker for your family.
- Core flow: you assign chores → kids check them off → you see what's done.
- No points, rewards, or rotation for V1.

## Forbidden Assumptions
- Cannot assume kids need their own accounts or logins.
- Cannot assume it needs a mobile app.
- Cannot assume it needs push notifications.

## Next Step
How will your kids see their chores?

A. They open a link on a shared family tablet or computer — everyone sees the same list with names next to each chore
B. Each kid gets their own link or page — they only see their own chores

Also, how many kids are we talking about?

Recommendation: If it's 2–3 kids and a shared device, A (one shared list) is the simplest — no separate links to manage.
```

### User Reply

```text
Two kids, ages 10 and 12. They'll use the family iPad. A shared list with names works fine.
```

### Ready Output

```markdown
## Current Conclusion
Status: Ready
Reason: Goal, user, core flow, V1 scope, non-goals, data behavior, and acceptance criteria are all confirmed.

## Confirmed
- Goal: Build a simple family chore tracker so the parent doesn't have to remind kids whose turn it is.
- User: Parent (assigns chores) + two kids (ages 10 and 12), using the family iPad.
- Core flow: Parent assigns chores with kid names → kids open the page on the iPad → kids check off chores when done → parent sees what's done and what's not.
- V1 must include: chore input (chore name + assigned kid), shared chore list with names, check-off action for each chore, clear view of what's done vs. not done.
- V1 will not include: separate logins for each kid, points or rewards, weekly rotation or calendar, push notifications, mobile app, history or stats.
- Data behavior: Chores persist across sessions. Data is stored in the browser; clearing browser data removes it.
- Acceptance criteria: Parent can add a chore and assign it to a kid; kids can check off chores; the list clearly shows what's done and what's not.

## Forbidden Assumptions
- Do not add accounts, login, points, rewards, rotation, calendar, notifications, mobile app, history, stats, or a tech stack recommendation.

## Acceptance Criteria
- Parent can add a chore and assign it to a specific kid.
- The shared page shows all chores with the assigned kid's name.
- Kids can check off a chore; checked-off chores are clearly marked as done.
- The list clearly distinguishes done vs. not-done chores.
```
