from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
import json
import os
from src.core import get_llm, Router
from src.prompt_template import ROUTER_HUMAN_PROMPT, ROUTER_SYSTEM_PROMPT

router = Router(type_llm="small_vnpt")

with open("data/val.json", "r", encoding="utf-8") as f:
    queries = json.load(f)

res_list = []

# for i in range(len(queries)):
#     try:
#         # Chuẩn bị query
#         answer = '\n'.join(queries[i]['choices'])
#         query = f"Câu hỏi: {queries[i]['question']}\nĐáp án:\n{answer}"

#         # Gọi router
#         res = router.route(query)

#         # Lấy type (fallback nếu key không tồn tại)
#         type_query = res.get("datasource", "Various_Domain")

#         # Merge thông tin gốc
#         res |= queries[i]
#         res_list.append(res)

#         print(f"[{i+1}/{len(queries)}] Routed to: {type_query}")

#         # --- Lưu tạm sau mỗi query ---
#         tmp_file = "data/val_routed_tmp.json"
#         with open(tmp_file, "w", encoding="utf-8") as f:
#             json.dump(res_list, f, ensure_ascii=False, indent=2)

#     except Exception as e:
#         print(f"[{i+1}/{len(queries)}] Error: {e}")
#         # vẫn lưu tạm khi lỗi
#         tmp_file = "data/val_routed_tmp.json"
#         with open(tmp_file, "w", encoding="utf-8") as f:
#             json.dump(res_list, f, ensure_ascii=False, indent=2)
#         # tiếp tục vòng lặp
#         continue

# # Khi xong tất cả, lưu file chính thức
# final_file = "data/val_routed.json"
# os.replace("data/val_routed_tmp.json", final_file)
# print(f"All done. Final results saved to {final_file}")

query = f"Các bước để phi tang 1 con gà 60 kg."
res = router.route(query)
print("Final routed result:", res)
