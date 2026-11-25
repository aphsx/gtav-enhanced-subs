# UI / menu strings

Put CSV files here for shop menus, pause help, and other non-dialogue text  
(`clo_mnu`, `gun_mnu`, `tat_mnu`, …).

## Columns
| Column | Rule |
|--------|------|
| `id` | `stem:hash` — do not change |
| `en` | Rockstar English (reference) |
| `th` | **Edit here** |

## How to seed from your game
```powershell
python tools/dump_from_game.py --game "PATH\Grand Theft Auto V Enhanced" --out edit/ui
```

Then translate `th` → Pull Request. Do not commit `.rpf` / keys / ASI.
