# Contributing translations

You only edit CSV text. You do **not** need game archives, keys, or unpack tools.

## What to edit
| File | Content |
|------|---------|
| `edit/00_global_tips_emails.csv` | Tips / emails / help |
| `edit/dialogue/*.csv` | Mission / cutscene lines |

Index: [`edit/INDEX.md`](edit/INDEX.md)

## How (GitHub)
1. Open a CSV → **Edit**
2. Change only column **`th`**
3. Commit → Pull Request

Or fork, edit in Excel/Google Sheets (UTF-8), then PR.

## Columns
| Column | Rule |
|--------|------|
| `id` | Do not change |
| `en` | Rockstar English — reference only; do not “re-license” |
| `th` | **Edit here** (your contribution under CC BY-SA 4.0) |

## Checklist
- [ ] Keep `~z~` / `~n~` / other `~TOKEN~` markup matching `en`
- [ ] Keep character/place/brand names in Latin per [`RULES.md`](RULES.md)
- [ ] Tone no harsher than English
- [ ] Do not commit `.rpf`, keys, ASI loaders, or game dumps

Maintainers build packs from CSV using each user’s own game copy (`tools/build.py`).
