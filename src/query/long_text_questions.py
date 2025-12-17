# src/query/long_text_questions.py
"""
Long_Text_Questions handler (theo logic long_text_handler.py của team bạn).

- Thử áp dụng RAGHandler.process(question) để lấy (context, refined_question)
- Nếu RAG fail -> dùng prompt thường
- Gọi LLM (llm được truyền từ predict.py)
- Nếu VNPT từ chối (text) hoặc BadRequestError -> return "" (đúng như handler của bạn bạn)
- Parse trả về 1 chữ cái A/B/C/...
"""

from __future__ import annotations
from typing import List, Optional, Tuple
import numpy as np
import json
from langchain_core.messages import SystemMessage, HumanMessage
from .common import build_mcq_prompt, parse_answer_letter
from ..core import VNPTAIEmbeddingClient

# ===== Optional RAGHandler (nếu project có) =====
_RAG = None

def _get_rag_handler():
    """
    Lazy init RAGHandler nếu tồn tại.
    Nếu chưa có rag/không import được -> trả None và handler sẽ fallback prompt thường.
    """
    global _RAG
    if _RAG is not None:
        return _RAG

    try:
        # Nếu dự án bạn có RAGHandler đúng tên/class
        from src.core import RAGHandler  # type: ignore
        _RAG = RAGHandler(chunk_size=300, chunk_overlap=50, top_k=3)
        return _RAG
    except Exception:
        _RAG = None
        return None


SYSTEM_PROMPT = """
Bạn là trợ lý làm bài trắc nghiệm nhiều lựa chọn.

Bạn sẽ được cung cấp một đoạn văn bản và một câu hỏi liên quan.
Hãy đọc kỹ đoạn văn và chọn ĐÚNG MỘT đáp án.

YÊU CẦU SUY LUẬN:
- Ưu tiên tìm thông tin trực tiếp trong đoạn văn để trả lời.
- Nếu không có thông tin rõ ràng, hãy suy luận hợp lý dựa trên ngữ cảnh và kiến thức chung.

QUY TẮC BẮT BUỘC VỀ OUTPUT:
- Chỉ trả về DUY NHẤT một JSON hợp lệ.
- JSON chỉ gồm 2 trường:
  - "thinking": mô tả NGẮN GỌN hướng suy luận (không trích dẫn dài, không liệt kê phương án).
  - "answer": duy nhất MỘT ký tự chữ cái của đáp án đúng (A, B, C, D, ...).
"""


# def _build_rag_prompt(context: str, question: str, choices: List[str]) -> str:
#     lines = [
#         "Dựa vào đoạn văn sau:",
#         "",
#         context,
#         "",
#         f"Câu hỏi: {question}",
#         "",
#         "Các lựa chọn:",
#     ]
#     for idx, choice in enumerate(choices):
#         letter = chr(ord("A") + idx)
#         lines.append(f"{letter}. {choice}")

#     lines.append("")
#     lines.append("Hãy trả lời CHỈ MỘT ký tự là chữ cái của đáp án đúng (A, B, C, ...).")
#     return "\n".join(lines)


# def _build_standard_prompt(question: str, choices: List[str]) -> str:
#     lines = [f"Câu hỏi: {question}", "", "Các lựa chọn:"]
#     for idx, choice in enumerate(choices):
#         letter = chr(ord("A") + idx)
#         lines.append(f"{letter}. {choice}")

#     lines.append("")
#     lines.append("Hãy trả lời CHỈ MỘT ký tự là chữ cái của đáp án đúng (A, B, C, ...).")
#     return "\n".join(lines)


# def _parse_answer(raw_answer: str, num_choices: int) -> str:
#     """
#     Parse theo đúng style của long_text_handler.py:
#     - Nếu raw chỉ 1 ký tự A..Z hợp lệ -> dùng
#     - Else: lấy ký tự A..Z hợp lệ đầu tiên trong output
#     - Fallback: "A"
#     """
#     if not raw_answer:
#         return "A"

#     text = raw_answer.strip().upper()

#     if len(text) == 1 and "A" <= text <= "Z":
#         idx = ord(text) - ord("A")
#         if 0 <= idx < num_choices:
#             return text

#     for ch in text:
#         if "A" <= ch <= "Z":
#             idx = ord(ch) - ord("A")
#             if 0 <= idx < num_choices:
#                 return ch

#     return "A"


# def _is_sensitive_text(raw_answer: str) -> bool:
#     t = (raw_answer or "").lower()
#     return ("không thể trả lời" in t) or ("không thể phản hồi" in t)


# def _is_sensitive_badrequest_error(e: Exception) -> bool:
#     msg = str(e)
#     return ("VNPT API logical error response" in msg) and ("BadRequestError" in msg)


# def solve_long_text(llm, question: str, choices: List[str]) -> str:
#     """
#     Entry cho predict.py: trả về answer letter.
#     Lưu ý: theo handler bạn bạn, nếu bị VNPT từ chối -> return "".
#     """
#     # 1) thử RAG
#     prompt: str
#     rag = _get_rag_handler()
#     if rag is not None:
#         try:
#             context, refined_question = rag.process(question)  # type: ignore
#             if context and refined_question:
#                 prompt = _build_rag_prompt(context, refined_question, choices)
#             else:
#                 prompt = _build_standard_prompt(question, choices)
#         except Exception:
#             prompt = _build_standard_prompt(question, choices)
#     else:
#         prompt = _build_standard_prompt(question, choices)

#     # 2) gọi LLM
#     messages = [
#         SystemMessage(content=SYSTEM_PROMPT),
#         HumanMessage(content=prompt),
#     ]

#     try:
#         ai_msg = llm.invoke(messages)
#         raw_answer = getattr(ai_msg, "content", str(ai_msg))

#         # 3) nếu VNPT “từ chối” bằng nội dung -> return "" (đúng logic bạn bạn)
#         if _is_sensitive_text(raw_answer):
#             return ""

#         # 4) parse letter
#         return _parse_answer(raw_answer, len(choices))

#     except Exception as e:
#         # VNPT policy block -> return ""
#         if _is_sensitive_badrequest_error(e):
#             return ""
#         # Lỗi khác: để an toàn pipeline không crash, fallback "A"
#         return "A"
    
def count_words(text: str) -> int:
    words = text.strip().split()
    return len(words)

def split_query(query: str):
    info = query['question'].split("Câu hỏi:")
    context = info[0].split('\n\n')
    question = info[1]
    
    chunk = []
    for i, raw_chunk in enumerate(context):
        print(count_words(raw_chunk))
        if count_words(raw_chunk) < 10:
            if i < len(context):
                context[i+1] = raw_chunk + '\n' + context[i+1]
        else:
            chunk.append(raw_chunk) 
    
    return question, chunk


def top_k_dot(query_emb, embeddings, k=5):
    sims = embeddings @ query_emb
    top_k_idx = np.argsort(sims)[-k:][::-1]
    return top_k_idx, sims[top_k_idx]

def filter_context(contexts: List[str], question: str, top_k: int = 3):
    embedder = VNPTAIEmbeddingClient()
    question_embed = np.array(embedder.embed(question))
    context_embed = np.array(embedder.embed(contexts))
    idx, val = top_k_dot(question_embed, context_embed, top_k)
    chosen_context = [contexts[i] for i in range(len(contexts)) if i in idx]
    return chosen_context

    
    

def solve_long_text(llm, question: str, choices: List[str], _ = None, debug=False) -> str:
    """
    Entry cho predict.py: trả về answer letter.
    Lưu ý: theo handler bạn bạn, nếu bị VNPT từ chối -> return "".
    """
    
    question, context = split_query(question)
    chosen_contexts = filter_context(context, question, top_k=3)

    prompt = build_mcq_prompt(question, choices, chosen_contexts)
    # 2) gọi LLM
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt),
    ]

    resp = llm.invoke(messages)
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