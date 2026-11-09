$ErrorActionPreference = 'Stop'
$taskRoot = '[REDACTED_HOME_PATH]
$logPath = Join-Path $taskRoot 'work\wsl-bootstrap.log'
$resultPath = Join-Path $taskRoot 'work\wsl-bootstrap-result.json'
$result = [ordered]@{
    Started = (Get-Date).ToString('o')
    BootTime = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime.ToString('o')
    Status = 'Running'
    ExitCode = $null
    VirtualMachinePlatform = $null
    Error = $null
}
$result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
Start-Transcript -LiteralPath $logPath -Force
try {
    # Official Microsoft installer. No distribution is installed here, and this
    # script never initiates a Windows restart.
    & "$env:SystemRoot\System32\wsl.exe" --install --no-distribution
    $result.ExitCode = $LASTEXITCODE
    $result.VirtualMachinePlatform = (Get-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform).State.ToString()
    if ($result.ExitCode -in @(0, 3010)) {
        $result.Status = 'BootstrapFinished'
    } else {
        $result.Status = 'InstallerNeedsReview'
    }
} catch {
    $result.Status = 'Failed'
    $result.Error = $_.Exception.Message
    Write-Output $result.Error
} finally {
    $result.Finished = (Get-Date).ToString('o')
    $result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
    Stop-Transcript
}
