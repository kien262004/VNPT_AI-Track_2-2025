import re
import faiss
import numpy as np
import json
import os
from typing import List, Dict

def count_words_clean(text: str) -> int:
    text = re.sub(r"[^\w\s]", " ", text)
    return len(text.split())

def get_data_macro(path_marco):
    with open(path_marco, 'r') as f:
        data = f.read()
        
    data = data.split('###')
    metadatas = [
        {'chunk_id': f'marco_econ_{i}', "source": section.split('\n')[0]} for i, section in enumerate(data)
    ]
    return data, metadatas

import re
from typing import Dict, Any


import re
from typing import List, Dict


def parse_markdown_to_tree(text: str) -> Dict:
    lines = text.splitlines()

    root = {
        "title": None,
        "level": 0,
        "content": "",
        "subsection": []
    }

    stack = [root]

    for line in lines:
        line = line.rstrip()
        if not line:
            continue

        match = re.match(r'^(#+)\s+(.*)', line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()

            node = {
                "title": title,
                "level": level,
                "content": "",
                "subsection": []
            }

            # pop đến đúng level cha
            while stack and stack[-1]["level"] >= level:
                stack.pop()

            stack[-1]["subsection"].append(node)
            stack.append(node)
        else:
            # content thường (không phải heading)
            stack[-1]["content"] += line + "\n"

    return root["subsection"][0] if root["subsection"] else root

def collect_chunks(tree):
    chunks = []
    metadatas = []
    def dfs(node, context_titles, idx=0):
        level = node["level"]
        title = node["title"]
        content = "".join(node["content"])

        # cập nhật context
        if level > 0:
            context_titles = context_titles + [title]

        # Nếu là bậc 3
        if level == 3:
            if node["subsection"]:  # có bậc 4
                for child in node["subsection"]:
                    child_text = "".join(child["content"])
                    chunk_text = "\n".join([
                        " > ".join(context_titles),  # bậc 1-2-3
                        child["title"],
                        child_text
                    ])
                    chunks.append(chunk_text)
                    metadatas.append({
                        'chunk_id': f"micro_econ_{idx}",
                        'source': " > ".join(context_titles)
                    })
                    idx += 1
            else:
                chunk_text = "\n".join([
                    " > ".join(context_titles[:-1]),  # bậc 1-2
                    title,
                    content
                ])
                chunks.append(chunk_text)
                metadatas.append({
                    'chunk_id': f"micro_econ_{idx}",
                    'source': " > ".join(context_titles[:-1])
                })
                idx += 1
        if 'subsection' in node:
            for child in node["subsection"]:
                idx = dfs(child, context_titles, idx+1)
        return idx

    dfs(tree, [])
    return chunks, metadatas

def get_data_micro(path_micro):
    with open(path_micro, 'r') as f:
        data = f.read()
    tree = parse_markdown_to_tree(data)
    chunks, metadatas = collect_chunks(tree)
    return chunks, metadatas

def get_data(path):
    if 'macro' in path:
        return get_data_macro(path)
    else:
        return get_data_micro(path)