import re

def count_words_clean(text: str) -> int:
    text = re.sub(r"[^\w\s]", " ", text)
    return len(text.split())

path_marco = 'data/econ/macro.md'

with open(path_marco, 'r') as f:
    data = f.read()
    
data = data.split('###')


# import re
# from collections import defaultdict

# import re

# def parse_note(text: str):
#     result = {
#         "id": None,
#         "title": None,
#         "section": None,
#         "definitions": [],
#         "formulas": [],
#         "rules": [],
#         "traps": []
#     }

#     current_block = None

#     lines = [l.rstrip() for l in text.splitlines() if l.strip()]

#     for line in lines:
#         # [M4-001] Title
#         m = re.match(r'\[(.*?)\]\s*(.*)', line)
#         if m:
#             result["id"] = m.group(1)
#             result["title"] = m.group(2)
#             continue

#         # Section
#         if line.startswith("- **Phần/Mục:**"):
#             result["section"] = line.split("**Phần/Mục:**")[-1].strip()
#             continue

#         # Block headers
#         if "**Định nghĩa lõi:**" in line:
#             current_block = "definitions"
#             result[current_block] = ''
#             continue
#         if "**Công thức/Quan hệ:**" in line:
#             current_block = "formulas"
#             result[current_block] = ''
#             continue
#         if "**Quy tắc suy luận nhanh" in line:
#             current_block = "rules"
#             result[current_block] = ''
#             continue
#         if "**Bẫy" in line:
#             current_block = "traps"
#             result[current_block] = ''
#             continue

#         # Bullet content
#         if current_block:
#             result[current_block] += line + '\n'

#     return result

# section_data = []
# for i, text in enumerate(data):
#     section = {}
#     struct = parse_note(text)
#     if len(struct.keys()) != 7:
#         print('Không đúng cấu trúc', i)
#     section['title'] = text.split('\n')[0]
#     section['secs'] = list(struct.values())[2:]
#     section_data.append(section)
# print(section_data[1])