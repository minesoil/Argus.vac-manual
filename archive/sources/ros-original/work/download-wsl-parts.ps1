$ErrorActionPreference = 'Stop'
$taskRoot = '[REDACTED_HOME_PATH]
$partRoot = Join-Path $taskRoot 'work\wsl-download-parts'
$installer = Join-Path $taskRoot 'work\wsl.3.0.1.0.x64.msi'
$url = 'https://github.com/microsoft/WSL/releases/download/3.0.1/wsl.3.0.1.0.x64.msi'
$totalBytes = 367669248L
$partBytes = 8MB
New-Item -ItemType Directory -Path $partRoot -Force | Out-Null
$count = [int][math]::Ceiling($totalBytes / $partBytes)
$config = [Collections.Generic.List[string]]::new()
for ($i = 0; $i -lt $count; $i++) {
    $start = [long]$i * $partBytes
    $end = [math]::Min($totalBytes - 1, $start + $partBytes - 1)
    $partPath = (Join-Path $partRoot ('part-{0:d3}.bin' -f $i)).Replace('\','/')
    if ($i -gt 0) { $config.Add('next') }
    $config.Add('url = "' + $url + '"')
    $config.Add('output = "' + $partPath + '"')
    $config.Add('range = "' + $start + '-' + $end + '"')
    $config.Add('location')
    $config.Add('fail')
    $config.Add('silent')
    $config.Add('show-error')
    $config.Add('proto = "=https"')
    $config.Add('tlsv1.2')
    $config.Add('retry = 3')
    $config.Add('retry-delay = 2')
    $config.Add('connect-timeout = 20')
    $config.Add('max-time = 600')
    $config.Add('write-out = "part %{urlnum}: HTTP %{http_code}, %{size_download} bytes\n"')
}
$configPath = Join-Path $partRoot 'download.curlrc'
[IO.File]::WriteAllLines($configPath, $config, [Text.UTF8Encoding]::new($false))
& curl.exe --parallel --parallel-immediate --parallel-max 8 --config $configPath
if ($LASTEXITCODE -ne 0) { throw "Chunk download failed: $LASTEXITCODE" }
for ($i = 0; $i -lt $count; $i++) {
    $partPath = Join-Path $partRoot ('part-{0:d3}.bin' -f $i)
    $expected = [math]::Min($partBytes, $totalBytes - [long]$i * $partBytes)
    if ((Get-Item -LiteralPath $partPath).Length -ne $expected) { throw "Incorrect length for $partPath" }
}
$output = [IO.File]::Create($installer)
try {
    for ($i = 0; $i -lt $count; $i++) {
        $inputPart = [IO.File]::OpenRead((Join-Path $partRoot ('part-{0:d3}.bin' -f $i)))
        try { $inputPart.CopyTo($output) } finally { $inputPart.Dispose() }
    }
} finally { $output.Dispose() }
$hash = (Get-FileHash -LiteralPath $installer -Algorithm SHA256).Hash.ToLowerInvariant()
if ($hash -ne '28b1a0d013640a2ac95898ea705fa186e5b4ff767a1c1b49257161bc106599c6') { throw 'WSL installer SHA256 mismatch.' }
$signature = Get-AuthenticodeSignature -LiteralPath $installer
if ($signature.Status -ne 'Valid' -or $signature.SignerCertificate.Subject -notmatch 'O=Microsoft Corporation') { throw 'Invalid Microsoft signature.' }
[pscustomobject]@{Installer=$installer; SHA256=$hash; SignatureStatus=$signature.Status.ToString(); Signer=$signature.SignerCertificate.Subject} | ConvertTo-Json | Tee-Object -FilePath (Join-Path $taskRoot 'work\wsl-installer-verification.json')
