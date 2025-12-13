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