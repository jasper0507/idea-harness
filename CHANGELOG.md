# Changelog

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
