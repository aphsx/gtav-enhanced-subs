# Players — install like a normal mod

1. GitHub repo → **Releases** → `GTA_V_Thai_Subs_DROP_IN.zip.001` + `.002`
2. Join parts (PowerShell below, or open `.001` in 7-Zip) → `GTA_V_Thai_Subs_DROP_IN.zip`
   ```powershell
   Get-Content .\GTA_V_Thai_Subs_DROP_IN.zip.* -Encoding Byte -ReadCount 0 |
     Set-Content .\GTA_V_Thai_Subs_DROP_IN.zip -Encoding Byte
   ```
3. Close GTA
4. Extract into `Grand Theft Auto V Enhanced` (merge / overwrite)
5. Language = **American / English**
6. Play Single Player

## Uninstall
Delete `mods\update` and `OpenRPF.asi` / `xinput1_4.dll` / `args.txt` if unused elsewhere.
