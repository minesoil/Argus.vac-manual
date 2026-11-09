$ErrorActionPreference = 'Stop'
$taskProblems = @()
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
foreach ($name in @('Vacuum-Lab.ps1', 'Controller-Panel.ps1', 'Check-Lab.ps1')) {
    $taskTokens=$null; $taskErrors=$null
    [void][Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot $name),[ref]$taskTokens,[ref]$taskErrors)
    $taskProblems += $taskErrors
}
if ($taskProblems.Count) { $taskProblems | Format-List; throw 'PowerShell parsing failed.' }
. (Join-Path $PSScriptRoot 'Controller-Panel.ps1')
if ([Runtime.InteropServices.Marshal]::SizeOf([type][VacuumJoystick+Caps]) -ne 728) { throw 'Unexpected joystick capability layout.' }
if ([Runtime.InteropServices.Marshal]::SizeOf([type][VacuumJoystick+Pos]) -ne 52) { throw 'Unexpected joystick position layout.' }
'PowerShell parsed; joystick interop compiled. Connected devices:'
[VacuumJoystick]::Devices() | ForEach-Object { $_.ToString() }
Show-ControllerPanel '' $PSScriptRoot -CheckOnly | Format-List
'No robot motion or Ubuntu changes were performed by this check.'
