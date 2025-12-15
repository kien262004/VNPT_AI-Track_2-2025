# import json
# import os
# from src.core import Router

# # ================== CONFIG ==================
# INPUT_FILE = "data/test.json"
# TMP_FILE = "data/test_routed_tmp.json"
# FINAL_FILE = "data/test_routed.json"

# LLM_TYPE = "small_vnpt"
# # ============================================


# def load_queries(path):
#     with open(path, "r", encoding="utf-8") as f:
#         return json.load(f)


# def load_resume_data(tmp_file):
#     """
#     Load dữ liệu đã route nếu tồn tại
#     """
#     if os.path.exists(tmp_file):
#         with open(tmp_file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#         print(f"🔁 Resume detected: {len(data)} queries already processed")
#         return data
#     else:
#         print("🆕 No resume file found, start from scratch")
#         return []


# def save_tmp(data, path):
#     """
#     Lưu tạm sau mỗi query (atomic write)
#     """
#     with open(path, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)


# def main():
#     router = Router(type_llm=LLM_TYPE)

#     queries = load_queries(INPUT_FILE)
#     res_list = load_resume_data(TMP_FILE)

#     start_idx = len(res_list)
#     total = len(queries)

#     print(f"▶️ Start routing from index {start_idx}/{total}")

#     for i in range(start_idx, total):
#         try:
#             item = queries[i]

#             answer = "\n".join(item.get("choices", []))
#             query = f"Câu hỏi: {item['question']}\nĐáp án:\n{answer}"

#             res = router.route(query)
#             type_query = res.get("datasource", "Various_Domain")

#             # merge dữ liệu gốc
#             res |= item
#             res_list.append(res)

#             print(f"[{i+1}/{total}] Routed to: {type_query}")

#             # lưu tạm sau mỗi query
#             save_tmp(res_list, TMP_FILE)

#         except Exception as e:
#             print(f"[{i+1}/{total}] ❌ Error: {e}")

#             # vẫn lưu để không mất dữ liệu
#             save_tmp(res_list, TMP_FILE)

#             # nếu lỗi quota / rate limit → dừng để resume sau
#             if any(k in str(e).lower() for k in ["quota", "rate", "limit"]):
#                 print("⚠️ Quota/Rate limit reached. Stop and resume later.")
#                 break

#             # lỗi khác → tiếp tục
#             continue

#     # nếu hoàn tất toàn bộ
#     if len(res_list) == total:
#         os.replace(TMP_FILE, FINAL_FILE)
#         print(f"✅ ALL DONE. Final results saved to {FINAL_FILE}")
#     else:
#         print(
#             f"⏸️ Progress saved: {len(res_list)}/{total}. "
#             f"Run the script again to resume."
#         )


# if __name__ == "__main__":
#     main()

from src.core.llm import VNPTAIEmbeddingClient

embeder = VNPTAIEmbeddingClient()
print(embeder.embed('Hello'))