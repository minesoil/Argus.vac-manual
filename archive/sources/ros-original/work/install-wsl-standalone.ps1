$ErrorActionPreference = 'Stop'
$taskRoot = '[REDACTED_HOME_PATH]
$installer = Join-Path $taskRoot 'work\wsl.3.0.1.0.x64.msi'
$resultPath = Join-Path $taskRoot 'work\wsl-standalone-result.json'
$msiLog = Join-Path $taskRoot 'work\wsl-msi-install.log'
$result = [ordered]@{
    Started = (Get-Date).ToString('o')
    BootTime = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime.ToString('o')
    Status = 'Running'
    MsiExitCode = $null
    VirtualMachinePlatform = $null
    RestartNeeded = $false
    Error = $null
}
$result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
try {
    $hash = (Get-FileHash -LiteralPath $installer -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($hash -ne '28b1a0d013640a2ac95898ea705fa186e5b4ff767a1c1b49257161bc106599c6') { throw 'Installer SHA256 mismatch.' }
    $signature = Get-AuthenticodeSignature -LiteralPath $installer
    if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -notmatch 'O=Microsoft Corporation') { throw 'Invalid Microsoft signature.' }
    $msi = Start-Process -FilePath "$env:SystemRoot\System32\msiexec.exe" -ArgumentList @('/i', ('"' + $installer + '"'), '/qn', '/norestart', '/L*v', ('"' + $msiLog + '"')) -WindowStyle Hidden -Wait -PassThru
    $result.MsiExitCode = $msi.ExitCode
    if ($msi.ExitCode -notin @(0,3010)) { throw "Windows Installer returned $($msi.ExitCode); inspect its log." }
    $feature = Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart
    $result.VirtualMachinePlatform = (Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform).State.ToString()
    $result.RestartNeeded = [bool]($feature.RestartNeeded -or $msi.ExitCode -eq 3010 -or $result.VirtualMachinePlatform -eq 'EnablePending')
    $result.Status = 'Installed'
} catch {
    $result.Status = 'Failed'
    $result.Error = $_.Exception.Message
} finally {
    $result.Finished = (Get-Date).ToString('o')
    $result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
}
# Deliberately no restart command. The user decides when to restart Windows.
