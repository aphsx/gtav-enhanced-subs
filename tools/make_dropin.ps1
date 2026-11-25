#Requires -Version 5.1
# Build DROP_IN zip for GitHub Releases (normal-mod UX).
# WARNING: output contains modified Rockstar archives — see LEGAL.md
param(
  [Parameter(Mandatory = $true)][string]$GameRoot,
  [string]$Python = "python"
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

if (Get-Process -Name GTA5_Enhanced, GTA5, PlayGTAV -EA SilentlyContinue) {
  throw "Close GTA first"
}
$gfx = Join-Path $Root "assets\font_lib_efigs_pc.gfx"
if (-not (Test-Path $gfx)) {
  $alt = Join-Path $Root "work\font_rebuild\font_lib_efigs_pc_SARABUN.gfx"
  if (Test-Path $alt) { Copy-Item -Force $alt $gfx } else { throw "Missing Thai font gfx at $gfx" }
}

& $Python tools/build.py --game $GameRoot --install
if ($LASTEXITCODE -ne 0) { throw "build/install failed" }

$out = Join-Path $Root "release\GTA_V_Thai_Subs_DROP_IN"
$modsOut = Join-Path $out "mods\update"
New-Item -ItemType Directory -Force -Path $modsOut | Out-Null

foreach ($name in @("OpenRPF.asi", "xinput1_4.dll", "args.txt")) {
  $src = Join-Path $GameRoot $name
  if (-not (Test-Path $src)) { throw "Missing in game folder: $name (install loader once, then re-run)" }
  Copy-Item -Force $src $out
}
Copy-Item -Force (Join-Path $GameRoot "mods\update\update.rpf") $modsOut
Copy-Item -Force (Join-Path $GameRoot "mods\update\update2.rpf") $modsOut
@"
GTA V Enhanced — Thai Subs DROP_IN

1. Close the game
2. Merge this folder into Grand Theft Auto V Enhanced
3. Language = American / English
4. Play Single Player

Unofficial fan mod. Own the game.
"@ | Set-Content (Join-Path $out "README.txt") -Encoding UTF8

$zip = Join-Path $Root "release\GTA_V_Thai_Subs_DROP_IN.zip"
$seven = @(
  "${env:ProgramFiles}\7-Zip\7z.exe",
  "${env:ProgramFiles(x86)}\7-Zip\7z.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $seven) { throw "Install 7-Zip to create the zip" }
if (Test-Path $zip) { Remove-Item $zip -Force }
& $seven a -tzip -mx=1 $zip "$out\*" | Out-Host
Write-Host "Release zip: $zip"
Write-Host "Upload this file to GitHub Releases."
