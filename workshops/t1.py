from collections import Counter
THAI_IP_DATASET = [
 # CLASS 0: ละเมิดสิทธิบัตร (40 ตัวอย่าง — MAJORITY)
 {"text": "จำเลยผลิตสินค้าที่เลียนแบบสิทธิบัตรการประดิษฐ์เลขที่ 12345", "label": 0},
 {"text": "ผู้ต้องหานำเข้าชิ้นส่วนที่ละเมิดสิทธิบัตรจากต่างประเทศ", "label": 0},
 {"text": "บริษัทจำเลยผลิตยาสามัญโดยละเมิดสิทธิบัตรยาต้นแบบ", "label":
0},
 {"text": "จำเลยนำเทคโนโลยีจดสิทธิบัตรไปใช้เชิงพาณิชย์โดยไม่ได้รับอนุญาต", "label": 0},
 {"text": "ผู้ต้องหาผลิตอุปกรณ์อิเล็กทรอนิกส์เลียนแบบสิทธิบัตรการประดิษฐ์", "label": 0},
 {"text": "จำเลยขายสินค้าปลอมแปลงที่ใช้กระบวนการผลิตตามสิทธิบัตร", "label":
0},
 {"text": "บริษัทนำเข้าผลิตภัณฑ์ที่ละเมิดอนุสิทธิบัตรของผู้เสียหาย", "label": 0},
 {"text": "จำเลยผลิตเครื่องจักรโดยใช้กลไกที่ได้รับสิทธิบัตรโดยไม่ได้รับอนุญาต", "label": 0},
 {"text": "ผู้ต้องหาส่งออกสินค้าที่ละเมิดสิทธิบัตรไปยังต่างประเทศ", "label": 0},
 {"text": "บริษัทจำเลยใช้สูตรเคมีที่ได้รับสิทธิบัตรในการผลิตเชิงอุตสาหกรรม", "label": 0},
 {"text": "จำเลยผลิตอุปกรณ์การแพทย์โดยละเมิดสิทธิบัตรโดยตรง", "label":
0},
 {"text": "ผู้ต้องหาทำซ้ำกระบวนการผลิตที่จดสิทธิบัตรแล้ว", "label":
0},
 {"text": "บริษัทจำเลยผลิตแบตเตอรี่โดยใช้เทคโนโลยีที่ได้รับสิทธิบัตร", "label": 0},
 {"text": "จำเลยใช้วิธีการทางวิศวกรรมที่ได้รับสิทธิบัตรโดยไม่ได้รับอนุญาต", "label": 0},
 {"text": "ผู้ต้องหาผลิตชิ้นส่วนยานยนต์โดยละเมิดสิทธิบัตรของบริษัทต่างชาติ", "label": 0},
 {"text": "บริษัทจำเลยนำกระบวนการผลิตที่จดสิทธิบัตรมาใช้โดยไม่ชำระค่าสิทธิ์", "label": 0},
 {"text": "จำเลยผลิตโดรนโดยใช้เทคโนโลยีที่ได้รับการจดสิทธิบัตรแล้ว", "label": 0},
 {"text": "ผู้ต้องหาเลียนแบบการออกแบบผลิตภัณฑ์ที่ได้รับอนุสิทธิบัตร", "label": 0},
 {"text": "บริษัทนำเข้าเครื่องพิมพ์ 3D ที่ใช้เทคโนโลยีละเมิดสิทธิบัตร", "label": 0},
 {"text": "จำเลยผลิตยาปฏิชีวนะโดยใช้สูตรที่อยู่ภายใต้สิทธิบัตรของผู้เสียหาย", "label": 0},
 {"text": "ผู้ต้องหาทำซ้ำกระบวนการหมักที่ได้รับสิทธิบัตรสำหรับผลิตภัณฑ์อาหาร", "label": 0},
 {"text": "บริษัทจำเลยผลิตเซมิคอนดักเตอร์โดยละเมิดสิทธิบัตรของบริษัทชั้นนำ", "label": 0},
 {"text": "จำเลยนำเข้าและจำหน่ายชิปที่ใช้สถาปัตยกรรมตามสิทธิบัตร", "label":
0},
 {"text": "ผู้ต้องหาผลิตอุปกรณ์โทรคมนาคมโดยละเมิดสิทธิบัตรมาตรฐาน", "label":
0},
 {"text": "บริษัทจำเลยใช้กระบวนการบำบัดน้ำที่ได้รับสิทธิบัตรโดยไม่ได้รับอนุญาต", "label": 0},
 {"text": "จำเลยผลิตแผงโซลาร์โดยใช้เทคโนโลยีที่ได้รับสิทธิบัตร", "label": 0},
 {"text": "ผู้ต้องหานำเข้าอุปกรณ์ฟอกไตที่ละเมิดสิทธิบัตรการประดิษฐ์", "label": 0},
 {"text": "บริษัทจำเลยผลิตสีอุตสาหกรรมโดยใช้สูตรที่ได้รับสิทธิบัตร", "label": 0},
 {"text": "จำเลยใช้อัลกอริทึมที่จดสิทธิบัตรในซอฟต์แวร์เชิงพาณิชย์", "label": 0},
 {"text": "ผู้ต้องหาผลิตอุปกรณ์ IoT โดยละเมิดสิทธิบัตรโปรโตคอลสื่อสาร", "label": 0},
 {"text": "บริษัทนำเข้าและจำหน่ายผลิตภัณฑ์ที่ใช้วัสดุนาโนตามสิทธิบัตร", "label": 0},
 {"text": "จำเลยผลิตชุดทดสอบโควิดที่เลียนแบบเทคโนโลยีสิทธิบัตรต่างชาติ", "label": 0},
 {"text": "ผู้ต้องหาใช้กระบวนการถลุงแร่ที่ได้รับสิทธิบัตรโดยไม่ได้รับอนุญาต", "label": 0},
 {"text": "บริษัทจำเลยผลิตวัคซีนโดยละเมิดสิทธิบัตรของบริษัทวิจัย", "label": 0},
 {"text": "จำเลยนำเทคโนโลยีบล็อกเชนที่จดสิทธิบัตรไปใช้ในแอปพลิเคชันพาณิชย์", "label": 0},
 {"text": "ผู้ต้องหาผลิตหุ่นยนต์อุตสาหกรรมโดยละเมิดสิทธิบัตรระบบควบคุม", "label": 0},
 {"text": "บริษัทจำเลยใช้เทคโนโลยีการพิมพ์ inkjet ที่จดสิทธิบัตรไว้", "label": 0},
 {"text": "จำเลยผลิตวัสดุก่อสร้างโดยใช้สูตรซีเมนต์ที่ได้รับสิทธิบัตร", "label": 0},
 {"text": "ผู้ต้องหานำเข้ายาชีววัตถุที่ละเมิดสิทธิบัตรของเจ้าของสิทธิ", "label": 0},
 {"text": "บริษัทจำเลยผลิตตัวเก็บประจุโดยใช้วัสดุไดอิเล็กตริกตามสิทธิบัตร", "label": 0},
 # CLASS 1: ละเมิดลิขสิทธิ์ (20 ตัวอย่าง — MEDIUM)
 {"text": "จำเลยทำซ้ำโปรแกรมคอมพิวเตอร์มีลิขสิทธิ์โดยไม่ได้รับอนุญาต", "label": 1},
 {"text": "ผู้ต้องหาเผยแพร่ภาพยนตร์บน YouTube โดยละเมิดลิขสิทธิ์", "label":
1},
 {"text": "จำเลยดัดแปลงงานศิลปกรรมและนำไปจำหน่ายโดยไม่ได้รับอนุญาต", "label":
1},
 {"text": "บริษัทจำเลยผลิตซีดีเพลงเถื่อนและจำหน่ายตามตลาดนัด", "label":
1},
 {"text": "ผู้ต้องหาทำซ้ำหนังสือเรียนและจำหน่ายโดยไม่ได้รับอนุญาต", "label": 1},
 {"text": "จำเลยนำภาพถ่ายของผู้เสียหายไปใช้เชิงพาณิชย์โดยไม่ได้รับอนุญาต", "label": 1},
 {"text": "บริษัทดาวน์โหลดซอฟต์แวร์ไม่มีใบอนุญาตและนำไปใช้งานในองค์กร", "label":
1},
 {"text": "จำเลยสตรีมเพลงโดยไม่ชำระค่าลิขสิทธิ์ให้เจ้าของสิทธิ์", "label": 1},
 {"text": "ผู้ต้องหาทำซ้ำหนังสือและจัดจำหน่ายผ่านช่องทางออนไลน์", "label":
1},
 {"text": "จำเลยใช้ภาพกราฟิกที่มีลิขสิทธิ์ในโฆษณาโดยไม่ได้รับอนุญาต", "label": 1},
 {"text": "บริษัทเผยแพร่ซอฟต์แวร์เกมละเมิดลิขสิทธิ์ผ่านเว็บไซต์", "label": 1},
 {"text": "ผู้ต้องหาทำซ้ำฐานข้อมูลที่มีลิขสิทธิ์เพื่อใช้เชิงพาณิชย์", "label": 1},
 {"text": "จำเลยแปลหนังสือโดยไม่ได้รับอนุญาตและจัดพิมพ์จำหน่าย", "label":
1},
 {"text": "บริษัทนำเนื้อหาจากเว็บไซต์ที่มีลิขสิทธิ์มาเผยแพร่ซ้ำโดยไม่ได้รับอนุญาต", "label": 1},
 {"text": "ผู้ต้องหาเผยแพร่ภาพยนตร์ผ่าน IPTV ที่ไม่มีใบอนุญาต", "label":
1},
 {"text": "จำเลยทำซ้ำซอฟต์แวร์ออกแบบและจำหน่ายให้บริษัทอื่น", "label":
1},
 {"text": "บริษัทใช้เพลงพื้นหลังในสื่อโฆษณาโดยไม่ชำระค่าลิขสิทธิ์", "label": 1},
 {"text": "ผู้ต้องหาบันทึกและแจกจ่ายการแสดงสดโดยไม่ได้รับอนุญาต", "label":
1},
 {"text": "จำเลยขายซอฟต์แวร์ละเมิดลิขสิทธิ์ผ่านแพลตฟอร์มออนไลน์", "label":
1},
 {"text": "บริษัทจำเลยทำซ้ำแผนที่ดิจิทัลที่มีลิขสิทธิ์โดยไม่ได้รับอนุญาต", "label": 1},
 # CLASS 2: ไม่ละเมิด (6 ตัวอย่าง — MINORITY)
 {"text": "บริษัทได้รับอนุญาตให้ใช้สิทธิบัตรอย่างถูกต้องตามสัญญา", "label": 2},
 {"text": "ผู้ผลิตชำระค่าลิขสิทธิ์ครบถ้วนตามข้อตกลง", "label":
2},
 {"text": "การใช้ซอฟต์แวร์ในขอบเขตใบอนุญาตที่ได้รับมาโดยชอบ", "label":
2},
 {"text": "นักวิจัยใช้สิทธิบัตรเพื่อวัตถุประสงค์ทดลองทางวิทยาศาสตร์", "label": 2},
 {"text": "สิทธิบัตรหมดอายุแล้ว บริษัทจึงสามารถผลิตได้โดยอิสระ", "label":
2},
 {"text": "ศิลปินสร้างงานใหม่โดยอาศัยแนวคิดทั่วไปที่ไม่ได้รับการคุ้มครอง", "label": 2},
]
LABEL_NAMES = ["ละเมิดสิทธิบัตร", "ละเมิดลิขสิทธิ์", "ไม่ละเมิด"]
labels = [d["label"] for d in THAI_IP_DATASET]
print("Distribution:", Counter(labels))
# Counter({0: 40, 1: 20, 2: 6}) Imbalance ratio ≈ 6.7x

import re

class ThaiLegalTokenizer:
    def __init__(self, remove_stopwords=False):
        # รายการคำศัพท์กฎหมายประสม (เรียงจากยาวไปสั้นตามกฎ v3-3)[cite: 1]
        self.legal_compounds = sorted([
            "สิทธิบัตรการประดิษฐ์", "ละเมิดสิทธิบัตร", "ละเมิดลิขสิทธิ์", 
            "แบบอรรถประโยชน์", "อนุสิทธิบัตร", "โปรแกรมคอมพิวเตอร์", 
            "ไม่ได้รับอนุญาต", "จดทะเบียนสิทธิบัตร"
        ], key=len, reverse=True)
        
        # Stopwords ภาษาไทยเบื้องต้นสำหรับงานกฎหมาย
        self.stopwords = ["และ", "ที่", "จาก", "โดย", "มี", "ได้", "นำ"] if remove_stopwords else []

    def tokenize(self, text):
        # สร้าง Regex Pattern จากรายการคำประสม[cite: 1]
        pattern = "|".join(map(re.escape, self.legal_compounds))
        # ใช้ pattern ร่วมกับการดึงพยัญชนะไทยเบื้องต้น
        tokens = re.findall(pattern + r"|[ก-๙]+", text)
        
        if self.stopwords:
            tokens = [t for t in tokens if t not in self.stopwords]
        return tokens

# --- ทดสอบโจทย์ 1.1 ---[cite: 2]
tok = ThaiLegalTokenizer(remove_stopwords=True)
sentences = [
    "จำเลยผลิตและจำหน่ายสินค้าที่เลียนแบบสิทธิบัตรการประดิษฐ์",
    "บริษัทนำเข้าชิ้นส่วนที่ละเมิดสิทธิบัตรจากต่างประเทศ",
    "ผู้ต้องหาทำซ้ำโปรแกรมคอมพิวเตอร์มีลิขสิทธิ์โดยไม่ได้รับอนุญาต"
]

for s in sentences:
    print(f"Tokens: {tok.tokenize(s)}")


    from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

class W1Pipeline:
    def __init__(self, max_features=50):
        self.tokenizer = ThaiLegalTokenizer()
        self.vectorizer = TfidfVectorizer(
            tokenizer=self.tokenizer.tokenize,
            max_features=max_features,
            token_pattern=None
        )

    def transform(self, texts):
        X = self.vectorizer.fit_transform(texts)
        feature_names = self.vectorizer.get_feature_names_out()
        return X, feature_names

    def get_oov_report(self, texts):
        # วิเคราะห์ OOV tokens (คำที่ไม่อยู่ใน top max_features)[cite: 2]
        all_tokens = []
        for t in texts:
            all_tokens.extend(self.tokenizer.tokenize(t))
        
        unique_tokens = set(all_tokens)
        vocab = set(self.vectorizer.get_feature_names_out())
        oov = unique_tokens - vocab
        return list(oov)[:5] # แสดงตัวอย่าง 5 คำ

# --- ทดสอบโจทย์ 1.2 ---[cite: 2]
# ใช้ข้อมูลจาก THAI_IP_DATASET ในไฟล์ pdf
texts = [
    "จำเลยผลิตสินค้าที่เลียนแบบสิทธิบัตรการประดิษฐ์",
    "จำเลยทำซ้ำโปรแกรมคอมพิวเตอร์มีลิขสิทธิ์โดยไม่ได้รับอนุญาต",
    "บริษัทได้รับอนุญาตให้ใช้สิทธิบัตรอย่างถูกต้องตามสัญญา"
]
w1 = W1Pipeline(max_features=10)
X, features = w1.transform(texts)

print(f"TF-IDF Shape: {X.shape}") # (Samples, Features)[cite: 2]
print(f"OOV Samples: {w1.get_oov_report(texts)}")

class ThaiIPEntityExtractor:
    def __init__(self, use_context_aware=True):
        self.use_context = use_context_aware

    def extract(self, text):
        # จำลองการดึง Entity (PATENT, COPYRIGHT, VIOLATION)[cite: 1, 2]
        entities = []
        if any(kw in text for kw in ["สิทธิบัตร", "การประดิษฐ์"]):
            entities.append(type('Entity', (), {'entity_type': 'PATENT_SUBJECT'})())
        if any(kw in text for kw in ["ลิขสิทธิ์", "โปรแกรม"]):
            entities.append(type('Entity', (), {'entity_type': 'COPYRIGHT_SUBJECT'})())
        if any(kw in text for kw in ["ละเมิด", "เลียนแบบ", "ทำซ้ำ"]):
            entities.append(type('Entity', (), {'entity_type': 'VIOLATION_ACT'})())
        return entities

class ThaiLegalHierarchy:
    def compute_physics_gate_weight(self, entities, confidence=0.85):
        # คำนวณน้ำหนักสำหรับสั่งการ IoT Sensor[cite: 2]
        # อ้างอิงจาก v3-4 Physics Gate Weight Preview[cite: 1]
        base_weight = 0.0
        for ent in entities:
            if ent.entity_type == 'PATENT_SUBJECT': base_weight += 1.5
            if ent.entity_type == 'VIOLATION_ACT': base_weight += 2.0
            
        final_weight = base_weight * confidence
        return min(10.0, final_weight) # จำกัดค่าสูงสุดที่ 10.0[cite: 1]

# --- ทดสอบโจทย์ 1.3 ---[cite: 2]
extractor = ThaiIPEntityExtractor()
hierarchy = ThaiLegalHierarchy()

sample_text = "จำเลยผลิตสินค้าที่เลียนแบบสิทธิบัตรการประดิษฐ์"
entities = extractor.extract(sample_text)
weight = hierarchy.compute_physics_gate_weight(entities)

print(f"Weight: {weight:.2f}")
print(f"Entities: {[e.entity_type for e in entities]}")