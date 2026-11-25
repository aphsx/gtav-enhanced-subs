# GTA V Enhanced — Thai Subtitles

แฟนมอดคำบรรยายไทย **Single Player**

## ดาวน์โหลดไปเล่น (จาก repo นี้)

คนเล่นไม่ต้อง clone / ไม่ต้อง Python

1. เปิดหน้า GitHub ของโปรเจกต์นี้ → แท็บ **Releases**
2. ดาวน์โหลด **`GTA_V_Thai_Subs_DROP_IN.zip`**
3. ปิดเกม → แตกซิป **ทับ** โฟลเดอร์ `Grand Theft Auto V Enhanced`
4. ตั้งภาษา **American / English** → เล่น SP

ได้ไฟล์: `OpenRPF.asi`, `xinput1_4.dll`, `args.txt`, `mods\update\update.rpf`, `mods\update\update2.rpf`

รายละเอียดสั้นๆ: [`PLAYERS.md`](PLAYERS.md)

> ทำไมไม่ใส่ซิปใน git? เพราะ `update.rpf` ~3GB — GitHub รับใน **Releases** ของ repo เดียวกัน (ยังถือว่าโหลดจากที่นี่)

## มาช่วยแปล

1. แก้เฉพาะคอลัมน์ `th` ใน [`edit/`](edit/) (CSV)
2. ส่ง Pull Request  

→ [`CONTRIBUTING.md`](CONTRIBUTING.md) · [`RULES.md`](RULES.md)

## Maintainer — อัป Release ให้คนโหลด

ปิดเกม แล้ว:

```powershell
.\tools\make_dropin.ps1 -GameRoot "D:\SteamLibrary\steamapps\common\Grand Theft Auto V Enhanced"
```

จะได้ `release\GTA_V_Thai_Subs_DROP_IN.zip`  
จากนั้นบน GitHub: **Releases → Create release → แนบซิปนี้**

## License
MIT (tools) · CC BY-SA 4.0 (ข้อความใน `edit/`) · OFL (Sarabun)  
GTA © Rockstar — [`NOTICE.md`](NOTICE.md)
