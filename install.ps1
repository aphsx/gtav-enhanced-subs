#Requires -Version 5.1
# Build + install from this repo into YOUR game copy. Close GTA first.
# Requires: Python, rpfpeek, keys for your own game. See LEGAL.md / THIRD_PARTY.md.
param(
  [Parameter(Mandatory = $true)][string]$GameRoot,
  [string]$Python = "python"
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (Get-Process -Name GTA5_Enhanced, GTA5, PlayGTAV -EA SilentlyContinue) {
  throw "Close GTA first"
}

& $Python -m pip install -r requirements.txt -q
& $Python tools/build.py --game $GameRoot --install
if ($LASTEXITCODE -ne 0) { throw "build failed" }
Write-Host "OK — install a mods loader yourself (THIRD_PARTY.md). Language = American/English."
