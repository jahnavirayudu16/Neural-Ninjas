## start_all.ps1
# Starts backend (using backend/.venv311) and frontend static server
$root = Split-Path -Parent $MyInvocation.MyCommand.Definition
$backendPython = Join-Path $root "backend\.venv311\Scripts\python.exe"
if (-not (Test-Path $backendPython)) {
    Write-Host "backend venv not found at $backendPython"
    Write-Host "Create it with: py -3.11 -m venv backend\\.venv311" -ForegroundColor Yellow
    exit 1
}

Write-Host "Starting backend using: $backendPython" -ForegroundColor Green
Start-Process -NoNewWindow -FilePath $backendPython -ArgumentList 'app.py' -WorkingDirectory (Join-Path $root 'backend')
Start-Sleep -Seconds 1

Write-Host "Starting frontend static server on port 8000" -ForegroundColor Green
Start-Process -NoNewWindow -FilePath 'py' -ArgumentList '-3.11','-m','http.server','8000' -WorkingDirectory (Join-Path $root 'frontend')

Write-Host "Started backend -> http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "Started frontend -> http://localhost:8000" -ForegroundColor Cyan

Write-Host "To stop: use Task Manager or run 'Get-Process python | Stop-Process -Force' with caution." -ForegroundColor Yellow
