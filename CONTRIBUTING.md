# Contributing

Open toolkit — help with **text**, **UI**, **fonts**, **scripts**, or **docs**.  
You do **not** need the game to translate. You **do** need your own game copy to dump/build.

## Lanes

| Lane | What | Needs game? |
|------|------|-------------|
| Translate | Edit `th` in [`edit/`](edit/) | No |
| Seed UI / missing stems | `tools/dump_from_game.py` → new CSV → translate | Yes |
| Build / install | `tools/build.py` / `install.ps1` | Yes |
| Font | `tools/rebuild_font.py` + [`assets/FONTS.md`](assets/FONTS.md) | Yes + FFDec |
| Tools / docs | Improve `tools/*`, README, ROADMAP | No |

Ideas we want help with: [`ROADMAP.md`](ROADMAP.md)

## Translate (GitHub)

1. Open a CSV under `edit/` → **Edit**
2. Change only column **`th`**
3. Commit → Pull Request

Or fork, edit in Excel/Google Sheets (UTF-8), then PR.

| Column | Rule |
|--------|------|
| `id` | Do not change (`stem:hash`) |
| `en` | Rockstar English — reference only |
| `th` | **Your text** (CC BY-SA 4.0) |

Checklist: [`RULES.md`](RULES.md) · keep `~TOKEN~` · Latin names/places · tone ≤ EN · no `.rpf` / keys / ASI in git

### Where text lives
| Path | Content |
|------|---------|
| `edit/00_global_tips_emails.csv` | Tips / emails / help |
| `edit/dialogue/*.csv` | Mission / cutscene |
| `edit/ui/*.csv` | Menus / UI (create via dump) |

`tools/load_csv.py` loads **all** `edit/**/*.csv`.

## Dump UI stubs (builders)

```powershell
python tools/dump_from_game.py --game "PATH\Grand Theft Auto V Enhanced"
python tools/dump_from_game.py --game "..." --all-missing
python tools/status.py
```

## Build

```powershell
python tools/build.py --game "PATH\Grand Theft Auto V Enhanced" --install
```

Maintainers ship DROP_IN via Releases; source stays free of game binaries.
