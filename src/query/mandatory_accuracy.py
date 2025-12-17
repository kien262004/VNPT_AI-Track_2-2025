# src/query/mandatory_accuracy.py
from __future__ import annotations
from typing import List
from langchain_core.messages import SystemMessage, HumanMessage
from .common import build_mcq_prompt, parse_answer_letter
import json

SYSTEM = """
Bạn là một hệ thống trả lời câu hỏi trắc nghiệm.

Nhiệm vụ của bạn:
1. Đọc kỹ CÂU HỎI và các PHƯƠNG ÁN TRẢ LỜI.
2. Đọc THÔNG TIN BỔ SUNG được cung cấp.
3. Ưu tiên tìm bằng chứng trực tiếp trong THÔNG TIN BỔ SUNG để chọn **1 đáp án đúng nhất**.
4. Nếu THÔNG TIN BỔ SUNG không chứa thông tin liên quan hoặc không đủ để trả lời, hãy **tự suy luận một cách hợp lý** dựa trên kiến thức chung.
5. Chỉ chọn **một** đáp án.

Yêu cầu đầu ra:
- Trả về **định dạng JSON hợp lệ**
- Bao gồm đúng **2 trường**:
  - "thinking": giải thích ngắn gọn quá trình suy luận (nêu rõ có dùng thông tin bổ sung hay suy luận).
  - "answer": đáp án cuối cùng (ví dụ: "A", "B", "C", hoặc "D").
"""

def solve_mandatory_accuracy(llm, 
                             question: str, 
                             choices: List[str], 
                             rag_contexts: List[str] = None,
                             debug=False) -> str:
    # TẠM THỜI: chưa web, cứ gọi LLM small
    prompt = build_mcq_prompt(question, choices, rag_contexts)

    resp = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=prompt)])
    raw = getattr(resp, "content", str(resp))
    
    try:
        raw = json.loads(raw.encode())
        if debug:
            print(raw['thinking'])
        raw = raw['answer']
    except:
        print('ERROR: không đúng định dạng json')
        raw = "A"
    return parse_answer_letter(raw, num_choices=len(choices))
