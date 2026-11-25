# GTA V Enhanced — Thai Subtitles (community source)

Unofficial **fan Thai subtitles** for GTA V Enhanced (Single Player).  
**Own a legal copy of the game.** This repo is translation + tools — not a pirate pack.

Read **[`LEGAL.md`](LEGAL.md)** before publishing or downloading.

## For players (recommended compliant path)

1. Buy / own **GTA V Enhanced**
2. Clone or download **this source**
3. Install a mods loader yourself (links in [`THIRD_PARTY.md`](THIRD_PARTY.md)) — we do **not** redistribute ASI binaries
4. Build against **your** game files:

```powershell
pip install -r requirements.txt
# optional: rebuild Thai font into YOUR stock efigs
# python tools/rebuild_font.py --game "..." --ffdec-cli "...\ffdec-cli.exe"
python tools/build.py --game "PATH\Grand Theft Auto V Enhanced" --install
```

5. In-game language: **American / English** · SP only

> We **do not** attach full `update.rpf` packs to public Releases (Rockstar assets).  
> Personal/offline use of a pack you built from your own game is on you — do not re-upload those RPFs to this repo.

## For translators (no game unpacking required)

1. Edit only column **`th`** in [`edit/`](edit/) CSV files  
2. Open a Pull Request  

→ [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`RULES.md`](RULES.md)

English column `en` is Rockstar’s text for reference only (not licensed by us).

## License map
| Part | License |
|------|---------|
| Scripts / docs | MIT (`LICENSE`) |
| Thai `th` text | CC BY-SA 4.0 |
| Sarabun GTA font | SIL OFL 1.1 |
| Rockstar EN / game files | **Not licensed here** |

Also: [`NOTICE.md`](NOTICE.md) · [`THIRD_PARTY.md`](THIRD_PARTY.md) · [`LEGAL.md`](LEGAL.md)
