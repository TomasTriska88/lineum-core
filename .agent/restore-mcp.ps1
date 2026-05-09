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

$clickupToken = [System.Environment]::GetEnvironmentVariable("CLICKUP_API_TOKEN", "User")
if ($clickupToken) {
    [System.Environment]::SetEnvironmentVariable("CLICKUP_API_KEY", $clickupToken, "User")
    Write-Host "CLICKUP_API_KEY environment variable synced successfully" -ForegroundColor Green
} else {
    Write-Host "WARNING: CLICKUP_API_TOKEN not set. ClickUp MCP will not authenticate." -ForegroundColor Yellow
}

$clickupTeamId = [System.Environment]::GetEnvironmentVariable("CLICKUP_TEAM_ID", "User")
if (-not $clickupTeamId) {
    Write-Host "WARNING: CLICKUP_TEAM_ID not set. ClickUp MCP will fail workspace lookups." -ForegroundColor Yellow
}

$configContent = [System.IO.File]::ReadAllText($repoConfigPath, [System.Text.Encoding]::UTF8)
$scriptPath = Join-Path $PSScriptRoot "mcp\lineum-clickup\index.js"
$escapedScriptPath = $scriptPath -replace '\\', '\\'
$configContent = $configContent.Replace('${SCRIPT_PATH}', $escapedScriptPath)
$utf8NoBom = New-Object System.Text.UTF8Encoding $False
[System.IO.File]::WriteAllText($targetConfigPath, $configContent, $utf8NoBom)

Write-Host "----------------------------------------"
Write-Host "MCP Configuration restoration complete!" -ForegroundColor Green
Write-Host "IMPORTANT: Restart your Gemini session after running this script." -ForegroundColor Yellow
Write-Host "IMPORTANT: Ensure CLICKUP_API_TOKEN is set in Windows Environment Variables." -ForegroundColor Yellow
Write-Host "IMPORTANT: Ensure CLICKUP_TEAM_ID is set in Windows Environment Variables." -ForegroundColor Yellow

