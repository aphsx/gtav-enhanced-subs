# Font asset (license-clear, Thai stacking fixed)

## Runtime file
`font_lib_efigs_pc.gfx` — Scaleform font library for GTA V Enhanced.

Built from:
1. **Stock** `font_lib_efigs_pc.gfx` from the game
2. Glyphs from **Sarabun Regular** (SIL OFL 1.1), with tone-mark outlines shifted up so พิ่ / พิ้ / ดิ้ do not overlap under Scaleform (which does not apply OpenType GPOS)

## Source
- `fonts/Sarabun-Regular-GTA.ttf` — Sarabun + baked mark metrics for GTA  
- Upstream Sarabun: https://github.com/google/fonts/tree/main/ofl/sarabun  
- License: `OFL-Sarabun.txt`

## Why not plain Noto/Sarabun?
Scaleform draws combining marks without Thai GPOS. Stock OFL fonts put sara-i and tone marks in the same Y band → they stack on top of each other. GTA-tuned file raises mai ek/tho/tri/chattawa/thanthakhat above upper vowels (same approach community Thai efigs used).

## Rebuild
```powershell
python tools/tune_thai_marks.py   # Sarabun → Sarabun-Regular-GTA.ttf
python tools/rebuild_font.py --game "..." --ffdec-cli "path\to\ffdec-cli.exe"
python tools/build.py --game "..." --install
```
