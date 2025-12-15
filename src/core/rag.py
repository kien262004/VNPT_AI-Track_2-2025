import re
import faiss
import numpy as np
import json
import os
from typing import List, Dict

class FaissVectorStore:
    def __init__(
        self,
        dim: int,
    ):
        self.dim = dim

        # cosine similarity = inner product + normalize
        self.index = faiss.IndexFlatIP(dim)
        self.metadata: List[Dict] = []

    # -----------------
    # Add vectors
    # -----------------
    def add(
        self,
        embeddings: List[List[float]],
        metadatas: List[Dict]
    ):
        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)
        self.metadata.extend(metadatas)

    # -----------------
    # Search
    # -----------------
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5
    ):
        q = np.array([query_embedding]).astype("float32")
        scores, indices = self.index.search(q, top_k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            results.append({
                "score": float(score),
                "metadata": self.metadata[idx]
            })
        return results

    # -----------------
    # Save / Load
    # -----------------
    def save(self, index_path: str, meta_path: str):
        os.makedirs(os.path.dirname(index_path), exist_ok=True)
        os.makedirs(os.path.dirname(meta_path), exist_ok=True)

        faiss.write_index(self.index, index_path)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)

    def load(
        self,
        index_path: str,
        meta_path: str,
        mode: str = "replace"  # "replace" | "append"
    ):
        assert mode in ["replace", "append"]

        loaded_index = faiss.read_index(index_path)
        with open(meta_path, "r", encoding="utf-8") as f:
            loaded_metadata = json.load(f)

        if mode == "replace":
            # ❗ Load toàn bộ
            self.index = loaded_index
            self.metadata = loaded_metadata

        else:
            # ➕ Append
            if self.index.ntotal == 0:
                self.index = loaded_index
            else:
                # add vectors từ index đã load
                xb = loaded_index.reconstruct_n(0, loaded_index.ntotal)
                self.index.add(xb)

            self.metadata.extend(loaded_metadata)