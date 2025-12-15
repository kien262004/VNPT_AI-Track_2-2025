# Query Handlers

Folder này chứa các handlers xử lý từng loại câu hỏi đã được phân loại bởi Router.

## 📁 Cấu trúc

```
query/
├── __init__.py                  # Export handlers
├── long_text_handler.py         # ✅ Long Text Questions
├── math_handler.py              # 🔜 Math & Logical Reasoning
├── mandatory_handler.py         # 🔜 Mandatory Accuracy Questions
├── various_handler.py           # 🔜 Various Domain
└── restricted_handler.py        # 🔜 Restricted Questions
```

## 🎯 Nhiệm vụ từng handler

| Handler | Datasource | Strategy |
|---------|-----------|----------|
| `long_text_handler.py` | Long_Text_Questions | RAG + Chunking |
| `math_handler.py` | Math_Logical_Reasoning | Chain of Thought |
| `mandatory_handler.py` | Mandatory_Accuracy_Questions | RAG + Fact Check |
| `various_handler.py` | Various_Domain | Multi-domain RAG |
| `restricted_handler.py` | Restricted_Questions | Auto-reject |

## 🚀 Cách dùng

### Import trong code:

```python
from query import LongTextQueryHandler

handler = LongTextQueryHandler()
handler.process_batch("data/val_routed.json", "data/long_text_results.json")
```

### Chạy trực tiếp:

```bash
python query/long_text_handler.py \
  --input data/val_routed.json \
  --output data/long_text_results.json \
  --max-calls 50
```

## 📋 Input/Output Format

### Input (val_routed.json):
```json
[
  {
    "qid": "q001",
    "question": "...",
    "choices": ["A", "B", "C"],
    "datasource": "Long_Text_Questions",
    "reasoning": "..."
  }
]
```

### Output (long_text_results.json):
```json
[
  {
    "qid": "q001",
    "answer": "B",
    "question": "...",
    "datasource": "Long_Text_Questions"
  }
]
```

## ⚙️ Configuration

Mỗi handler có thể config riêng:

```python
handler = LongTextQueryHandler(
    llm_type="large_vnpt",
    llm_cfg={
        "temperature": 0.0,
        "top_p": 1.0,
        "top_k": 20,
        "max_tokens": 128,
    },
    rag_chunk_size=300,
    rag_chunk_overlap=50,
    rag_top_k=3
)
```

## 🔧 Tạo handler mới

Template cho handler mới:

```python
class NewTypeHandler:
    def __init__(self, llm_type="large_vnpt", llm_cfg=None):
        self.llm = get_llm(llm_type, cfg=llm_cfg)
        # Setup strategy-specific components
    
    def process_single_question(self, item: dict) -> str:
        # Xử lý 1 câu hỏi
        return answer_letter
    
    def process_batch(self, input_file: str, output_file: str, max_calls: int):
        # Xử lý batch từ file
        pass
```

## 📊 Status

- ✅ **Long Text Handler**: Hoàn thiện, có thể dùng
- 🔜 **Math Handler**: Cần implement
- 🔜 **Mandatory Handler**: Cần implement
- 🔜 **Various Handler**: Cần implement
- 🔜 **Restricted Handler**: Cần implement

## 🐛 Debug

Test handler:
```bash
python query/long_text_handler.py --max-calls 5
```

Xem kết quả:
```bash
cat data/long_text_results.json | jq .
```
