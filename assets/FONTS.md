# Fonts (OFL only in git)

## Shipped
- `fonts/Sarabun-Regular-GTA.ttf` — Sarabun Regular with tone-mark outlines raised for Scaleform (no OpenType GPOS).  
- License: SIL OFL 1.1 — `OFL-Sarabun.txt`  
- Upstream: https://github.com/google/fonts/tree/main/ofl/sarabun  

## Not shipped
Compiled `font_lib_efigs_pc.gfx` is **not** in git (it embeds game Scaleform data).  
Rebuild locally from **your** stock efigs:

```powershell
python tools/rebuild_font.py --game "PATH\Grand Theft Auto V Enhanced" --ffdec-cli "PATH\ffdec-cli.exe"
python tools/build.py --game "..." --install
```

Output gfx is written under `assets/` / `patch/` on your machine only (gitignored patterns apply to `*.gfx` where configured).
