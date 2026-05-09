# Changelog

## v1.0.0 - 2026-05-09

首个正式发布版本。全面工程化重构，在不改变功能的前提下达到开源可发布水准。

### 重构

- EXAMPLES.md 从 8 个示例精简为 5 个最具代表性的示例（删除 3 个结构雷同的例子）。
- EXAMPLES.md 所有 Ready 输出的"不做事项"修复为逐条附带原因，与 OUTPUTS.md 规则一致。
- OUTPUTS.md 合并冗余规则段落。
- SKILL.md frontmatter 描述从中英混杂整理为结构清晰的格式。
- STATE-MACHINE.md、PRECISION-GATE.md、VOCABULARY.md 精简冗余表述。
- SMOKE_TESTS.md 从 `skills/idea-harness/` 移至仓库根目录（不属于 skill 运行时文件）。
- SMOKE_TESTS.md 移除与 verify 脚本重复的静态检查命令。
- 两份 README 精简结构、统一信息量。

### 新增

- `.gitignore`。
- `.editorconfig`（UTF-8 / LF / 去尾部空白）。
- README 顶部添加 CI、License、Release 徽章。
- 快速上手覆盖 Claude Code / Cursor / Codex / Hermes Agent / OpenClaw 五个工具的一行加载命令。
- verify 脚本新增第 5 项检查：EXAMPLES.md 不做事项格式校验。

---

## v0.5.1 - 2026-05-09

- 修正 README 中的项目结构说明。
- 新增 `scripts/verify.sh` 与 `scripts/verify.ps1`。
- 新增 GitHub Actions 工作流。

## v0.5.0 - 2026-05-06

- 从规则清单升级为硬状态机（`gathering` / `needs-precision` / `blocked` / `ready`）。
- 新增精确度检查（四项检查）。
- 七个门槛从线性清单改为决策树。
- SKILL.md 从 250 行精简到 ~95 行，拆分到四个支撑文件。

## v0.4.0 - 2026-05-06

- 升级为严格苏格拉底式需求控制器。
- 引入七个固定澄清门槛。
- 新增 Harness Gate 内部控制结构。

## v0.3.0 - 2026-05-06

- 清理为 skill-only 结构。

## v0.2.0 - 2026-05-06

- 新增中英文 README。

## v0.1.0 - 2026-05-06

- 初始版本。
