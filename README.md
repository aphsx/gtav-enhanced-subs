# GTA V Enhanced — Thai Subtitles (community)

แฟนมอดคำบรรยายไทยสำหรับ **GTA V Enhanced (Single Player)**  
แก้ข้อความใน CSV ได้เลย — **ไม่ต้อง reverse / ไม่ต้องแกะเกม**

## ช่วยแปล
อ่าน [`CONTRIBUTING.md`](CONTRIBUTING.md)  
เริ่มง่ายๆ ที่ [`edit/00_global_tips_emails.csv`](edit/00_global_tips_emails.csv) (ทิป/เมล)  
หรือบทพูดใน [`edit/dialogue/`](edit/dialogue/)

## ผู้เล่น (ติดตั้งแพ็ก)
Release จะแนบ zip แพ็ก + `install.ps1`  
หรือดูโฟลเดอร์ `GTA_V_Thai_Subs_ONLY_v3_PUBLIC` บนเครื่องผู้ดูแล

## ผู้ดูแล (build จาก CSV)
```bash
python tools/csv_to_maps.py
# แล้วใช้ merge toolchain / install.ps1 ของแพ็กปล่อย
```

## License
- สคริปต์: MIT  
- ข้อความไทยใน `edit/`: CC BY-SA 4.0  
- GTA © Rockstar — ดู [`NOTICE.md`](NOTICE.md)
