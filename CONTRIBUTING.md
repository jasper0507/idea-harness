# 贡献指南

感谢你对 [Idea Harness](https://github.com/jasper0507/idea-harness) 的关注。本仓库是 **skill-only** 项目：交付物主要是 `skills/idea-harness/` 下的 Markdown 契约，加上最小的校验脚本与 CI。

## 你可以如何贡献

- **改进文档**：错别字、歧义、翻译不一致、示例过时 → 用 Issue 模板「文档改进」或直接 PR。
- **真实澄清案例**：`skills/idea-harness/EXAMPLES.md` 欢迎覆盖不同场景的最小示例 → Issue 模板「贡献真实澄清案例」或 PR。
- **工程化**：CI、链接检查、拼写、pre-commit、Release 自动化等 → PR；请保持改动可审查、可回滚。
- **行为契约讨论**：若建议会扩大职责（例如默认生成代码、替用户选技术栈），很可能不符合项目边界；请先开 Issue 讨论。

社区准则见 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。安全披露见 [SECURITY.md](SECURITY.md)。

## 本地校验

**POSIX（Linux / macOS / Git Bash）**

```bash
bash scripts/verify.sh
```

**Windows（需已安装 [ripgrep](https://github.com/BurntSushi/ripgrep)）**

```powershell
pwsh -File scripts/verify.ps1
```

可选：与 CI 对齐的 Markdown / 拼写检查（需本机安装 Node.js；拼写检查可用 [`typos`](https://github.com/crate-ci/typos) 或交给 CI）。

```bash
npx --yes markdownlint-cli2 "**/*.md"
```

## Pre-commit（可选）

安装 [pre-commit](https://pre-commit.com/) 后：

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

钩子包含：基础 hygiene、`markdownlint-cli2`、以及 [**Conventional Commits**](https://www.conventionalcommits.org/) 的 `commit-msg` 校验。

## Commit message 与 PR 标题

- **Commits**：推荐 Conventional Commits，例如 `docs: fix typo in README`、`ci: add lychee`。
- **Pull Request 标题**：CI 使用 [`action-semantic-pull-request`](https://github.com/amannn/action-semantic-pull-request) 校验，格式须为 `type: subject` 或 `type(scope): subject`，且 subject 不以大写字母开头。常用 `type`：`feat`、`fix`、`docs`、`style`、`refactor`、`perf`、`test`、`build`、`ci`、`chore`、`revert`。

## Pull Request

- 小而专注，描述「动机 + 变更范围」。
- 勾选 `.github/pull_request_template.md` 中的自检项。
- 若改动用户可见措辞，请避免暴露内部术语（见 `scripts/verify.sh` 中的泄漏检测）。

## 版本与 Release

- **CHANGELOG**：面向用户的变更写入 [CHANGELOG.md](CHANGELOG.md)，遵循现有条目风格。
- **SemVer**：`MAJOR.MINOR.PATCH`；破坏性契约变更递增 MAJOR。
- **GitHub Release**：推送形如 `v1.2.3` 的 tag 后，由 [`.github/workflows/release.yml`](.github/workflows/release.yml) 自动创建 Release 并生成 release notes（`Generate release notes`）。

```bash
git tag -a v1.1.0 -m "chore: release v1.1.0"
git push origin v1.1.0
```

如需补发 **历史 tag** 的 Release：在 GitHub 打开 **Actions** → **Release** → **Run workflow**，输入远端已存在的 tag（例如 `v1.0.0`）；也可在仓库 **Releases** 页面手动创建。

## GitHub 设置（维护者）

上游仓库 **jasper0507/idea-harness** 已开启 **Discussions**，并与 Issue 模板中的入口对应。若你维护 fork，可在 fork 的 **Settings → General → Features** 中自行开启。

**默认分支 `main`** 已启用分支保护与 Rules：`Verify` 工作流的四项检查（`smoke-static` / `markdownlint` / `typos` / `links`）、PR 标题规范检查（`conventional`），以及必须通过 Pull Request 合入（审批准许数为 0，可自行合并自己的 PR）。

## Contributing (English)

- Run `bash scripts/verify.sh` before sending a PR.
- PR titles must follow Conventional Commits (enforced in CI).
- Security reports go through GitHub Security Advisories — see [SECURITY.md](SECURITY.md).
