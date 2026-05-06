# Changelog

这个文件记录 Idea Harness 的公开版本变化。

## v0.4.0 - 2026-05-06

当前推荐版本。

- 将 Idea Harness 升级为严格的苏格拉底式需求控制器。
- 引入七个固定澄清门槛：问题 / 痛点、用户 / 利益相关者、使用背景 / 场景、第一版主动作、数据行为、不做事项 / 约束、验收标准。
- 默认 `Need More Info` 输出只展示 `已确认` 和 `下一步`。
- 默认 `Ready` 输出只展示 `需求简报`。
- 将 Harness Gate 保持为内部控制结构，防止下游 agent 添加未确认功能。
- 只有用户明确要求时，才输出可交给 Codex、Claude Code 或 Cursor 的执行 Prompt。
- 新增 `skills/idea-harness/SMOKE_TESTS.md`，记录 v0.4.0 冒烟测试清单。

## v0.3.0 - 2026-05-06

- 清理仓库为正式 skill-only 结构。
- 保留唯一 skill 入口：`skills/idea-harness/SKILL.md`。
- 将详细案例放到 `skills/idea-harness/EXAMPLES.md`。
- 删除根目录重复的 `SKILL.md` 和 `EXAMPLES.md`。
- README 入口统一为 `README.md` 中文、`README.en.md` 英文。
- 保留 MIT `LICENSE`。

## v0.2.0 - 2026-05-06

文档版本。

- 新增英文 README。
- 新增中文 README。
- 保留根目录 `SKILL.md` 和 `EXAMPLES.md`。

## v0.1.0 - 2026-05-06

初始 skill 版本。

- 新增 `SKILL.md`，定义 Idea Harness 的澄清流程、门禁和输出格式。
- 新增 `EXAMPLES.md`，提供详细的中英文澄清示例。
