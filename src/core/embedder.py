"""
VNPT Embedding API Wrapper
Sử dụng API embedding của VNPT để tạo vector embeddings cho text
"""

import requests
import os
from typing import List, Union
import numpy as np


class VNPTEmbedding:
    """Wrapper cho VNPT Embedding API"""
    
    def __init__(self):
        """Khởi tạo với credentials từ .env"""
        self.url = "https://api.idg.vnpt.vn/data-service/vnptai-hackathon-embedding"
        self.model = "vnptai_hackathon_embedding"
        
        # Load credentials từ .env
        self.headers = {
            'Authorization': f"Bearer {os.getenv('AUTHORIZATION_VNPT_EMBEDDING')}",
            'Token-id': os.getenv('TOKEN_ID_VNPT_EMBEDDING'),
            'Token-key': os.getenv('TOKEN_KEY_VNPT_EMBEDDING'),
            'Content-Type': 'application/json',
        }
    
    def embed_text(self, text: str) -> List[float]:
        """
        Tạo embedding cho 1 đoạn text
        
        Args:
            text: Văn bản cần embed
            
        Returns:
            Vector embedding (list of floats)
        """
        json_data = {
            'model': self.model,
            'input': text,
            'encoding_format': 'float'
        }
        
        try:
            # Retry logic: 3 attempts with 60s timeout
            for attempt in range(3):
                try:
                    response = requests.post(self.url, headers=self.headers, json=json_data, timeout=60)
                    result = response.json()
                    
                    # Extract embedding từ response
                    if 'data' in result and len(result['data']) > 0:
                        return result['data'][0]['embedding']
                    break
                except requests.exceptions.Timeout:
                    if attempt < 2:  # Retry if not last attempt
                        print(f"  → Timeout (attempt {attempt+1}/3), retrying...")
                        continue
                    else:
                        raise  # Re-raise on final attempt
            else:
                raise ValueError(f"Unexpected API response format: {result}")
                
        except Exception as e:
            raise ValueError(f"VNPT Embedding API error: {e}")
    
    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Tạo embeddings cho nhiều texts
        
        Args:
            texts: List các văn bản
            
        Returns:
            List các vectors
        """
        embeddings = []
        for text in texts:
            emb = self.embed_text(text)
            embeddings.append(emb)
        return embeddings
    
    @staticmethod
    def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
        """
        Tính cosine similarity giữa 2 vectors
        
        Args:
            vec1, vec2: Embedding vectors
            
        Returns:
            Similarity score (0-1, càng cao càng giống)
        """
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)


# Test function
def test_embedding():
    """Test VNPT Embedding API"""
    embedder = VNPTEmbedding()
    
    # Test single text
    text = "Xin chào, mình là VNPT AI."
    embedding = embedder.embed_text(text)
    print(f"Text: {text}")
    print(f"Embedding dimension: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")
    
    # Test similarity
    text1 = "Thủ đô của Việt Nam là Hà Nội"
    text2 = "Hà Nội là thủ đô của nước Việt Nam"
    text3 = "Con mèo đang ngủ trên ghế"
    
    emb1 = embedder.embed_text(text1)
    emb2 = embedder.embed_text(text2)
    emb3 = embedder.embed_text(text3)
    
    sim_12 = VNPTEmbedding.cosine_similarity(emb1, emb2)
    sim_13 = VNPTEmbedding.cosine_similarity(emb1, emb3)
    
    print(f"\nSimilarity Test:")
    print(f"Text 1: {text1}")
    print(f"Text 2: {text2}")
    print(f"Text 3: {text3}")
    print(f"Sim(1,2): {sim_12:.4f} (similar content)")
    print(f"Sim(1,3): {sim_13:.4f} (different content)")


if __name__ == "__main__":
    test_embedding()
