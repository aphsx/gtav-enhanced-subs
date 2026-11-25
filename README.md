# GTA V Enhanced — Thai Subtitles (community)

แฟนมอดคำบรรยายไทย **Single Player**

| คุณคือ | ทำอะไร |
|--------|--------|
| **ผู้เล่น** | ลงแบบมอดทั่วไป → [`PLAYERS.md`](PLAYERS.md) |
| **มาช่วยแปล** | แก้ CSV ใน `edit/` → [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| **maintainer** | build / ทำซิปปล่อย → ด้านล่าง |

## ผู้เล่น (ง่ายสุด — ลงแล้วเล่น)
1. ดาวน์โหลด **`GTA_V_Thai_Subs_DROP_IN.zip`** จาก GitHub Releases  
   (หรือให้ maintainer รัน `tools/make_dropin.ps1`)
2. ปิดเกม → แตกซิปทับโฟลเดอร์ `Grand Theft Auto V Enhanced`
3. ภาษา **American / English** → เล่น SP

ได้ไฟล์: `OpenRPF.asi`, `xinput1_4.dll`, `args.txt`, `mods\update\*.rpf`

## ช่วยแปล (ไม่ต้อง reverse)
1. เปิด [`edit/00_global_tips_emails.csv`](edit/00_global_tips_emails.csv) หรือ `edit/dialogue/*.csv`
2. แก้เฉพาะคอลัมน์ **`th`**
3. Pull Request  

รายละเอียด: [`CONTRIBUTING.md`](CONTRIBUTING.md) · กฎโทน: [`RULES.md`](RULES.md)

## Maintainer — สร้างแพ็ก drop-in / ติดตั้งเครื่องนี้
ความต้องการ: Python 3.10+, `rpfpeek`, คีย์ที่ `%USERPROFILE%\.rpfpeek\keys`, **ปิดเกม**

```powershell
pip install -r requirements.txt
# ลงเข้าเกมเครื่องนี้
python tools/build.py --game "D:\...\Grand Theft Auto V Enhanced" --install
# หรือทำซิปให้คนอื่นลากลงเกมได้เลย
.\tools\make_dropin.ps1 -GameRoot "D:\...\Grand Theft Auto V Enhanced"
```

## โครงสร้าง repo
| โฟลเดอร์ | ใช้ทำอะไร |
|----------|-----------|
| `edit/` | ข้อความให้คนแก้ |
| `tools/` | build / ฟอนต์ / ทำซิป drop-in |
| `assets/` | ฟอนต์ OFL + loaders |
| `release/` | ผลซิปผู้เล่น (gitignore ไฟล์ .rpf ใหญ่ได้) |

## สถานะพร้อมขึ้น GitHub?
- ช่วยแปลผ่าน CSV: **พร้อม**
- เอกสาร contribute / license / NOTICE: **พร้อม**
- ผู้เล่นแบบมอดทั่วไป: **พร้อมเมื่อมีไฟล์ใน Releases** (`make_dropin.ps1`)  
  อย่า commit `update.rpf` เต็มเข้า git — ใส่ใน Release อย่างเดียว

## License
- สคริปต์: MIT · ข้อความใน `edit/`: CC BY-SA 4.0 · ฟอนต์ Sarabun: OFL  
- เกม © Rockstar — ดู [`NOTICE.md`](NOTICE.md)
