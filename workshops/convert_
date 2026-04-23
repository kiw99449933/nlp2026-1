import re
import json

# 1. กำหนดคำศัพท์
KEYWORDS = {
    "VIOLATION": ["ก๊อป", "ลอก", "ขโมย", "แอบอ้าง", "ละเมิด", "ทำซ้ำ"],
    "PATENT": ["สิทธิบัตร", "สิ่งประดิษฐ์", "เครื่องจักร", "แบบร่าง", "วงจร"],
    "COPYRIGHT": ["ลิขสิทธิ์", "รูปภาพ", "เพลง", "หนัง", "นิยาย", "การ์ตูน", "ฟอนต์"]
}

def detect_category(text):
    # ตรวจสอบการละเมิดก่อน (ถ้าไม่มีคำกลุ่มนี้ ให้ถือว่าปกติ)
    is_violation = any(re.search(k, text) for k in KEYWORDS["VIOLATION"])
    if not is_violation:
        return 0, "Normal"

    # แยกหมวด Patent (1) หรือ Copyright (2)
    is_patent = any(re.search(k, text) for k in KEYWORDS["PATENT"])
    is_copyright = any(re.search(k, text) for k in KEYWORDS["COPYRIGHT"])

    if is_patent: return 1, "Patent"
    if is_copyright: return 2, "Copyright"
    
    return 3, "General Violation" # มีการก๊อปแต่ไม่ระบุประเภท

# 2. ฟังก์ชันสร้างผลลัพธ์แบบง่าย
def simple_report(doc_id, text):
    label_id, label_name = detect_category(text)
    
    return {
        "id": doc_id,
        "content": text,
        "result": {
            "type_id": label_id,
            "type_name": label_name
        }
    }

# --- ทดสอบรัน ---
samples = [
    "โดนก๊อปรูปวาดไปลงไอจี",
    "มีการแอบอ้างสิทธิบัตรเครื่องยนต์",
    "ลอกนิยายในเว็บไปขายต่อ",
    "คนทั่วไปเดินเล่น"
]

results = [simple_report(i+1, s) for i, s in enumerate(samples)]
print(json.dumps(results, indent=4, ensure_ascii=False))