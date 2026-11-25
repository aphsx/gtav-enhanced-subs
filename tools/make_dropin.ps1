#Requires -Version 5.1
# Build install into game, then copy a normal "drop into game folder" pack + zip.
param(
  [string]$GameRoot = "D:\SteamLibrary\steamapps\common\Grand Theft Auto V Enhanced",
  [string]$Python = ""
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

if (Get-Process -Name GTA5_Enhanced, GTA5, PlayGTAV -EA SilentlyContinue) {
  throw "Close GTA first"
}

if (-not $Python) {
  $venv = "C:\Users\aphis\AppData\Local\Temp\gtav-rpf-tools\gtav-enhanced-rpf\.venv\Scripts\python.exe"
  $Python = if (Test-Path $venv) { $venv } else { "python" }
}

& $Python -m pip install -r requirements.txt -q
& $Python tools/build.py --game $GameRoot --install
if ($LASTEXITCODE -ne 0) { throw "build/install failed" }

$out = Join-Path $Root "release\GTA_V_Thai_Subs_DROP_IN"
$modsOut = Join-Path $out "mods\update"
New-Item -ItemType Directory -Force -Path $modsOut | Out-Null

Copy-Item -Force (Join-Path $Root "assets\loaders\OpenRPF.asi") $out
Copy-Item -Force (Join-Path $Root "assets\loaders\xinput1_4.dll") $out
Copy-Item -Force (Join-Path $Root "assets\loaders\args.txt") $out
Copy-Item -Force (Join-Path $GameRoot "mods\update\update.rpf") $modsOut
Copy-Item -Force (Join-Path $GameRoot "mods\update\update2.rpf") $modsOut
Copy-Item -Force (Join-Path $Root "PLAYERS.md") (Join-Path $out "README_ติดตั้ง.txt")

# Compress-Archive cannot handle >2GiB update.rpf — prefer 7-Zip, else leave folder.
$zip = Join-Path $Root "release\GTA_V_Thai_Subs_DROP_IN.zip"
$seven = @(
  "${env:ProgramFiles}\7-Zip\7z.exe",
  "${env:ProgramFiles(x86)}\7-Zip\7z.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($seven) {
  if (Test-Path $zip) { Remove-Item $zip -Force }
  & $seven a -tzip -mx=1 $zip "$out\*" | Out-Host
  Write-Host "ZIP: $zip"
} else {
  Write-Host "No 7-Zip — share the folder as-is (or install 7-Zip and re-run):"
}

Write-Host "DROP-IN ready:"
Write-Host "  $out"
Write-Host "Players: copy folder contents into Grand Theft Auto V Enhanced (merge)."