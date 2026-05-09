#!/usr/bin/env bash
# Static checks aligned with skills/idea-harness/SMOKE_TESTS.md
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v rg >/dev/null 2>&1; then
  echo "verify.sh: ripgrep (rg) is required." >&2
  echo "Install: https://github.com/BurntSushi/ripgrep#installation" >&2
  exit 1
fi

LEAK_PATTERN='Status:|Reason:|## 不能先假设|## Current Conclusion|## Forbidden Assumptions|精确度缺口|阻断条件|Precision Gap|Blocking Condition|Harness Gate'

echo "1/4 User-visible files must not leak internal terms..."
if rg -n "${LEAK_PATTERN}" skills/idea-harness/EXAMPLES.md README.md README.en.md; then
  echo "FAIL: internal terms found in user-visible files." >&2
  exit 1
fi

echo "2/4 Required references and sections must exist..."
must_match() {
  local pattern=$1
  shift
  if ! rg -q -n "${pattern}" "$@"; then
    echo "FAIL: expected rg match for: ${pattern}" >&2
    exit 1
  fi
}

must_match "PRECISION-GATE|STATE-MACHINE|VOCABULARY|OUTPUTS" skills/idea-harness/SKILL.md
must_match "## 需求简报|## Requirements Brief|## 执行 Prompt|## Execution Prompt|Harness Gate" skills/idea-harness/OUTPUTS.md
must_match "gathering|needs-precision|blocked|ready" skills/idea-harness/STATE-MACHINE.md
must_match "目标一致性|隐藏默认值|场景走查|矛盾扫描" skills/idea-harness/PRECISION-GATE.md

echo "3/4 SKILL.md line count (<= 120)..."
lines=$(wc -l <"skills/idea-harness/SKILL.md" | tr -d ' ')
if [ "${lines}" -gt 120 ]; then
  echo "FAIL: SKILL.md has ${lines} lines (max 120)." >&2
  exit 1
fi

echo "4/4 OK (${lines} lines in SKILL.md). All static smoke checks passed."
