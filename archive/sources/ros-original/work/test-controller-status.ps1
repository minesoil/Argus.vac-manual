$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
. (Join-Path (Split-Path $PSScriptRoot) 'outputs\Controller-Panel.ps1')
$device=[VacuumJoystick]::Devices() | Where-Object DisplayName -match 'Alpha' | Select-Object -First 1
if ($device) {
    [uint32]$bits=0
    $axes=[VacuumJoystick]::Read($device,[ref]$bits)
    $pressed=for($i=0;$i -lt 32;$i++) { if (([uint64]$bits -band ([uint64]1 -shl $i)) -ne 0) { $i+1 } }
    Write-Output ('Alpha live axes: '+($axes -join ', ')+'; buttons: '+($pressed -join ', '))
}
$psi=New-Object Diagnostics.ProcessStartInfo
$psi.FileName='C:\Program Files\WSL\wsl.exe'
$psi.Arguments='-d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec /bin/bash -lc "source env.sh; exec python3 tools/controller_bridge.py"'
$psi.UseShellExecute=$false; $psi.CreateNoWindow=$true
$psi.RedirectStandardInput=$true; $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true
$proc=New-Object Diagnostics.Process
$proc.StartInfo=$psi
try {
    [void]$proc.Start()
    $pump=New-Object VacuumJoystick+OutputPump($proc.StandardOutput)
    $errorTask=$proc.StandardError.ReadToEndAsync()
    $end=(Get-Date).AddSeconds(6)
    while ((Get-Date) -lt $end) {
        if ($proc.HasExited) { throw ('Bridge exited: '+$errorTask.Result) }
        $proc.StandardInput.WriteLine('{"v":0,"w":0,"held":false}');$proc.StandardInput.Flush()
        Start-Sleep -Milliseconds 50
    }
    $status=$pump.Latest | ConvertFrom-Json
    if (-not $pump.Fresh -or -not $status.ready -or $status.output_v -ne 0) { throw 'Live stopped/ready status was not received.' }
    $status | ConvertTo-Json -Compress
    $proc.StandardInput.Close()
    if (-not $proc.WaitForExit(5000)) { throw 'Bridge did not stop on EOF.' }
    if ($proc.ExitCode -ne 0) { throw ('Bridge failed: '+$errorTask.Result) }
    Write-Output 'Windows status pump, Ubuntu guard health, zero input, and EOF shutdown passed.'
} finally {
    if (-not $proc.HasExited) { $proc.StandardInput.Close() }
    $proc.Dispose()
}
