#Requires -Version 5.1
# Build + install from this repo (uses YOUR game copy). Close GTA first.
param(
  [string]$GameRoot = "",
  [string]$Python = "python"
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (Get-Process -Name GTA5_Enhanced, GTA5, PlayGTAV -EA SilentlyContinue) {
  throw "Close GTA first"
}

& $Python -m pip install -r requirements.txt -q
$args = @("tools/build.py", "--install")
if ($GameRoot) { $args += @("--game", $GameRoot) }
& $Python @args
if ($LASTEXITCODE -ne 0) { throw "build failed" }
Write-Host "OK — launch game, language = American/English"
