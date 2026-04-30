import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np
import torch 
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE, RandomOverSampler
from collections import Counter

# 1. Shadow Data Augmentation (จำลองรายงานการปรากฏตัวของเกต)
HUNTER_SYNONYMS = {
    "มอนสเตอร์": ["อสูรเวท", "สิ่งมีชีวิตมิติอื่น", "บอสประจำชั้น"],
    "เกต": ["รอยแยกมิติ", "ดันเจี้ยน", "ประตูสีน้ำเงิน"],
    "จู่โจม": ["กวาดล้าง", "เคลียร์ดันเจี้ยน", "ล่า"],
    "อันตราย": ["ระดับหายนะ", "ความกดดันมหาศาล"]
}

def augment_shadow_text(text):
    words = text.split()
    new_words = words.copy()
    for i, word in enumerate(words):
        if word in HUNTER_SYNONYMS:
            new_words[i] = random.choice(HUNTER_SYNONYMS[word])
    return " ".join(new_words)

# --- ตัวอย่างการใช้งาน ---
report = "ฮันเตอร์ เตรียม จู่โจม มอนสเตอร์ ใน เกต"
print(f"Original Report: {report}")
print(f"Shadow Augmented: {augment_shadow_text(report)}\n")

# 2. SMOTE with Fallback (จัดการข้อมูลระดับ S-Rank ที่หาได้ยาก)
def balance_hunter_data(X, y):
    counts = Counter(y)
    min_samples = min(counts.values())
    # ถ้าคลาสหายากมีมากกว่า 1 แต่ไม่พอสำหรับ SMOTE มาตรฐาน จะปรับ k_neighbors
    if min_samples > 1:
        sampler = SMOTE(k_neighbors=min(2, min_samples-1), random_state=42)
    else:
        sampler = RandomOverSampler(random_state=42)
    X_res, y_res = sampler.fit_resample(X, y)
    return X_res, y_res

# จำลองข้อมูล: E-Rank=20, A-Rank=5, S-Rank=2 (Imbalance สุดๆ)
X_mock = np.random.randn(27, 10) 
y_mock = np.array([0]*20 + [1]*5 + [2]*2) 
X_res, y_res = balance_hunter_data(X_mock, y_mock)

# แปลงเป็น 3D Tensor สำหรับ LSTM (Batch, Seq_len, Input_size)
X_res_3d = torch.tensor(X_res, dtype=torch.float32).unsqueeze(1)
y_res_tensor = torch.tensor(y_res, dtype=torch.long)

# 3. Model Architecture: Shadow-BiLSTM
class ShadowBiLSTM(nn.Module):
    def __init__(self, input_dim=10, hidden_dim=32, output_dim=3):
        super(ShadowBiLSTM, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_dim * 2, output_dim)
        nn.init.xavier_uniform_(self.fc.weight)

    def forward(self, x):
        lstm_out, _ = self.lstm(x)
        # Mean Pooling วิเคราะห์บรรยากาศโดยรวมของมานา
        pooled = torch.mean(lstm_out, dim=1)
        return self.fc(pooled)

# 4. Train and Evaluate with "System Notification"
def train_shadow_system(model_class, name, X, y, class_names):
    model = model_class()
    # ให้ Weight กับ S-Rank มากเป็นพิเศษ (ป้องกันการประเมินต่ำเกินไปจนฮันเตอร์ตาย)
    weights = torch.tensor([1.0, 4.0, 10.0]) 
    criterion = nn.CrossEntropyLoss(weight=weights)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.02)

    for epoch in range(60):
        model.train()
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

    # Evaluation
    model.eval()
    with torch.no_grad():
        logits = model(X)
        probs = F.softmax(logits, dim=1)
        y_pred = torch.argmax(probs, dim=1).numpy()
        
    # --- Shadow Extraction Logic ---
    # ถ้าความมั่นใจ (Confidence) ต่ำกว่า 0.7 หรือทายผิด ระบบจะทำ 'Wake Up' เปลี่ยนเป็นเงา
    shadow_count = 0
    for i in range(len(y)):
        confidence = probs[i][y_pred[i]].item()
        if confidence < 0.7 or y_pred[i] != y[i]:
            shadow_count += 1
            
    print(f"--- [SYSTEM NOTIFICATION: {name}] ---")
    print(f"Dungeons Cleared. Shadow Soldiers Extracted: {shadow_count}")
    
    # Heat Map
    cm = confusion_matrix(y, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap="Purples", xticklabels=class_names, yticklabels=class_names)
    plt.title(f"Rank Classification: {name}")
    plt.ylabel("Actual Rank")
    plt.xlabel("Predicted Rank")
    plt.show()

# รันระบบ
class_list = ['E-RANK', 'A-RANK', 'S-RANK']
train_shadow_system(ShadowBiLSTM, "Sung Jin-Woo's Perception", X_res_3d, y_res_tensor, class_list)