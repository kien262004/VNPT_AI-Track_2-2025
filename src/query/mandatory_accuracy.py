# src/query/mandatory_accuracy.py
from __future__ import annotations
from typing import List
from langchain_core.messages import SystemMessage, HumanMessage
from .common import build_mcq_prompt, parse_answer_letter

SYSTEM = (
    "Bạn là trợ lý làm trắc nghiệm.\n"
    "CHỈ trả về 1 ký tự A/B/C/... tương ứng đáp án.\n"
    "Không giải thích.\n"
)

def solve_mandatory_accuracy(llm, question: str, choices: List[str]) -> str:
    # TẠM THỜI: chưa web, cứ gọi LLM small
    prompt = build_mcq_prompt(question, choices)
    resp = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=prompt)])
    raw = getattr(resp, "content", str(resp))
    return parse_answer_letter(raw, num_choices=len(choices))
