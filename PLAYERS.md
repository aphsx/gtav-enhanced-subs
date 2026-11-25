# Playing the mod (from source)

This project’s **public GitHub tree does not ship** a ready `update.rpf` (that would redistribute Rockstar files).

## Steps
1. Own GTA V Enhanced  
2. Install a mods folder loader from upstream ([`THIRD_PARTY.md`](THIRD_PARTY.md)) into the game folder  
3. From this repo (with Python + `rpfpeek` + your game keys for your own copy):

```powershell
pip install -r requirements.txt
python tools/build.py --game "PATH\Grand Theft Auto V Enhanced" --install
```

4. Language **American / English** · Single Player  

## Uninstall
Delete `mods\update` and any loader files you added yourself.
