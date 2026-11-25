# GTA V Enhanced — Thai Subtitles

Unofficial fan Thai subtitles for **GTA V Enhanced** (Single Player).  
Own a legal copy of the game. Not affiliated with Rockstar.

## Download & play (like a normal mod)

1. Open this repo on GitHub → **Releases**
2. Download **`GTA_V_Thai_Subs_DROP_IN.zip`**
3. Close the game
4. Extract / merge into `Grand Theft Auto V Enhanced`
5. Set language **American / English** → play SP

Files inside the zip:

```
OpenRPF.asi
xinput1_4.dll
args.txt
mods\update\update.rpf
mods\update\update2.rpf
README.txt
```

Details: [`PLAYERS.md`](PLAYERS.md)

> This Release redistributes modified game archives for convenience (common for GTA mods).  
> Higher copyright risk than source-only — see [`LEGAL.md`](LEGAL.md).

## Help translate

Edit only column **`th`** in [`edit/`](edit/) → Pull Request  
→ [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`RULES.md`](RULES.md)

## Maintainer — rebuild DROP_IN

```powershell
# game closed; Sarabun gfx present at assets\font_lib_efigs_pc.gfx (local)
python tools/build.py --game "PATH\Grand Theft Auto V Enhanced" --install
.\tools\make_dropin.ps1 -GameRoot "PATH\Grand Theft Auto V Enhanced"
# upload release\GTA_V_Thai_Subs_DROP_IN.zip to GitHub Releases
```

## License
| Part | License |
|------|---------|
| Scripts | MIT |
| Thai `th` text | CC BY-SA 4.0 |
| Sarabun font source | OFL |
| Game EN / RPF in Releases | © Rockstar — not licensed by this project |

[`NOTICE.md`](NOTICE.md) · [`THIRD_PARTY.md`](THIRD_PARTY.md) · [`LEGAL.md`](LEGAL.md)
