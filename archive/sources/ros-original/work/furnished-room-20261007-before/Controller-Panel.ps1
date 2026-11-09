# Built-in Windows joystick reader: no USB forwarding, drivers, or Python install.
Add-Type -TypeDefinition @'
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public static class VacuumJoystick {
    [StructLayout(LayoutKind.Sequential, CharSet=CharSet.Unicode)]
    public struct Caps {
        public ushort Mid, Pid;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst=32)] public string Name;
        public uint Xmin,Xmax,Ymin,Ymax,Zmin,Zmax,Buttons,PeriodMin,PeriodMax;
        public uint Rmin,Rmax,Umin,Umax,Vmin,Vmax,Flags,MaxAxes,Axes,MaxButtons;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst=32)] public string RegKey;
        [MarshalAs(UnmanagedType.ByValTStr, SizeConst=260)] public string Oem;
    }
    [StructLayout(LayoutKind.Sequential)]
    public struct Pos {
        public uint Size,Flags,X,Y,Z,R,U,V,Buttons,ButtonNumber,Pov,Reserved1,Reserved2;
    }
    public class Device {
        public uint Id; public Caps Info; public string DisplayName;
        public override string ToString() { return DisplayName + " (" + Info.Axes + " axes, " + Info.Buttons + " buttons)"; }
    }
    [DllImport("winmm.dll", EntryPoint="joyGetDevCapsW", CharSet=CharSet.Unicode)]
    static extern uint GetCaps(UIntPtr id, out Caps caps, uint size);
    [DllImport("winmm.dll", EntryPoint="joyGetPosEx")]
    static extern uint GetPos(uint id, ref Pos pos);
    public static Device[] Devices() {
        var result = new List<Device>();
        for(uint id=0;id<16;id++) {
            Caps caps; Pos pos = new Pos {Size=52,Flags=255};
            if(GetCaps(new UIntPtr(id),out caps,(uint)Marshal.SizeOf(typeof(Caps)))==0 && GetPos(id,ref pos)==0) {
                string name=caps.Name;
                string key="System\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM\\VID_"+
                           caps.Mid.ToString("X4")+"&PID_"+caps.Pid.ToString("X4");
                foreach(var hive in new[] {Microsoft.Win32.Registry.CurrentUser,Microsoft.Win32.Registry.LocalMachine}) {
                    using(var entry=hive.OpenSubKey(key)) {
                        var friendly=entry==null ? null : entry.GetValue("OEMName") as string;
                        if(!String.IsNullOrEmpty(friendly)) { name=friendly; break; }
                    }
                }
                result.Add(new Device {Id=id,Info=caps,DisplayName=name});
            }
        }
        return result.ToArray();
    }
    public static double[] Read(Device device, out uint buttons) {
        Caps caps; Pos pos = new Pos {Size=52,Flags=255};
        if(GetCaps(new UIntPtr(device.Id),out caps,(uint)Marshal.SizeOf(typeof(Caps)))!=0 ||
           caps.Mid!=device.Info.Mid || caps.Pid!=device.Info.Pid || caps.Name!=device.Info.Name ||
           GetPos(device.Id,ref pos)!=0) throw new Exception("Controller disconnected or changed.");
        uint[] raw={pos.X,pos.Y,pos.Z,pos.R,pos.U,pos.V};
        uint[] min={caps.Xmin,caps.Ymin,caps.Zmin,caps.Rmin,caps.Umin,caps.Vmin};
        uint[] max={caps.Xmax,caps.Ymax,caps.Zmax,caps.Rmax,caps.Umax,caps.Vmax};
        var axes=new double[6];
        for(int i=0;i<6;i++) axes[i]=max[i]>min[i] ? Math.Max(-1,Math.Min(1,2.0*(raw[i]- (double)min[i])/(max[i]-min[i])-1)) : 0;
        buttons=pos.Buttons; return axes;
    }
    public static bool Supports(Device device, int axis) {
        return axis>=0 && axis<6 && (axis<2 || (device.Info.Flags & (1u << (axis-2)))!=0);
    }
    // Read Ubuntu status off the UI thread; a delayed read cannot freeze input.
    public class OutputPump {
        private readonly object gate = new object();
        private string latest = "", log = "";
        public System.Threading.Tasks.Task Completion;
        public OutputPump(System.IO.StreamReader reader) {
            Completion = System.Threading.Tasks.Task.Run(() => {
                string line;
                while ((line = reader.ReadLine()) != null) {
                    lock (gate) {
                        if (line.StartsWith("{")) latest = line;
                        log += line + "\n";
                        if (log.Length > 8192) log = log.Substring(log.Length - 8192);
                    }
                }
            });
        }
        public string Latest { get { lock (gate) return latest; } }
        public string Log { get { lock (gate) return log; } }
    }
}
'@

function Show-ControllerPanel([string]$wslPath, [string]$profileRoot, [switch]$CheckOnly) {
    $panel = New-Object Windows.Forms.Form
    $panel.Text = 'Drive robot — push forward / pull reverse'
    $panel.Size = New-Object Drawing.Size(650, 790)
    $panel.StartPosition = 'CenterParent'
    $panel.FormBorderStyle = 'FixedDialog'
    $panel.MaximizeBox = $false
    $panel.Font = New-Object Drawing.Font('Segoe UI', 10)
    $state = @{ Armed=$false; Process=$null; Pump=$null; Centers=@(0.,0.,0.,0.,0.,0.); Axes=$null; Buttons=[uint32]0; Device=$null }

    function Label-At($text,$y) {
        $label = New-Object Windows.Forms.Label
        $label.Text=$text; $label.SetBounds(20,$y,595,30); $panel.Controls.Add($label)
        return $label
    }
    $null = Label-At 'Push forward. Pull back to reverse. Turn the yoke to steer.' 16
    $device = New-Object Windows.Forms.ComboBox
    $device.DropDownStyle='DropDownList'; $device.SetBounds(20,50,590,30)
    $panel.Controls.Add($device)
    foreach ($item in [VacuumJoystick]::Devices()) { [void]$device.Items.Add($item) }
    if ($device.Items.Count) { $device.SelectedIndex=0 }
    for ($i=0;$i -lt $device.Items.Count;$i++) {
        if ($device.Items[$i].DisplayName -match 'Honeycomb|Alpha') { $device.SelectedIndex=$i; break }
    }
    $live = Label-At 'Connect a controller before opening this panel.' 94
    $live.Height=52
    $null = Label-At 'Speed axis                     Steering axis                      Dead zone (%)' 156
    $speed = New-Object Windows.Forms.ComboBox
    $steer = New-Object Windows.Forms.ComboBox
    foreach ($box in @($speed,$steer)) {
        $box.DropDownStyle='DropDownList'; $box.Items.AddRange(@('X','Y','Z','R','U','V')); $panel.Controls.Add($box)
    }
    $speed.SetBounds(20,186,170,30); $speed.SelectedIndex=1
    $steer.SetBounds(220,186,170,30); $steer.SelectedIndex=0
    $dead = New-Object Windows.Forms.NumericUpDown
    $dead.Minimum=5; $dead.Maximum=40; $dead.Value=10; $dead.SetBounds(420,186,160,30)
    $panel.Controls.Add($dead)
    $invertSpeed = New-Object Windows.Forms.CheckBox
    $invertSpeed.Text='Invert speed'; $invertSpeed.Checked=$true; $invertSpeed.SetBounds(20,224,170,30)
    $invertSteer = New-Object Windows.Forms.CheckBox
    $invertSteer.Text='Invert steering'; $invertSteer.Checked=$true; $invertSteer.SetBounds(220,224,190,30)
    $panel.Controls.AddRange(@($invertSpeed,$invertSteer))
    $null = Label-At 'Hold-to-drive button          Stop button (latched)' 268
    $hold = New-Object Windows.Forms.NumericUpDown
    $stop = New-Object Windows.Forms.NumericUpDown
    foreach ($box in @($hold,$stop)) { $box.Minimum=1; $box.Maximum=32; $panel.Controls.Add($box) }
    $hold.SetBounds(20,298,170,30); $hold.Value=1
    $stop.SetBounds(220,298,170,30); $stop.Value=3
    $message = Label-At 'Center the yoke, Arm drive, then hold your drive button to move.' 344
    $message.Height=48
    $arm = New-Object Windows.Forms.Button
    $arm.Text='Arm drive'; $arm.SetBounds(20,405,175,42)
    $disarm = New-Object Windows.Forms.Button
    $disarm.Text='STOP / disarm'; $disarm.SetBounds(220,405,175,42)
    $center = New-Object Windows.Forms.Button
    $center.Text='Set neutral center'; $center.SetBounds(420,405,190,42)
    $panel.Controls.AddRange(@($arm,$disarm,$center))
    $save = New-Object Windows.Forms.Button
    $save.Text='Save custom profile'; $save.SetBounds(20,465,175,42)
    $load = New-Object Windows.Forms.Button
    $load.Text='Load custom profile'; $load.SetBounds(220,465,175,42)
    $preset = New-Object Windows.Forms.Button
    $preset.Text='Honeycomb Alpha'; $preset.SetBounds(420,465,190,42)
    $panel.Controls.AddRange(@($save,$load,$preset))
    $pull = New-Object Windows.Forms.Button
    $pull.Text='Set pull = reverse'; $pull.SetBounds(20,520,175,36)
    $panel.Controls.Add($pull)
    $pullHint = Label-At 'Pull the yoke fully back, then click Set pull = reverse.' 523
    $pullHint.SetBounds(220,523,390,42)
    $null = Label-At 'Preview: push must produce + speed; pulling must produce − speed.' 569
    $background = New-Object Windows.Forms.CheckBox
    $background.Text='Keep drive armed when switching windows (hold button required)'
    $background.Checked=$true; $background.SetBounds(20,606,595,30)
    $panel.Controls.Add($background)
    $guardStatus = Label-At 'Ubuntu guard: connecting...' 643
    $guardStatus.Height=48
    $footer = Label-At 'Drive stops on release, STOP, disconnect, or stale input.' 697
    $footer.Height=55
    $footer.Text += "`r`nSpeed cap: +0.50 / −0.30 m/s. Turn cap: 1.2 rad/s."

    function Send-Drive($v,$w,$held) {
        if ($state.Process -and -not $state.Process.HasExited) {
            $packet = @{v=[double]$v;w=[double]$w;held=[bool]$held} | ConvertTo-Json -Compress
            try {
                $state.Process.StandardInput.WriteLine($packet)
                $state.Process.StandardInput.Flush()
            } catch {
                $state.Armed=$false
                $message.Text='Stopped: Ubuntu input connection was lost.'
            }
        }
    }
    function Disarm-Drive {
        $state.Armed=$false
        Send-Drive 0 0 $false
        $arm.Text='Arm drive'
    }
    function Axis-Value($index,$invert) {
        $value = [Math]::Max(-1,[Math]::Min(1,$state.Axes[$index]-$state.Centers[$index]))
        $zone = [double]$dead.Value / 100
        if ([Math]::Abs($value) -le $zone) { return 0. }
        $value = [Math]::Sign($value) * ([Math]::Abs($value)-$zone)/(1-$zone)
        if ($invert) { $value = -$value }
        return $value
    }
    $device.Add_SelectedIndexChanged({ Disarm-Drive; $state.Centers=@(0.,0.,0.,0.,0.,0.) })
    foreach ($box in @($speed,$steer)) { $box.Add_SelectedIndexChanged({ Disarm-Drive }) }
    foreach ($box in @($hold,$stop,$dead)) { $box.Add_ValueChanged({ Disarm-Drive }) }
    foreach ($box in @($invertSpeed,$invertSteer)) { $box.Add_CheckedChanged({ Disarm-Drive }) }
    $disarm.Add_Click({ Disarm-Drive; $message.Text='Stopped. Center the yoke and release buttons before arming again.' })
    $center.Add_Click({
        Disarm-Drive
        if ($state.Axes) { $state.Centers = @($state.Axes); $message.Text='Neutral center saved for this session. Check your preview values.' }
    })
    $arm.Add_Click({
        if (-not $state.Axes -or -not $state.Process -or $state.Process.HasExited) { $message.Text='Controller or Ubuntu input bridge unavailable.'; return }
        if ($hold.Value -eq $stop.Value -or $speed.SelectedIndex -eq $steer.SelectedIndex) { $message.Text='Choose distinct axes and distinct hold/stop buttons.'; return }
        if (-not [VacuumJoystick]::Supports($device.SelectedItem,$speed.SelectedIndex) -or -not [VacuumJoystick]::Supports($device.SelectedItem,$steer.SelectedIndex)) { $message.Text='Choose axes supported by this controller.'; return }
        if ($hold.Value -gt $device.SelectedItem.Info.Buttons -or $stop.Value -gt $device.SelectedItem.Info.Buttons) { $message.Text='Choose buttons that exist on this controller.'; return }
        $driveMask = ([uint64]1 -shl ([int]$hold.Value-1)) -bor ([uint64]1 -shl ([int]$stop.Value-1))
        if ((Axis-Value $speed.SelectedIndex $false) -ne 0 -or (Axis-Value $steer.SelectedIndex $false) -ne 0 -or ([uint64]$state.Buttons -band $driveMask) -ne 0) {
            $message.Text='Center the selected axes and release the hold/stop buttons before arming.'; return
        }
        $state.Armed=$true; $arm.Text='Drive armed'
        $message.Text='Hold the bound drive button to move. Release to stop.'
    })
    $preset.Add_Click({
        Disarm-Drive; $speed.SelectedIndex=1; $steer.SelectedIndex=0
        $invertSpeed.Checked=$true; $invertSteer.Checked=$true; $hold.Value=1; $stop.Value=3; $dead.Value=10
        $state.Centers=@(0.,0.,0.,0.,0.,0.)
        $message.Text='Alpha starting profile loaded. Verify live axes/buttons; actual numbering may vary.'
    })
    $pull.Add_Click({
        Disarm-Drive
        if (-not $state.Axes) { $message.Text='Connect a controller first.'; return }
        $raw = $state.Axes[$speed.SelectedIndex] - $state.Centers[$speed.SelectedIndex]
        if ([Math]::Abs($raw) -lt .3) { $message.Text='Pull the yoke further back, then click Set pull = reverse.'; return }
        $invertSpeed.Checked = $raw -gt 0
        $message.Text='Pulling is now reverse. Return to neutral before arming.'
    })
    $save.Add_Click({
        Disarm-Drive
        if (-not $device.SelectedItem) { return }
        $dialog = New-Object Windows.Forms.SaveFileDialog
        $dialog.Filter='Controller profile (*.json)|*.json'; $dialog.InitialDirectory=$profileRoot; $dialog.FileName='my-controller.json'
        if ($dialog.ShowDialog() -eq 'OK') {
            @{ version=1; device=$device.SelectedItem.DisplayName; speed=$speed.SelectedIndex; steering=$steer.SelectedIndex;
               invertSpeed=$invertSpeed.Checked; invertSteering=$invertSteer.Checked; hold=[int]$hold.Value;
               stop=[int]$stop.Value; deadZone=[int]$dead.Value; centers=@($state.Centers) } |
                ConvertTo-Json | Set-Content -LiteralPath $dialog.FileName -Encoding UTF8
            $message.Text='Custom bindings saved.'
        }
        $dialog.Dispose()
    })
    $load.Add_Click({
        Disarm-Drive
        $dialog=New-Object Windows.Forms.OpenFileDialog
        $dialog.Filter='Controller profile (*.json)|*.json'; $dialog.InitialDirectory=$profileRoot
        if ($dialog.ShowDialog() -eq 'OK') {
            try {
                $p = Get-Content -LiteralPath $dialog.FileName -Raw | ConvertFrom-Json
                if ($p.version -ne 1 -or $p.speed -notin 0..5 -or $p.steering -notin 0..5 -or
                    $p.hold -notin 1..32 -or $p.stop -notin 1..32 -or $p.deadZone -notin 5..40 -or
                    $p.centers.Count -ne 6 -or $p.invertSpeed -isnot [bool] -or $p.invertSteering -isnot [bool]) { throw 'Invalid profile values.' }
                foreach ($value in $p.centers) { if ($value -isnot [ValueType] -or [double]::IsNaN($value) -or [Math]::Abs($value) -gt 1) { throw 'Invalid center.' } }
                $speed.SelectedIndex=$p.speed; $steer.SelectedIndex=$p.steering; $hold.Value=$p.hold; $stop.Value=$p.stop
                $dead.Value=$p.deadZone; $invertSpeed.Checked=$p.invertSpeed; $invertSteer.Checked=$p.invertSteering
                $state.Centers=@($p.centers)
                $message.Text="Loaded bindings for $($p.device). Verify them on the selected controller."
            } catch { $message.Text="Could not load profile: $_" }
        }
        $dialog.Dispose()
    })
    $background.Add_CheckedChanged({ Disarm-Drive; $message.Text='Focus behavior changed. Center and re-arm to drive.' })
    $panel.Add_Deactivate({
        if (-not $background.Checked) {
            Disarm-Drive; $message.Text='Disarmed: panel lost focus. Re-arm or enable switching windows.'
        }
    })
    $timer = New-Object Windows.Forms.Timer
    $timer.Interval=50
    $timer.Add_Tick({
        try {
            if (-not $device.SelectedItem) { Send-Drive 0 0 $false; return }
            [uint32]$bits=0
            $state.Axes=[VacuumJoystick]::Read($device.SelectedItem,[ref]$bits)
            $state.Buttons=$bits
            $axesText = for ($i=0;$i -lt 6;$i++) { '{0}: {1:F2}' -f @('X','Y','Z','R','U','V')[$i],$state.Axes[$i] }
            $pressed = for ($i=0;$i -lt 32;$i++) { if (([uint64]$bits -band ([uint64]1 -shl $i)) -ne 0) { $i+1 } }
            $live.Text = ($axesText -join '   ') + "`r`nPressed buttons: " + ($pressed -join ', ')
            $preview = Axis-Value $speed.SelectedIndex $invertSpeed.Checked
            $previewSpeed = $preview * $(if ($preview -ge 0) { .50 } else { .30 })
            $live.Text += ('   Speed: {0:+0.000;-0.000;0.000} m/s' -f $previewSpeed)
            if (-not $background.Checked -and -not $panel.ContainsFocus) { Disarm-Drive }
            if (([uint64]$bits -band ([uint64]1 -shl ([int]$stop.Value-1))) -ne 0) {
                Disarm-Drive; $message.Text='STOP button is pressed. Release it, center the yoke, then re-arm.'
            }
            $held = $state.Armed -and (([uint64]$bits -band ([uint64]1 -shl ([int]$hold.Value-1))) -ne 0)
            $v=0.; $w=0.
            if ($held) {
                $a=Axis-Value $speed.SelectedIndex $invertSpeed.Checked
                $v=$a * $(if ($a -ge 0) { .50 } else { .30 })
                $w=(Axis-Value $steer.SelectedIndex $invertSteer.Checked) * 1.2
            }
            Send-Drive $v $w $held
            if ($state.Armed) {
                if (-not $held) { $message.Text="Armed. Hold button $($hold.Value) to drive (see live pressed buttons above)." }
                elseif ([Math]::Abs($v) + [Math]::Abs($w) -lt .001) { $message.Text='Drive button held. Move the selected axes beyond the dead zone.' }
                else { $message.Text='Drive button held. Release to stop, or press STOP to disarm.' }
            }
            if ($state.Pump -and $state.Pump.Latest) {
                $health = $state.Pump.Latest | ConvertFrom-Json
                $guardStatus.Text = 'Ubuntu guard: ' + $health.reason + "`r`n" +
                    ('Guard output: {0:+0.00;-0.00;0.00} m/s, turn {1:0.00} rad/s' -f $health.output_v,$health.output_w)
                $guardStatus.ForeColor = $(if (-not $health.ready -or $health.reason -match 'stop|blocks|missing|stale') { [Drawing.Color]::Firebrick } else { [Drawing.Color]::DarkGreen })
            }
            if ($state.Process.HasExited) { throw 'Ubuntu controller bridge stopped; close this panel and check lab logs.' }
        } catch {
            $state.Armed=$false; $arm.Text='Arm drive'; $message.Text="Stopped: $_"
            try { Send-Drive 0 0 $false } catch { }
        }
    })
    if ($CheckOnly) {
        $state.Axes=@(0.,1.,0.,0.,0.,0.)
        $pullSpeed=(Axis-Value $speed.SelectedIndex $invertSpeed.Checked) * .30
        $state.Axes=@(0.,-1.,0.,0.,0.,0.)
        $pushSpeed=(Axis-Value $speed.SelectedIndex $invertSpeed.Checked) * .50
        if ($pullSpeed -ge 0 -or $pushSpeed -le 0) { throw 'Alpha profile does not map both speed directions.' }
        [pscustomobject]@{ Controls=$panel.Controls.Count; SelectedDevice=[string]$device.SelectedItem;
            SpeedAxis=$speed.SelectedItem; SteeringAxis=$steer.SelectedItem; Armed=$state.Armed;
            PullSpeed=$pullSpeed; PushSpeed=$pushSpeed }
        $timer.Dispose(); $panel.Dispose()
        return
    }
    try {
        $psi=New-Object Diagnostics.ProcessStartInfo
        $psi.FileName=$wslPath
        $psi.Arguments='-d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec /bin/bash -lc "source env.sh; exec python3 tools/controller_bridge.py"'
        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true; $psi.RedirectStandardInput=$true
        $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true
        $state.Process=New-Object Diagnostics.Process
        $state.Process.StartInfo=$psi
        [void]$state.Process.Start()
        $state.Pump=New-Object VacuumJoystick+OutputPump($state.Process.StandardOutput)
        $bridgeErr=$state.Process.StandardError.ReadToEndAsync()
        $timer.Start()
        [void]$panel.ShowDialog()
    } finally {
        $timer.Stop(); $timer.Dispose()
        if ($state.Process) {
            try { Disarm-Drive; $state.Process.StandardInput.Close(); [void]$state.Process.WaitForExit(3000) } catch { }
            if ($state.Process.HasExited) {
                [void]$state.Pump.Completion.Wait(500)
                ($state.Pump.Log + $bridgeErr.Result) | Set-Content (Join-Path $profileRoot 'controller-bridge-last.log')
            }
            # Never terminate WSL service or unrelated Linux jobs. EOF ends the bridge;
            # if it stalls, its monotonic input watchdog emits zero within 300 ms.
            $state.Process.Dispose()
        }
        $panel.Dispose()
    }
}
