param([ValidateSet('status','start','drive','stop')][string]$Action='status')
$ErrorActionPreference='Stop'
$script:root=Join-Path (Split-Path $PSScriptRoot) 'outputs'
$script:job=$null
$wsl='C:\Program Files\WSL\wsl.exe'
$status=[pscustomobject]@{Text=''}
$output=[pscustomobject]@{Text=''}
$gazebo=[pscustomobject]@{Checked=$false;Enabled=$true}
$script:actionButtons=@()
$tokens=$null; $errors=$null
$ast=[Management.Automation.Language.Parser]::ParseFile((Join-Path $script:root 'Vacuum-Lab.ps1'),[ref]$tokens,[ref]$errors)
$function=$ast.Find({param($node) $node -is [Management.Automation.Language.FunctionDefinitionAst] -and $node.Name -eq 'Start-LabAction'},$true)
. ([scriptblock]::Create($function.Extent.Text))
Start-LabAction $Action
[void](Wait-Job $script:job -Timeout 240)
$result=Receive-Job $script:job
Remove-Job $script:job
$result | Format-List
if ($result.Code -ne 0) { throw 'Windows-to-Ubuntu launcher job failed.' }
if ($Action -eq 'status' -and $result.Text -notmatch 'simulation: running') { throw 'Status was not running.' }
if ($Action -eq 'start' -and $result.Text -notmatch 'Ready\.|already running') { throw 'Startup was not ready.' }
if ($Action -eq 'drive' -and $result.Text -notmatch 'Ready to drive') { throw 'Driving startup was not ready.' }
if ($Action -eq 'stop' -and $result.Text -notmatch 'Lab stopped') { throw 'Shutdown did not finish.' }
