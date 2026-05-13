# Restore MCP Configuration
# This script securely copies the repository's MCP config to the global agent directory.
# The config in git contains NO secrets. Secrets are loaded from Windows Environment Variables.
#
# ============================================================
# ONBOARDING: Required Environment Variables
# ============================================================
# Before running this script, ensure the following Windows User
# environment variables are set. These are SHARED service account
# credentials — every team member uses the same values.
#
# Run the following two commands in PowerShell (no admin required):
#
#   [System.Environment]::SetEnvironmentVariable("CLICKUP_API_TOKEN", "<obtain from team password manager>", "User")
#   [System.Environment]::SetEnvironmentVariable("CLICKUP_TEAM_ID", "<obtain from team password manager>", "User")
#
# CLICKUP_API_TOKEN : API token for the core@lineum.io ClickUp service account.
#                     Used by the MCP to authenticate against the ClickUp API.
#                     Obtain the value from the shared team password manager — NEVER hardcode it here.
# CLICKUP_TEAM_ID   : Workspace ID for the "Lineum Dynamics" ClickUp workspace.
#                     Obtain the value from the shared team password manager — NEVER hardcode it here.
#
# After setting these variables, close and reopen PowerShell,
# then run this script to restore the MCP configuration.
# Finally, restart your Gemini/Antigravity session.
# ============================================================

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

