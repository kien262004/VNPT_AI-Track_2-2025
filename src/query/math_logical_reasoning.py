# src/query/math_logical_reasoning.py
from __future__ import annotations
from typing import List, Optional
from langchain_core.messages import SystemMessage, HumanMessage

from .common import build_mcq_prompt, parse_answer_letter

SYSTEM = """Bạn là trợ lý giải Toán/Logic cho câu hỏi trắc nghiệm.

YÊU CẦU SUY LUẬN (làm trong đầu, KHÔNG được in ra):
1) Xác định dạng bài và công thức/định lý liên quan.
2) Biến đổi/tính toán cẩn thận đến kết quả cuối.
3) Kiểm tra điều kiện, miền giá trị, dấu, nghiệm ngoại lai nếu có.
4) So khớp kết quả với các lựa chọn A, B, C, ...

QUY TẮC TRẢ LỜI:
- Chỉ trả về DUY NHẤT 1 ký tự chữ cái đáp án (A/B/C/...), KHÔNG thêm gì khác.
- Không giải thích, không thêm dấu chấm, không thêm ký tự.
"""

def solve_math_logical(
    llm,
    question: str,
    choices: List[str],
    rag_context: Optional[str] = None,
) -> str:
    sys = SYSTEM
    if rag_context:
        # Sau này bạn cắm RAG cho toán/logic (ví dụ định lý ít gặp, bài đặc biệt)
        sys = sys + "\n\nNGỮ CẢNH BỔ SUNG (RAG):\n" + rag_context

    prompt = build_mcq_prompt(question, choices)
    resp = llm.invoke([SystemMessage(content=sys), HumanMessage(content=prompt)])
    raw = getattr(resp, "content", str(resp))
    return parse_answer_letter(raw, num_choices=len(choices))
