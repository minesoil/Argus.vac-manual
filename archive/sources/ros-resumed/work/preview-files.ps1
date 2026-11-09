$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[Windows.Forms.Application]::EnableVisualStyles()
$appRoot=Join-Path (Split-Path $PSScriptRoot) 'outputs'
. (Join-Path $appRoot 'Modern-Theme.ps1')
. (Join-Path $appRoot 'Files-Panel.ps1')
Show-LabFiles 'C:\Program Files\WSL\wsl.exe' $appRoot '' -PreviewPath (Join-Path $PSScriptRoot 'files-preview.png')
