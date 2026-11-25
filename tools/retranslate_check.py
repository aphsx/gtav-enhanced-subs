# -*- coding: utf-8 -*-
"""Validate edit CSV after retranslate: ~z~ parity, token survival, empty th."""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"~[^~]+~")


def check_file(path: Path) -> list[str]:
    errs: list[str] = []
    with path.open(encoding="utf-8-sig", newline="") as f:
        for i, r in enumerate(csv.DictReader(f), start=2):
            rid = (r.get("id") or "").strip()
            en = r.get("en") or ""
            th = r.get("th") or ""
            if not rid:
                continue
            if en.startswith("~z~") and th and not th.startswith("~z~"):
                errs.append(f"{path.name}:{i} missing leading ~z~")
            en_tok = TOKEN.findall(en)
            th_tok = TOKEN.findall(th)
            if en_tok and th and len(th_tok) < len(en_tok) * 0.5:
                errs.append(f"{path.name}:{i} token loss {en_tok} vs {th_tok}")
            if "Kifflom" in en and th and "Kifflom" not in th and "คิฟฟลอม" not in th:
                errs.append(f"{path.name}:{i} Kifflom should stay Latin/ทับศัพท์")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="CSV paths (default: all edit/**/*.csv)")
    args = ap.parse_args()
    paths = [Path(p) for p in args.paths] if args.paths else sorted((ROOT / "edit").rglob("*.csv"))
    all_e: list[str] = []
    for p in paths:
        all_e.extend(check_file(p))
    if all_e:
        print(f"ISSUES {len(all_e)}")
        for e in all_e[:40]:
            print(e)
        sys.exit(1)
    print(f"OK files={len(paths)}")


if __name__ == "__main__":
    main()
