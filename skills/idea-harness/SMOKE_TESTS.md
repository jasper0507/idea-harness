# Idea Harness v0.4.0 冒烟测试

这些测试用于手动验证 skill 行为契约。仓库保持 skill-only，因此测试以用户输入、预期可见输出规则和静态检查命令的形式记录。

## 静态检查

实现后运行：

```powershell
rg -n "## 当前结论|Status:|Reason:|## 不能先假设|## Current Conclusion|## Forbidden Assumptions" skills\idea-harness\SKILL.md skills\idea-harness\EXAMPLES.md README.md README.en.md
```

预期：无输出。

```powershell
rg -n "## 需求简报|## Requirements Brief|## 执行 Prompt|## Execution Prompt|Harness Gate" skills\idea-harness\SKILL.md skills\idea-harness\EXAMPLES.md README.md README.en.md
```

预期：有命中，分别对应 v0.4.0 的 Ready 简报、按需执行 Prompt 和内部 Harness Gate 规则。

## Case 1：模糊想法必须保持 Need More Info

用户输入：

```text
我想做一个学习管理网站。
```

预期可见输出：

- 只展示 `## 已确认` 和 `## 下一步`。
- 不展示 `Status`、`Reason`、`仍缺`、`为什么重要`、`不能先假设` 或 `Harness Gate`。
- 问题聚焦具体学习痛点，不问技术栈。
- 给 2 到 4 个有意义选项。
- 包含一个面向最小可用第一版的推荐。

必需追问方向：

```markdown
## 下一步
“学习管理网站”还不是一个清楚的问题。你现在最想先摆脱哪种学习上的麻烦？
```

## Case 2：用户说“都要”不能进入 Ready

用户输入：

```text
这些功能都要。
```

预期可见输出：

- 继续澄清。
- 直接说明第一版不能一次接受所有功能。
- 只问第一版先做哪一个。
- 不输出需求简报。
- 不输出执行 Prompt。

## Case 3：用户说“你决定”必须要求确认

用户输入：

```text
你决定吧。
```

预期可见输出：

- 推荐一个选项。
- 说明为什么它是最小可用第一版。
- 要求用户确认推荐方案。
- 在用户确认前不能进入 Ready。

## Case 4：Ready 默认只输出需求简报

已确认事实：

- 问题 / 痛点：个人浏览器待办清单，用来避免忘记当天任务。
- 用户 / 利益相关者：只有用户自己。
- 使用背景 / 场景：工作日用电脑浏览器打开。
- 第一版主动作：添加任务并标记完成。
- 数据行为：关闭再打开同一浏览器后任务仍然存在。
- 不做事项 / 约束：不做账号、分享、提醒、分类、截止日期、手机 App、同步。
- 验收标准：能添加任务、标记完成、关闭再打开后仍看到同一列表。

预期可见输出：

- 展示 `## 需求简报`。
- 包含问题、用户、场景、第一版主动作、数据行为、不做事项和验收标准。
- 不展示 `Harness Gate`。
- 不展示 `执行 Prompt`。

## Case 5：只有明确要求时才输出执行 Prompt

用户输入：

```text
现在生成可以交给 Codex 的执行 Prompt。
```

预期可见输出：

- 先展示 `## 需求简报`。
- 再展示 `## 执行 Prompt`。
- 执行 Prompt 只包含已确认需求。
- 执行 Prompt 明确禁止未确认的登录、后端、支付、AI、统计、通知、分享、同步功能。
- 除非用户已确认技术栈，否则不选择技术栈。

## Case 6：隐藏假设必须被阻止

用户输入：

```text
我想做个记账工具，能记录每天花了多少钱。
```

预期可见输出：

- 不假设账号、云同步、数据库、图表、预算、导出或多人使用。
- 追问真实需求分叉，例如记录完后用户想拿记录做什么。

## Case 7：冲突答案只问冲突点

已知用户之前说：

```text
第一版不需要登录。
```

之后又说：

```text
每个人登录后看自己的内容。
```

预期可见输出：

- 用普通话指出冲突。
- 只问第一版到底是否需要登录和每个人看自己的内容。
- 不在同一轮问无关问题。

## Case 8：Harness Gate 控制执行 Prompt

在一个 Ready 对话中，用户明确要求生成执行 Prompt 后，人工检查输出。

预期可见输出：

- 默认需求简报先出现。
- 执行 Prompt 包含必须实现、不得实现、禁止假设、验收标准。
- 执行 Prompt 不包含未确认功能。
- 内部 Harness Gate 本身不作为审计结构展示给用户。

## 手动通过标准

v0.4.0 实现通过的条件：

- Need More Info 可见输出只包含已确认事实和下一步问题。
- Ready 可见输出默认只包含需求简报。
- 执行 Prompt 只在用户明确要求后出现。
- 七个门槛全部确认后才能 Ready。
- “都要”和“你决定”不能跳过确认。
- 用户可见案例不暴露内部 status、reason、missing gates、forbidden assumptions 或 Harness Gate。
- 默认输出不发明登录、后端、支付、AI、统计、通知、分享、同步或技术栈。
