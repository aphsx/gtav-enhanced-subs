# GTA V Enhanced — Thai Subtitles (community)

แฟนมอดคำบรรยายไทย **Single Player**  
แก้ข้อความใน CSV ได้เลย — **ไม่ต้อง reverse**  
build แพ็กใหม่จากเกมของตัวเองได้ด้วยสคริปต์ใน repo นี้

## โครงสร้าง

| โฟลเดอร์ | ใช้ทำอะไร |
|----------|-----------|
| `edit/` | **แก้ตรงนี้** — tips/เมล + บทพูด (CSV) |
| `tools/` | แปลง CSV → แพ็ก `american_rel.rpf` + ติดตั้ง |
| `assets/` | ฟอนต์ไทย + OpenRPF loaders |
| `dist/` | ผล build (สร้างโดยสคริปต์) |

## ช่วยแปล (contributor)

1. เปิด [`edit/00_global_tips_emails.csv`](edit/00_global_tips_emails.csv) หรือไฟล์ใน `edit/dialogue/`
2. แก้เฉพาะคอลัมน์ **`th`** (อย่าแตะ `id` / `en`)
3. ส่ง Pull Request

รายละเอียด: [`CONTRIBUTING.md`](CONTRIBUTING.md) · กฎโทน: [`RULES.md`](RULES.md)

## สร้างแพ็กใช้เอง (builder / คุณ)

ความต้องการ
- GTA V Enhanced ที่ซื้อถูกกฏหมาย
- Python 3.10+
- แพ็กเกจ `rpfpeek` + คีย์เกมที่ `%USERPROFILE%\.rpfpeek\keys`

```powershell
cd gtav-enhanced-thai-subs
python -m pip install -r requirements.txt

# แค่สร้าง dist/american_rel.rpf
python tools/build.py --game "D:\SteamLibrary\steamapps\common\Grand Theft Auto V Enhanced"

# สร้าง + ติดตั้งเข้า mods\ (ปิดเกมก่อน)
python tools/build.py --game "..." --install
# หรือ
.\install.ps1 -GameRoot "D:\...\Grand Theft Auto V Enhanced"
```

ในเกม: ภาษา **American / English**

ถอดมอด: ลบ `mods\update` (+ `OpenRPF.asi` / `xinput1_4.dll` ถ้าไม่ใช้มอดอื่น)

## License
- สคริปต์: MIT  
- ข้อความใน `edit/`: CC BY-SA 4.0  
- เกม © Rockstar — ดู [`NOTICE.md`](NOTICE.md)
