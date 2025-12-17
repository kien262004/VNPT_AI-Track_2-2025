# src/query/restricted.py
from __future__ import annotations
from typing import List, Optional

REFUSAL_KEYWORDS_STRONG = [
    "tôi không thể", "không thể", "không cung cấp", "không chia sẻ",
    "không được phép", "xin lỗi", "từ chối", "không hỗ trợ",
    "không thể trả lời", "không thể giúp", "không thể hướng dẫn",
]

REFUSAL_KEYWORDS_WEAK = [
    "an toàn", "phù hợp", "thuần phong", "không phù hợp", "vi phạm",
    "không thể đáp ứng", "không có thông tin",
]

def _score_choice(text: str) -> int:
    t = (text or "").strip().lower()
    score = 0
    for k in REFUSAL_KEYWORDS_STRONG:
        if k in t:
            score += 5
    for k in REFUSAL_KEYWORDS_WEAK:
        if k in t:
            score += 2
    return score

def find_refusal_choice_letter(choices: List[str]) -> Optional[str]:
    best_i = None
    best_score = 0
    for i, c in enumerate(choices):
        s = _score_choice(c)
        if s > best_score:
            best_score = s
            best_i = i
    if best_i is None or best_score < 3:
        return None
    return chr(ord("A") + best_i)

def solve_restricted(llm, question: str, choices: List[str], context: List[str], debug=False) -> str:
    """
    Restricted handler: KHÔNG gọi LLM.
    - Nếu có phương án từ chối: chọn nó
    - Nếu không có: fallback ("" hoặc "A")
    """
    letter = find_refusal_choice_letter(choices)
    if letter is not None:
        return letter

    # Fallback: nếu BTC bắt buộc chữ cái -> "A", còn nếu cho phép trống -> ""
    return "A"
