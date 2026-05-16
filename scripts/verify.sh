#!/usr/bin/env bash
# Static smoke checks — contract notes in repo CLAUDE.md and skills/idea-harness/SKILL.md
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v rg >/dev/null 2>&1; then
  echo "verify.sh: ripgrep (rg) is required." >&2
  echo "Install: https://github.com/BurntSushi/ripgrep#installation" >&2
  exit 1
fi

LEAK_PATTERN='Status:|Reason:|## 不能先假设|## Current Conclusion|## Forbidden Assumptions|精确度缺口|阻断条件|Precision Gap|Blocking Condition|Harness Gate'

echo "1/6 User-visible files must not leak internal terms..."
if rg -n "${LEAK_PATTERN}" skills/idea-harness/EXAMPLES.md README.md README.en.md; then
  echo "FAIL: internal terms found in user-visible files." >&2
  exit 1
fi

echo "2/6 Markdown code blocks in EXAMPLES.md and READMEs must not contain forbidden vocabulary..."
BLOCK_LEAK_PATTERN='门槛|精确度缺口|隐藏默认值|危险假设|范围边界|阻断条件|行为契约|状态机|Harness Gate|Precision Gap|Blocking Condition|Dangerous Assumption|Hidden Default|Scope Boundary|Behavior Contract|MVP|PRD|需求规格|验收测试|利益相关者|用例|user story|stakeholder|use case|CRUD|localStorage|SDK'
for f in skills/idea-harness/EXAMPLES.md README.md README.en.md; do
  block_content=$(awk '/^```markdown/{flag=1; next} /^```/{flag=0} flag' "$f")
  if [ -n "$block_content" ] && echo "$block_content" | rg -n "${BLOCK_LEAK_PATTERN}"; then
    echo "FAIL: forbidden vocabulary found inside markdown code blocks in ${f}." >&2
    exit 1
  fi
done

echo "3/6 Required references and sections must exist..."
must_match() {
  local pattern=$1
  shift
  if ! rg -q -n "${pattern}" "$@"; then
    echo "FAIL: expected rg match for: ${pattern}" >&2
    exit 1
  fi
}

must_match "PRECISION-GATE|STATE-MACHINE|VOCABULARY|OUTPUTS" skills/idea-harness/SKILL.md
must_match "## 需求简报|## Requirements Brief|## 执行 Prompt|## Execution Prompt" skills/idea-harness/OUTPUTS.md
must_match "gathering|needs-precision|blocked|ready" skills/idea-harness/STATE-MACHINE.md
must_match "目标一致性|隐藏默认值|场景走查|矛盾扫描" skills/idea-harness/PRECISION-GATE.md

echo "4/6 SKILL.md line count (<= 120)..."
lines=$(wc -l <"skills/idea-harness/SKILL.md" | tr -d ' ')
if [ "${lines}" -gt 120 ]; then
  echo "FAIL: SKILL.md has ${lines} lines (max 120)." >&2
  exit 1
fi

echo "5/6 Non-goals in EXAMPLES.md must include reasons (— separator)..."
in_nongoals=0
fail=0
while IFS= read -r line; do
  if echo "$line" | rg -q '不做事项：|Non-goals:|不得实现：|Must not implement:'; then
    in_nongoals=1
    continue
  fi
  if [ "$in_nongoals" = "1" ]; then
    if echo "$line" | rg -q '^- '; then
      if ! echo "$line" | rg -q ' — '; then
        echo "FAIL: non-goal line missing reason: $line" >&2
        fail=1
      fi
    else
      in_nongoals=0
    fi
  fi
done < skills/idea-harness/EXAMPLES.md
if [ "$fail" = "1" ]; then
  exit 1
fi

echo "6/6 OK (${lines} lines in SKILL.md). All static smoke checks passed."
