# src/query/common.py
from __future__ import annotations
from typing import List

def idx_to_letter(i: int) -> str:
    return chr(ord("A") + i)

def build_mcq_prompt(question: str, choices: List[str], contexts: List[str] = None) -> str:
    lines = [f"Câu hỏi: {question}", "", "Các lựa chọn:"]
    for i, c in enumerate(choices):
        lines.append(f"{idx_to_letter(i)}. {c}")
    lines.append("")
    lines.append("CHỈ trả lời DUY NHẤT 1 ký tự là chữ cái đáp án (A, B, C, ...).")
    if contexts is not None:
        lines.append("\nCác thông tin bổ trợ:")
        for context in contexts:
            lines.append(context)
    return "\n".join(lines)

def parse_answer_letter(raw: str, num_choices: int) -> str:
    if not raw:
        return "A"
    s = raw.strip().upper()
    if len(s) == 1 and "A" <= s <= "Z":
        k = ord(s) - ord("A")
        if 0 <= k < num_choices:
            return s
    for ch in s:
        if "A" <= ch <= "Z":
            k = ord(ch) - ord("A")
            if 0 <= k < num_choices:
                return ch
    return "A"
