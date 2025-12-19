"""
Long Text Query Handler
Xử lý câu hỏi dài (>500 từ) với RAG strategy
"""

import json
import os
import sys
from typing import List, Dict, Any

# Thêm thư mục gốc vào Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.messages import SystemMessage, HumanMessage
from src.core import get_llm, RAGHandler


class LongTextQueryHandler:
    """Handler xử lý câu hỏi Long_Text_Questions"""
    
    def __init__(
        self,
        llm_type: str = "large_vnpt",
        llm_cfg: dict = None,
        rag_chunk_size: int = 300,
        rag_chunk_overlap: int = 50,
        rag_top_k: int = 3
    ):
        """
        Args:
            llm_type: Loại LLM ('large_vnpt', 'small_vnpt', 'google')
            llm_cfg: Config cho LLM (temperature, top_p, etc.)
            rag_chunk_size: Kích thước chunk cho RAG
            rag_chunk_overlap: Số từ overlap giữa chunks
            rag_top_k: Số chunks liên quan lấy ra
        """
        # Khởi tạo LLM
        if llm_cfg is None:
            llm_cfg = {
                "temperature": 0.0,
                "top_p": 1.0,
                "top_k": 20,
                "max_tokens": 128,
            }
        
        try:
            self.llm = get_llm(llm_type, cfg=llm_cfg)
        except TypeError:
            # Fallback nếu get_llm không nhận cfg
            self.llm = get_llm(llm_type)
        
        # Khởi tạo RAG Handler
        self.rag_handler = RAGHandler(
            chunk_size=rag_chunk_size,
            chunk_overlap=rag_chunk_overlap,
            top_k=rag_top_k
        )
        
        # System prompt cho câu hỏi dài
        self.system_prompt = (
            "Bạn là trợ lý làm bài trắc nghiệm nhiều lựa chọn.\n"
            "Bạn sẽ được cung cấp một đoạn văn bản và câu hỏi liên quan.\n"
            "Hãy đọc kỹ đoạn văn và chọn ĐÚNG MỘT đáp án.\n\n"
            "QUY TẮC BẮT BUỘC:\n"
            "- CHỈ trả về duy nhất MỘT ký tự là chữ cái của đáp án (A, B, C, D, ...).\n"
            "- KHÔNG giải thích, không thêm bất kỳ ký tự hay câu chữ nào khác.\n"
            "- Không trả về nội dung của phương án, chỉ trả về chữ cái.\n"
        )
    
    def process_single_question(self, item: Dict[str, Any]) -> str:
        """
        Xử lý 1 câu hỏi dài
        
        Args:
            item: Dict chứa question, choices, qid, etc.
            
        Returns:
            answer_letter: Đáp án (A, B, C, D, ...)
        """
        question = item["question"]
        choices = item["choices"]
        qid = item.get("qid", "unknown")
        
        print(f"[LONG-TEXT] Processing qid={qid}...")
        
        # Áp dụng RAG
        try:
            context, refined_question = self.rag_handler.process(question)
            
            # Nếu tách được thì dùng prompt với context thu gọn
            if context and refined_question:
                prompt = self._build_rag_prompt(context, refined_question, choices)
                print(f"  → RAG success: {len(context.split())} words in context")
            else:
                # Fallback về prompt thường
                prompt = self._build_standard_prompt(question, choices)
                print(f"  → RAG failed, using standard prompt")
        except Exception as e:
            print(f"  → RAG error: {e}, fallback to standard")
            prompt = self._build_standard_prompt(question, choices)
        
        # Gọi LLM
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=prompt)
        ]
        
        try:
            ai_msg = self.llm.invoke(messages)
            raw_answer = getattr(ai_msg, "content", str(ai_msg))
            
            # Xử lý câu hỏi nhạy cảm
            if "không thể trả lời" in raw_answer.lower() or "không thể phản hồi" in raw_answer.lower():
                print(f"  → SENSITIVE: VNPT từ chối")
                return ""
            
            # Parse answer
            answer_letter = self._parse_answer(raw_answer, len(choices))
            print(f"  → Answer: {answer_letter} (raw: {raw_answer!r})")
            
            return answer_letter
            
        except Exception as e:
            msg = str(e)
            if "VNPT API logical error response" in msg and "BadRequestError" in msg:
                print(f"  → SENSITIVE-ERROR: VNPT từ chối")
                return ""
            
            # Lỗi khác
            print(f"  → ERROR: {e}")
            raise
    
    def process_batch(
        self,
        input_file: str,
        output_file: str,
        max_calls: int = 50
    ):
        """
        Xử lý batch câu hỏi từ file đã được route
        
        Args:
            input_file: File input (val_routed.json)
            output_file: File output (long_text_results.json)
            max_calls: Số câu tối đa xử lý (tránh quota)
        """
        # Đọc dữ liệu đã được route
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Lọc chỉ lấy Long_Text_Questions
        long_text_questions = [
            item for item in data 
            if item.get("datasource") == "Long_Text_Questions"
        ]
        
        print(f"Tìm thấy {len(long_text_questions)} câu hỏi Long_Text")
        print(f"Sẽ xử lý tối đa {max_calls} câu")
        
        # Đọc kết quả cũ nếu có
        processed_qids = set()
        results = []
        
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                results = json.load(f)
                processed_qids = {r["qid"] for r in results}
            print(f"Đã có {len(processed_qids)} câu đã xử lý trước đó")
        
        # Xử lý từng câu
        calls_made = 0
        
        for idx, item in enumerate(long_text_questions, start=1):
            qid = item.get("qid")
            
            # Skip nếu đã xử lý
            if qid in processed_qids:
                print(f"[{idx}/{len(long_text_questions)}] SKIP qid={qid}")
                continue
            
            # Kiểm tra quota
            if calls_made >= max_calls:
                print(f"\nĐã đạt giới hạn {max_calls} calls, dừng lại.")
                break
            
            # Xử lý câu hỏi
            try:
                answer = self.process_single_question(item)
                
                # Lưu kết quả
                result = {
                    "qid": qid,
                    "answer": answer,
                    "question": item["question"][:100] + "...",  # Lưu preview
                    "datasource": "Long_Text_Questions"
                }
                results.append(result)
                
                # Ghi ngay vào file (để không mất dữ liệu nếu crash)
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                
                calls_made += 1
                print(f"[{idx}/{len(long_text_questions)}] Done. Total calls: {calls_made}\n")
                
            except Exception as e:
                print(f"[{idx}/{len(long_text_questions)}] ERROR: {e}")
                # Lưu lại progress trước khi crash
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                break
        
        print(f"\n{'='*50}")
        print(f"HOÀN TẤT!")
        print(f"- Đã xử lý: {calls_made} câu mới")
        print(f"- Tổng cộng: {len(results)} câu trong {output_file}")
        print(f"{'='*50}")
    
    def _build_rag_prompt(self, context: str, question: str, choices: List[str]) -> str:
        """Tạo prompt với context đã được RAG"""
        lines = [
            "Dựa vào đoạn văn sau:",
            "",
            context,
            "",
            f"Câu hỏi: {question}",
            "",
            "Các lựa chọn:"
        ]
        
        for idx, choice in enumerate(choices):
            letter = chr(ord("A") + idx)
            lines.append(f"{letter}. {choice}")
        
        lines.append("")
        lines.append("Hãy trả lời CHỈ MỘT ký tự là chữ cái của đáp án đúng (A, B, C, ...).")
        
        return "\n".join(lines)
    
    def _build_standard_prompt(self, question: str, choices: List[str]) -> str:
        """Tạo prompt thường (không RAG)"""
        lines = [f"Câu hỏi: {question}", "", "Các lựa chọn:"]
        
        for idx, choice in enumerate(choices):
            letter = chr(ord("A") + idx)
            lines.append(f"{letter}. {choice}")
        
        lines.append("")
        lines.append("Hãy trả lời CHỈ MỘT ký tự là chữ cái của đáp án đúng (A, B, C, ...).")
        
        return "\n".join(lines)
    
    def _parse_answer(self, raw_answer: str, num_choices: int) -> str:
        """Parse answer từ LLM thành chữ cái A, B, C, ..."""
        if not raw_answer:
            return "A"
        
        text = raw_answer.strip().upper()
        
        # Nếu chỉ có 1 ký tự
        if len(text) == 1 and "A" <= text <= "Z":
            idx = ord(text) - ord("A")
            if 0 <= idx < num_choices:
                return text
        
        # Tìm ký tự đầu tiên trong A..Z
        for ch in text:
            if "A" <= ch <= "Z":
                idx = ord(ch) - ord("A")
                if 0 <= idx < num_choices:
                    return ch
        
        # Fallback
        return "A"


def main():
    """Entry point để chạy riêng file này"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Process long text questions")
    parser.add_argument(
        "--input",
        default="data/val_routed.json",
        help="Input file (đã được route)"
    )
    parser.add_argument(
        "--output",
        default="data/long_text_results.json",
        help="Output file"
    )
    parser.add_argument(
        "--max-calls",
        type=int,
        default=50,
        help="Số câu tối đa xử lý"
    )
    
    args = parser.parse_args()
    
    # Khởi tạo handler
    handler = LongTextQueryHandler()
    
    # Xử lý batch
    handler.process_batch(
        input_file=args.input,
        output_file=args.output,
        max_calls=args.max_calls
    )


if __name__ == "__main__":
    main()
