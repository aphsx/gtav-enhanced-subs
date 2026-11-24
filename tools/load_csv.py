# -*- coding: utf-8 -*-
"""Load edit/**/*.csv → {stem: {hash: th}}."""
from __future__ import annotations

import csv
from pathlib import Path


def has_thai(s: str) -> bool:
    return any("\u0e00" <= c <= "\u0e7f" for c in s)


def load_translations(edit_dir: Path) -> dict[str, dict[int, str]]:
    by: dict[str, dict[int, str]] = {}
    files = []
    g = edit_dir / "00_global_tips_emails.csv"
    if g.exists():
        files.append(g)
    dial = edit_dir / "dialogue"
    if dial.is_dir():
        files.extend(sorted(dial.glob("*.csv")))
    for path in files:
        with path.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                rid = (r.get("id") or "").strip()
                th = r.get("th") or ""
                if ":" not in rid or not has_thai(th):
                    continue
                stem, h = rid.split(":", 1)
                by.setdefault(stem, {})[int(h)] = th
    return by
