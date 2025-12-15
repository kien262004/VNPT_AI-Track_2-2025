# src/query/long_text_questions.py
from __future__ import annotations
from typing import List
from langchain_core.messages import SystemMessage, HumanMessage
from .common import build_mcq_prompt, parse_answer_letter

SYSTEM = (
    "Bạn là trợ lý làm trắc nghiệm.\n"
    "CHỈ trả về 1 ký tự A/B/C/... tương ứng đáp án.\n"
    "Không giải thích.\n"
)

def _is_policy_block(e: Exception) -> bool:
    s = str(e).lower()
    return ("badrequesterror" in s) or ("không thể trả lời" in s) or ("thuần phong mỹ tục" in s)

def solve_long_text(llm, question: str, choices: list) -> str:
    prompt = build_mcq_prompt(question, choices)
    try:
        resp = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=prompt)])
        raw = getattr(resp, "content", str(resp))
        return parse_answer_letter(raw, len(choices))
    except Exception as e:
        # nếu bị policy block do từ khóa bạo lực/hành hình... -> fallback A (hoặc "")
        if _is_policy_block(e):
            return "A"
        # lỗi khác thì cũng fallback A để không crash pipeline
        return "A"
