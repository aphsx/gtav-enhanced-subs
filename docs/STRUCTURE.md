# Project structure

## This repo (OSS source) — `gtav-enhanced-thai-subs`
| Path | Role |
|------|------|
| `edit/**/*.csv` | **Source of truth** for Thai text (dialogue / tips / UI) |
| `tools/` | Build, dump, status, font rebuild |
| `assets/` | OFL fonts + loader notes (no ASI/dll in git) |
| `ROADMAP.md` / docs | Contribution roadmap |

Do not commit `.rpf` / `.asi` / `.dll` / `.gfx` / keys.

## Local player packs on this machine (not in git)
These are **drop-in / legacy install folders** built earlier. Keep them local; rebuild from this repo instead of editing them as source.

| Path | Notes |
|------|-------|
| `%USERPROFILE%\Downloads\GTA_V_Thai_Subs_ONLY_v3` | Older full drop-in (loaders + patch) |
| `%USERPROFILE%\Downloads\GTA_V_Thai_Subs_ONLY_v3_PUBLIC` | Public-oriented copy |
| `release\` (gitignored) | Current DROP_IN zip / split parts |
| `work\` (gitignored) | Font experiments, dump temps, retranslate batches |

**Rule:** CSV in `edit/` wins. Legacy Downloads packs are installs only — do not treat as translation source.

## Flow
```
edit/*.csv  →  tools/build.py  →  your game mods/  →  optional make_dropin.ps1 → Releases
```
