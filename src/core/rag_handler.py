"""
RAG Handler for Long Text Questions
Xử lý câu hỏi dài (>500 từ) bằng cách:
1. Tách câu hỏi và đoạn văn context
2. Chia văn bản thành chunks nhỏ
3. Tìm chunks liên quan nhất (similarity search)
4. Trả về context thu gọn để gửi cho LLM
"""

from typing import List, Tuple, Optional
import re


class RAGHandler:
    """Handler xử lý câu hỏi dài với RAG strategy"""
    
    def __init__(
        self, 
        chunk_size: int = 300,
        chunk_overlap: int = 50,
        top_k: int = 3
    ):
        """
        Args:
            chunk_size: Số từ tối đa trong mỗi chunk
            chunk_overlap: Số từ overlap giữa các chunks
            top_k: Số lượng chunks liên quan nhất để lấy
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.top_k = top_k
        
    def process(self, full_question: str) -> Tuple[str, str]:
        """
        Xử lý câu hỏi dài và trả về context thu gọn + câu hỏi
        
        Args:
            full_question: Câu hỏi đầy đủ (bao gồm cả đoạn văn dài)
            
        Returns:
            (context_thu_gọn, câu_hỏi_chính)
        """
        # Bước 1: Tách context và question
        context, question = self._parse_input(full_question)
        
        # Nếu không tách được, return nguyên văn
        if not context or not question:
            return full_question, ""
        
        # Bước 2: Chia context thành chunks
        chunks = self._create_chunks(context)
        
        # Nếu chỉ có 1 chunk hoặc ít chunks, return luôn
        if len(chunks) <= self.top_k:
            return "\n\n".join(chunks), question
        
        # Bước 3: Tìm chunks liên quan nhất (simple keyword matching)
        relevant_chunks = self._retrieve_relevant_chunks(chunks, question)
        
        # Bước 4: Ghép lại thành context thu gọn
        refined_context = "\n\n".join(relevant_chunks)
        
        return refined_context, question
    
    def _parse_input(self, text: str) -> Tuple[str, str]:
        """
        Tách văn bản và câu hỏi từ input
        
        Format mong đợi:
        - "Đoạn văn: ... Câu hỏi: ..."
        - "Văn bản: ... Hỏi: ..."
        - Hoặc đơn giản là phân đoạn dài + câu hỏi ngắn ở cuối
        
        Returns:
            (context, question)
        """
        # Pattern 1: Có keyword "Câu hỏi", "Hỏi", "Question"
        patterns = [
            r'(?:Đoạn văn|Văn bản|Bài đọc|Context)[:\s]*(.+?)(?:Câu hỏi|Hỏi|Question)[:\s]*(.+)',
            r'(.+?)(?:Câu hỏi|Hỏi|Question)[:\s]*(.+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
            if match:
                context = match.group(1).strip()
                question = match.group(2).strip()
                return context, question
        
        # Pattern 2: Không có keyword rõ ràng
        # Giả định: 80% đầu là context, 20% cuối là câu hỏi
        words = text.split()
        split_point = int(len(words) * 0.8)
        
        context = " ".join(words[:split_point])
        question = " ".join(words[split_point:])
        
        return context, question
    
    def _create_chunks(self, text: str) -> List[str]:
        """
        Chia text thành các chunks với overlap
        
        Args:
            text: Văn bản cần chia
            
        Returns:
            List các chunks
        """
        # Tách thành các câu (split by . ! ?)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        chunks = []
        current_chunk = []
        current_word_count = 0
        
        for sentence in sentences:
            sentence_words = sentence.split()
            sentence_word_count = len(sentence_words)
            
            # Nếu thêm câu này vào chunk hiện tại mà vượt quá chunk_size
            if current_word_count + sentence_word_count > self.chunk_size and current_chunk:
                # Lưu chunk hiện tại
                chunks.append(" ".join(current_chunk))
                
                # Tạo chunk mới với overlap
                # Lấy một số câu cuối của chunk cũ làm đầu chunk mới
                overlap_words = []
                overlap_count = 0
                for s in reversed(current_chunk):
                    s_words = s.split()
                    if overlap_count + len(s_words) <= self.chunk_overlap:
                        overlap_words.insert(0, s)
                        overlap_count += len(s_words)
                    else:
                        break
                
                current_chunk = overlap_words + [sentence]
                current_word_count = sum(len(s.split()) for s in current_chunk)
            else:
                current_chunk.append(sentence)
                current_word_count += sentence_word_count
        
        # Thêm chunk cuối cùng
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks
    
    def _retrieve_relevant_chunks(self, chunks: List[str], question: str) -> List[str]:
        """
        Tìm các chunks liên quan nhất đến câu hỏi
        
        Strategy: Simple keyword matching (TF-IDF-like)
        - Đếm số từ khóa trong question xuất hiện ở chunk nào
        - Rank theo số lượng match
        
        Args:
            chunks: List các chunks
            question: Câu hỏi
            
        Returns:
            Top-k chunks liên quan nhất
        """
        # Extract keywords từ question (bỏ stopwords)
        stopwords = {
            'là', 'của', 'và', 'có', 'được', 'trong', 'các', 'một', 'những', 
            'để', 'này', 'đó', 'cho', 'từ', 'với', 'theo', 'như', 'khi',
            'câu', 'hỏi', 'nào', 'gì', 'ai', 'đâu', 'sao', 'thế',
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'what', 'which'
        }
        
        question_words = [
            w.lower() for w in re.findall(r'\w+', question)
            if w.lower() not in stopwords and len(w) > 2
        ]
        
        # Tính điểm cho mỗi chunk
        chunk_scores = []
        for chunk in chunks:
            chunk_lower = chunk.lower()
            score = sum(1 for word in question_words if word in chunk_lower)
            chunk_scores.append((chunk, score))
        
        # Sort theo score giảm dần
        chunk_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Lấy top-k chunks
        top_chunks = [chunk for chunk, score in chunk_scores[:self.top_k]]
        
        # Nếu không có chunk nào match, lấy chunks đầu tiên
        if not any(score > 0 for _, score in chunk_scores[:self.top_k]):
            return chunks[:self.top_k]
        
        return top_chunks


# Test function (chỉ dùng khi develop)
def _test_rag_handler():
    """Test RAGHandler với ví dụ đơn giản"""
    handler = RAGHandler(chunk_size=50, chunk_overlap=10, top_k=2)
    
    sample_text = """
    Đoạn văn: Việt Nam là một quốc gia nằm ở khu vực Đông Nam Á. 
    Việt Nam có diện tích khoảng 331,212 km². Thủ đô của Việt Nam là Hà Nội.
    Thành phố lớn nhất là Thành phố Hồ Chí Minh. Việt Nam có dân số khoảng 100 triệu người.
    Việt Nam có biên giới với Trung Quốc ở phía bắc, Lào và Campuchia ở phía tây.
    Việt Nam có bờ biển dài 3,260 km. Khí hậu Việt Nam là nhiệt đới gió mùa.
    
    Câu hỏi: Thủ đô của Việt Nam là gì?
    """
    
    context, question = handler.process(sample_text)
    print("=" * 50)
    print("CONTEXT THU GỌN:")
    print(context)
    print("\n" + "=" * 50)
    print("CÂU HỎI:")
    print(question)
    print("=" * 50)


if __name__ == "__main__":
    _test_rag_handler()
