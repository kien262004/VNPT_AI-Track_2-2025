import re
import faiss
import numpy as np
import json
import os
from typing import List, Dict
from src.core import *
from src.crawl.processing_econ_doc import *

def count_words_clean(text: str) -> int:
    text = re.sub(r"[^\w\s]", " ", text)
    return len(text.split())

files = [
    'data/econ/macro.md',
    'data/econ/micro.md'
]
embedder = VNPTAIEmbeddingClient()
dim = len(embedder.embed('dump'))
store = FaissVectorStore(dim)

for filename in files:
    data, metadatas = get_data(filename)
    print(len(data))
    embeddings = embedder.embed(data, normalize=True)
    print(len(embeddings))
    store.add(embeddings, metadatas)
store.save(index_path='data/database/faiss_eco.index', meta_path='data/database/meta_eco.json')
