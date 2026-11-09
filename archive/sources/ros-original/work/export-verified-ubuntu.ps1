$ErrorActionPreference = 'Stop'
$wslExe = 'C:\Program Files\WSL\wsl.exe'
$backupDirectory = 'F:\VacuumRobotBackups'
$backupDrive = [System.IO.DriveInfo]::new('F:\')
if (-not $backupDrive.IsReady -or $backupDrive.AvailableFreeSpace -lt 20GB) {
    throw 'Backup drive F: must be connected with at least 20 GB free.'
}
if (-not (Test-Path -LiteralPath $backupDirectory)) {
    New-Item -ItemType Directory -Path $backupDirectory | Out-Null
}
$backupFile = Join-Path $backupDirectory ('VacuumRobot-24.04-verified-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.tar')
if (Test-Path -LiteralPath $backupFile) { throw 'Refuse to replace an existing backup.' }
$backupFile | Set-Content -LiteralPath '[REDACTED_HOME_PATH]
& $wslExe --terminate VacuumRobot-24.04
if ($LASTEXITCODE -ne 0) { throw 'Could not stop Ubuntu for backup.' }
& $wslExe --export VacuumRobot-24.04 $backupFile
if ($LASTEXITCODE -ne 0) { throw 'Ubuntu export failed; retain partial file for diagnosis.' }
$archiveEntries = & "$env:SystemRoot\System32\tar.exe" -tf $backupFile 2>&1
if ($LASTEXITCODE -ne 0) { throw 'Export tar structure could not be read.' }
$requiredEntries = @('etc/os-release', 'home/robot/vacuum_ws/env.sh', 'home/robot/vacuum_ws/src/vacuum_sim/package.xml', 'opt/ros/jazzy/setup.bash')
foreach ($entry in $requiredEntries) {
    if (-not ($archiveEntries -contains $entry -or $archiveEntries -contains ('./' + $entry))) {
        throw "Backup is missing required path: $entry"
    }
}
$hash = (Get-FileHash -LiteralPath $backupFile -Algorithm SHA256).Hash.ToLowerInvariant()
($hash + '  ' + [System.IO.Path]::GetFileName($backupFile)) | Set-Content -LiteralPath ($backupFile + '.sha256') -Encoding ascii
$result = [ordered]@{
    Completed = $true
    Path = $backupFile
    Bytes = (Get-Item -LiteralPath $backupFile).Length
    SHA256 = $hash
    ArchiveStructureVerified = $true
    RestoreBootTested = $false
    Finished = (Get-Date).ToString('o')
}
$result | ConvertTo-Json | Set-Content -LiteralPath '[REDACTED_HOME_PATH] -Encoding utf8
$result | ConvertTo-Json
