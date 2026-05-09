# Idea Harness

[![CI](https://github.com/jasper0507/idea-harness/actions/workflows/verify.yml/badge.svg)](https://github.com/jasper0507/idea-harness/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/jasper0507/idea-harness)](https://github.com/jasper0507/idea-harness/releases)

> **大多数模糊想法死在 AI 第一轮脑补。**
> Idea Harness 专门在这一步给 AI **套上缰绳**。

把非程序员一句模糊的"小应用想法"，**澄清到 AI 可以安全执行、但绝不乱猜** 的程度。

简体中文 | [English](README.en.md)

---

## 问题

AI Coding Agent 遇到"我想做一个记账 App"这类输入时，会立刻脑补账号系统、数据库、推送通知……结果做出来一个你不想要的东西。

核心原因：**LLM 在需求不清时很容易主动补全未确认假设。**

## 解决方案

**Idea Harness 只做一件事 —— 需求澄清。**

- 只认用户明确说过或确认过的事实
- 七个澄清门槛，按决策树而非线性清单检查
- 四项精确度检查拦住"表面完整但不够精确"的需求
- 硬状态机：`gathering` → `needs-precision` → `blocked` → `ready`
- 默认每次只问一个最关键的问题
- Ready 后才输出需求简报；执行 Prompt 仅在用户明确要求时生成

---

## 快速上手

### 1. 获取 skill

```bash
git clone https://github.com/jasper0507/idea-harness.git
```

### 2. 加载到你的 AI 工具

**Claude Code**
```bash
cp -r idea-harness/skills/idea-harness ~/.claude/skills/
```

**Cursor**
```bash
cp -r idea-harness/skills/idea-harness .cursor/skills/
```

**Codex (OpenAI)**
```bash
# 在项目根目录的 AGENTS.md 中引用
echo "Read and follow skills/idea-harness/SKILL.md when clarifying app ideas." >> AGENTS.md
```

**Hermes Agent**
```bash
cp -r idea-harness/skills/idea-harness ~/.hermes/skills/
```

**OpenClaw**
```bash
cp -r idea-harness/skills/idea-harness ~/.openclaw/skills/
```

### 3. 开始对话

```text
使用 idea-harness 先澄清我的小应用想法。
我想做一个 [你的模糊想法]。
```

---

## 输出示例

**苏格拉底式追问**——不是选择题轰炸，而是帮你发现自己没想清楚的地方：

```markdown
## 已确认
- 你想做一个背单词的工具。
- 你觉得市面上的背单词 App 太复杂。

## 追问
上一次你用背单词 App 觉得"太复杂"的那个瞬间，具体是什么让你烦了？
```

当用户的回答暗含未检验的假设时，skill 会直接拆穿：

```markdown
## 追问
你说想看"哪些还记得、哪些忘了"——你是想让工具自动帮你安排今天该复习哪些词，还是自己翻着看就行？
```

七个门槛全部确认且精确度检查通过后输出需求简报。用户明确要求时才生成执行 Prompt。

---

## 设计原则

- **窄一点，比全能更有用** —— 专精于澄清阶段
- **问少一点，比问全更容易推进**
- **先定边界，再让 AI 实现**
- **澄清给机器，启发给人** —— 约束下游 agent 的同时，帮用户自己想清楚

---

## 使用场景

**推荐**：只有一句模糊想法 · 技术小白想把 idea 变成需求 · 想做极小但正确的第一版 · 害怕 AI 自作主张

**不适合**：已有清晰 PRD · 需要立即写代码 · 需要商业模式规划

---

## 项目结构

```text
skills/idea-harness/
  SKILL.md             # 核心入口
  STATE-MACHINE.md     # 状态机
  PRECISION-GATE.md    # 精确度检查
  OUTPUTS.md           # 输出模板
  VOCABULARY.md        # 用语规范
  EXAMPLES.md          # 完整对话示例
CLAUDE.md              # 给 AI agent 的仓库说明
LICENSE                # MIT
CHANGELOG.md           # 版本记录
.github/workflows/verify.yml
scripts/verify.sh      # 静态冒烟检查
```

Skill-only 项目：无运行时依赖；除 skill 与校验脚本外，仅有许可证、变更记录和最小 CI。

---

## 贡献

欢迎提交你用过的**真实模糊想法 + 澄清过程**，直接 PR 更新 `skills/idea-harness/EXAMPLES.md` 即可。

---

**许可证**: MIT　·　**作者**: jasper0507
