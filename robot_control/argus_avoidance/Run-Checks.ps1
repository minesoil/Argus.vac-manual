param([string]$PythonPath)
$ErrorActionPreference = 'Stop'

if (-not $PythonPath) {
    $bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
    if (Test-Path -LiteralPath $bundledPython) {
        $PythonPath = $bundledPython
    } else {
        $existingPython = Get-Command python -ErrorAction SilentlyContinue
        if ($existingPython -and $existingPython.Source -notlike '*WindowsApps*') {
            $PythonPath = $existingPython.Source
        } else {
            throw 'Supply an existing Python 3.10+ interpreter with -PythonPath. No installation is performed.'
        }
    }
}

Push-Location -LiteralPath $PSScriptRoot
try {
    & $PythonPath -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { throw 'Verification failed; see test results above.' }
    & $PythonPath -m argus_avoidance.simulate --output reports/standalone-simulation.json
    if ($LASTEXITCODE -ne 0) { throw 'A standalone simulation scenario failed.' }
} finally {
    Pop-Location
}
