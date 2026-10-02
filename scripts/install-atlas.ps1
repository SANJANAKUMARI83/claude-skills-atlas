param(
  [string]$Target = "$HOME/.claude/skills"
)

$RepoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
New-Item -ItemType Directory -Force -Path $Target | Out-Null

if (Test-Path "$RepoRoot\skills") {
  Copy-Item "$RepoRoot\skills\*" $Target -Recurse -Force
}

Write-Host "Claude Skills Atlas skills copied to: $Target"
Write-Host "Prompts remain available in: $RepoRoot\prompts"
