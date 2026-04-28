# Idea Harness

Idea Harness 是一个 Codex plugin skill，用来在需求还没说清楚时阻止 AI 过早脑补、规划或生成执行 prompt。

它适合这样的场景：你只有一个模糊的小网站、小工具或小应用想法，但还没有把目标、使用者、核心流程、第一版范围、不要做什么、数据行为和验收标准说清楚。Idea Harness 会先把“用户明确说过的内容”和“AI 推测的内容”分开，只允许有证据的需求进入最终执行。

## 快速开始

在让 Codex 设计或写代码前，先这样调用 skill：

```text
使用 $idea-harness 先澄清我的小应用想法。
我想做一个学习管理网站。
```

像“学习管理网站”这种输入太宽泛，预期状态应该是 `Blocked`。这时 skill 应该列出已知信息、缺失信息、AI 不能假设的内容，并且只问一个最关键的下一步问题。

`Blocked` 状态不应该输出：

- `Requirement Contract`
- `Final AI Execution Prompt`

只有当目标、使用者、核心流程、MVP 必做项、明确不做项、数据保存行为和验收标准都被用户确认后，状态才可以变成 `Execution-Ready`，这时才允许输出 `Final AI Execution Prompt`。

## 怎么读这个项目

如果你完全不懂代码，按这个顺序看：

```text
README.md
skills/idea-harness/SKILL.md
skills/idea-harness/references/output-templates.md
tests/idea-harness/fixtures/valid-blocked.md
tests/idea-harness/fixtures/invalid-blocked-final-prompt.md
```

你可以把这个项目理解成三层：

- `skills/idea-harness/` 是真正运行时会加载的 skill 本体。Codex 主要从 `SKILL.md` 开始读规则。
- `scripts/validate_output.py` 是仓库里的 QA harness，用来检查 skill 产出的 Markdown 是否守住门禁；它不是 skill 运行时依赖。
- `tests/idea-harness/fixtures/` 是测试样例。`valid-*.md` 应该通过验证，`invalid-*.md` 应该失败。

## 目录结构

```text
idea-harness/
  .codex-plugin/
    plugin.json
  docs/
    idea-harness-prd.md
  scripts/
    validate_output.py
  skills/
    idea-harness/
      SKILL.md
      agents/
        openai.yaml
      references/
        control-status-rubric.md
        evidence-ledger-template.md
        output-templates.md
        examples.md
  tests/
    idea-harness/
      test_validate_output.py
      fixtures/
      manual-scenarios.md
```

## 四种输出状态

| State | 含义 | 能输出最终执行 prompt 吗 |
|---|---|---|
| `Blocked` | 想法太模糊，或者高风险门禁缺失。 | 不能 |
| `Draftable` | 基本方向有了，但执行仍需要 AI 猜。 | 不能 |
| `Contract-Ready` | 可以形成需求契约草案，但仍有内容要确认。 | 不能 |
| `Execution-Ready` | 所有执行门禁都有用户证据并且是 `Confirmed`。 | 可以 |

核心规则只有一句：只有 `Confirmed` 的用户证据可以变成硬需求。`Candidate`、`Missing`、`Conflict` 都不能解锁 `Execution-Ready`。

## 一个例子

输入：

```text
我想做一个学习管理网站。
```

为什么它应该是 `Blocked`：

- “学习管理”范围太大，可能是任务、笔记、课程、时间记录或别的东西。
- 主要使用者没有确认。
- 核心流程、MVP 必做项、明确不做项和验收标准都缺失。
- AI 不能擅自假设登录、数据库、图表、AI 功能、手机 App、部署方式或具体产品形态。

预期输出：

- 输出 `Idea Control Status`、`Evidence Ledger`、`Blocking Unknowns`、`Assumption Firewall` 和一个 `Next Best Question`。
- 不输出 `Requirement Contract`。
- 不输出 `Final AI Execution Prompt`。

## 验证方式

运行项目基础检查：

```powershell
python -m json.tool .codex-plugin/plugin.json
python -X utf8 C:/Users/12694/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/idea-harness
python -X utf8 -m unittest discover -s tests/idea-harness -p "test_*.py"
```

验证单个输出文件：

```powershell
python -X utf8 scripts/validate_output.py --output tests/idea-harness/fixtures/valid-blocked.md
```

批量验证所有 fixtures：

```powershell
python -X utf8 scripts/validate_output.py --fixtures-dir tests/idea-harness/fixtures
```

生成 JSON 报告：

```powershell
python -X utf8 scripts/validate_output.py --fixtures-dir tests/idea-harness/fixtures --json
```

批量模式会递归读取 `*.md`。空目录会失败；Markdown fixture 必须命名为 `valid-*.md` 或 `invalid-*.md`，否则也会失败。

退出码：

- `0`：验证结果符合预期。
- `1`：输出违反规则，或 fixture 的 `valid-*` / `invalid-*` 预期不匹配。
- `2`：命令参数、路径或文件读取错误。

`--json` 会在参数解析成功后输出机器可读报告；如果连参数本身都不合法，`argparse` 仍会按 Python 默认方式在 stderr 输出用法错误。

验证器只做结构和门禁校验，不判断自然语言语义是否百分百正确。比如一段自由文本是否偷偷表达了未确认需求，仍然需要人工 review。

## 当前边界

这个仓库目前仍是内部工程化原型：

- Markdown-only skill。
- 不包含 MCP server。
- 不包含 Web app。
- 不包含数据库。
- 不负责直接生成用户应用代码。
- 暂不补公开发布材料。
- `.codex-plugin/plugin.json` 保持 `UNLICENSED`。
