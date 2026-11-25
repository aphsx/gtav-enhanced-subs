# Roadmap — open contributions welcome

Ship what helps players and contributors. PRs appreciated.

**Paused handoff / where we left off:** [`docs/CONTINUE.md`](docs/CONTINUE.md)

## Text
- [x] Bulk SP dialogue + tips Thai present (~99.5% rows) — tip `b5638ab`
- [ ] Stiff calque pass (~70 lines: ฉันหมายถึง / พวกเขาก็ / …)
- [ ] Hand-pass large stems still thin (`fb3aud`, `fam6aud`, `armsaud`, `rbh2aud`, …)
- [ ] Seed + translate UI menus (`edit/ui/` via `dump_from_game.py`)
- [ ] Coverage gaps: `python tools/status.py --by-file`
- [ ] Optional: more languages later (same CSV layout, new column or `edit/<lang>/`)


## Font / rendering
- [ ] Tone-mark / stacking edge cases on Scaleform
- [ ] Document FFDec versions that work for `rebuild_font.py`
- [ ] Alternate OFL faces if Sarabun fails a glyph set

## Tools
- [ ] CI: CSV schema check (columns, `~z~` parity, no binary paths)
- [ ] `status.py` JSON output for badges
- [ ] Safer dry-run for `build.py` (report only, no write)
- [ ] Split / upload helpers for Releases (>2 GB)

## Player UX
- [ ] Clearer DROP_IN join instructions / checksums
- [ ] Uninstall notes per loader type

## Out of scope (keep out of git)
- Game `.rpf` dumps, ASI loaders, decryption keys, prebuilt game gfx
