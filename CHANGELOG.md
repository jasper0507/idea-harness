# Changelog

## v2.2.0 - 2026-05-16

上线打磨：补齐示例覆盖、拧紧输出守卫、强化核心原则、收紧产品边界。

### 新增

- `skills/idea-harness/EXAMPLES.md`：
  - Example 2 追加 Round 5 — 用户索取执行 Prompt 后的完整输出，首次演示 README 承诺的最终交付物。
  - 新增例3（中文记账工具）— 覆盖 `ready → gathering` 回退路径 + "你决定"类 blocked 处理，两条此前从未演示的核心状态转移。
  - 文件头更新为三条示例索引，标注各自覆盖的状态路径。
- `scripts/verify.sh` check 2/6：提取 EXAMPLES.md 及 README 的 ```markdown 代码块，扫描 VOCABULARY.md 全部禁用词（内部术语 + 流程术语 + 技术术语，共 28 项）。
- `scripts/verify.sh` check 5/6：扩展为同时校验 `Must not implement:` / `不得实现：` 段落的原因分隔符。
- `skills/idea-harness/SKILL.md` 门槛 6：写入"需求简报的不做事项是所有边界的唯一源头；执行 Prompt 不得新增"原则。
- `.gitattributes`：统一行尾为 LF，避免 Windows 上 git auto-CRLF 导致 verify.sh 的 awk 代码块匹配失效。

### 变更

- `skills/idea-harness/OUTPUTS.md`：需求简报与执行 Prompt 模板中的 `— 原因：...` 改为 `— <原因>` 占位符，消除下游 agent 照抄伪标签的风险。

### 删除

- `skills/idea-harness/OUTPUTS.md`：移除"内部 Harness Gate"模板段（22 行）。该控制结构与执行 Prompt 完全重复，且从未在示例中演示或暴露给用户。执行 Prompt 已承担其全部职责。
- `skills/idea-harness/SKILL.md`：移除"审计记录"引用（当前 skill 无审计机制，属历史残留）。
- `README.md` / `README.en.md`：移除 Hermes Agent 与 OpenClaw 的安装片段（非主流工具，给用户增加认知噪音）。保留 Claude Code、Cursor、Codex 三个真实集成路径。

---

## v2.1.0 - 2026-05-09

苏格拉底式澄清收底：精简示例、对齐输出模板与文档定位。

- GitHub Release：https://github.com/jasper0507/idea-harness/releases/tag/v2.1.0

- `skills/idea-harness/SKILL.md`：强调「约束下游 + 帮用户自己想清楚」；反对选择题轰炸式追问。
- `skills/idea-harness/OUTPUTS.md`：Need More Info 默认开放追问，选项仅在明确取舍时出现。
- `skills/idea-harness/EXAMPLES.md`：重写为两条深路径示例（中文背单词 / 英文读书会投票），覆盖 needs-precision 与 blocked。
- `README.md`、`README.en.md`：输出示例与设计原则与上述定位一致。

---

## v2.0.1 - 2026-05-09

收底：对齐文档与实际仓库状态。

- `scripts/verify.sh` 注释不再引用已删除的 `SMOKE_TESTS.md`。
- `CLAUDE.md` 修正为支撑文件数量表述（五份）。
- 中英文 README「项目结构」补充 `LICENSE`、`CHANGELOG.md`、`.github/workflows/verify.yml`。

---

## v2.0.0 - 2026-05-09

激进精简：砍掉一切不直接服务于 skill 本身的文件，对标纯 skill 仓库的极简哲学。

### 删除

- 所有 lint 配置（markdownlint、typos、lychee、pre-commit）。
- 社区治理文件（CONTRIBUTING、SECURITY、CODE_OF_CONDUCT）。
- Issue 模板、PR 模板、dependabot。
- 多余 CI 工作流（pr-title、release）。
- Windows 校验脚本（verify.ps1）。
- SMOKE_TESTS.md。
- 分支保护与 Ruleset。

### 新增

- `CLAUDE.md` — 给 AI agent 的仓库上下文说明。

### 变更

- CI 精简为单 job：只跑 `scripts/verify.sh`。
- README 项目结构段落更新。

---

## v1.0.0 - 2026-05-09

首个正式发布版本。全面工程化重构。

## v0.5.0 - 2026-05-06

状态机架构、精确度检查、决策树。

## v0.4.0 - 2026-05-06

苏格拉底式需求控制器、七个澄清门槛。
