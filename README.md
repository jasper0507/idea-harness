# Idea Harness

Idea Harness 是一个 Codex plugin skill，用来把普通人的模糊小应用想法，轻量澄清成 AI 可以安全执行的范围。

它的体验目标不是生成一份厚重 PRD，而是先回答两个问题：

- 现在信息够不够让 AI 开始做？
- 如果不够，下一步只需要问用户什么？

## 快速开始

在让 Codex 设计或写代码前，先这样调用 skill：

```text
使用 $idea-harness 先澄清我的小应用想法。
我想做一个学习管理网站。
```

像“学习管理网站”这种输入太宽泛，预期公开状态应该是 `Need More Info`。这时 skill 只输出必要内容：

```markdown
## 当前结论
Status: Need More Info
Reason: “学习管理”还太宽，最容易跑偏的是先管理哪类学习内容。

## 已确认
- 用户想做一个“学习管理网站”。

## 不能先假设
- 不能假设它是任务管理器、课程表、笔记库、登录产品、数据库产品或图表看板。

## 下一步
你最想先管理哪一类学习内容？
A. 每天要做的学习任务
B. 作业和截止日期
C. 学习笔记或资料
D. 学习时间和打卡
```

`Need More Info` 状态不输出 `执行 Prompt`。只有当目标、使用者、核心流程、第一版范围、明确不做项、数据保存行为和验收标准都被用户确认后，公开状态才可以变成 `Ready`，这时才允许输出 `执行 Prompt`。

## 当前定位

一句话：**面向非程序员的小应用想法澄清器。**

内部仍然有证据账本、假设隔离和执行门禁，但默认不把这些审计结构展示给用户。用户只看到：

- `当前结论`
- `已确认`
- `不能先假设`
- `下一步`，仅在还缺信息时出现
- `执行 Prompt`，仅在可以执行时出现

## 怎么读这个项目

如果你完全不懂代码，按这个顺序看：

```text
README.md
skills/idea-harness/SKILL.md
skills/idea-harness/references/output-templates.md
tests/idea-harness/fixtures/valid-light-need-more-info.md
tests/idea-harness/fixtures/valid-light-ready.md
```

你可以把这个项目理解成三层：

- `skills/idea-harness/` 是真正运行时会加载的 skill 本体。
- `scripts/validate_output.py` 是仓库里的 QA harness，用来检查输出是否守住轻量公开格式和执行门禁。
- `tests/idea-harness/fixtures/` 是测试样例。`valid-*.md` 应该通过验证，`invalid-*.md` 应该失败。

## 公开状态

| Status | 含义 | 能输出执行 Prompt 吗 |
|---|---|---|
| `Need More Info` | 还缺关键确认，AI 继续做会猜。 | 不能 |
| `Ready` | 所有执行门禁都有用户证据。 | 可以 |

内部仍可使用 `Blocked`、`Draftable`、`Contract-Ready`、`Execution-Ready` 做判断，但这些不默认暴露给用户。

## 验证方式

运行项目基础检查：

```powershell
python -m json.tool .codex-plugin/plugin.json
python -X utf8 C:/Users/12694/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/idea-harness
python -X utf8 -m unittest discover -s tests/idea-harness -p "test_*.py"
```

验证单个输出文件：

```powershell
python -X utf8 scripts/validate_output.py --output tests/idea-harness/fixtures/valid-light-need-more-info.md
```

批量验证所有 fixtures：

```powershell
python -X utf8 scripts/validate_output.py --fixtures-dir tests/idea-harness/fixtures
```

生成 JSON 报告：

```powershell
python -X utf8 scripts/validate_output.py --fixtures-dir tests/idea-harness/fixtures --json
```

## 当前边界

这个仓库目前仍是内部工程化原型：

- Markdown-only skill。
- 不包含 MCP server。
- 不包含 Web app。
- 不包含数据库。
- 不负责直接生成用户应用代码。
- 暂不补公开发布材料。
- `.codex-plugin/plugin.json` 保持 `UNLICENSED`。
