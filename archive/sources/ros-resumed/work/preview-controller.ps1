$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[Windows.Forms.Application]::EnableVisualStyles()
$appRoot=Join-Path (Split-Path $PSScriptRoot) 'outputs'
. (Join-Path $appRoot 'Modern-Theme.ps1')
. (Join-Path $appRoot 'Controller-Panel.ps1')
Show-ControllerPanel '' $appRoot -CheckOnly -PreviewPath (Join-Path $PSScriptRoot 'modern-controller.png') | Format-List
