# ผู้เล่น — ลงแล้วเล่น (แบบมอดทั่วไป)

ไม่ต้อง Python / ไม่ต้อง build

## สิ่งที่ต้องมี
โฟลเดอร์ปล่อยชื่อประมาณ `GTA_V_Thai_Subs_DROP_IN` (สร้างด้วย `tools/make_dropin.ps1` หลังปิดเกม — หรือดาวน์โหลดจาก GitHub **Releases**)

## ลงยังไง
1. ปิดเกม
2. คัดลอกไปที่โฟลเดอร์เกม `Grand Theft Auto V Enhanced\`:

```
OpenRPF.asi
xinput1_4.dll
args.txt
mods\update\update.rpf
mods\update\update2.rpf
```

จากในซิปจะมีโครงสร้างเดียวกันแล้ว — ลากทั้งก้อนทับโฟลเดอร์เกมได้

3. เปิดเกม → ภาษา **American / English**
4. Single Player

## ถอดมอด
ลบ `mods\update` และไฟล์ `OpenRPF.asi` / `xinput1_4.dll` / `args.txt` ถ้าไม่ใช้มอดอื่น

## หมายเหตุ
ไฟล์ `update.rpf` / `update2.rpf` ในแพ็ก drop-in มาจากเกม Enhanced ของคนที่ build  
อัปเดตเกมใหญ่ๆ อาจต้อง build แพ็กใหม่
