# src/query/math_logical_reasoning.py
from __future__ import annotations
from typing import List, Optional
import json
from langchain_core.messages import SystemMessage, HumanMessage

from .common import build_mcq_prompt, parse_answer_letter

SYSTEM = """Bạn là trợ lý giải Toán/Logic cho câu hỏi trắc nghiệm.

YÊU CẦU SUY LUẬN (làm trong đầu):
1) Xác định dạng bài và công thức/định lý liên quan.
2) Thực hiện biến đổi và tính toán để tìm kết quả.
3) Kiểm tra điều kiện xác định, miền giá trị, dấu, nghiệm ngoại lai (nếu có).
4) So khớp kết quả với các phương án A, B, C, ...

QUY TẮC TRẢ LỜI:
- Trả về DUY NHẤT một JSON hợp lệ.
- JSON chỉ gồm 2 trường:
  - "thinking": mô tả NGẮN GỌN hướng suy luận.
  - "answer": 1 ký tự chữ cái đáp án đúng (A/B/C/...).
"""

def solve_math_logical(
    llm,
    question: str,
    choices: List[str],
    rag_context: Optional[str] = None,
    debug=False
) -> str:
    sys = SYSTEM

    prompt = build_mcq_prompt(question, choices, rag_context)
    resp = llm.invoke([SystemMessage(content=sys), HumanMessage(content=prompt)])
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
