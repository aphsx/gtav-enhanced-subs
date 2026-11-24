# -*- coding: utf-8 -*-
"""Convert edit/**/*.csv -> maps/mXXXX.json (250 rows each) for the RPF build pipeline."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDIT = ROOT / "edit"
OUT = ROOT / "maps"
CHUNK = 250


def load_rows() -> list[dict]:
    rows: list[dict] = []
    files = [EDIT / "00_global_tips_emails.csv"]
    files += sorted((EDIT / "dialogue").glob("*.csv"))
    for path in files:
        if not path.exists():
            continue
        with path.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                rid = (r.get("id") or "").strip()
                if ":" not in rid:
                    continue
                stem, h = rid.split(":", 1)
                rows.append(
                    {
                        "stem": stem,
                        "h": int(h),
                        "en": r.get("en") or "",
                        "th": r.get("th") or "",
                    }
                )
    return rows


def main() -> None:
    rows = load_rows()
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("m*.json"):
        old.unlink()
    for i in range(0, len(rows), CHUNK):
        chunk = rows[i : i + CHUNK]
        obj = {f"{r['stem']}:{r['h']}": r for r in chunk}
        idx = i // CHUNK
        (OUT / f"m{idx:04d}.json").write_text(
            json.dumps(obj, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
    print(f"wrote {(len(rows) + CHUNK - 1) // CHUNK} map files, {len(rows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
