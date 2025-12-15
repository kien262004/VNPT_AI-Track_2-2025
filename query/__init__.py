"""
Query handlers for different question types
Xử lý từng loại câu hỏi đã được phân loại bởi Router
"""

from .long_text_handler import LongTextQueryHandler

__all__ = ["LongTextQueryHandler"]
