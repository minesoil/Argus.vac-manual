$ErrorActionPreference='Stop'
$deviceId='ROOT\VID\0000'
$resultPath='[REDACTED_HOME_PATH]
$initial=Get-PnpDevice -InstanceId $deviceId -ErrorAction Stop
$result=[ordered]@{Device=$deviceId;InitialStatus=$initial.Status;InitialProblem=$initial.Problem.ToString();FinalStatus=$null;FinalProblem=$null;Error=$null}
try {
    if($initial.Problem -ne 'CM_PROB_DISABLED'){throw 'Device is not disabled; refusing to change an unexpected state.'}
    Enable-PnpDevice -InstanceId $deviceId -Confirm:$false -ErrorAction Stop
    $final=Get-PnpDevice -InstanceId $deviceId
    $result.FinalStatus=$final.Status
    $result.FinalProblem=$final.Problem.ToString()
} catch {
    $result.Error=$_.Exception.Message
} finally {
    $result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
}
