param([switch]$DriveNow, [switch]$Files, [switch]$Designer, [switch]$CheckOnly, [string]$PreviewPath)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$script:job = $null
$script:started = $null
$script:root = Split-Path $PSScriptRoot
$wsl = 'C:\Program Files\WSL\wsl.exe'
$code = '[REDACTED_HOME_PATH] VS Code\bin\code.cmd'
$linuxRoot = '\\wsl.localhost\VacuumRobot-24.04\home\robot\vacuum_ws'
. (Join-Path $PSScriptRoot 'Modern-Theme.ps1')
. (Join-Path $PSScriptRoot 'Controller-Panel.ps1')
. (Join-Path $PSScriptRoot 'Files-Panel.ps1')

$form = New-Object Windows.Forms.Form
$form.Text = 'Vacuum Lab'
$form.ClientSize = New-Object Drawing.Size(1060,790)
$form.FormBorderStyle='FixedSingle'; $form.MaximizeBox=$false
$form.StartPosition='CenterScreen'
$script:actionButtons=@()
function Add-LabLabel($text,$x,$y,$width,$height,$size=10,$tag='') {
    $label=New-Object Windows.Forms.Label
    $label.Text=$text; $label.SetBounds($x,$y,$width,$height); $label.Tag=$tag
    $label.Font=New-Object Drawing.Font('Segoe UI',$size)
    $form.Controls.Add($label); return $label
}
function Add-LabButton($text,$x,$y,$handler,$managed=$false,$width=166,$height=44,$tag='') {
    $button=New-Object Windows.Forms.Button
    $button.Text=$text; $button.SetBounds($x,$y,$width,$height); $button.Tag=$tag
    $button.Add_Click($handler); $form.Controls.Add($button)
    if ($managed) { $script:actionButtons += $button }
}
$null=Add-LabLabel 'VACUUM' 24 28 180 35 20 'accent'
$null=Add-LabLabel 'LAB / 02' 26 72 164 30 12 'muted'
$null=Add-LabLabel 'WORKSPACE' 26 148 166 24 9 'muted'
$null=Add-LabLabel 'ROS 2 JAZZY' 26 626 170 25 9 'accent'
$null=Add-LabLabel 'GAZEBO HARMONIC' 26 653 175 25 9 'muted'
$null=Add-LabLabel 'SIMULATION STUDIO' 244 30 450 24 10 'accent'
$null=Add-LabLabel 'Design. Test. Drive.' 242 65 780 58 30
$null=Add-LabLabel 'Edit your robot and test it in the simulator.' 244 128 720 30 12 'muted'
$null=Add-LabLabel 'TAKE CONTROL' 244 174 330 26 9 'muted'
$gazebo=New-Object Windows.Forms.CheckBox
$gazebo.Text='Open the Gazebo 3D view as well'
$gazebo.SetBounds(244,400,350,30); $form.Controls.Add($gazebo)
$preview=New-Object Windows.Forms.PictureBox
$preview.SetBounds(618,174,406,256); $preview.SizeMode='Zoom'
$imagePath=Join-Path $script:root 'assets\Furnished-room-preview.png'
if (Test-Path -LiteralPath $imagePath) { $preview.Image=[Drawing.Image]::FromFile($imagePath) }
$form.Controls.Add($preview)
$null=Add-LabLabel '16 x 12 m / FURNISHED TEST WORLD' 618 438 406 27 9 'muted'
foreach ($metric in @(@('1.5 m/s','FORWARD SPEED',244),@('70 mm','WHEEL DIAMETER',506),@('50 Hz','DIRECT INPUT',768))) {
    $null=Add-LabLabel $metric[0] $metric[2] 478 230 43 24 'accent'
    $null=Add-LabLabel $metric[1] $metric[2] 524 230 24 9 'muted'
}
$null=Add-LabLabel 'YOUR ROBOT' 244 564 760 24 9 'muted'
$null=Add-LabLabel 'NEMA 17 x2  /  TB6600 x2  /  Arduino Mega 2560' 244 592 780 27 12
$null=Add-LabLabel 'Orange Pi 5  /  RPLIDAR C1  /  Motors below the acrylic chassis' 244 620 790 26 10 'muted'
$status=Add-LabLabel 'Ready. Choose a workflow to begin.' 244 656 780 27 10 'accent'
$output=New-Object Windows.Forms.TextBox
$output.Multiline=$true; $output.ReadOnly=$true; $output.ScrollBars='Vertical'
$output.SetBounds(244,688,780,76)
$output.Text='Arm once, then drive with the yoke. Center it to stop.'
$form.Controls.Add($output)
function Start-LabAction([string]$action) {
    if ($script:job) { return }
    $files = @{}
    foreach ($name in @('lab_controller.py','run_sim.py','prepare_lab.py','controller_bridge.py','command_gate.py','check_lab.py','wait_ready.py','activate_guard.py','workspace_paths.py','robot-profile.json')) {
        $sourcePath=if ($name -eq 'robot-profile.json') { Join-Path $script:root 'config\simulation.json' } else { Join-Path $script:root ('simulation\tools\'+$name) }; $files[$name] = [Convert]::ToBase64String([IO.File]::ReadAllBytes($sourcePath))
    }
    $source = $files | ConvertTo-Json -Compress
    $script:operation = $action
    $script:started = Get-Date
    $status.Text = "Working: $action ..."
    $output.Text = 'Ubuntu is preparing the requested action. Startup may take a few minutes.'
    foreach ($button in $script:actionButtons) { $button.Enabled = $false }
    $gazebo.Enabled = $false
    $script:job = Start-Job -ArgumentList $wsl,$source,$action,$gazebo.Checked -ScriptBlock {
        param($wslPath,$payload,$operation,$showGazebo)
        $bootstrap = @"
import base64, json, pathlib, runpy, sys
tools = pathlib.Path('/home/robot/vacuum_ws/tools')
if not tools.is_dir():
    raise SystemExit('Ubuntu vacuum workspace is missing.')
decoded = {name: base64.b64decode(value) for name, value in json.loads('$payload').items()}
for name, data in decoded.items():
    if name.endswith('.py'):
        compile(data, name, 'exec')
for name, data in decoded.items():
    if name == 'robot-profile.json' and (tools.parent / '.lab/custom-design.json').exists():
        continue
    p = tools / name
    if not p.exists() or p.read_bytes() != data:
        p.write_bytes(data)
p = tools / 'lab_controller.py'
sys.path.insert(0, str(tools))
sys.argv = [str(p), '$operation'] + (['--gazebo'] if '$showGazebo' == 'True' else [])
runpy.run_path(str(p), run_name='__main__')
"@
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $wslPath
        $psi.Arguments = '-d VacuumRobot-24.04 -u robot --exec python3 -'
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        $psi.RedirectStandardInput = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        $psi.StandardOutputEncoding = [Text.Encoding]::UTF8
        $psi.StandardErrorEncoding = [Text.Encoding]::UTF8
        $proc = New-Object System.Diagnostics.Process
        $proc.StartInfo = $psi
        try {
            [void]$proc.Start()
            $stdout = $proc.StandardOutput.ReadToEndAsync()
            $stderr = $proc.StandardError.ReadToEndAsync()
            $proc.StandardInput.Write($bootstrap)
            $proc.StandardInput.Close()
            $proc.WaitForExit()
            [pscustomobject]@{ Code = $proc.ExitCode; Text = $stdout.Result + $stderr.Result }
        } finally { $proc.Dispose() }
    }
}

Add-LabButton 'Drive now' 244 206 { Start-LabAction 'drive' } $true 350 52 'primary'
Add-LabButton 'Mapping + navigation' 244 270 { Start-LabAction 'start' } $true 350 52
Add-LabButton 'All project files' 244 334 { Show-LabFiles $wsl $script:root $code } $false 350 52
Add-LabButton 'Open robot code' 24 184 {
    if (Test-Path $code) { Start-Process -FilePath $code -ArgumentList '--remote wsl+VacuumRobot-24.04 /home/robot/vacuum_ws' -WindowStyle Hidden }
}
Add-LabButton 'Ubuntu terminal' 24 238 {
    Start-Process -FilePath $wsl -ArgumentList '-d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws'
}
Add-LabButton 'Save current map' 24 292 { Start-LabAction 'save-map' } $true
Add-LabButton 'Check lab status' 24 346 { Start-LabAction 'status' } $true
Add-LabButton 'Quick guide' 24 400 {
    Start-Process notepad.exe -ArgumentList ('"'+(Join-Path $script:root 'README.md')+'"')
}
Add-LabButton 'Design robot' 24 454 {
    try { & (Join-Path $PSScriptRoot 'Start-Designer.ps1') -RepoRoot $script:root | Out-Null }
    catch { $status.Text='Designer could not start.'; $output.Text=[string]$_ }
}
Add-LabButton 'Stop lab' 24 710 { Start-LabAction 'stop' } $true 166 52 'danger'

$timer = New-Object System.Windows.Forms.Timer
$timer.Interval = 1000
$timer.Add_Tick({
    if (-not $script:job) { return }
    if ($script:job.State -in @('Completed', 'Failed', 'Stopped')) {
        $result = Receive-Job $script:job -ErrorAction SilentlyContinue
        $failure = $script:job.ChildJobs[0].JobStateInfo.Reason
        if ($result) {
            $output.Text = ($result.Text -replace "`r?`n", "`r`n")
            $status.Text = if ($result.Code -eq 0) { 'Done. See the details below.' } else { 'Action failed. See the details below.' }
        } else {
            $output.Text = "The action could not complete. $failure"
            $status.Text = 'Action failed.'
        }
        $openController = $script:operation -in @('manual','drive') -and $result -and $result.Code -eq 0
        Remove-Job $script:job
        $script:job = $null
        foreach ($button in $script:actionButtons) { $button.Enabled = $true }
        $gazebo.Enabled = $true
        if ($openController) { Show-ControllerPanel $wsl $script:root }
    } else {
        $elapsed = [int]((Get-Date) - $script:started).TotalSeconds
        $status.Text = "Working in Ubuntu ... ${elapsed}s"
    }
})
$form.Add_FormClosing({
    param($sender, $event)
    if ($script:job) {
        $event.Cancel = $true
        [void][Windows.Forms.MessageBox]::Show('Wait for this action to finish before closing the launcher.')
    }
})
$form.Add_Shown({ if ($DriveNow) { Start-LabAction 'drive' }; if ($Files) { Show-LabFiles $wsl $script:root $code }; if ($Designer) { & (Join-Path $PSScriptRoot 'Start-Designer.ps1') -RepoRoot $script:root } })
Set-LabTheme $form
if ($CheckOnly) {
    if ($PreviewPath) {
        $form.Show(); $form.Refresh()
        $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
        try { $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height))); $bitmap.Save($PreviewPath) }
        finally { $bitmap.Dispose(); $form.Hide() }
    }
    [pscustomobject]@{ Title=$form.Text; Controls=$form.Controls.Count; FileBrowser=$true; Armed=$false } | ConvertTo-Json -Compress
    $timer.Dispose(); if ($preview.Image) { $preview.Image.Dispose() }; $form.Dispose()
    exit 0
}
$timer.Start()
try { [void]$form.ShowDialog() } finally { $timer.Stop(); $timer.Dispose(); if ($preview.Image) { $preview.Image.Dispose() }; $form.Dispose() }
