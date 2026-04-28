# Idea Harness

Idea Harness 是一个本地原型级 Codex 插件包，用来承载 `$idea-harness` Skill。

它面向不会编程、不会写 PRD、但想用 AI 做小网站、小工具或小应用的人。核心目标不是生成更长的文档，而是在需求阶段控制 AI：只有用户已经明确确认的内容才能进入需求契约；缺失、冲突和 AI 推测必须被显式标出来。

## 交付内容

- Evidence Ledger：把每个需求判断绑定到用户原话。
- Assumption Firewall：阻止登录、数据库、多用户、付费、AI 功能、部署等未确认假设进入 V1。
- Execution Gate：用 `Blocked`、`Draftable`、`Contract-Ready`、`Execution-Ready` 控制允许输出的内容。
- Requirement Contract：在需求足够清楚时生成可验收的需求契约。
- Final AI Execution Prompt：仅当状态为 `Execution-Ready` 时生成。

## 目录结构

```text
idea-harness/
  .codex-plugin/
    plugin.json
  docs/
    idea-harness-prd.md
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
      manual-scenarios.md
```

## V1 Boundaries

- Markdown-only Skill.
- No MCP server.
- No Web app.
- No database.
- No code generation for the user's app.
- No browser screenshot workflow in V1.
- No marketplace metadata or public release packaging.

## Validation

Run the structural checks:

```powershell
python -m json.tool .codex-plugin/plugin.json
python -X utf8 C:/Users/12694/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/idea-harness
```

Then review `tests/idea-harness/manual-scenarios.md` against the Skill behavior.
