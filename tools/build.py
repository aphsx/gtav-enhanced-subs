# -*- coding: utf-8 -*-
"""
Build Thai american_rel.rpf from edit/**/*.csv using YOUR game files.
No reverse-engineering required for contributors — only maintainers/builders run this.

Usage:
  python tools/build.py --game "D:\\...\\Grand Theft Auto V Enhanced"
  python tools/build.py --game "..." --install
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gxt2_io import read_gxt2, write_gxt2  # noqa: E402
from load_csv import has_thai, load_translations  # noqa: E402

SKIP_STEMS = {
    "clo_mnu", "mod_mnu", "snk_mnu", "tat_mnu", "gun_mnu", "har_mnu", "dir_mnu",
    "credit", "trackid", "pubc", "report", "mishsta", "fmmc", "mpawd", "mp_rng",
    "animlau", "ng_install",
}


def find_python_rpfpeek() -> list[str]:
    return [sys.executable, "-m", "rpfpeek"]


def rpf(keys: Path, *args: str) -> None:
    cmd = find_python_rpfpeek() + ["--keys", str(keys), *args]
    subprocess.check_call(cmd)


def find_game(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        if not (p / "GTA5_Enhanced.exe").exists() and not (p / "update" / "update2.rpf").exists():
            raise SystemExit(f"Not an Enhanced game folder: {p}")
        return p
    cands = [
        Path(r"D:\SteamLibrary\steamapps\common\Grand Theft Auto V Enhanced"),
        Path(r"C:\Program Files (x86)\Steam\steamapps\common\Grand Theft Auto V Enhanced"),
        Path(r"C:\Program Files\Epic Games\GTAVEnhanced"),
    ]
    for c in cands:
        if (c / "update" / "update2.rpf").exists():
            return c
    raise SystemExit("Pass --game path to Grand Theft Auto V Enhanced")


def apply_thai(van_dir: Path, out_dir: Path, maps: dict[str, dict[int, str]]) -> tuple[int, int]:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    covered = missing = 0
    for p in sorted(van_dir.glob("*.gxt2")):
        stem = p.stem
        entries = read_gxt2(p)
        mp = maps.get(stem, {})
        out = []
        for h, en in entries:
            if h in mp and has_thai(mp[h]):
                out.append((h, mp[h]))
                covered += 1
            else:
                out.append((h, en))
                if stem not in SKIP_STEMS and (en.startswith("~z~") or stem == "global"):
                    if any(c.isalpha() for c in en):
                        missing += 1
        write_gxt2(out_dir / f"{stem}.gxt2", out)
    return covered, missing


def build(game: Path, keys: Path, do_install: bool) -> Path:
    maps = load_translations(ROOT / "edit")
    if not maps:
        raise SystemExit("No Thai rows in edit/**/*.csv")
    print(f"loaded stems={len(maps)} hashes={sum(len(v) for v in maps.values())}")

    stock_u2 = game / "update" / "update2.rpf"
    stock_u = game / "update" / "update.rpf"
    font = ROOT / "assets" / "font_lib_efigs_pc.gfx"
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    am_out = dist / "american_rel.rpf"

    with tempfile.TemporaryDirectory(prefix="gtav_thai_build_") as tmp:
        tmp_p = Path(tmp)
        # NG encryption is filename-bound — keep exact name american_rel.rpf
        am_dir = tmp_p / "am"
        am_dir.mkdir()
        van = tmp_p / "van_gxt"
        th_gxt = tmp_p / "th_gxt"

        print("extract american_rel from your update2.rpf ...")
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
            raise SystemExit("extract failed: american_rel.rpf not found")
        am_stock = found[0]
        rpf(keys, "encryption", str(am_stock), "open", "-q")

        print("extract gxt2 ...")
        rpf(keys, "extract", str(am_stock), "-o", str(van), "--flatten", "-q")
        gxts = list(van.rglob("*.gxt2"))
        if not gxts:
            raise SystemExit("no gxt2 inside american_rel")
        flat = tmp_p / "van_flat"
        flat.mkdir()
        for g in gxts:
            shutil.copy2(g, flat / g.name)

        covered, missing = apply_thai(flat, th_gxt, maps)
        print(f"gxt covered_th={covered} still_scope_enish≈{missing}")

        if am_out.exists():
            am_out.unlink()
        print("pack OPEN nocomp american_rel.rpf ...")
        rpf(
            keys,
            "pack",
            str(th_gxt),
            "-o",
            str(am_out),
            "--encryption",
            "open",
            "--no-compress",
            "--overwrite",
            "-q",
        )
        print(f"wrote {am_out} ({am_out.stat().st_size} bytes)")

        patch = ROOT / "patch"
        patch.mkdir(exist_ok=True)
        shutil.copy2(am_out, patch / "american_rel.rpf")
        if font.exists():
            shutil.copy2(font, patch / "font_lib_efigs_pc.gfx")

        if not do_install:
            return am_out

        if not stock_u.exists():
            raise SystemExit(f"missing {stock_u}")
        try:
            out = subprocess.check_output(["tasklist"], text=True, errors="ignore")
            if any(x in out for x in ("GTA5_Enhanced.exe", "GTA5.exe", "PlayGTAV.exe")):
                raise SystemExit("Close GTA first")
        except subprocess.CalledProcessError:
            pass

        mods = game / "mods" / "update"
        mods.mkdir(parents=True, exist_ok=True)
        work = tmp_p / "modsbuild"
        work.mkdir()

        print("install: update.rpf (font) ...")
        shutil.copy2(stock_u, work / "update.rpf")
        rpf(keys, "encryption", str(work / "update.rpf"), "open", "-q")
        if font.exists():
            plat = work / "scaleform_platform_pc.rpf"
            rpf(
                keys,
                "extract",
                str(work / "update.rpf"),
                "x64/data/cdimages/scaleform_platform_pc.rpf",
                "-o",
                str(work),
                "-q",
            )
            plat_found = list(work.rglob("scaleform_platform_pc.rpf"))
            if not plat_found:
                raise SystemExit("platform rpf extract failed")
            plat = plat_found[0]
            rpf(keys, "encryption", str(plat), "open", "-q")
            rpf(
                keys,
                "replace",
                str(plat),
                "font_lib_efigs_pc.gfx",
                str(font),
                "--no-compress",
                "-q",
            )
            rpf(
                keys,
                "replace",
                str(work / "update.rpf"),
                "x64/data/cdimages/scaleform_platform_pc.rpf",
                str(plat),
                "--no-compress",
                "-q",
            )
        shutil.copy2(work / "update.rpf", mods / "update.rpf")

        print("install: update2.rpf (thai text) ...")
        shutil.copy2(stock_u2, work / "update2.rpf")
        rpf(keys, "encryption", str(work / "update2.rpf"), "open", "-q")
        rpf(
            keys,
            "replace",
            str(work / "update2.rpf"),
            "x64/data/lang/american_rel.rpf",
            str(am_out),
            "--no-compress",
            "-q",
        )
        shutil.copy2(work / "update2.rpf", mods / "update2.rpf")

        loaders = ROOT / "assets" / "loaders"
        for name in ("OpenRPF.asi", "xinput1_4.dll", "args.txt"):
            src = loaders / name
            if src.exists():
                shutil.copy2(src, game / name)
        print(f"installed into {mods}")
        print("Set language = American/English. SP only.")
        return am_out


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Thai subs from edit/*.csv")
    ap.add_argument("--game", default="", help="Path to GTA V Enhanced")
    ap.add_argument(
        "--keys",
        default=str(Path.home() / ".rpfpeek" / "keys"),
        help="rpfpeek keys directory",
    )
    ap.add_argument("--install", action="store_true", help="Also write mods/ + loaders")
    args = ap.parse_args()
    game = find_game(args.game or None)
    keys = Path(args.keys)
    if not keys.exists():
        raise SystemExit(
            f"Missing keys at {keys}\n"
            "Install rpfpeek and place game keys there (see README)."
        )
    build(game, keys, args.install)


if __name__ == "__main__":
    main()
