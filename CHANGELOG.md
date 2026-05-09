# Changelog

这个文件记录 Idea Harness 的公开版本变化。

## v0.5.1 - 2026-05-09

当前推荐版本。

- 修正 `README.md` / `README.en.md` 中的项目结构说明（移除仓库中不存在的 `docs/` 路径）。
- 新增 `scripts/verify.sh` 与 `scripts/verify.ps1`，一键运行与 `SMOKE_TESTS.md` 一致的静态冒烟检查。
- 新增 GitHub Actions 工作流，在推送与拉取请求上自动执行上述检查。

## v0.5.0 - 2026-05-06

- 从规则清单升级为硬状态机：`gathering` / `needs-precision` / `blocked` / `ready` 四个显式状态，带转移规则和阻断条件。
- 新增精确度检查（Precision Gate）：拦住"表面完整但不够精确"的需求。四项检查——目标一致性、隐藏默认值、场景走查、矛盾扫描。
- 把七个门槛从线性清单改为决策树：每个回答判断打开了哪个分支、阻塞了哪个后续决策。
- 不做事项升级为范围边界：每条附带原因（为什么 V1 不做）。
- 执行 Prompt 升级为行为契约风格：描述行为而非 UI 元素。
- 新增可选任务切片输出和原型逃生口。
- 将 SKILL.md 从 250 行精简到 ~95 行，复杂逻辑拆分到四个支撑文件。
- 新增 `skills/idea-harness/STATE-MACHINE.md`，定义状态、转移规则和决策树优先级。
- 新增 `skills/idea-harness/PRECISION-GATE.md`，定义精确度四项检查和追问策略。
- 新增 `skills/idea-harness/OUTPUTS.md`，统一所有输出模板。
- 新增 `skills/idea-harness/VOCABULARY.md`，定义内部术语和用户用语规范。
- 更新 `skills/idea-harness/SMOKE_TESTS.md`，新增精确度检查、状态机、术语一致性、场景走查等测试用例。

## v0.4.0 - 2026-05-06

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
