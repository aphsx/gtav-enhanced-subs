# -*- coding: utf-8 -*-
"""GXT2 IO for GTA V Enhanced: UTF-8 NUL-terminated strings."""
from __future__ import annotations

import struct
from pathlib import Path


def read_gxt2(path: str | Path) -> list[tuple[int, str]]:
    data = Path(path).read_bytes()
    if data[:4] != b"2TXG":
        raise ValueError(f"not gxt2: {path}")
    count = struct.unpack_from("<I", data, 4)[0]
    table = [struct.unpack_from("<II", data, 8 + i * 8) for i in range(count)]
    by_off = sorted(table, key=lambda t: t[1])
    tmp: dict[int, str] = {}
    for idx, (h, off) in enumerate(by_off):
        end = by_off[idx + 1][1] if idx + 1 < len(by_off) else len(data)
        chunk = data[off:end]
        nul = chunk.find(b"\x00")
        if nul >= 0:
            chunk = chunk[:nul]
        tmp[h] = chunk.decode("utf-8", errors="replace")
    return [(h, tmp[h]) for h, _ in table]


def write_gxt2(path: str | Path, entries: list[tuple[int, str]]) -> None:
    entries = sorted(entries, key=lambda t: t[0])
    count = len(entries)
    header = 8 + count * 8
    blobs: list[bytes] = []
    offsets: list[int] = []
    cur = header
    for h, s in entries:
        b = s.encode("utf-8") + b"\x00"
        offsets.append(cur)
        blobs.append(b)
        cur += len(b)
    out = bytearray(b"2TXG" + struct.pack("<I", count))
    for (h, _), off in zip(entries, offsets):
        out += struct.pack("<II", h, off)
    for b in blobs:
        out += b
    Path(path).write_bytes(bytes(out))
