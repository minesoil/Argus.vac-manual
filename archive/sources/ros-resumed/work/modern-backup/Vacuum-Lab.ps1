param([switch]$DriveNow, [switch]$Files, [switch]$CheckOnly)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$script:job = $null
$script:started = $null
$script:root = $PSScriptRoot
$wsl = 'C:\Program Files\WSL\wsl.exe'
$code = '[REDACTED_HOME_PATH] VS Code\bin\code.cmd'
$linuxRoot = '\\wsl.localhost\VacuumRobot-24.04\home\robot\vacuum_ws'
. (Join-Path $script:root 'Controller-Panel.ps1')
. (Join-Path $script:root 'Files-Panel.ps1')

$form = New-Object System.Windows.Forms.Form
$form.Text = 'Vacuum Lab'
$form.Size = New-Object System.Drawing.Size(720, 640)
$form.MinimumSize = $form.Size
$form.StartPosition = 'CenterScreen'
$form.BackColor = [System.Drawing.Color]::FromArgb(245, 247, 250)
$form.Font = New-Object System.Drawing.Font('Segoe UI', 10)

$heading = New-Object System.Windows.Forms.Label
$heading.Text = 'Your Ubuntu vacuum workspace'
$heading.Font = New-Object System.Drawing.Font('Segoe UI', 18, [System.Drawing.FontStyle]::Bold)
$heading.SetBounds(24, 20, 650, 40)
$form.Controls.Add($heading)
$intro = New-Object System.Windows.Forms.Label
$intro.Text = 'Drive now opens your controller directly. Push forward; pull back to reverse.'
$intro.SetBounds(26, 66, 650, 28)
$form.Controls.Add($intro)
$gazebo = New-Object System.Windows.Forms.CheckBox
$gazebo.Text = 'Also open the Gazebo 3D view (uses more graphics resources)'
$gazebo.SetBounds(26, 100, 650, 30)
$form.Controls.Add($gazebo)
$script:actionButtons = @()

function Add-LabButton($text, $x, $y, $handler, $managed = $false) {
    $button = New-Object System.Windows.Forms.Button
    $button.Text = $text
    $button.SetBounds($x, $y, 205, 44)
    $button.FlatStyle = 'Flat'
    $button.BackColor = [System.Drawing.Color]::White
    $button.Add_Click($handler)
    $form.Controls.Add($button)
    if ($managed) { $script:actionButtons += $button }
}

$status = New-Object System.Windows.Forms.Label
$status.Text = 'Ready to start. This lab operates only the simulated robot.'
$status.SetBounds(26, 314, 650, 45)
$form.Controls.Add($status)
$output = New-Object System.Windows.Forms.TextBox
$output.Multiline = $true
$output.ReadOnly = $true
$output.ScrollBars = 'Vertical'
$output.SetBounds(26, 366, 650, 155)
$output.Anchor = 'Top,Bottom,Left,Right'
$output.Text = 'Drive now opens the simulator and your controller panel.' +
    "`r`nCamera: 60 FPS target. Push forward, pull back to reverse, rotate to steer."
$form.Controls.Add($output)
$note = New-Object System.Windows.Forms.Label
$note.Text = 'Drive now: manual driving. Mapping + navigation: mapping and destination goals.' +
    "`r`nClosing this window leaves the lab running; use Stop lab to shut it down."
$note.SetBounds(26, 533, 650, 55)
$note.Anchor = 'Bottom,Left,Right'
$form.Controls.Add($note)

function Start-LabAction([string]$action) {
    if ($script:job) { return }
    $files = @{}
    foreach ($name in @('lab_controller.py','prepare_lab.py','controller_bridge.py','command_gate.py','check_lab.py','wait_ready.py','activate_guard.py')) {
        $files[$name] = [Convert]::ToBase64String([IO.File]::ReadAllBytes((Join-Path $script:root $name)))
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
    compile(data, name, 'exec')
for name, data in decoded.items():
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

Add-LabButton 'Drive now' 26 148 { Start-LabAction 'drive' } $true
Add-LabButton 'Save current map' 248 148 { Start-LabAction 'save-map' } $true
Add-LabButton 'Stop lab' 470 148 { Start-LabAction 'stop' } $true
Add-LabButton 'Open robot code' 26 206 {
    if (Test-Path $code) {
        Start-Process -FilePath $code -ArgumentList '--remote wsl+VacuumRobot-24.04 /home/robot/vacuum_ws' -WindowStyle Hidden
    } else { [void][Windows.Forms.MessageBox]::Show('VS Code was not found at its existing installation path.') }
}
Add-LabButton 'Ubuntu terminal' 248 206 {
    Start-Process -FilePath $wsl -ArgumentList '-d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws'
}
Add-LabButton 'All project files' 470 206 {
    Show-LabFiles $wsl $script:root $code
}
Add-LabButton 'Mapping + navigation' 26 264 { Start-LabAction 'start' } $true
Add-LabButton 'Check lab status' 248 264 { Start-LabAction 'status' } $true
Add-LabButton 'Quick guide' 470 264 {
    Start-Process -FilePath 'notepad.exe' -ArgumentList ('"' + (Join-Path $script:root 'Vacuum-Lab-Quickstart.md') + '"')
}

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
$form.Add_Shown({ if ($DriveNow) { Start-LabAction 'drive' }; if ($Files) { Show-LabFiles $wsl $script:root $code } })
if ($CheckOnly) {
    [pscustomobject]@{ Title=$form.Text; Controls=$form.Controls.Count; FileBrowser=$true; Armed=$false } | ConvertTo-Json -Compress
    $timer.Dispose(); $form.Dispose()
    exit 0
}
$timer.Start()
try { [void]$form.ShowDialog() } finally { $timer.Stop(); $timer.Dispose(); $form.Dispose() }
