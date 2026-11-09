$ErrorActionPreference='Stop'
$taskRoot='[REDACTED_HOME_PATH]
$resultPath=Join-Path $taskRoot 'work\ubuntu-install-result.json'
$location='E:\WSL\VacuumRobot\Ubuntu-24.04'
$result=[ordered]@{Name='VacuumRobot-24.04';Location=$location;Installed=$false;ExitCode=$null;Error=$null}
try {
    foreach($id in @('ROOT\VDRVROOT\0000','ROOT\VID\0000')) {
        if((Get-PnpDevice -InstanceId $id).Status -ne 'OK'){throw "Required device $id is not ready."}
    }
    if(Test-Path -LiteralPath $location){throw 'Install location already exists; inspect before proceeding.'}
    if((Get-Service vmcompute).Status -ne 'Running'){Start-Service vmcompute}
    $wsl=Join-Path $env:ProgramFiles 'WSL\wsl.exe'
    $text=(& $wsl --install --from-file 'E:\WSL\VacuumRobot\ubuntu-24.04.5-wsl-amd64.wsl' --name VacuumRobot-24.04 --location $location --no-launch --version 2 --vhd-size 40GB 2>&1 | Out-String) -replace "`0",''
    $result.ExitCode=$LASTEXITCODE
    $text | Set-Content -LiteralPath (Join-Path $taskRoot 'work\ubuntu-install.log') -Encoding UTF8
    if($result.ExitCode -ne 0){throw "Ubuntu installer returned $($result.ExitCode). Inspect ubuntu-install.log."}
    $result.Installed=$true
} catch {
    $result.Error=$_.Exception.Message
} finally {
    $result | ConvertTo-Json | Set-Content -LiteralPath $resultPath -Encoding UTF8
}
