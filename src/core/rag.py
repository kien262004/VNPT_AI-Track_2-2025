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
        


class VectorDB:
    def __init__(
        self,
        book_index_path: str,
        book_meta_path: str,
        web_index_path: str,
        web_meta_path: str,
        mmap: bool = True,
        source_weight: Dict[str, float] = None,
    ):
        self.book_index, self.book_meta = self._load_db(
            book_index_path, book_meta_path, mmap
        )
        self.web_index, self.web_meta = self._load_db(
            web_index_path, web_meta_path, mmap
        )

        self.source_weight = source_weight or {
            "book": 1.0,
            "web": 0.8,
        }

    # ------------------------
    # Load FAISS + metadata
    # ------------------------
    def _load_db(self, index_path, meta_path, mmap):
        index = faiss.read_index(
            index_path,
            faiss.IO_FLAG_MMAP if mmap else 0
        )
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

        assert index.ntotal == len(meta), \
            f"Index ({index.ntotal}) != Metadata ({len(meta)})"

        return index, meta

    # ------------------------
    # Search single index
    # ------------------------
    def _search(
        self,
        index,
        metadata,
        query_emb: np.ndarray,
        k: int,
        source: str
    ) -> List[Dict]:
        query_emb = query_emb.reshape(1, -1).astype("float32")
        scores, indices = index.search(query_emb, k)

        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx == -1:
                continue
            item = metadata[idx]
            results.append({
                "score": float(score),
                "text": item["content"],
                "source": source,
            })
        return results

    # ------------------------
    # Weighted fusion
    # ------------------------
    def _fuse(self, book_res, web_res):
        all_res = book_res + web_res
        for r in all_res:
            r["final_score"] = r["score"] * self.source_weight.get(
                r["source"], 0.5
            )
        return sorted(all_res, key=lambda x: x["final_score"], reverse=True)

    # ------------------------
    # Public API
    # ------------------------
    def retrieve(
        self,
        query_emb: np.ndarray,
        book_k: int = 5,
        web_k: int = 10,
        final_k: int = 6,
    ) -> List[Dict]:
        book_res = self._search(
            self.book_index,
            self.book_meta,
            query_emb,
            book_k,
            source="book",
        )
        web_res = self._search(
            self.web_index,
            self.web_meta,
            query_emb,
            web_k,
            source="web",
        )

        fused = self._fuse(book_res, web_res)
        return fused[:final_k]

