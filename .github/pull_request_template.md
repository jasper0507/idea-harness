## 摘要

<!-- 用一两句话说明本 PR 做什么 -->

## 变更类型

<!-- PR 标题须符合 Conventional Commits，例如 docs(ci): … -->

- [ ] Skill 行为或契约（`skills/idea-harness/`）
- [ ] 文档 / 示例
- [ ] CI、脚本或工程化工具链
- [ ] 其他：<!-- 说明 -->

## 自检

- [ ] 我已本地或通过 CI 跑通校验：`bash scripts/verify.sh`（POSIX）或 `pwsh -File scripts/verify.ps1`（Windows）
- [ ] 若为 Markdown 变更：`markdownlint-cli2` / `typos` 无新增问题（或在 CI 中已通过）
- [ ] 用户可见文本未暴露内部术语（参见 `scripts/verify.sh` 中的泄漏检测）

## 关联

<!-- 关闭 issue 时填写 Closes #123 -->
