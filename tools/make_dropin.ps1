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

$zip = Join-Path $Root "release\GTA_V_Thai_Subs_DROP_IN.zip"
if (Test-Path $zip) { Remove-Item $zip -Force }
Compress-Archive -Path (Join-Path $out "*") -DestinationPath $zip -CompressionLevel Optimal

Write-Host "DROP-IN ready:"
Write-Host "  $out"
Write-Host "  $zip"
Write-Host "Players: unzip into Grand Theft Auto V Enhanced folder (merge)."
