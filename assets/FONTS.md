# Font asset (license-clear)

## Runtime file
`font_lib_efigs_pc.gfx` — Scaleform font library for GTA V Enhanced.

Built from:
1. **Stock** `font_lib_efigs_pc.gfx` extracted from the user’s / builder’s game `update.rpf`
2. Glyphs replaced via JPEXS FFDec from **Noto Sans Thai Looped Regular**

## Source font
- Family: Noto Sans Thai Looped  
- File: `fonts/NotoSansThaiLooped-Regular.ttf`  
- License: **SIL Open Font License 1.1** — see `OFL-NotoSansThaiLooped.txt`  
- Upstream: https://github.com/notofonts/thai  

Covers Thai (no tofu □) + basic Latin.

## Rebuild
```powershell
# needs FFDec CLI 26+ and stock efigs extracted once
ffdec-cli -replace stock_efigs.gfx out.gfx 9 NotoSansThaiLooped-Regular.ttf 7 NotoSansThaiLooped-Regular.ttf 1 NotoSansThaiLooped-Regular.ttf 3 NotoSansThaiLooped-Regular.ttf 5 NotoSansThaiLooped-Regular.ttf
```
Character ids: `$Font2`(9), Arial(7), timer(1), Pricedown(3), Cologne(5).


