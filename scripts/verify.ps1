# Static checks aligned with skills/idea-harness/SMOKE_TESTS.md
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if (-not (Get-Command rg -ErrorAction SilentlyContinue)) {
    Write-Error "verify.ps1: ripgrep (rg) is required. Install: https://github.com/BurntSushi/ripgrep#installation"
}

$leakPattern = "Status:|Reason:|## 不能先假设|## Current Conclusion|## Forbidden Assumptions|精确度缺口|阻断条件|Precision Gap|Blocking Condition|Harness Gate"
Write-Host "1/4 User-visible files must not leak internal terms..."
$leak = rg -n $leakPattern "skills/idea-harness/EXAMPLES.md", "README.md", "README.en.md" 2>$null
if ($leak) {
    $leak
    throw "FAIL: internal terms found in user-visible files."
}

function Assert-Match([string]$Pattern, [string[]]$Paths) {
    foreach ($p in $Paths) {
        $m = rg -n $Pattern $p 2>$null
        if (-not $m) { throw "FAIL: expected rg match for '$Pattern' in $p" }
    }
}

Write-Host "2/4 Required references and sections must exist..."
Assert-Match "PRECISION-GATE|STATE-MACHINE|VOCABULARY|OUTPUTS" @("skills/idea-harness/SKILL.md")
Assert-Match "## 需求简报|## Requirements Brief|## 执行 Prompt|## Execution Prompt|Harness Gate" @("skills/idea-harness/OUTPUTS.md")
Assert-Match "gathering|needs-precision|blocked|ready" @("skills/idea-harness/STATE-MACHINE.md")
Assert-Match "目标一致性|隐藏默认值|场景走查|矛盾扫描" @("skills/idea-harness/PRECISION-GATE.md")

Write-Host "3/4 SKILL.md line count (<= 120)..."
$lines = (Get-Content "skills/idea-harness/SKILL.md" | Measure-Object -Line).Lines
if ($lines -gt 120) { throw "FAIL: SKILL.md has $lines lines (max 120)." }

Write-Host "4/4 OK ($lines lines in SKILL.md). All static smoke checks passed."
