# -*- coding: utf-8 -*-
"""Load edit/**/*.csv → {stem: {hash: th}}.

Any CSV under edit/ with columns id,en,th is picked up (dialogue, tips, ui, …).
Later files in sorted path order overwrite earlier hashes for the same stem.
"""
from __future__ import annotations

import csv
from pathlib import Path


def has_thai(s: str) -> bool:
    return any("\u0e00" <= c <= "\u0e7f" for c in s)


def iter_edit_csvs(edit_dir: Path) -> list[Path]:
    if not edit_dir.is_dir():
        return []
    return sorted(p for p in edit_dir.rglob("*.csv") if p.is_file())


def load_translations(edit_dir: Path) -> dict[str, dict[int, str]]:
    by: dict[str, dict[int, str]] = {}
    for path in iter_edit_csvs(edit_dir):
        with path.open(encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                rid = (r.get("id") or "").strip()
                th = r.get("th") or ""
                if ":" not in rid or not has_thai(th):
                    continue
                stem, h = rid.split(":", 1)
                try:
                    hv = int(h)
                except ValueError:
                    continue
                by.setdefault(stem, {})[hv] = th
    return by
