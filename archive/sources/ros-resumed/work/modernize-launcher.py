from pathlib import Path

out = Path(__file__).resolve().parents[1] / 'outputs'
launcher = out / 'Vacuum-Lab.ps1'
text = launcher.read_text(encoding='utf-8-sig')
text = text.replace('[switch]$CheckOnly)', '[switch]$CheckOnly, [string]$PreviewPath)', 1)
text = text.replace(". (Join-Path $script:root 'Controller-Panel.ps1')", ". (Join-Path $script:root 'Modern-Theme.ps1')\n. (Join-Path $script:root 'Controller-Panel.ps1')")
start = text.index('$form = New-Object')
end = text.index('function Start-LabAction', start)
text = text[:start] + '''$form = New-Object Windows.Forms.Form
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
$null=Add-LabLabel 'Build. Drive. Explore.' 242 65 780 58 30
$null=Add-LabLabel 'Your hardware. A bigger room. Direct control.' 244 128 720 30 12 'muted'
$null=Add-LabLabel 'TAKE CONTROL' 244 174 330 26 9 'muted'
$gazebo=New-Object Windows.Forms.CheckBox
$gazebo.Text='Open the Gazebo 3D view as well'
$gazebo.SetBounds(244,400,350,30); $form.Controls.Add($gazebo)
$preview=New-Object Windows.Forms.PictureBox
$preview.SetBounds(618,174,406,256); $preview.SizeMode='Zoom'
$imagePath=Join-Path $script:root 'Furnished-room-preview.png'
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
''' + text[end:]
text = text.replace("'activate_guard.py'))", "'activate_guard.py','apply_robot_profile.py','robot-profile.json'))")
text = text.replace("    compile(data, name, 'exec')", "    if name.endswith('.py'):\n        compile(data, name, 'exec')")
start = text.index("Add-LabButton 'Drive now'")
end = text.index('$timer =', start)
text = text[:start] + '''Add-LabButton 'Drive now' 244 206 { Start-LabAction 'drive' } $true 350 52 'primary'
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
    Start-Process notepad.exe -ArgumentList ('"'+(Join-Path $script:root 'Vacuum-Lab-Quickstart.md')+'"')
}
Add-LabButton 'Robot profile' 24 454 {
    Start-Process notepad.exe -ArgumentList ('"'+(Join-Path $script:root 'Hardware-Profile.md')+'"')
}
Add-LabButton 'Stop lab' 24 710 { Start-LabAction 'stop' } $true 166 52 'danger'

''' + text[end:]
text = text.replace('if ($CheckOnly) {', '''Set-LabTheme $form
if ($CheckOnly) {
    if ($PreviewPath) {
        $form.Show(); $form.Refresh()
        $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
        try { $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height))); $bitmap.Save($PreviewPath) }
        finally { $bitmap.Dispose(); $form.Hide() }
    }''')
text = text.replace('$form.Dispose()', 'if ($preview.Image) { $preview.Image.Dispose() }; $form.Dispose()')
launcher.write_text(text, encoding='utf-8-sig')

controller = out / 'Controller-Panel.ps1'
text = controller.read_text(encoding='utf-8-sig')
text = text.replace('[switch]$CheckOnly)', '[switch]$CheckOnly, [string]$PreviewPath)', 1)
text = text.replace('    $panel = New-Object', "    $driveProfile=(Get-Content -LiteralPath (Join-Path $profileRoot 'robot-profile.json') -Raw | ConvertFrom-Json).drive\n    $panel = New-Object", 1)
text = text.replace("'Drive robot — push forward / pull reverse'", "'Vacuum Lab / Direct drive'")
text = text.replace('    $dead.Minimum=5; $dead.Maximum=40; $dead.Value=10;', '    $dead.Minimum=2; $dead.Maximum=40; $dead.Value=5;')
text = text.replace("'Hold-to-drive button          Stop button (latched)'", "'Optional hold button          Stop button (latched)'")
text = text.replace('    $message = Label-At', '''    $requireHold=New-Object Windows.Forms.CheckBox
    $requireHold.Text='Require drive button'
    $requireHold.Checked=$false; $requireHold.SetBounds(420,270,195,28)
    $hold.Enabled=$false; $panel.Controls.Add($requireHold)
    $requireHold.Add_CheckedChanged({ Disarm-Drive; $hold.Enabled=$requireHold.Checked; $message.Text='Drive mode changed. Center the yoke and re-arm.' })
    $message = Label-At''', 1)
text = text.replace("'Center the yoke, Arm drive, then hold your drive button to move.'", "'Center the yoke and arm once. Move the yoke to drive; center to stop.'")
text = text.replace("'Keep drive armed when switching windows (hold button required)'", "'Keep drive armed when switching windows'")
text = text.replace("'Drive stops on release, STOP, disconnect, or stale input.'", "'Center the yoke to stop. STOP disarms. Input loss also stops drive.'")
text = text.replace('Speed cap: +0.50 / −0.30 m/s. Turn cap: 1.2 rad/s.', 'Speed: +1.50 / -0.90 m/s. Responsive steering: 2.4 rad/s.')
text = text.replace('function Send-Drive($v,$w,$held)', 'function Send-Drive($v,$w,$enabled)')
text = text.replace('held=[bool]$held', 'enabled=[bool]$enabled')
text = text.replace('$hold.Value -eq $stop.Value', '($requireHold.Checked -and $hold.Value -eq $stop.Value)')
text = text.replace('Choose distinct axes and distinct hold/stop buttons.', 'Choose distinct axes; optional hold and stop must be different.')
text = text.replace('$hold.Value -gt $device.SelectedItem.Info.Buttons', '($requireHold.Checked -and $hold.Value -gt $device.SelectedItem.Info.Buttons)')
text = text.replace('$driveMask = ([uint64]1 -shl ([int]$hold.Value-1)) -bor ([uint64]1 -shl ([int]$stop.Value-1))', '$driveMask = ([uint64]1 -shl ([int]$stop.Value-1))\n        if ($requireHold.Checked) { $driveMask = $driveMask -bor ([uint64]1 -shl ([int]$hold.Value-1)) }')
text = text.replace('Center the selected axes and release the hold/stop buttons before arming.', 'Center the selected axes and release STOP before arming.')
text = text.replace("'Hold the bound drive button to move. Release to stop.'", "'Armed. Move the yoke to drive; center the yoke to stop.'")
text = text.replace('$dead.Value=10', '$dead.Value=5; $requireHold.Checked=$false')
text = text.replace('version=1; device=', 'version=2; requireHold=$requireHold.Checked; device=')
text = text.replace('$p.version -ne 1', '$p.version -notin @(1,2)')
text = text.replace('$p.deadZone -notin 5..40', '$p.deadZone -notin 2..40')
text = text.replace('                $state.Centers=@($p.centers)', "                $requireHold.Checked=($p.version -eq 2 -and $p.requireHold -eq $true)\n                $state.Centers=@($p.centers)")
text = text.replace('$timer.Interval=50', '$timer.Interval=20')
text = text.replace('$(if ($preview -ge 0) { .50 } else { .30 })', '$(if ($preview -ge 0) { $driveProfile.forward_m_s } else { $driveProfile.reverse_m_s })')
text = text.replace('$held = $state.Armed -and (([uint64]$bits -band ([uint64]1 -shl ([int]$hold.Value-1))) -ne 0)', '$held = $state.Armed -and (-not $requireHold.Checked -or (([uint64]$bits -band ([uint64]1 -shl ([int]$hold.Value-1))) -ne 0))')
text = text.replace('$(if ($a -ge 0) { .50 } else { .30 })', '$(if ($a -ge 0) { $driveProfile.forward_m_s } else { $driveProfile.reverse_m_s })')
text = text.replace('* 1.2', '* $driveProfile.turn_rad_s')
text = text.replace("'Drive button held. Move the selected axes beyond the dead zone.'", "'Armed at neutral. Move the yoke to drive.'")
text = text.replace("'Drive button held. Release to stop, or press STOP to disarm.'", "'Driving. Center the yoke to stop, or press STOP to disarm.'")
text = text.replace('    if ($CheckOnly) {', '''    Set-LabTheme $panel
    if ($CheckOnly) {
        if ($PreviewPath) {
            $panel.Show(); $panel.Refresh()
            $bitmap=New-Object Drawing.Bitmap($panel.Width,$panel.Height)
            try { $panel.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$panel.Width,$panel.Height))); $bitmap.Save($PreviewPath) }
            finally { $bitmap.Dispose(); $panel.Hide() }
        }''')
text = text.replace('* .30', '* $driveProfile.reverse_m_s').replace('* .50', '* $driveProfile.forward_m_s')
text = text.replace('Armed=$state.Armed;', 'Armed=$state.Armed; RequireHold=$requireHold.Checked; InputPeriodMs=$timer.Interval;')
controller.write_text(text, encoding='utf-8-sig')

files=out / 'Files-Panel.ps1'
text=files.read_text(encoding='utf-8-sig')
text=text.replace('    if ($CheckOnly) {', '    Set-LabTheme $filesForm\n    if ($CheckOnly) {')
files.write_text(text, encoding='utf-8-sig')

check=out / 'Check-Lab.ps1'
text=check.read_text(encoding='utf-8-sig').replace("'Files-Panel.ps1',", "'Files-Panel.ps1', 'Modern-Theme.ps1',")
text=text.replace(". (Join-Path $PSScriptRoot 'Controller-Panel.ps1')", ". (Join-Path $PSScriptRoot 'Modern-Theme.ps1')\n. (Join-Path $PSScriptRoot 'Controller-Panel.ps1')")
check.write_text(text, encoding='utf-8-sig')
print('Launcher, controller and files page updated.')
