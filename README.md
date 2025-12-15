# Hướng thực hiện
- Sử dụng Module Router nhằm phân tách các task, mỗi task 1 cách thực hiện
- `Math_Logical_Reasoning`: Cần yêu cầu llm sinh theo từ cơ sở 1, có thể lưu các định lý, công thức nếu cần
- `Mandatory_Accuracy_Questions`, `Various_Domain`: Cần truy vấn thông tin web để củng cố thông tin lựa chọn
- `Restricted`: Cần xác định được câu nhạy cảm để lựa chọn (Gợi ý: có thể dựa vào các lựa chọn nếu có lựa chọn ko trả lời, ta có thể suy đoán)
- `Long_Text_Questions`: chia chunk đoạn văn và RAG đoạn văn đấy.

# Pipeline:
1. Crawl

Phần crawl sẽ tạo cơ sở dữ liệu cho task: `Math_Logical_Reasoning`, `Mandatory_Accuracy_Questions`, `Various_Domain`.
```
- Route ->  |-- Math_Logical_Reasoning -> Search web câu hỏi -> tìm các bổ để, ĐL, CT -> embedding
            |
            |-- Mandatory_Accuracy_Questions |
            |                                |--> Sinh thông tin cần truy xuất --> Crawl web -> Embedding
            |-- Various_Domain               |
```
2. Query
```
- Route -> |-- Restricted -> Chọn từ chối
           |-- Math_Logical_Reasoning -> Dùng Prompt Chain of thought (kết hợp RAG logic)
           |-- Mandatory_Accuracy_Questions -> RAG 
           |-- Various_Domain -> RAG
           |-- Long_Text_Questions -> RAG trên văn bản
```

---

## 📚 Long Text Questions Handler (ĐÃ TRIỂN KHAI)

### Mô tả
Xử lý câu hỏi có văn bản dài (>500 từ) bằng RAG (Retrieval-Augmented Generation) với VNPT Embedding API.

### Kiến trúc

```
Long Text Question
       ↓
[RAG Handler] → Chunk văn bản (300 words, 50 overlap)
       ↓
[VNPT Embedding API] → Vector embeddings
       ↓
Cosine Similarity → Retrieve top-k chunks
       ↓
[Large LLM] → Answer (A/B/C/D)
```

### Các file đã tạo

#### 1. **`src/core/embedder.py`**
Wrapper cho VNPT Embedding API để tạo vector embeddings.

**Chức năng:**
- `embed_text()`: Tạo embedding cho 1 đoạn text
- `embed_batch()`: Batch embedding nhiều chunks cùng lúc
- `cosine_similarity()`: Tính similarity giữa 2 vectors
- **Retry logic**: Tự động retry 3 lần khi timeout
- **Timeout**: 60s (tránh API quá tải)

**Credentials cần thiết** (trong `.env`):
```env
AUTHORIZATION_VNPT_EMBEDDING=Bearer <token>
TOKEN_ID_VNPT_EMBEDDING=<token_id>
TOKEN_KEY_VNPT_EMBEDDING=<token_key>
```

#### 2. **`src/core/rag_handler.py`**
Xử lý RAG pipeline hoàn chỉnh.

**Chức năng:**
- Chunk văn bản dài thành các đoạn nhỏ (sliding window)
- Hỗ trợ 2 chế độ retrieval:
  - **Embedding-based** (mặc định): Sử dụng VNPT Embedding + cosine similarity
  - **Keyword-based** (fallback): Đếm từ khóa chung khi embedding lỗi
- Trả về context thu gọn cho LLM

**Tham số:**
```python
RAGHandler(
    chunk_size=300,      # Kích thước chunk (words)
    chunk_overlap=50,    # Overlap giữa chunks
    top_k=3,             # Số chunks retrieve
    use_embedding=True   # True: embedding, False: keywords
)
```

#### 3. **`query/long_text_handler.py`**
Handler chính để xử lý batch câu hỏi Long_Text.

**Chức năng:**
- Đọc `data/val_routed.json` → lọc Long_Text_Questions
- Xử lý từng câu: RAG → LLM → Predict
- Resume logic: Tự động skip câu đã xử lý
- Lưu kết quả vào `data/long_text_results.json`
- Rate limiting: Dừng khi đạt max API calls

**Chạy:**
```bash
python query/long_text_handler.py --max-calls 50
```

**Output:** `data/long_text_results.json`
```json
{
  "val_0001": {
    "qid": "val_0001",
    "predicted_answer": "B",
    "raw_response": "B",
    "timestamp": "2025-12-15T10:30:45"
  }
}
```

#### 4. **`evaluate.py`**
Script đánh giá accuracy so với ground truth.

**Chức năng:**
- So sánh predictions với đáp án đúng trong `val_routed.json`
- Tính accuracy tổng thể
- Hiển thị danh sách câu đúng/sai
- Lưu báo cáo vào `data/evaluation_report.json`

**Chạy:**
```bash
python evaluate.py
```

**Output:**
```
========================================
EVALUATION REPORT
========================================
Total questions: 20
Correct: 16
Incorrect: 4
Accuracy: 80.00%
```

#### 5. **`test_rag.py`**
Demo so sánh 2 phương pháp RAG.

**Chức năng:**
- Test song song keyword matching vs embedding-based
- Hiển thị context thu gọn và similarity scores
- Dùng để debug và verify RAG logic

**Chạy:**
```bash
python test_rag.py
```

### Kết quả hiện tại
- ✅ **20/20 câu Long_Text** đã được xử lý
- 📊 **Accuracy**: 80% với embedding-based RAG
- 🚀 **Cải tiến**: Từ keyword matching → VNPT Embedding API

### Cấu trúc thư mục
```
VNPT_AI-Track_2-2025/
├── query/
│   ├── long_text_handler.py    # Handler chính
│   └── __init__.py
├── src/
│   └── core/
│       ├── embedder.py          # VNPT Embedding wrapper
│       ├── rag_handler.py       # RAG pipeline
│       ├── llm.py               # VNPT LLM wrappers (timeout 60s)
│       └── __init__.py
├── data/
│   ├── val_routed.json          # Input questions
│   └── long_text_results.json   # Output predictions
├── evaluate.py                  # Evaluation script
├── test_rag.py                  # RAG comparison demo
└── requirements.txt             # Dependencies (numpy added)
```

### Dependencies mới
```txt
numpy>=1.24.0  # Cho cosine similarity tính toán
```

### Cách chạy đầy đủ
```bash
# 1. Xử lý tất cả Long_Text questions
python query/long_text_handler.py --max-calls 50

# 2. Đánh giá kết quả
python evaluate.py

# 3. Test so sánh RAG methods (optional)
python test_rag.py
```

### Next steps
- [ ] Implement handlers cho 4 loại còn lại:
  - `query/math_handler.py` (Math_Logical_Reasoning)
  - `query/mandatory_handler.py` (Mandatory_Accuracy_Questions)
  - `query/various_handler.py` (Various_Domain)
  - `query/restricted_handler.py` (Restricted_Questions)
- [ ] Merge tất cả results vào `submission.csv`
- [ ] Optimize RAG parameters (chunk_size, top_k, etc.)