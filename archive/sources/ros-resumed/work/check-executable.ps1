$ErrorActionPreference='Stop'
$appRoot=Join-Path (Split-Path $PSScriptRoot) 'outputs'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
. (Join-Path $appRoot 'Modern-Theme.ps1')
. (Join-Path $appRoot 'Files-Panel.ps1')
Show-LabFiles 'C:\Program Files\WSL\wsl.exe' $appRoot '' -CheckOnly | Format-List
if ((ConvertTo-LabLinuxPath '[REDACTED_HOME_PATH] -ne '/mnt/c/Users/justi/Documents/Codex/2026-10-07/re/outputs') { throw 'Windows path conversion failed.' }
if ((Get-LabWindowsPath '/home/robot/vacuum_ws/.lab' $false) -ne '\\wsl.localhost\VacuumRobot-24.04\home\robot\vacuum_ws\.lab') { throw 'WSL path conversion failed.' }
function Read-Listing($path,$query) {
    $job=Start-LabFileListing 'C:\Program Files\WSL\wsl.exe' $appRoot $path $query
    try {
        $result=Wait-Job $job -Timeout 20
        if (-not $result) { throw 'File listing timed out.' }
        ((Receive-Job $job -ErrorAction Stop) -join '') | ConvertFrom-Json
    } finally { Stop-Job $job; Remove-Job $job -Force }
}
$windows=Read-Listing (ConvertTo-LabLinuxPath $appRoot) ''
if ('Vacuum Lab.exe' -notin $windows.entries.name -or 'Files-Panel.ps1' -notin $windows.entries.name) { throw 'Packaged-file listing failed.' }
$linux=Read-Listing '/home/robot/vacuum_ws' ''
if ('.lab' -notin $linux.entries.name -or 'src' -notin $linux.entries.name -or 'install' -notin $linux.entries.name) { throw 'Complete/hidden workspace listing failed.' }
$search=Read-Listing '/home/robot/vacuum_ws/src' 'vacuum.urdf'
if ('vacuum.urdf.xacro' -notin $search.entries.name) { throw 'Recursive search failed.' }
$missing=Read-Listing '/home/robot/this-folder-does-not-exist' ''
if (-not $missing.errors.Count) { throw 'Missing-folder error was not reported.' }
$report=Join-Path $PSScriptRoot 'exe-check.txt'
$exe=Join-Path $appRoot 'Vacuum Lab.exe'
$process=Start-Process -FilePath $exe -ArgumentList ('--check --report "'+$report+'"') -WindowStyle Hidden -PassThru
if (-not $process.WaitForExit(20000) -or $process.ExitCode -ne 0) { throw 'Packaged EXE failed its startup check.' }
$contents=[IO.File]::ReadAllText($report)
if ($contents -notmatch '"FileBrowser":true' -or $contents -notmatch '"Armed":false') { throw 'Packaged launcher check did not confirm menu and disarmed state.' }
$verification=@{ Date=(Get-Date -Format 'yyyy-MM-dd'); Executable='Vacuum Lab.exe'; Passed=$true; Checks=@('Embedded payload extraction','Packaged launcher startup','Files panel construction','Windows file listing','Hidden/live Ubuntu workspace files','Recursive search','Unavailable folder feedback','Path conversion','Disarmed controller default'); SHA256=(Get-FileHash -LiteralPath $exe -Algorithm SHA256).Hash }
$verification | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $appRoot 'executable-verification.json') -Encoding UTF8
$contents
'Executable and file browser checks passed.'
