param([string]$RepoRoot=(Split-Path $PSScriptRoot), [switch]$NoBrowser)
$ErrorActionPreference='Stop'
. (Join-Path $PSScriptRoot 'Files-Panel.ps1')
$stateRoot=Join-Path $env:LOCALAPPDATA 'VacuumLab'
$sessionFile=Join-Path $stateRoot 'designer-session.json'
$designRoot=Join-Path $stateRoot 'designs'
[void][IO.Directory]::CreateDirectory($stateRoot)
[void][IO.Directory]::CreateDirectory($designRoot)
if (Test-Path -LiteralPath $sessionFile) {
    try {
        $existing=Get-Content -LiteralPath $sessionFile -Raw | ConvertFrom-Json
        $health=Invoke-RestMethod -Uri ("http://localhost:"+$existing.port+"/api/state") -Headers @{'X-Robot-Lab-Token'=$existing.token} -TimeoutSec 2
        if ($health.version -eq '3.0') {
            if (-not $NoBrowser) { Start-Process $existing.url }
            $existing | ConvertTo-Json -Compress
            return
        }
    } catch { }
}
$wsl='C:\Program Files\WSL\wsl.exe'
$token=[Guid]::NewGuid().ToString('N')+[Guid]::NewGuid().ToString('N')
$ready=Join-Path $stateRoot ('designer-ready-'+[Guid]::NewGuid().ToString('N')+'.json')
$server=ConvertTo-LabLinuxPath (Join-Path $RepoRoot 'designer\server.py')
$data=ConvertTo-LabLinuxPath $designRoot
$readyLinux=ConvertTo-LabLinuxPath $ready
$arguments='-d VacuumRobot-24.04 -u robot --exec python3 "'+$server+'" --data-dir "'+$data+'" --ready-file "'+$readyLinux+'" --workspace /home/robot/vacuum_ws --port 8765 --token '+$token
$process=Start-Process -FilePath $wsl -ArgumentList $arguments -WindowStyle Hidden -PassThru -RedirectStandardOutput (Join-Path $stateRoot 'designer.log') -RedirectStandardError (Join-Path $stateRoot 'designer-error.log')
$deadline=(Get-Date).AddSeconds(20)
while (-not (Test-Path -LiteralPath $ready) -and (Get-Date) -lt $deadline -and -not $process.HasExited) { Start-Sleep -Milliseconds 200 }
if (-not (Test-Path -LiteralPath $ready)) { throw ('Designer could not start. '+(Get-Content -LiteralPath (Join-Path $stateRoot 'designer-error.log') -Raw)) }
$session=Get-Content -LiteralPath $ready -Raw | ConvertFrom-Json
$session | ConvertTo-Json | Set-Content -LiteralPath $sessionFile -Encoding UTF8
if (-not $NoBrowser) { Start-Process $session.url }
$session | ConvertTo-Json -Compress
