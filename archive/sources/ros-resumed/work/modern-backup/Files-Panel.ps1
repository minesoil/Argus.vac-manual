function ConvertTo-LabLinuxPath([string]$path) {
    $full = [IO.Path]::GetFullPath($path)
    if ($full -notmatch '^([A-Za-z]):\\(.*)$') { throw 'Expected a Windows drive path.' }
    '/mnt/' + $Matches[1].ToLowerInvariant() + '/' + $Matches[2].Replace('\','/')
}

function Get-LabLocations([string]$appRoot) {
    @(
        [pscustomobject]@{ Name='Launcher, guides and bundled files'; Path=(ConvertTo-LabLinuxPath $appRoot); Windows=$true }
        [pscustomobject]@{ Name='Live robot workspace - every file'; Path='/home/robot/vacuum_ws'; Windows=$false }
        [pscustomobject]@{ Name='Robot models, worlds and configuration'; Path='/home/robot/vacuum_ws/src'; Windows=$false }
        [pscustomobject]@{ Name='Robot tools and control scripts'; Path='/home/robot/vacuum_ws/tools'; Windows=$false }
        [pscustomobject]@{ Name='Saved maps'; Path='/home/robot/vacuum_ws/maps'; Windows=$false }
        [pscustomobject]@{ Name='Session logs and process state'; Path='/home/robot/vacuum_ws/.lab'; Windows=$false }
        [pscustomobject]@{ Name='Validation results and images'; Path='/home/robot/vacuum_ws/validation'; Windows=$false }
        [pscustomobject]@{ Name='Model rollback backups'; Path='/home/robot/vacuum_ws/model-backups'; Windows=$false }
        [pscustomobject]@{ Name='ROS 2 installed packages'; Path='/opt/ros/jazzy'; Windows=$false }
        [pscustomobject]@{ Name='Ubuntu filesystem'; Path='/'; Windows=$false }
        [pscustomobject]@{ Name='This project - Windows files'; Path='/mnt/c/Users/justi/Documents/Codex/2026-10-07/re'; Windows=$true }
        [pscustomobject]@{ Name='Original project and installation files'; Path='/mnt/c/Users/justi/Documents/Codex/2026-09-30/pl'; Windows=$true }
        [pscustomobject]@{ Name='Ubuntu disk and installation image'; Path='/mnt/e/WSL/VacuumRobot'; Windows=$true }
        [pscustomobject]@{ Name='Full Ubuntu backups'; Path='/mnt/f/VacuumRobotBackups'; Windows=$true }
    )
}

function Get-LabWindowsPath([string]$path, [bool]$windows) {
    if ($windows -and $path -match '^/mnt/([a-z])(?:/(.*))?$') {
        return $Matches[1].ToUpperInvariant() + ':\' + $Matches[2].Replace('/','\')
    }
    '\\wsl.localhost\VacuumRobot-24.04' + $path.Replace('/','\')
}

function Start-LabFileListing([string]$wslPath, [string]$appRoot, [string]$path, [string]$query) {
    $payload = [Convert]::ToBase64String([IO.File]::ReadAllBytes((Join-Path $appRoot 'file_catalog.py')))
    $request = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes((@{path=$path;query=$query} | ConvertTo-Json -Compress)))
    Start-Job -ArgumentList $wslPath,$payload,$request -ScriptBlock {
        param($wsl,$source,$request)
        $psi = New-Object Diagnostics.ProcessStartInfo
        $psi.FileName=$wsl; $psi.Arguments='-d VacuumRobot-24.04 -u robot --exec python3 -'
        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true
        $psi.RedirectStandardInput=$true; $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true
        $psi.StandardOutputEncoding=[Text.Encoding]::UTF8; $psi.StandardErrorEncoding=[Text.Encoding]::UTF8
        $proc=New-Object Diagnostics.Process; $proc.StartInfo=$psi
        try {
            [void]$proc.Start()
            $stdout=$proc.StandardOutput.ReadToEndAsync(); $stderr=$proc.StandardError.ReadToEndAsync()
            $proc.StandardInput.WriteLine("import base64, io, sys; sys.stdin=io.StringIO(base64.b64decode('$request').decode()); exec(compile(base64.b64decode('$source'), 'file_catalog.py', 'exec'))")
            $proc.StandardInput.Close()
            if (-not $proc.WaitForExit(60000)) { $proc.Kill(); throw 'File search timed out; choose a smaller folder.' }
            if (-not $stdout.Result.Trim()) { throw $stderr.Result }
            $stdout.Result
        } finally { $proc.Dispose() }
    }
}

function Show-LabFiles([string]$wslPath, [string]$appRoot, [string]$codePath, [switch]$CheckOnly, [string]$PreviewPath) {
    $filesForm=New-Object Windows.Forms.Form
    $filesForm.Text='Vacuum Lab - All project files'
    $filesForm.Size=New-Object Drawing.Size(1120,720)
    $filesForm.MinimumSize=New-Object Drawing.Size(1080,580)
    $filesForm.StartPosition='CenterParent'
    $filesForm.Font=New-Object Drawing.Font('Segoe UI',10)
    $layout=New-Object Windows.Forms.TableLayoutPanel
    $layout.Dock='Fill'; $layout.ColumnCount=1; $layout.RowCount=5; $layout.Padding=New-Object Windows.Forms.Padding(12)
    foreach ($height in @(44,44,44)) { [void]$layout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',$height))) }
    [void]$layout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Percent',100)))
    [void]$layout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',54)))
    $filesForm.Controls.Add($layout)
    $location=New-Object Windows.Forms.ComboBox; $location.Dock='Fill'; $location.DropDownStyle='DropDownList'; $location.DisplayMember='Name'
    foreach ($root in (Get-LabLocations $appRoot)) { [void]$location.Items.Add($root) }
    $layout.Controls.Add($location,0,0)
    $pathBox=New-Object Windows.Forms.TextBox; $pathBox.Dock='Fill'; $pathBox.ReadOnly=$true
    $layout.Controls.Add($pathBox,0,1)
    $toolbar=New-Object Windows.Forms.FlowLayoutPanel; $toolbar.Dock='Fill'; $toolbar.WrapContents=$false
    $queryBox=New-Object Windows.Forms.TextBox; $queryBox.Width=245
    $toolbar.Controls.Add($queryBox)
    $buttons=@{}
    foreach ($label in @('Search','Up','Refresh','Open','Show in Explorer','Copy path')) {
        $button=New-Object Windows.Forms.Button; $button.Text=$label; $button.AutoSize=$true
        $toolbar.Controls.Add($button); $buttons[$label]=$button
    }
    $layout.Controls.Add($toolbar,0,2)
    $listing=New-Object Windows.Forms.ListView
    $listing.Dock='Fill'; $listing.View='Details'; $listing.FullRowSelect=$true; $listing.MultiSelect=$false; $listing.HideSelection=$false
    [void]$listing.Columns.Add('Name',280); [void]$listing.Columns.Add('Type',85); [void]$listing.Columns.Add('Size',85); [void]$listing.Columns.Add('Path',550)
    $layout.Controls.Add($listing,0,3)
    $help=New-Object Windows.Forms.Label; $help.Dock='Fill'
    $help.Text='Choose a location. Search matches names throughout the current folder. Hidden files are included.'
    $layout.Controls.Add($help,0,4)
    $browseState=@{Job=$null; Path=''; Root=''; Windows=$false; Query=''; Pending=$null}
    $loadFolder={ param([string]$nextPath,[string]$search)
        if ($browseState.Job) { $browseState.Pending=@($nextPath,$search); $help.Text='Waiting for current listing...'; return }
        $browseState.Path=$nextPath; $browseState.Query=$search; $location.Enabled=$false
        $pathBox.Text=Get-LabWindowsPath $nextPath $browseState.Windows
        $listing.Items.Clear(); $help.Text='Loading files from Ubuntu...'
        $browseState.Job=Start-LabFileListing $wslPath $appRoot $nextPath $search
    }
    $navigate={
        if ($listing.SelectedItems.Count) {
            $item=$listing.SelectedItems[0].Tag
            if ($item.folder) { $queryBox.Clear(); & $loadFolder $item.path '' }
            else {
                try {
                    $visiblePath=Get-LabWindowsPath $item.path $browseState.Windows
                    if (-not $browseState.Windows -and (Test-Path -LiteralPath $codePath)) {
                        Start-Process -FilePath $codePath -ArgumentList ('--remote wsl+VacuumRobot-24.04 "'+$item.path+'"') -WindowStyle Hidden
                    } else { Start-Process -FilePath $visiblePath }
                } catch { [void][Windows.Forms.MessageBox]::Show($_.Exception.Message,'Could not open file') }
            }
        }
    }
    $location.Add_SelectedIndexChanged({
        $selected=$location.SelectedItem
        $browseState.Windows=$selected.Windows; $browseState.Root=$selected.Path
        $queryBox.Clear(); & $loadFolder $selected.Path ''
    })
    $buttons['Search'].Add_Click({ & $loadFolder $browseState.Path $queryBox.Text })
    $queryBox.Add_KeyDown({ if ($_.KeyCode -eq 'Enter') { $_.SuppressKeyPress=$true; & $loadFolder $browseState.Path $queryBox.Text } })
    $buttons['Refresh'].Add_Click({ & $loadFolder $browseState.Path $browseState.Query })
    $buttons['Up'].Add_Click({
        if ($browseState.Path -ne $browseState.Root) {
            $parent=$browseState.Path.TrimEnd('/') -replace '/[^/]+$',''
            if (-not $parent) { $parent='/' }
            $queryBox.Clear(); & $loadFolder $parent ''
        }
    })
    $listing.Add_DoubleClick($navigate); $buttons['Open'].Add_Click($navigate)
    $buttons['Copy path'].Add_Click({
        $selectedPath=if ($listing.SelectedItems.Count) { Get-LabWindowsPath $listing.SelectedItems[0].Tag.path $browseState.Windows } else { $pathBox.Text }
        if ($selectedPath) { [Windows.Forms.Clipboard]::SetText($selectedPath) }
    })
    $buttons['Show in Explorer'].Add_Click({
        try {
            if ($listing.SelectedItems.Count) {
                $selectedPath=Get-LabWindowsPath $listing.SelectedItems[0].Tag.path $browseState.Windows
                Start-Process explorer.exe -ArgumentList ('/select,"'+$selectedPath+'"')
            } elseif ($pathBox.Text) { Start-Process explorer.exe -ArgumentList ('"'+$pathBox.Text+'"') }
        } catch { [void][Windows.Forms.MessageBox]::Show($_.Exception.Message,'Explorer unavailable') }
    })
    $fileTimer=New-Object Windows.Forms.Timer; $fileTimer.Interval=250
    $fileTimer.Add_Tick({
        if (-not $browseState.Job -or $browseState.Job.State -notin @('Completed','Failed','Stopped')) { return }
        try {
            $received=Receive-Job $browseState.Job -ErrorAction Stop
            $data=($received -join '') | ConvertFrom-Json
            $listing.BeginUpdate()
            foreach ($entry in $data.entries) {
                $row=New-Object Windows.Forms.ListViewItem($entry.name)
                [void]$row.SubItems.Add($(if ($entry.folder) {'Folder'} elseif ($entry.link) {'Link'} else {'File'}))
                [void]$row.SubItems.Add($(if ($entry.folder) {''} else {$entry.size.ToString('N0')}))
                [void]$row.SubItems.Add((Get-LabWindowsPath $entry.path $browseState.Windows)); $row.Tag=$entry
                [void]$listing.Items.Add($row)
            }
            $help.Text="$($listing.Items.Count) items. Double-click a folder to browse or a file to open."
            if ($data.errors.Count) { $help.Text += " $($data.errors.Count) unavailable items: " + ($data.errors -join '; ') }
        } catch { $help.Text='Listing failed: '+$_.Exception.Message }
        finally {
            $listing.EndUpdate(); Remove-Job $browseState.Job -Force; $browseState.Job=$null; $location.Enabled=$true
            if ($browseState.Pending) { $next=$browseState.Pending; $browseState.Pending=$null; & $loadFolder $next[0] $next[1] }
        }
        if ($PreviewPath) {
            $bitmap=New-Object Drawing.Bitmap($filesForm.Width,$filesForm.Height)
            try {
                $filesForm.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$filesForm.Width,$filesForm.Height)))
                $bitmap.Save($PreviewPath,[Drawing.Imaging.ImageFormat]::Png)
            } finally { $bitmap.Dispose() }
            $filesForm.Close()
        }
    })
    if ($CheckOnly) {
        $filesForm.CreateControl(); $layout.PerformLayout()
        [pscustomobject]@{ Title=$filesForm.Text; Locations=$location.Items.Count; Columns=$listing.Columns.Count; Buttons=$buttons.Count }
        $fileTimer.Dispose(); $filesForm.Dispose(); return
    }
    $filesForm.Add_Shown({ $location.SelectedIndex=0 })
    $fileTimer.Start()
    try { [void]$filesForm.ShowDialog() }
    finally {
        $fileTimer.Stop(); $fileTimer.Dispose()
        if ($browseState.Job) { Stop-Job $browseState.Job; Remove-Job $browseState.Job -Force }
        $filesForm.Dispose()
    }
}
