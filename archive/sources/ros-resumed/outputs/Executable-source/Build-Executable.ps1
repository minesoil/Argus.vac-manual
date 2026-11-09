param([string]$OutputRoot=(Split-Path $PSScriptRoot), [string]$BuildRoot)
$ErrorActionPreference='Stop'
if (-not $BuildRoot) { $BuildRoot=Join-Path (Split-Path $OutputRoot) 'work\executable-build' }
[void][IO.Directory]::CreateDirectory($BuildRoot)
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$bundlePath=Join-Path $BuildRoot 'payload.zip'
$stream=[IO.File]::Open($bundlePath,[IO.FileMode]::Create)
$zip=New-Object IO.Compression.ZipArchive($stream,[IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($file in (Get-ChildItem -LiteralPath $OutputRoot -File -Recurse -Force | Sort-Object FullName)) {
        if ($file.Extension -eq '.exe' -or $file.FullName -match '\\__pycache__\\' -or $file.Name -eq 'executable-verification.json' -or $file.Name -eq 'controller-bridge-last.log') { continue }
        $relative=$file.FullName.Substring($OutputRoot.TrimEnd('\').Length+1).Replace('\','/')
        [void][IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip,$file.FullName,$relative,[IO.Compression.CompressionLevel]::Optimal)
    }
} finally { $zip.Dispose(); $stream.Dispose() }
$compiler=Join-Path $env:WINDIR 'Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$binary=Join-Path $OutputRoot 'Vacuum Lab.exe'
& $compiler /nologo /target:winexe /platform:x64 /optimize+ "/out:$binary" "/win32icon:$(Join-Path $OutputRoot 'Vacuum-Lab.ico')" /reference:System.Windows.Forms.dll /reference:System.IO.Compression.dll /reference:System.IO.Compression.FileSystem.dll "/resource:$bundlePath,VacuumLab.Payload" (Join-Path $PSScriptRoot 'Launcher.cs')
if ($LASTEXITCODE -ne 0) { throw 'Executable compilation failed.' }
Get-Item -LiteralPath $binary | Select-Object FullName,Length
Get-FileHash -LiteralPath $binary -Algorithm SHA256
