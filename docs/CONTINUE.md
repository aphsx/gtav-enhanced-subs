# Continue here (paused 2026-11-25)

Resume from tip **`b5638ab`** on `main`  
Repo: https://github.com/aphsx/gtav-enhanced-subs

## Done this session
- OSS toolkit layout: `edit/ui/`, `tools/status.py`, `tools/dump_from_game.py`, `tools/retranslate_check.py`
- README branding + logo (`docs/assets/logo.jpg`) + multi-license badges
- Bulk dialogue/tips polish (v3 maps + scene tone). **~99.5%** rows have Thai
- DROP_IN release **0.0.1** (split `.001`/`.002`) already published
- Legacy player zips on this PC stay **out of git** — see [`STRUCTURE.md`](STRUCTURE.md)

## Do **not** resume
- Google / MyMemory / `deep_translator` / `tools/retranslate_inplace.py`  
  They hang, rate-limit, and corrupt lines. Kill any leftover `python` running those scripts.

## Snapshot (at pause)
| Metric | Value |
|--------|-------|
| CSV rows | 67,651 |
| With Thai | 67,331 (**99.5%**) |
| Empty `th` | 320 (mostly non-spoken / keep-EN) |
| Token / `~z~` breaks | 0 (run `python tools/retranslate_check.py`) |
| Stiff calques left | ~70 (`ฉันหมายถึง` / `พวกเขาก็` / …) |
| Match old v3 maps | ~83% — **17%** intentionally polished away from maps |

## Next work (priority order)
1. **Stiff-line pass** — rewrite ~70 calques; start with  
   `00_global_tips_emails`, `armsaud`, `cst2aud`/`cst*`, `chatcau`, `d1aud`/`d2baud`, `clothau`, `bb3aud`
2. **Large stems quality** — spot-check / hand-pass where polish was thin:  
   `fb3aud`, `fam6aud`, `armsaud`, `rbh2aud`, `ct_aud`, `bs2baud`, `finc1au`
3. **UI lane** — `python tools/dump_from_game.py --game "…"` → translate `edit/ui/*.csv`
4. **Empty `th` audit** — `python tools/status.py --by-file`; fill only if spoken/tips worth translating
5. **Rebuild + DROP_IN** when text settles: `build.py --install` → `make_dropin.ps1` → new release tag
6. **CI** — wire `retranslate_check.py` (or schema check) on PRs

## Local junk (do not commit)
```
tools/apply_ordered.py
tools/apply_th_map.py
tools/retranslate_inplace.py
tools/apply_th_json.py   # dirty helper; keep out unless cleaned
work/                    # gitignored — maps, logs, MT scraps
```

## Useful commands
```powershell
python tools/status.py
python tools/retranslate_check.py
python tools/dump_from_game.py --game "PATH\Grand Theft Auto V Enhanced"
python tools/build.py --game "PATH\Grand Theft Auto V Enhanced" --install
```

v3 map cache on this machine (optional reference, verify every line vs `en`):  
`C:\Users\aphis\AppData\Local\Temp\gtav-rpf-tools\work\v3_retranslate\maps`
