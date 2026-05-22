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
#   [System.Environment]::SetEnvironmentVariable("RAILWAY_TOKEN", "<obtain from team password manager>", "User")
#   [System.Environment]::SetEnvironmentVariable("MYINVOICE_API_TOKEN", "mi_pat_...", "User")
#   [System.Environment]::SetEnvironmentVariable("MYINVOICE_URL", "https://flux.lineum.io", "User")
#   [System.Environment]::SetEnvironmentVariable("CLOUDFLARE_API_TOKEN", "cfut_...", "User")
#   [System.Environment]::SetEnvironmentVariable("CLOUDFLARE_ACCOUNT_ID", "...", "User")
#   [System.Environment]::SetEnvironmentVariable("CLOUDFLARE_ZONE_ID", "...", "User")
#
# CLICKUP_API_TOKEN : API token for the core@lineum.io ClickUp service account.
#                     Used by the MCP to authenticate against the ClickUp API.
#                     Obtain the value from the shared team password manager — NEVER hardcode it here.
# CLICKUP_TEAM_ID   : Workspace ID for the "Lineum Dynamics" ClickUp workspace.
#                     Obtain the value from the shared team password manager — NEVER hardcode it here.
# RAILWAY_TOKEN     : API token for the Railway.app integration.
#                     Used by the official Railway MCP to manage infrastructure.
# MYINVOICE_API_TOKEN : Personal Access Token for MyInvoice with read_write scope.
# MYINVOICE_URL       : Production URL for the MyInvoice instance (e.g. https://flux.lineum.io).
# CLOUDFLARE_API_TOKEN: Cloudflare Token with Account/Zone DNS/Access edit permissions.
# CLOUDFLARE_ACCOUNT_ID: Cloudflare Account ID for Zero Trust operations.
# CLOUDFLARE_ZONE_ID  : Cloudflare Zone ID for DNS operations.
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

$railwayToken = [System.Environment]::GetEnvironmentVariable("RAILWAY_TOKEN", "User")
if ($railwayToken) {
    Write-Host "RAILWAY_TOKEN environment variable found" -ForegroundColor Green
} else {
    Write-Host "WARNING: RAILWAY_TOKEN not set. Railway MCP will not authenticate." -ForegroundColor Yellow
}

$myinvoiceToken = [System.Environment]::GetEnvironmentVariable("MYINVOICE_API_TOKEN", "User")
$myinvoiceUrl = [System.Environment]::GetEnvironmentVariable("MYINVOICE_URL", "User")
if ($myinvoiceToken -and $myinvoiceUrl) {
    Write-Host "MYINVOICE_API_TOKEN and MYINVOICE_URL environment variables found" -ForegroundColor Green
} else {
    Write-Host "WARNING: MYINVOICE_API_TOKEN or MYINVOICE_URL not set. MyInvoice MCP will not authenticate." -ForegroundColor Yellow
}

$cloudflareToken = [System.Environment]::GetEnvironmentVariable("CLOUDFLARE_API_TOKEN", "User")
if ($cloudflareToken) {
    Write-Host "CLOUDFLARE_API_TOKEN environment variable found" -ForegroundColor Green
} else {
    Write-Host "WARNING: CLOUDFLARE_API_TOKEN not set. Cloudflare MCP will not authenticate." -ForegroundColor Yellow
}

$configContent = [System.IO.File]::ReadAllText($repoConfigPath, [System.Text.Encoding]::UTF8)

# Dynamically resolve Node.exe path on Windows to avoid sandbox/PATH resolution issues
$nodePath = "node"
$nodeCmd = Get-Command node -ErrorAction SilentlyContinue
if ($nodeCmd) {
    $nodePath = $nodeCmd.Source
}
$escapedNodePath = $nodePath -replace '\\', '\\'
$configContent = $configContent.Replace('"command": "node"', "`"command`": `"$escapedNodePath`"")

$scriptPath = Join-Path $PSScriptRoot "mcp\lineum-clickup\index.js"
$escapedScriptPath = $scriptPath -replace '\\', '\\'
$configContent = $configContent.Replace('${SCRIPT_PATH}', $escapedScriptPath)

$myinvoiceScriptPath = Join-Path $PSScriptRoot "mcp\lineum-myinvoice\index.js"
$escapedMyinvoiceScriptPath = $myinvoiceScriptPath -replace '\\', '\\'
$configContent = $configContent.Replace('${MYINVOICE_SCRIPT_PATH}', $escapedMyinvoiceScriptPath)

$cloudflareScriptPath = Join-Path $PSScriptRoot "mcp\lineum-cloudflare\index.js"
$escapedCloudflareScriptPath = $cloudflareScriptPath -replace '\\', '\\'
$configContent = $configContent.Replace('${CLOUDFLARE_SCRIPT_PATH}', $escapedCloudflareScriptPath)

$railwayScriptPath = Join-Path $PSScriptRoot "mcp\lineum-railway\index.js"
$escapedRailwayScriptPath = $railwayScriptPath -replace '\\', '\\'
$configContent = $configContent.Replace('${RAILWAY_SCRIPT_PATH}', $escapedRailwayScriptPath)

$utf8NoBom = New-Object System.Text.UTF8Encoding $False
[System.IO.File]::WriteAllText($targetConfigPath, $configContent, $utf8NoBom)

# Install MCP dependencies (node_modules are gitignored — must be installed locally)
$clickupMcpDir = Join-Path $PSScriptRoot "mcp\lineum-clickup"
if (Test-Path $clickupMcpDir) {
    Write-Host "----------------------------------------"
    Write-Host "Installing ClickUp MCP dependencies..." -ForegroundColor Cyan
    Push-Location $clickupMcpDir
    npm install --silent
    Pop-Location
    Write-Host "Dependencies installed successfully." -ForegroundColor Green
} else {
    Write-Host "WARNING: MCP directory not found at $clickupMcpDir. Skipping npm install." -ForegroundColor Yellow
}

$railwayMcpDir = Join-Path $PSScriptRoot "mcp\lineum-railway"
if (Test-Path $railwayMcpDir) {
    Write-Host "----------------------------------------"
    Write-Host "Installing Railway MCP dependencies..." -ForegroundColor Cyan
    Push-Location $railwayMcpDir
    npm install --silent
    Pop-Location
    Write-Host "Dependencies installed successfully." -ForegroundColor Green
} else {
    Write-Host "WARNING: MCP directory not found at $railwayMcpDir. Skipping npm install." -ForegroundColor Yellow
}

$myinvoiceMcpDir = Join-Path $PSScriptRoot "mcp\lineum-myinvoice"
if (Test-Path $myinvoiceMcpDir) {
    Write-Host "----------------------------------------"
    Write-Host "Installing MyInvoice MCP dependencies..." -ForegroundColor Cyan
    Push-Location $myinvoiceMcpDir
    npm install --silent
    Pop-Location
    Write-Host "Dependencies installed successfully." -ForegroundColor Green
} else {
    Write-Host "WARNING: MCP directory not found at $myinvoiceMcpDir. Skipping npm install." -ForegroundColor Yellow
}

$cloudflareMcpDir = Join-Path $PSScriptRoot "mcp\lineum-cloudflare"
if (Test-Path $cloudflareMcpDir) {
    Write-Host "----------------------------------------"
    Write-Host "Installing Cloudflare MCP dependencies..." -ForegroundColor Cyan
    Push-Location $cloudflareMcpDir
    npm install --silent
    Pop-Location
    Write-Host "Dependencies installed successfully." -ForegroundColor Green
} else {
    Write-Host "WARNING: MCP directory not found at $cloudflareMcpDir. Skipping npm install." -ForegroundColor Yellow
}

Write-Host "----------------------------------------"
Write-Host "Configuring Git hooks path..." -ForegroundColor Cyan
Push-Location $repoRoot
git config core.hooksPath .agent/hooks
Pop-Location
Write-Host "Git hooks path set to .agent/hooks." -ForegroundColor Green

Write-Host "----------------------------------------"
Write-Host "Configuring Browser Allowlist..." -ForegroundColor Cyan

$browserDomains = @"
app.clickup.com
clickup.com
workplace.zoho.eu
zoho.eu
railway.app
cloudflare.com
dash.cloudflare.com
github.com
flux.lineum.io
lineum.io
"@

# Write to both antigravity and antigravity-ide (IDE version) directories
$browserAllowlistPaths = @(
    "$env:USERPROFILE\.gemini\antigravity\browserAllowlist.txt",
    "$env:USERPROFILE\.gemini\antigravity-ide\browserAllowlist.txt"
)

foreach ($allowlistPath in $browserAllowlistPaths) {
    $dir = Split-Path $allowlistPath
    if (Test-Path $dir) {
        [System.IO.File]::WriteAllText($allowlistPath, $browserDomains, [System.Text.Encoding]::UTF8)
        Write-Host "Browser allowlist written to: $allowlistPath" -ForegroundColor Green
    } else {
        Write-Host "Skipping $allowlistPath (directory does not exist yet)" -ForegroundColor Yellow
    }
}

Write-Host "----------------------------------------"
Write-Host "MCP Configuration restoration complete!" -ForegroundColor Green
Write-Host "IMPORTANT: Restart your Gemini session after running this script." -ForegroundColor Yellow
