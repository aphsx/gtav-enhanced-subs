# -*- coding: utf-8 -*-
"""Coverage report for edit/**/*.csv (no game required).

Usage:
  python tools/status.py
  python tools/status.py --by-file
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from load_csv import has_thai, iter_edit_csvs  # noqa: E402


def bucket_for(path: Path) -> str:
    rel = path.relative_to(ROOT / "edit").as_posix()
    if rel.startswith("dialogue/"):
        return "dialogue"
    if rel.startswith("ui/"):
        return "ui"
    if path.name.startswith("00_global"):
        return "global"
    return "other"


def main() -> None:
    ap = argparse.ArgumentParser(description="Thai CSV coverage status")
    ap.add_argument("--by-file", action="store_true", help="Per-file lines")
    args = ap.parse_args()

    by_bucket: dict[str, dict[str, int]] = defaultdict(lambda: {"rows": 0, "thai": 0, "empty": 0})
    per_file: list[tuple[str, int, int, int]] = []

    for path in iter_edit_csvs(ROOT / "edit"):
        rows = thai = empty = 0
        with path.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                rid = (r.get("id") or "").strip()
                if ":" not in rid:
                    continue
                rows += 1
                th = r.get("th") or ""
                if has_thai(th):
                    thai += 1
                else:
                    empty += 1
        b = bucket_for(path)
        by_bucket[b]["rows"] += rows
        by_bucket[b]["thai"] += thai
        by_bucket[b]["empty"] += empty
        if args.by_file:
            rel = path.relative_to(ROOT).as_posix()
            per_file.append((rel, rows, thai, empty))

    print("bucket\trows\tthai\tempty\tpct")
    total = {"rows": 0, "thai": 0, "empty": 0}
    for name in ("global", "dialogue", "ui", "other"):
        d = by_bucket.get(name)
        if not d or d["rows"] == 0:
            continue
        pct = 100.0 * d["thai"] / d["rows"] if d["rows"] else 0.0
        print(f"{name}\t{d['rows']}\t{d['thai']}\t{d['empty']}\t{pct:.1f}%")
        for k in total:
            total[k] += d[k]
    if total["rows"]:
        pct = 100.0 * total["thai"] / total["rows"]
        print(f"TOTAL\t{total['rows']}\t{total['thai']}\t{total['empty']}\t{pct:.1f}%")

    if args.by_file:
        print("\nfile\trows\tthai\tempty")
        for rel, rows, thai, empty in per_file:
            if empty:
                print(f"{rel}\t{rows}\t{thai}\t{empty}")


if __name__ == "__main__":
    main()
