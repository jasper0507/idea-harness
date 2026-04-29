# Idea Harness PRD

## 1. 产品概述

**产品名称：** Idea Harness

**一句话定位：** Idea Harness 是一个面向非程序员的轻量小应用想法澄清 Skill。它帮助想用 AI 做小网站、小工具、小应用的人，用最少的公开输出确认目标、边界和验收标准，并在信息不够时阻止 AI 过早进入开发计划或代码实现。

**目标用户：** 不会编程、不会写需求、不会写产品文档，但有一个想法并希望借助 AI 做出小网站、小工具或小应用的人。

典型输入：

```text
我想做一个学习管理网站
我想做一个记账工具
我想做一个帮我整理资料的小应用
我想做一个日记网站
```

**核心问题：** 普通 AI 虽然也会追问，但追问过程不稳定，容易在用户没有确认的情况下默认登录、数据库、数据统计、AI 功能、多用户、部署方案或复杂架构。Idea Harness 要解决的不是“把 prompt 写长”，而是“在需求阶段阻止 AI 乱猜和乱做”。

**核心承诺：** Idea Harness 不把用户的模糊想法伪装成完整需求。它在内部记录证据、拦截危险假设、判断执行门禁；对用户只暴露必要结论、已确认内容、不能假设的内容，以及一个下一步问题或最终执行 Prompt。

## 2. 参考模型与借鉴模式

Idea Harness 可以借鉴成熟项目和方法，但必须保留自己的轻量定位。

- **GitHub Spec Kit：** 借鉴显式不确定标记，如 `[NEEDS CLARIFICATION]`、规格检查清单，以及“先规格、后实现”的思想。参考：https://github.com/github/spec-kit 和 https://github.com/github/spec-kit/blob/main/spec-driven.md
- **requirements-clarity skill：** 借鉴分阶段澄清、清晰度门槛、小轮次提问。不要照搬它偏 PRD、偏程序员的重流程。参考：https://playbooks.com/skills/davila7/claude-code-templates/requirements-clarity
- **ask-questions-if-underspecified：** 借鉴“只问避免做错所必需的问题”，避免一次性抛出大量问题。参考：https://skills.sh/skillcreatorai/ai-agent-skills/ask-questions-if-underspecified
- **prompt-optimizer / EARS：** 借鉴可测试需求句式，例如 “When X, the system shall Y”，用于生成验收标准。参考：https://skills.sh/daymade/claude-code-skills/prompt-optimizer
- **OpenAI Harness Engineering：** 借鉴工程化视角，让 agent 工作过程可读、可版本化、可约束、可验证。参考：https://openai.com/index/harness-engineering/
- **Anthropic long-running agent harnesses：** 借鉴长期任务中用持久产物、状态和反馈循环减少 agent 猜测的思想。参考：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Jobs To Be Done：** 借鉴“先找用户真正想完成的事”，而不是一上来堆功能。
- **5 Whys：** 借鉴轻量根因追问，但最多问 1 到 2 次“为什么”，避免让非程序员有被审问的感觉。
- **MoSCoW：** 借鉴 Must / Should / Could / Won't，用于划分 MVP 边界。
- **Kano 模型：** 借鉴“基础需求、性能需求、惊喜需求”的区分，防止炫技功能默认进入第一版。
- **INVEST 与 Definition of Ready：** 借鉴“需求是否足够小、足够有价值、足够可测试”的判断方式，用于决定是否能进入 AI 执行阶段。
- **Gherkin / Given-When-Then：** 借鉴简单验收测试表达，让非技术用户也能理解完成标准。
- **影响-成本思路：** 借鉴“优先处理高影响、低负担问题”，用于选择下一轮最值得问的问题，但不引入量化计算。

### 2.1 轻量算法栈

Idea Harness 不应在每次输入时运行所有成熟框架。那会让 Skill 变慢、变重、变难用。V1 使用一套轻量分阶段算法栈：

| 阶段 | 借鉴算法 | 目的 | 轻量化用法 |
|---|---|---|---|
| 理解问题 | Jobs To Be Done + 5 Whys | 找到模糊想法背后的真实任务 | 问“你希望它帮你省掉哪件麻烦事？”最多再追问一次为什么 |
| 发现缺口 | Spec Kit 式澄清标记 + Evidence Ledger | 防止隐藏歧义 | 缺失字段标为 `[NEEDS CLARIFICATION]` |
| 判断能否执行 | Definition of Ready + INVEST | 给 AI 执行阶段设置门槛 | 必须确认目标、用户、流程、MVP、非目标、数据行为、验收标准 |
| 控制范围 | MoSCoW + Kano | 保持第一版足够小 | Should / Could / Delighter 默认不进入 Must-have |
| 选择下一问 | 高影响问题选择规则 | 减少用户负担 | 只问最能防止 AI 跑偏、且用户容易回答的问题 |
| 生成验收 | EARS + Gherkin | 把需求转成可检查结果 | 生成 When / If / Given-When-Then 句式 |

### 2.2 下一问选择规则

当存在多个未知项时，Idea Harness 不应全部追问，也不应使用复杂计算伪装精确。它应该按需求阶段的 Harness 目标，选择“当前最能约束 AI 行为”的那个问题。

下一问选择顺序：

```text
1. 先问不回答就会导致产品方向错误的问题
2. 再问不回答就会导致 MVP 范围失控的问题
3. 再问不回答就会导致数据行为错误的问题
4. 再问不回答就会导致验收标准不可判断的问题
5. 最后才问偏好、技术、样式、实现方式
```

判断一个问题是否值得先问，使用四个定性标准：

- 它是否能阻止 AI 做错方向。
- 它是否会改变核心功能、数据行为或 MVP 边界。
- 用户是否能用普通生活经验回答。
- 如果暂时不问它，AI 是否仍能安全停留在当前阶段。

规则：

- 在 `Blocked` 状态，只问 1 个最能解除阻塞的问题。
- 如果问题包含技术词，必须改写成日常语言。
- 优先问产品方向、使用者、核心流程，再问数据保存和限制条件。
- V1 默认不问技术栈，除非用户主动提到。

例子：

用户说“我想做一个学习管理网站”。  
此时应先问“你最想先管理什么：任务、作业、资料还是学习时间？”，而不是问“你想用 React 还是 Vue？”。前者能约束产品方向，后者只是实现细节。

## 3. 独到创新点

Idea Harness 不能被包装成另一个 Prompt 优化器、PRD 生成器，或者“会提问的 AI”。它的原创性来自三个轻量控制机制的组合：

### 3.1 Evidence Ledger，证据账本

- 每一个需求判断都必须绑定用户原话或明确回答。
- 没有用户证据的字段只能标记为 `Missing` 或 `Candidate`，不能标记为 `Confirmed`。
- 这样可以防止 AI 因为“看起来合理”就给需求打高分。

### 3.2 Assumption Firewall，假设防火墙

- 把 AI 推测和用户确认严格分开。
- 登录、数据库、多用户、付费、AI 功能、图表、部署、移动端等内容，如果用户没有确认，必须进入“禁止假设”列表。
- 这是 Idea Harness 和普通 AI 追问最大的区别之一。

### 3.3 Execution Gate，执行门禁

- Skill 使用明确状态控制允许输出什么。
- 如果存在阻塞未知项，Skill 可以问问题或生成需求草图，但不能生成最终 AI 编程 Prompt。
- 输出由需求准备度决定，而不是由 AI 的自信程度决定。

设计目标不是“让需求更长”，而是“让 AI 不能越过证据向前乱做”。

## 4. 范围

### 4.1 V1 范围内

- 面向小网站、小工具、小应用的需求澄清。
- 面向不懂编程概念的用户。
- 使用轻量 Markdown Skill 实现。
- 对用户只暴露两个公开状态：`Need More Info` 和 `Ready`。
- 内部仍支持状态判断：`Blocked`、`Draftable`、`Contract-Ready`、`Execution-Ready`。
- 支持内部证据账本、假设防火墙、执行门禁，以及公开的 `Need More Info` / `Ready` 输出。
- 提供常见非程序员想法的示例。

### 4.2 V1 范围外

- 不直接生成代码。
- 不生成大型商业系统完整 PRD。
- 不把技术栈选择当作用户必须提供的需求。
- 不在用户没要求时设计后端、数据库、安全架构。
- 不做多 agent 编排。
- 不做复杂脚本、数据库、前端 UI 或 Web 应用。
- 不保证另一个 AI 最终实现出的产品一定正确。

## 5. 用户流程

### 5.1 用户旅程

1. 用户给出一个模糊想法。
   - 例子：“我想做一个管理学习的网站。”
2. Idea Harness 抽取用户原话中的证据。
3. 生成 Evidence Ledger。
4. 找出阻塞未知项和危险假设。
5. 判断当前控制状态。
6. 根据状态，提出下一问或生成公开执行 Prompt。
7. 当内部需求达到 `Execution-Ready`，公开状态变为 `Ready`，生成执行 Prompt、验收标准和禁止假设项。

### 5.2 语气要求

- 使用普通语言。
- 避免技术术语，除非同时解释。
- 提问必须是非程序员能回答的问题。
- 当用户卡住时，优先给具体选项。

表达转换示例：

- 不问：“是否需要持久化存储？”
- 改问：“关闭页面后，下次打开时这些内容还需要保留吗？”

## 6. 核心系统设计

### 6.1 Skill 文件结构

V1 保持轻量：

```text
idea-harness/
  SKILL.md
  agents/
    openai.yaml
  references/
    control-status-rubric.md
    evidence-ledger-template.md
    output-templates.md
    examples.md
```

工程化版本加入：

```text
idea-harness/
  scripts/
    validate_output.py
  tests/
    idea-harness/
      test_validate_output.py
      fixtures/
```

Markdown Skill 仍保持轻量；可执行脚本只校验输出结构和门禁规则，不接管语义判断。

架构边界：

- `skills/idea-harness/` 是运行时 Skill，可被插件加载。
- `scripts/validate_output.py` 是仓库级 QA harness，不是 Skill 运行时依赖。
- `tests/idea-harness/fixtures/` 是 golden / negative examples，用于验证门禁规则。

### 6.2 SKILL.md 职责

`SKILL.md` 只放核心工作流：

- 判断用户是否在描述小网站、小工具或小应用。
- 抽取用户提供的证据。
- 填写 Evidence Ledger。
- 标记 `Missing`、`Candidate`、`Confirmed`、`Conflict`。
- 生成 Assumption Firewall。
- 判断当前控制状态。
- 提出下一问或输出当前状态允许的产物。
- 存在阻塞未知项时，绝不生成最终执行 Prompt。

详细门禁规则和模板放到 `references/`，让 `SKILL.md` 保持短小。

## 7. 需求准备度模型

### 7.0 算法护栏

需求准备度模型要足够确定，以减少幻觉。AI 可以推理，但不能偷偷发明“准备好了”的结论。每次状态转换必须满足以下规则：

- **证据优先：** 一个字段只有在有用户证据时才能变成 `Confirmed`。
- **默认缺失：** 没有证据时标记为 `Missing`，不能写“可能是”然后当成已确认。
- **候选隔离：** AI 猜测可以写成 `Candidate`，但 Candidate 不能解锁 `Execution-Ready`。
- **阻塞优先：** 只要存在高影响阻塞项，就不能进入执行阶段。
- **非技术优先：** 面向用户的问题优先澄清意图和行为，不先问实现技术。

V1 把算法当作护栏，而不是复杂数学模型。目标是稳定行为，不是学术精度。

### 7.1 证据状态

每个需求字段必须使用四种状态之一：

- `Confirmed`：用户明确说过。
- `Candidate`：AI 推测它可能成立，但用户没有确认。
- `Missing`：没有证据。
- `Conflict`：用户表达之间存在冲突，或方向不兼容。

只有 `Confirmed` 字段可以作为最终执行 Prompt 中的硬需求。

### 7.2 Evidence Ledger 字段

V1 的 Evidence Ledger 评估以下字段：

| 字段 | 含义 |
|---|---|
| Goal | 这个工具、网站或应用解决什么问题 |
| Primary user | 谁会使用它 |
| Usage scenario | 用户什么时候、为什么使用 |
| Core workflow | 从开始到结束的主要操作流程 |
| MVP must-haves | 第一版必须包含什么 |
| Explicit non-goals | 第一版明确不做什么 |
| Data persistence | 关闭后内容是否需要保存 |
| Input/output | 用户输入什么，得到什么 |
| Acceptance criteria | 用户如何判断它做成了 |

命名约定：Evidence Ledger 内部使用 `Explicit non-goals` 作为门禁字段名；公开输出把同一概念渲染为更面向用户的 `第一版不做`。

技术栈不是 V1 必填字段，因为目标用户是非程序员。

### 7.3 阻塞未知项

阻塞未知项是会导致 AI 无法安全执行的缺失或冲突字段。

V1 中，以下字段缺失或冲突时，禁止生成最终执行 Prompt：

- Goal
- Primary user
- Core workflow
- MVP must-haves
- Explicit non-goals
- Data persistence，当产品涉及用户输入内容记录时
- Acceptance criteria

### 7.4 控制状态

Idea Harness 内部使用四状态门禁，而不是 AI 自信程度；对用户只映射为 `Need More Info` 或 `Ready`。

| 内部状态 | 含义 | 公开状态 |
|---|---|---|
| `Blocked` | 想法太模糊，或存在高风险缺失项 | `Need More Info` |
| `Draftable` | 基本方向存在，但执行仍会要求 AI 猜测 | `Need More Info` |
| `Contract-Ready` | 可以生成需求契约草案，但最终执行前仍需确认 | `Need More Info` |
| `Execution-Ready` | 无阻塞未知项 | `Ready` |

### 7.4.1 状态转换规则

使用以下规则保证状态转换可预测：

```text
如果 Goal 不是 Confirmed -> Blocked
否则如果 Primary user 不是 Confirmed -> Blocked
否则如果 Core workflow 不是 Confirmed -> 最多 Draftable
否则如果 MVP must-haves 或 Explicit non-goals 不是 Confirmed -> 最多 Draftable
否则如果 data persistence 相关且不是 Confirmed -> 最多 Contract-Ready
否则如果 Acceptance criteria 不是 Confirmed -> 最多 Contract-Ready
否则 -> Execution-Ready
```

状态由阻塞项决定，不由 AI 自信程度决定。

例子：

- 一个细节很多但没有明确“第一版不做什么”的需求，不能是 `Execution-Ready`，因为 AI 仍可能过度设计。
- 一个很简单但目标、用户、流程、MVP、非目标、数据行为、验收标准都清楚的需求，可以是 `Execution-Ready`，即使没有技术细节。

### 7.5 执行门禁清单

Idea Harness 不做清晰度量化评估。是否允许进入下一阶段，只看门禁清单。

进入 `Execution-Ready` 前必须满足：

| 门禁项 | 要求 |
|---|---|
| 目标门禁 | 用户明确说明这个工具要解决什么问题 |
| 用户门禁 | 用户明确说明主要使用者是谁 |
| 流程门禁 | 已有一个从开始到结束的核心使用流程 |
| MVP 门禁 | 已明确第一版必须做什么 |
| 非目标门禁 | 已明确第一版不做什么 |
| 数据门禁 | 如果涉及用户输入内容，已确认是否需要保存 |
| 验收门禁 | 已有可观察、可判断的完成标准 |

规则：

- 任一门禁项不是 `Confirmed`，不能进入 `Execution-Ready`。
- AI 推测的 Candidate 不能通过门禁。
- 用户未确认的功能不能进入最终执行 Prompt。
- 技术栈不是 V1 门禁项，除非用户主动提出技术约束。

### 7.6 字段对应算法

| Evidence 字段 | 主要借鉴算法 | 原因 |
|---|---|---|
| Goal | Jobs To Be Done | 找出想法背后的真实任务 |
| Primary user | 用户故事 / Persona | 防止为想象中的用户开发 |
| Usage scenario | Given-When-Then | 让使用情境可观察 |
| Core workflow | User Story Mapping | 形成端到端主流程 |
| MVP must-haves | MoSCoW | 区分必须功能和可选功能 |
| Explicit non-goals | Kano + MoSCoW Won't-have | 把惊喜功能挡在 V1 外 |
| Data persistence | 风险驱动澄清 | 防止默认数据库假设 |
| Input/output | EARS | 把自然语言转成具体行为 |
| Acceptance criteria | EARS + Gherkin | 让完成标准可测试 |

这些框架主要作为内部判断，不需要在用户输出中频繁解释。

## 8. 输出规格

### 8.0 内部处理顺序

每轮对话中，Idea Harness 按以下顺序处理：

```text
1. 抽取用户原话证据。
2. 填写 Evidence Ledger。
3. 用 `[NEEDS CLARIFICATION]` 标记阻塞项。
4. 生成 Assumption Firewall。
5. 按下一问选择规则确定最关键问题。
6. 按状态转换规则确定当前状态。
7. 把内部状态映射为公开状态，只输出轻量公开内容。
```

顺序很重要。Skill 不能先写最终 Prompt，再回头补证据。

### 8.1 标准输出模板

公开输出只使用两个状态：`Need More Info` 和 `Ready`。

非 Ready 状态统一使用：

```markdown
## 当前结论
Status: Need More Info
Reason: ...

## 已确认
- ...

## 不能先假设
- ...

## 下一步
...
```

`Need More Info` 必须停在澄清阶段，不输出 `执行 Prompt`。它只问一个下一步问题。

Ready 状态使用：

```markdown
## 当前结论
Status: Ready
Reason: 目标、使用者、流程、第一版范围、不做内容、数据行为和验收标准都已确认。

## 已确认
- 目标：...
- 使用者：...
- 核心流程：...
- 第一版必须有：...
- 第一版不做：...
- 数据保存：...
- 验收标准：...

## 不能先假设
- ...

## 执行 Prompt
你将基于以下已确认需求实现一个小网站/小工具/小应用。只实现用户确认过的内容，不要加入“不能先假设”中的功能。

已确认需求：
- 目标：...
- 使用者：...
- 核心流程：...
- 第一版必须有：...
- 第一版不做：...
- 数据保存：...

验收标准：
- 当 ... 时，系统应该 ...

禁止假设：
- ...
```

内部的 `Evidence Ledger`、`Blocking Unknowns`、`Assumption Firewall`、`Requirement Contract` 和四状态门禁只用于判断与测试，不默认展示给普通用户。

### 8.2 提问规则

- `Need More Info` 状态只问 1 个问题。
- `Ready` 状态不继续提问，除非用户改变范围。
- 面向非技术用户时，优先使用选择题。
- 每个问题必须降低阻塞未知项或高风险假设。
- 问题应按下一问选择规则提出，而不是按模板顺序机械提出。
- 如果两个问题同样关键，先问用户更容易回答的问题。

### 8.3 验收标准规则

验收标准必须是行为化、可观察、可测试的。

允许句式：

- `当 [用户行为] 时，系统应该 [可观察结果]。`
- `如果 [条件]，系统应该 [处理方式]。`
- `第一版不应包含 [明确非目标]。`

避免模糊标准：

- “界面要好看。”
- “工具要智能。”
- “应用要完整。”

### 8.4 MVP 范围规则

内部使用 MoSCoW 和 Kano：

- `Must`：第一版有用所必需。
- `Should`：很有用，但不影响第一版先跑起来。
- `Could`：可以以后做。
- `Won't`：第一版明确不做。
- `Delighter`：听起来很酷，但除非用户明确确认，否则不进入 V1。

默认规则：用户没有明确确认为 `Must` 的功能，不放进 V1 must-haves。

## 9. 示例行为

### 输入

```text
我想做一个管理学习的网站。
```

### V1 预期输出形态

```markdown
## 当前结论
Status: Need More Info
Reason: “管理学习”还太宽，最容易跑偏的是先管理哪类学习内容。

## 已确认
- 用户想做一个“管理学习的网站”。

## 不能先假设
- 不能假设它是任务管理器、课程表、背单词工具、资料库、打卡工具、登录产品、数据库产品或图表看板。

## 下一步
你最想先管理哪一类学习内容？
A. 每天要做的学习任务
B. 作业和截止日期
C. 学习笔记或资料
D. 学习时间和打卡
```

## 10. 工程计划

### 阶段 1：Markdown Skill MVP

交付：

- `SKILL.md`
- `agents/openai.yaml`
- `references/control-status-rubric.md`
- `references/evidence-ledger-template.md`
- `references/output-templates.md`
- `references/examples.md`

验证：

- 至少测试 5 个模糊输入。
- 确认存在阻塞未知项时，Skill 不输出最终执行 Prompt。
- 确认每个 `Confirmed` 字段都有用户证据。
- 确认 `不能先假设` 覆盖常见危险假设。

### 阶段 2：轻量输出校验脚本

当 Skill 开始承担 harness 门禁职责后，必须加入可执行校验，避免输出规则只停留在人工 review。

交付：

- `scripts/validate_output.py`
- `tests/idea-harness/test_validate_output.py`
- `tests/idea-harness/fixtures/*.md`

脚本职责：

- 检查轻量公开标题是否存在：`当前结论`、`已确认`、`不能先假设`。
- 检查 `Need More Info` 状态下是否错误输出了 `执行 Prompt`。
- 检查 `Need More Info` 状态是否只问 1 个下一步问题。
- 检查 `Ready` 状态下是否缺少 `执行 Prompt`。
- 检查 `Ready` 状态下是否缺少目标、使用者、核心流程、第一版必须有、第一版不做、数据保存和验收标准。
- 检查 `Ready` 输出中是否仍包含 `[NEEDS CLARIFICATION]`、`待确认` 或 `未确认`。
- 检查 `Ready` 的 `执行 Prompt` 是否包含验收标准和禁止假设。
- 支持 `--output` 单文件校验。
- 支持 `--fixtures-dir` 批量校验 `valid-*.md` 和 `invalid-*.md`。
- 支持 `--json` 输出机器可读报告，包含 `mode`、`summary` 和 `results`。
- 空 fixtures 目录必须失败。
- fixtures 批量模式下，Markdown 文件必须使用 `valid-*.md` 或 `invalid-*.md` 命名，否则必须失败。
- `--json` 在参数解析成功后输出机器可读报告；`argparse` 自身的命令用法错误仍按 Python 默认方式输出到 stderr。
- 验证器只做结构和门禁校验，不判断自然语言语义是否完全正确；自由文本中的隐性需求泄漏仍需要人工 review。

当前不加入开源发布材料：不新增 `LICENSE`、`CONTRIBUTING.md`、GitHub Actions、issue templates、release notes 或 security policy，`.codex-plugin/plugin.json` 保持 `UNLICENSED`。

### 阶段 3：示例与比赛材料

交付：

- 3 组前后对比示例对话。
- 1 张展示 `Need More Info` 轻量澄清状态的截图。
- 1 张展示 `不能先假设` 如何拦截危险扩展的截图。
- 1 张展示 `Ready` 状态下 `执行 Prompt` 的截图。
- 一段强调“需求阶段 AI 控制面”的作品简介。

## 11. 成功指标

V1 成功标准：

- 模糊想法不会立刻产出最终编码 Prompt。
- 相比普通 AI 闲聊，Skill 问的问题更少但更关键。
- 已确认需求必须引用用户证据。
- 未确认猜测不能进入 `已确认` 或 `执行 Prompt`。
- 只有阻塞未知项解决后，才输出最终执行 Prompt。
- 普通用户默认不需要阅读 Evidence Ledger、门禁表或内部状态。
- 非程序员能看懂每个问题，不需要技术背景。

## 12. 风险与缓解

| 风险 | 缓解 |
|---|---|
| AI 编造证据 | 内部要求引用用户原话；没有证据就标记 Missing |
| AI 试图绕过门禁 | 阻塞未知项未解决时，禁止输出 `执行 Prompt` |
| Skill 变得太重 | 公开输出只保留当前结论、已确认、不能先假设、下一步或执行 Prompt |
| 用户被问题压垮 | `Need More Info` 状态只问 1 个问题 |
| 看起来像普通 PRD 工具 | 强调轻量澄清和执行门禁，不默认展示内部审计结构 |
| 验收标准变虚 | 使用 EARS / Gherkin 行为模板 |

## 13. 产品叙事

普通 AI 帮用户扩展想法。Idea Harness 帮用户控制想法。

这个产品的核心洞察是：非程序员不需要一个更重的 PRD 生成器，而需要一个轻量、安全的需求入口，让 AI 在没有证据时不能偷偷填空。Idea Harness 在内部把用户的话变成证据、把缺失信息变成阻塞项、把 AI 的猜测挡在假设防火墙之外；对用户则只展示必要结论和下一步。

因此，Idea Harness 应被描述为：

**需求阶段的 AI 控制面，而不是 Prompt 优化器。**

## 14. 与 Superpowers 的区分与协作关系

Superpowers 是一套面向 AI 编程代理的完整软件开发方法论，覆盖从头脑风暴、设计文档、实施计划、TDD、调试、验证到分支收尾的开发流程。Idea Harness 不试图替代 Superpowers，而是补上它前面更窄、更早、更面向非程序员的一层：需求入口控制。

一句话区分：

**Superpowers 解决的是“如何让 AI 更可靠地开发”，Idea Harness 解决的是“开发前如何不让 AI 拿错需求”。**

| 维度 | Superpowers | Idea Harness |
|---|---|---|
| 核心定位 | 软件开发工作流方法论 | 需求阶段 Harness / AI 输入控制面 |
| 使用时机 | 已准备进入设计、计划或实现阶段 | 用户只有模糊想法，尚不能安全进入设计或开发 |
| 目标用户 | 会和 AI 协作开发的工程用户或高阶使用者 | 不懂编程、不懂 PRD、只会描述想法的普通用户 |
| 主要产物 | 设计文档、实施计划、测试与代码执行流程 | 当前结论、已确认内容、不能先假设、下一步问题或执行 Prompt |
| 风险控制点 | 防止 AI 乱写代码、跳过测试、实现失控 | 防止 AI 在需求阶段偷偷补全、过早规划、错误假设 |
| 问题风格 | 面向功能、架构、实现、测试的设计澄清 | 面向目标、使用者、场景、MVP 边界、数据行为的生活化澄清 |
| 成功标准 | 开发过程可执行、可测试、可验证 | 需求输入有证据、有边界、无阻塞未知项 |

用户不直接使用 Superpowers 的理由：

- 当用户连“自己到底要做什么”都没有说清时，Superpowers 的设计和计划能力会过早介入。
- Superpowers 会追求形成设计文档和实施计划，而 Idea Harness 会先判断 AI 是否有资格继续往下生成。
- 非程序员不需要一开始就面对架构、文件、测试、分支、实现计划；他们需要先把目标、边界和验收说清。
- Idea Harness 在内部把 AI 的猜测隔离为 `Candidate`，并阻止这些猜测进入公开的 `执行 Prompt`。
- Idea Harness 的最终产物可以交给 Superpowers、Codex、Claude Code 或其他 AI 编程工具继续执行，因此它是前置入口，而不是后续开发框架。

推荐协作链路：

```text
模糊想法
-> Idea Harness
-> Ready 状态下的执行 Prompt
-> Superpowers brainstorming / writing-plans
-> 实施、测试、验证
```

产品叙事上应避免说“Idea Harness 比 Superpowers 更强”。更准确的说法是：

**Idea Harness 给 Superpowers 提供更干净、更受控、更少幻觉的需求输入。**

## 15. 与同类 Skills / MCP 的客观区分

Idea Harness 的竞品不只是某一个 Skill，而是几类相邻工具：

| 竞品类型 | 代表形态 | 主要能力 | 与 Idea Harness 的重合 | Idea Harness 的区别 |
|---|---|---|---|---|
| 需求清晰度 Skill | Requirements Clarity、ask-questions-if-underspecified | 发现需求不清，追问用户，阻止错误执行 | 高 | Idea Harness 不使用分数机制，不追求完整 PRD，而是用证据、假设防火墙和执行门禁控制 AI 能否继续 |
| PRD 生成器 | PRD Generator、PRD Creator MCP、MakePRD | 把想法生成标准 PRD、用户故事、技术规格 | 中高 | Idea Harness 的第一目标不是“生成一份文档”，而是判断哪些内容还不能被写进最终执行 Prompt |
| 规格驱动开发框架 | GitHub Spec Kit、Agent OS | 让规格成为开发源头，再生成计划和代码 | 中 | Idea Harness 只处理规格形成前的模糊想法入口，尤其面向非程序员和小工具场景 |
| 任务编排 / Task Master 类 | Task Master、PRD-Taskmaster | 把 PRD 拆成任务、依赖、执行计划 | 中 | Idea Harness 不拆任务、不管进度，只负责产出更可信的前置执行输入 |
| Agentic Agile 框架 | BMad Method | 多角色 agent 共同产出 PRD、架构、故事、代码 | 中 | Idea Harness 更轻，不引入团队角色、架构阶段和复杂流程；适合一个普通用户的一句话想法 |
| 专家咨询 MCP | AI Expert Workflow MCP | 调用产品、UX、架构等专家角色进行咨询和文档生成 | 中 | Idea Harness 不强调专家角色，而强调证据绑定、未知项暴露和禁止假设 |
| Prompt 工程指南 | 面向非技术用户的 Prompt 教程 | 教用户如何写更好的 Prompt | 低中 | Idea Harness 不要求用户学会 Prompt 工程，而是让 Skill 代替用户约束 AI |

客观优势：

- **更窄**：只做“小网站 / 小工具 / 小应用”的需求入口，不试图覆盖完整开发生命周期。
- **更轻**：V1 可以是 Markdown-only Skill，不依赖 MCP、数据库、CLI 或多 agent 编排。
- **更适合非程序员**：不强迫用户回答技术栈、架构、文件、测试、部署等工程问题。
- **更强调控制而非生成**：普通竞品多以“生成 PRD / 生成计划 / 生成任务”为卖点，Idea Harness 以“阻止 AI 在证据不足时继续生成”为卖点。
- **更抗幻觉**：通过 Evidence Ledger 区分 `Confirmed`、`Candidate`、`Missing`、`Conflict`，避免 AI 把合理猜测伪装成用户需求。
- **更适合比赛叙事**：可以展示龙虾如何从一句模糊想法中识别未知项、拦截危险假设、只问关键问题，并最终生成受控执行 Prompt。

客观劣势：

- 不如成熟 PRD 工具完整，缺少行业模板、指标框架、版本管理和导出能力。
- 不如 MCP 插件自动化强，不能直接连接外部系统、任务管理器或文档平台。
- 不如 BMad / Superpowers 这类框架覆盖完整，不能负责后续开发、测试、验收和分支流。
- 如果用户已经有清晰 PRD 或已经是开发者，Idea Harness 的价值会下降。
- 如果 Skill 只停留在“会追问”，区分度不够；必须把门禁、证据账本、假设防火墙做成稳定输出。

因此，Idea Harness 的可选理由不是“它生成的 PRD 最完整”，而是：

**当用户只有模糊想法且不懂技术时，它是一个轻量的需求入口控制器，先防止 AI 乱猜，再允许 AI 生成。**

不适合选择 Idea Harness 的情况：

- 用户已经有完整 PRD。
- 用户需要完整敏捷开发框架。
- 用户需要自动拆任务、管理依赖或执行代码。
- 用户需要多角色专家协作。
- 用户需要企业级架构、安全、合规和交付流程。

适合选择 Idea Harness 的情况：

- 用户只有一句模糊想法。
- 用户不知道如何写需求。
- 用户担心 AI 自作主张扩展功能。
- 用户想先做一个很小的 V1。
- 用户希望把最终 Prompt 交给其他 AI 编程工具执行。
