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

import numpy as np

# ============================================================
# 3.1 Sinusoidal Positional Encoding
# ============================================================
class SinusodalPositionEncoding:
    def __init__(self, max_seq_len=10, d_model=16):
        pe = np.zeros((max_seq_len, d_model))
        pos = np.arange(max_seq_len).reshape(-1, 1)
        # สูตรมาตรฐาน: 10000^(2i/d_model)[cite: 2]
        div = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))
        
        pe[:, 0::2] = np.sin(pos * div)
        pe[:, 1::2] = np.cos(pos * div)
        self.pe = pe

    def encode(self, X):
        return X + self.pe[:X.shape[0], :]

    def show_with_words(self, words):
        print(f"\n{'index':<7} | {'word':<10} | {'Positional Encoding (First 4 dims)':<40}")
        print("-" * 70)
        for i, word in enumerate(words):
            if i >= len(self.pe): break
            vec = self.pe[i, :4]
            vec_str = " ".join(f"{v:+.3f}" for v in vec)
            print(f"Pos_{i:<3} | {word:<10} | [{vec_str}...]")

# ============================================================
# 3.2 & 3.3 Multi-Head Attention (Pre-Norm & Causal Mask)
# ============================================================
def scale_dot_product_attention(Q, K, V, causal_mask=None):
    d_k = Q.shape[-1]
    # Scaled Dot-Product: (Q @ K.T) / sqrt(d_k)[cite: 2]
    scores = np.matmul(Q, K.transpose(0, 2, 1)) / np.sqrt(d_k)

    if causal_mask is not None:
        # ใช้ -1e9 เพื่อให้ Softmax กลายเป็น 0 ในตำแหน่งที่ถูก Mask[cite: 2]
        scores = np.where(causal_mask, -1e9, scores)

    exp_s = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    weights = exp_s / exp_s.sum(axis=-1, keepdims=True)
    return np.matmul(weights, V), weights

class MultiHeadAttentionSimple:
    def __init__(self, d_model=16, n_heads=4, seed=42):
        rng = np.random.RandomState(seed)
        self.n_heads = n_heads
        self.d_k = d_model // n_heads
        
        self.W_q = rng.randn(d_model, d_model) * 0.1
        self.W_k = rng.randn(d_model, d_model) * 0.1
        self.W_v = rng.randn(d_model, d_model) * 0.1
        self.W_o = rng.randn(d_model, d_model) * 0.1

    def split_heads(self, x, batch, seq):
        return x.reshape(batch, seq, self.n_heads, self.d_k).transpose(0, 2, 1, 3)

    def forward(self, x, causal_mask=None, return_weights=False):
        if x.ndim == 2: x = x[np.newaxis, :]
        batch, seq, d_model = x.shape
        
        # Pre-Norm: Normalize ก่อนทำ Attention[cite: 2]
        x_norm = (x - x.mean(axis=-1, keepdims=True)) / (x.std(axis=-1, keepdims=True) + 1e-6)

        Q = self.split_heads(np.matmul(x_norm, self.W_q), batch, seq)
        K = self.split_heads(np.matmul(x_norm, self.W_k), batch, seq)
        V = self.split_heads(np.matmul(x_norm, self.W_v), batch, seq)

        Q_r = Q.reshape(-1, seq, self.d_k)
        K_r = K.reshape(-1, seq, self.d_k)
        V_r = V.reshape(-1, seq, self.d_k)
        
        cm = None
        if causal_mask is not None:
            cm = np.tile(causal_mask, (batch * self.n_heads, 1, 1))

        out_r, weights_r = scale_dot_product_attention(Q_r, K_r, V_r, cm)

        # Combine Heads
        out = out_r.reshape(batch, self.n_heads, seq, self.d_k).transpose(0, 2, 1, 3).reshape(batch, seq, d_model)
        
        # Residual Connection: บวก x เดิมกลับเข้าไป[cite: 2]
        output = np.matmul(out, self.W_o) + x
        
        output = output.squeeze(0)
        weights = weights_r.reshape(batch, self.n_heads, seq, seq).squeeze(0)
        
        return (output, weights) if return_weights else output

# ============================================================
# 3.4 XAI & Physics Gate Analysis
# ============================================================
def explainable_attention(tokens, weights):
    # เฉลี่ยน้ำหนักจากทุก Head เพื่อดูความสำคัญรายคำ[cite: 2]
    avg_importance = weights.mean(axis=0).mean(axis=0)
    
    print("\n--- XAI : Legal Entity Importance Analysis ---")
    for i, token in enumerate(tokens):
        score = avg_importance[i]
        bar = "█" * int(score * 40)
        print(f"{token:<12} | {bar} ({score:.4f})")

# ============================================================
# EXECUTION (รันโจทย์ 3.1 - 3.4)
# ============================================================
if __name__ == "__main__":
    print("=== Workshop W3: Attention & Transformer ===")
    
    # โจทย์ 3.1: Positional Encoding
    tokens = ["จำเลย", "ผลิต", "สินค้า", "ละเมิด", "สิทธิบัตร"]
    pe_gen = SinusodalPositionEncoding(max_seq_len=10, d_model=16)
    pe_gen.show_with_words(tokens)

    # โจทย์ 3.2: Multi-Head Attention Shape Analysis
    X_input = np.random.randn(5, 16) 
    mha = MultiHeadAttentionSimple(d_model=16, n_heads=4)
    out_enc, w_enc = mha.forward(X_input, return_weights=True)
    
    print(f"\n[3.2] Input Shape  : {X_input.shape}")
    print(f"[3.2] Output Shape : {out_enc.shape}")
    print(f"[3.2] Weights Shape: {w_enc.shape} (Heads, Seq, Seq)")

    # โจทย์ 3.3: Causal Mask (Decoder)
    # สร้าง Mask สำหรับป้องกันการมองเห็นอนาคต[cite: 1, 2]
    causal_mask = np.triu(np.ones((5, 5), dtype=bool), k=1)
    out_dec, w_dec = mha.forward(X_input, causal_mask=causal_mask, return_weights=True)
    
    print(f"\n[3.3] Causal Mask Pattern (True = Masked):")
    print(causal_mask.astype(int))

    # โจทย์ 3.4: XAI Analysis
    explainable_attention(tokens, w_enc)
    
    # Physics Gate Simulation (โจทย์ 1.3/3.4)
    confidence = 0.85
    base_weight = 1.3 # สำหรับคำว่า 'ผลิต'
    # จำลองค่า attention ที่ได้จากโมเดลสำหรับคำว่า 'ผลิต' (index 1)
    attn_score = w_enc.mean(axis=0).mean(axis=0)[1] 
    physics_score = min(2.0, base_weight * attn_score * confidence)
    print(f"\n[3.4] Physics Score for 'ผลิต': {physics_score:.4f}")
    if physics_score > 0.4:
        print(">> Trigger: MANUFACTURING SENSOR ACTIVATED!")