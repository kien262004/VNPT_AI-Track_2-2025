import json
import faiss
import numpy as np

import numpy as np
import faiss


def safe_normalize(embeddings, tol=1e-3):
    """
    embeddings: np.ndarray (N, d)
    tol: sai số cho phép so với norm = 1
    """
    norms = np.linalg.norm(embeddings, axis=1)

    # Kiểm tra: có vector nào chưa norm không?
    need_norm = np.any(np.abs(norms - 1.0) > tol)

    if need_norm:
        faiss.normalize_L2(embeddings)
        print("🔄 Embeddings were NOT normalized → normalized now.")
    else:
        print("✅ Embeddings already normalized → skip.")

    return embeddings


def save_index_streaming(
    input_json_path,
    index_out_path,
    batch_size=4096,
):
    with open(input_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    dim = len(data[0]["embeddings"])
    index = faiss.IndexFlatIP(dim)

    buf = []

    for i, item in enumerate(data):
        buf.append(item["embeddings"])

        if len(buf) == batch_size:
            batch = np.array(buf, dtype="float32")
            index.add(batch)
            buf.clear()

            if i % (batch_size * 10) == 0:
                print(f"Added {index.ntotal} vectors")

    # add phần còn lại
    if buf:
        batch = np.array(buf, dtype="float32")
        index.add(batch)

    faiss.write_index(index, index_out_path)
    print(f"Saved index: {index.ntotal} vectors")

save_index_streaming('database/embedded_chunks_web.json', 'database/embedded_chunks_web.index')