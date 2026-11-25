#Requires -Version 5.1
# PERSONAL / OFFLINE ONLY — builds a drop-in folder from YOUR game copy.
# Do NOT upload the resulting update.rpf / update2.rpf to GitHub Releases or public mirrors
# (those archives contain Rockstar copyrighted data). See LEGAL.md.
param(
  [string]$GameRoot = "",
  [string]$Python = ""
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

Write-Host "WARNING: Output RPFs are for your own machine. Do not publish them. (LEGAL.md)" -ForegroundColor Yellow

if (-not $GameRoot) {
  throw "Pass -GameRoot to your Grand Theft Auto V Enhanced folder"
}
if (Get-Process -Name GTA5_Enhanced, GTA5, PlayGTAV -EA SilentlyContinue) {
  throw "Close GTA first"
}
if (-not $Python) {
  $Python = "python"
}

& $Python -m pip install -r requirements.txt -q
& $Python tools/build.py --game $GameRoot --install
if ($LASTEXITCODE -ne 0) { throw "build/install failed" }

$out = Join-Path $Root "release\PERSONAL_DROP_IN_DO_NOT_UPLOAD"
$modsOut = Join-Path $out "mods\update"
New-Item -ItemType Directory -Force -Path $modsOut | Out-Null
Copy-Item -Force (Join-Path $GameRoot "mods\update\update.rpf") $modsOut
Copy-Item -Force (Join-Path $GameRoot "mods\update\update2.rpf") $modsOut
Copy-Item -Force (Join-Path $Root "LEGAL.md") (Join-Path $out "READ_LEGAL_BEFORE_SHARING.txt")

Write-Host "Personal folder (DO NOT upload RPFs): $out"
Write-Host "Get ASI loaders from upstream links in THIRD_PARTY.md"
