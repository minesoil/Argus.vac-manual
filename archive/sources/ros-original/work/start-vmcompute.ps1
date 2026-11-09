$ErrorActionPreference='Stop'
$resultPath='[REDACTED_HOME_PATH]
$result=[ordered]@{Started=(Get-Date).ToString('o');InitialStatus=(Get-Service vmcompute).Status.ToString();FinalStatus=$null;Error=$null}
try {
    if($result.InitialStatus -ne 'Running') { Start-Service vmcompute -ErrorAction Stop }
    $result.FinalStatus=(Get-Service vmcompute).Status.ToString()
} catch {
    $result.Error=$_.Exception.Message
    $result.FinalStatus=(Get-Service vmcompute).Status.ToString()
} finally {
    $result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
}
