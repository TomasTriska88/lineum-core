# Restore MCP Configuration
# This script securely copies the repository's MCP config to the global agent directory.
# The config in git contains NO secrets. Secrets are loaded from Windows Environment Variables.

$appDataPath = "$env:USERPROFILE\.gemini\antigravity"
$repoConfigPath = Join-Path $PSScriptRoot "mcp_config.json"
$targetConfigPath = Join-Path $appDataPath "mcp_config.json"

Write-Host "Restoring MCP Configuration..."
Write-Host "From: $repoConfigPath"
Write-Host "To:   $targetConfigPath"
Write-Host "----------------------------------------"

if (-Not (Test-Path -Path $repoConfigPath)) {
    Write-Host "ERROR: Repository config not found at $repoConfigPath" -ForegroundColor Red
    Exit 1
}

if (-Not (Test-Path -Path $appDataPath)) {
    New-Item -ItemType Directory -Force -Path $appDataPath | Out-Null
}

Copy-Item -Path $repoConfigPath -Destination $targetConfigPath -Force

Write-Host "----------------------------------------"
Write-Host "MCP Configuration restoration complete!" -ForegroundColor Green
Write-Host "IMPORTANT: Make sure your GITHUB_PERSONAL_ACCESS_TOKEN is set in your Windows Environment Variables." -ForegroundColor Yellow
