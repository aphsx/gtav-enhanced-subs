# -*- coding: utf-8 -*-
"""Rebuild assets/font_lib_efigs_pc.gfx from stock game efigs + OFL Noto Thai.

Requires: FFDec CLI (ffdec-cli.exe) 26+, rpfpeek, game keys.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TTF = ROOT / "assets" / "fonts" / "Sarabun-Regular-GTA.ttf"
OUT = ROOT / "assets" / "font_lib_efigs_pc.gfx"
# $Font2, Arial, timer, Pricedown, Cologne — common readable faces
FONT_IDS = (9, 7, 1, 3, 5)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True)
    ap.add_argument("--keys", default=str(Path.home() / ".rpfpeek" / "keys"))
    ap.add_argument("--ffdec-cli", required=True, help="Path to ffdec-cli.exe")
    args = ap.parse_args()
    game = Path(args.game)
    keys = Path(args.keys)
    ffdec = Path(args.ffdec_cli)
    if not TTF.exists():
        raise SystemExit(f"missing {TTF}")
    py = [sys.executable, "-m", "rpfpeek", "--keys", str(keys)]

    with tempfile.TemporaryDirectory(prefix="efigs_") as tmp:
        tmp_p = Path(tmp)
        subprocess.check_call(
            py
            + [
                "extract",
                str(game / "update" / "update.rpf"),
                "x64/data/cdimages/scaleform_platform_pc.rpf",
                "-o",
                str(tmp_p),
                "-q",
            ]
        )
        plat = next(tmp_p.rglob("scaleform_platform_pc.rpf"))
        subprocess.check_call(py + ["encryption", str(plat), "open", "-q"])
        subprocess.check_call(
            py + ["extract", str(plat), "font_lib_efigs_pc.gfx", "-o", str(tmp_p), "-q"]
        )
        stock = next(tmp_p.rglob("font_lib_efigs_pc.gfx"))
        out_tmp = tmp_p / "out.gfx"
        cmd = [str(ffdec), "-replace", str(stock), str(out_tmp)]
        for i in FONT_IDS:
            cmd += [str(i), str(TTF)]
        subprocess.check_call(cmd)
        shutil.copy2(out_tmp, OUT)
        shutil.copy2(out_tmp, ROOT / "patch" / "font_lib_efigs_pc.gfx")
        print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
