# -*- coding: utf-8 -*-
"""Raise Thai tone-mark glyphs so they clear upper vowels without OpenType GPOS.

Scaleform/GTA does not position marks via GPOS, so plain Sarabun stacks
wrong on sequences like พิ้. This bakes vertical separation into outlines.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SRC = ROOT / "work" / "font_rebuild" / "fonts_try" / "Sarabun-Regular.ttf"
DEFAULT_OUT = ROOT / "assets" / "fonts" / "Sarabun-Regular-GTA.ttf"

UPPER = [0x0E31, 0x0E34, 0x0E35, 0x0E36, 0x0E37, 0x0E47, 0x0E4D]
TONES = [0x0E48, 0x0E49, 0x0E4A, 0x0E4B, 0x0E4C]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=DEFAULT_SRC)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--gap", type=int, default=50)
    args = ap.parse_args()
    if not args.src.exists():
        raise SystemExit(f"missing source font: {args.src}")

    font = TTFont(str(args.src))
    cmap: dict[int, str] = {}
    for t in font["cmap"].tables:
        cmap.update(t.cmap)
    glyf = font["glyf"]
    uy = max(glyf[cmap[cp]].yMax for cp in UPPER if cp in cmap)
    for cp in TONES:
        if cp not in cmap:
            continue
        g = glyf[cmap[cp]]
        if g.numberOfContours <= 0:
            continue
        need = (uy + args.gap) - g.yMin
        if need <= 0:
            continue
        coords = g.coordinates
        for i in range(len(coords)):
            x, y = coords[i]
            coords[i] = (x, y + need)
        g.coordinates = coords
        g.recalcBounds(glyf)
        print(f"{hex(cp)} shift={need} y=[{g.yMin},{g.yMax}]")

    tmax = max(glyf[cmap[cp]].yMax for cp in TONES if cp in cmap)
    if tmax > font["hhea"].ascent:
        font["hhea"].ascent = int(tmax + 40)
        if "OS/2" in font:
            font["OS/2"].sTypoAscender = int(max(font["OS/2"].sTypoAscender, tmax + 40))
            font["OS/2"].usWinAscent = int(max(font["OS/2"].usWinAscent, tmax + 40))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    font.save(str(args.out))
    print(f"wrote {args.out} ({args.out.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
