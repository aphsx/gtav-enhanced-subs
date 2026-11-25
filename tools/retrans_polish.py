# -*- coding: utf-8 -*-
"""In-place Thai polish from en + rules; optional id overrides JSON."""
from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN = re.compile(r"~[^~]+~")
ROUGH = re.compile(
    r"\b(fuck|fucking|motherfucker|asshole|shit|damn|bitch|dick|piss)\b",
    re.I,
)

LATIN_FIX = {
    "ไมเคิล": "Michael",
    "แฟรงคลิน": "Franklin",
    "เทรเวอร์": "Trevor",
    "ลามาร์": "Lamar",
    "จอช": "Josh",
    "โทนี่": "Tony",
    "เอเวอรี่": "Avery",
    "เลนนี่": "Lenny",
    "เคลีตัส": "Cletus",
    "รอน": "Ron",
    "ฟิลลิปส์": "Philips",
    "ริคกี้": "Rickie",
    "เจย์": "Jay",
    "สเตรทช์": "Stretch",
    "ร้านขายอาวุธ": "Ammu-Nation",
    "บิลิงเกต": "Bilingsgate",
}

SUBS = [
    ("ฉันหมายถึง", ""),
    ("พวกเขาก็", "ก็"),
    ("พวกเขา", "พวกมัน"),
    ("คอมพิวเตอร์", "คอม"),
    ("รถบบรทุก", "รถบรรทุก"),
    ("เบิร์นสไตน์", "Bernstein"),
    ("เบิร์นสตีน", "Bernstein"),
    (" ~ blip_", " ~BLIP_"),
    ("~ blip_", "~BLIP_"),
    ("จิ้มจุ่ม", "บุ๊บบุ๊บ"),
    ("ประสานเจ้าพนักงาน", "ขัดขวางการทำงานของตำรวจ"),
    ("ช่วยที", "ช่วยด้วย"),
    ("แผนแตกแล้ว", "โดนจับได้"),
    ("แยกย้ายเร็ว", "แยกกันเถอะ"),
    ("ไอ้กระจอก", "ไอ้หมอยแห้ง"),
    ("ค่าจ้างก็ต่ำ", "หุ้นไม่มีค่าอะไร"),
    ("เป็นคนจริงจัง", "รู้ว่าตัวเองอยากได้อะไร"),
    ("ลดราคา", "ย่อธุรกิจลง"),
    ("ลดพิเศษ", "ย่อธุรกิจลง"),
    ("เป็นข้อตกลง", "พร้อม"),
    ("น้ำมันเบนซิน", "น้ำมัน"),
    ("พ่อเล้า", "คนจ้าง"),
]

STREET_TO_GU = [
    ("ฉัน", "กู"),
    ("ผม", "กู"),
    ("นาย", "มึง"),
    ("คุณ", "มึง"),
]


def polish_th(en: str, th: str) -> str:
    if not en.strip():
        return th
    out = th
    for a, b in LATIN_FIX.items():
        out = out.replace(a, b)
    for a, b in SUBS:
        out = out.replace(a, b)
    if en.startswith("~z~") and out and not out.startswith("~z~"):
        out = "~z~" + out.lstrip("~z~")
    if ROUGH.search(en) and not re.search(r"[กูมึง]", out):
        for a, b in STREET_TO_GU:
            if a in out:
                out = out.replace(a, b, 1)
                break
    return out


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--overrides", type=Path)
    args = ap.parse_args()
    overrides: dict[str, str] = {}
    if args.overrides:
        overrides = json.loads(args.overrides.read_text(encoding="utf-8"))
    n = 0
    for path in args.paths:
        if not path.is_absolute():
            path = ROOT / path
        with path.open(encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            fieldnames = list(reader.fieldnames or [])
            rows = list(reader)
        for r in rows:
            rid = (r.get("id") or "").strip()
            en = r.get("en") or ""
            if rid in overrides:
                r["th"] = overrides[rid]
            else:
                r["th"] = polish_th(en, r.get("th") or "")
            n += 1
        write_csv(path, fieldnames, rows)
    print(f"polished rows: {n}")


if __name__ == "__main__":
    main()