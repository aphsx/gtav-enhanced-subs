# -*- coding: utf-8 -*-
"""Merge id->th JSON patches into edit CSV (id/en unchanged)."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def apply(path: Path, by_id: dict[str, str]) -> tuple[int, int]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)
    hit = 0
    for r in rows:
        rid = (r.get("id") or "").strip()
        if rid in by_id:
            r["th"] = by_id[rid]
            hit += 1
    write_csv(path, fieldnames, rows)
    return hit, len(rows)


def load_maps(maps_dir: Path, base: str) -> dict[str, str]:
  out: dict[str, str] = {}
  for p in sorted(maps_dir.glob(f"{base}_p*.json")):
      for item in json.loads(p.read_text(encoding="utf-8")):
          out[f"{base}:{item['h']}"] = item["th"]
  return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", type=Path, nargs="+")
    ap.add_argument("--json", type=Path, help="id->th JSON object")
    ap.add_argument("--maps-dir", type=Path, help="gtav-rpf-tools maps folder")
    args = ap.parse_args()
    for csv_path in args.csv:
        by_id: dict[str, str] = {}
        if args.json and args.json.exists():
            by_id.update(json.loads(args.json.read_text(encoding="utf-8")))
        if args.maps_dir:
            base = csv_path.stem
            by_id.update(load_maps(args.maps_dir, base))
        hit, total = apply(csv_path, by_id)
        print(f"{csv_path.name}: {hit}/{total}")


if __name__ == "__main__":
    main()