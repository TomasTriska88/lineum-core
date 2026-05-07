# Restore Knowledge Base to Agent's Internal Memory
# This script copies the KIs from the git repository backup back into the agent's native AppData folder.

$appDataPath = "$env:USERPROFILE\.gemini\antigravity\knowledge"
$repoKnowledgePath = Join-Path $PSScriptRoot "knowledge"

Write-Host "Restoring Lineum Knowledge Base..."
Write-Host "From: $repoKnowledgePath"
Write-Host "To:   $appDataPath"
Write-Host "----------------------------------------"

if (-Not (Test-Path -Path $repoKnowledgePath)) {
    Write-Host "ERROR: Backup directory not found at $repoKnowledgePath" -ForegroundColor Red
    Exit 1
}

if (-Not (Test-Path -Path $appDataPath)) {
    Write-Host "Creating target directory in AppData..." -ForegroundColor Yellow
    New-Item -ItemType Directory -Force -Path $appDataPath | Out-Null
}

Write-Host "Copying knowledge files..." -ForegroundColor Yellow
Copy-Item -Path "$repoKnowledgePath\*" -Destination $appDataPath -Recurse -Force

Write-Host "----------------------------------------"
Write-Host "Knowledge Base restoration complete!" -ForegroundColor Green
Write-Host "AI Agents will now natively recognize context about Company Admin, Licensing, and Branding."
