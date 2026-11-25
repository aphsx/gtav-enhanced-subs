# -*- coding: utf-8 -*-
"""Dump English gxt2 rows from YOUR game into edit CSV stubs (th empty).

Default: UI / menu stems → edit/ui/*.csv
Use --all-missing to also emit stems not already covered under edit/.

Usage:
  python tools/dump_from_game.py --game "PATH\\Grand Theft Auto V Enhanced"
  python tools/dump_from_game.py --game "..." --out edit/ui --stems clo_mnu,gun_mnu
  python tools/dump_from_game.py --game "..." --all-missing
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gxt2_io import read_gxt2  # noqa: E402
from load_csv import iter_edit_csvs  # noqa: E402

DEFAULT_UI_STEMS = (
    "clo_mnu",
    "mod_mnu",
    "snk_mnu",
    "tat_mnu",
    "gun_mnu",
    "har_mnu",
    "dir_mnu",
)


def rpf(keys: Path, *args: str) -> None:
    subprocess.check_call([sys.executable, "-m", "rpfpeek", "--keys", str(keys), *args])


def find_game(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        if not (p / "GTA5_Enhanced.exe").exists() and not (p / "update" / "update2.rpf").exists():
            raise SystemExit(f"Not an Enhanced game folder: {p}")
        return p
    for c in (
        Path(r"C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V Enhanced"),
        Path(r"C:\Program Files\Epic Games\GTAVEnhanced"),
    ):
        if (c / "update" / "update2.rpf").exists():
            return c
    raise SystemExit("Pass --game path to Grand Theft Auto V Enhanced")


def existing_ids_and_stems(edit_dir: Path) -> tuple[set[str], set[str]]:
    ids: set[str] = set()
    stems: set[str] = set()
    for path in iter_edit_csvs(edit_dir):
        with path.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                rid = (r.get("id") or "").strip()
                if ":" not in rid:
                    continue
                ids.add(rid)
                stems.add(rid.split(":", 1)[0])
    return ids, stems


def write_csv(path: Path, rows: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["id", "en", "th"])
        for rid, en, th in rows:
            w.writerow([rid, en, th])


def main() -> None:
    ap = argparse.ArgumentParser(description="Dump game EN strings into edit CSV stubs")
    ap.add_argument("--game", default="", help="Path to GTA V Enhanced")
    ap.add_argument(
        "--keys",
        default=str(Path.home() / ".rpfpeek" / "keys"),
        help="rpfpeek keys directory",
    )
    ap.add_argument("--out", default=str(ROOT / "edit" / "ui"), help="Output directory")
    ap.add_argument(
        "--stems",
        default="",
        help="Comma-separated stems (default: common *_mnu UI stems)",
    )
    ap.add_argument(
        "--all-missing",
        action="store_true",
        help="Dump every stem that has no rows under edit/ yet",
    )
    ap.add_argument(
        "--merge",
        action="store_true",
        help="Skip row ids that already exist anywhere under edit/",
    )
    args = ap.parse_args()

    game = find_game(args.game or None)
    keys = Path(args.keys)
    if not keys.exists():
        raise SystemExit(f"Missing keys at {keys}")
    out_dir = Path(args.out)
    if not out_dir.is_absolute():
        out_dir = ROOT / out_dir

    known_ids, known_stems = existing_ids_and_stems(ROOT / "edit")
    stem_filter: set[str] | None
    if args.stems.strip():
        stem_filter = {s.strip() for s in args.stems.split(",") if s.strip()}
    elif args.all_missing:
        stem_filter = None
    else:
        stem_filter = set(DEFAULT_UI_STEMS)

    stock_u2 = game / "update" / "update2.rpf"
    wrote = 0
    with tempfile.TemporaryDirectory(prefix="gtav_dump_") as tmp:
        tmp_p = Path(tmp)
        am_dir = tmp_p / "am"
        am_dir.mkdir()
        print("extract american_rel ...")
        rpf(
            keys,
            "extract",
            str(stock_u2),
            "x64/data/lang/american_rel.rpf",
            "-o",
            str(am_dir),
            "-q",
        )
        found = list(am_dir.rglob("american_rel.rpf"))
        if not found:
            raise SystemExit("american_rel.rpf not found")
        am = found[0]
        rpf(keys, "encryption", str(am), "open", "-q")
        van = tmp_p / "van"
        van.mkdir()
        rpf(keys, "extract", str(am), "-o", str(van), "--flatten", "-q")
        gxts = sorted(van.rglob("*.gxt2"))
        if not gxts:
            raise SystemExit("no gxt2")

        for g in gxts:
            stem = g.stem
            if stem_filter is not None and stem not in stem_filter:
                continue
            if args.all_missing and stem in known_stems:
                continue

            entries = read_gxt2(g)
            rows: list[tuple[str, str, str]] = []
            for h, en in entries:
                rid = f"{stem}:{h}"
                if args.merge and rid in known_ids:
                    continue
                rows.append((rid, en, ""))
            if not rows:
                continue
            dest = out_dir / f"{stem}.csv"
            write_csv(dest, rows)
            wrote += 1
            print(f"wrote {dest.relative_to(ROOT)} ({len(rows)} rows)")

    print(f"done files={wrote} out={out_dir}")
    print("Translate column th, then PR. Do not commit game binaries.")


if __name__ == "__main__":
    main()
