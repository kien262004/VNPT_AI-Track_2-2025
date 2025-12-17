import os
import sys
import json
import csv
import argparse
import numpy as np
from typing import List, Dict, Set, Tuple, Optional

# Cho phép chạy `python3 predict.py` từ root mà import được src/...
sys.path.append(os.path.abspath("."))

from src.core import get_llm, Router, VectorDB, VNPTAIEmbeddingClient

# Handlers: mỗi handler chịu trách nhiệm logic đặc thù + tự chống policy block nếu cần
from src.query.math_logical_reasoning import solve_math_logical
from src.query.restricted import solve_restricted
from src.query.mandatory_accuracy import solve_mandatory_accuracy
from src.query.long_text_questions import solve_long_text


# ===== BTC defaults (entry-point end-to-end) =====
DEFAULT_TEST_PATH = "/code/private_test.json"
DEFAULT_SUBMISSION_PATH = "/code/submission.csv"
DEFAULT_DEBUG_PATH = "/code/submission_debug.csv"

METADATA_BOOK_PATH = 'database/chunks_textbook.json'
EMBEDDED_BOOK_PATH = 'database/embedded_chunks_textbook.index'

METADATA_WEB_PATH = 'database/chunks_web.json'
EMBEDDED_WEB_PATH = 'database/embedded_chunks_web.index'

DEBUG = True



def load_test(test_path: str) -> List[dict]:
    with open(test_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_answered_qids(csv_path: str) -> Set[str]:
    answered = set()
    if not os.path.exists(csv_path):
        return answered

    with open(csv_path, "r", encoding="utf-8") as f:
        # tolerate both header/no-header
        first = f.read(1024)
        f.seek(0)
        has_header = ("qid" in first.lower()) and ("answer" in first.lower())
        if has_header:
            reader = csv.DictReader(f)
            for row in reader:
                qid = (row.get("qid") or "").strip()
                if qid:
                    answered.add(qid)
        else:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                qid = (row[0] or "").strip()
                if qid and qid.lower() != "qid":
                    answered.add(qid)

    return answered


def ensure_csv_writer_2cols(path: str) -> Tuple[csv.writer, "TextIO"]:
    existed = os.path.exists(path)
    fh = open(path, "a", newline="", encoding="utf-8")
    w = csv.writer(fh)
    if not existed:
        w.writerow(["qid", "answer"])
        fh.flush()
    return w, fh


def ensure_csv_writer_3cols(path: str) -> Tuple[csv.writer, "TextIO"]:
    existed = os.path.exists(path)
    fh = open(path, "a", newline="", encoding="utf-8")
    w = csv.writer(fh)
    if not existed:
        w.writerow(["qid", "answer", "route"])
        fh.flush()
    return w, fh


def build_router_input(question: str, choices: List[str]) -> str:
    # gộp cả choices để router phân loại tốt hơn
    lines = [question, "", "Choices:"]
    for i, c in enumerate(choices):
        letter = chr(ord("A") + i)
        lines.append(f"{letter}. {c}")
    return "\n".join(lines)


def normalize_datasource(ds: Optional[str]) -> str:
    if not ds:
        return "Various_Domain"
    ds = ds.strip()
    if ds in ("Restricted", "Restricted_Questions"):
        return "Restricted_Questions"
    return ds


def _derive_routed_paths(test_path: str) -> Tuple[str, str]:
    """
    giống classify.py: tạo tmp + final routed json theo tên file input
    ví dụ /code/private_test.json -> /code/private_test_routed_tmp.json + /code/private_test_routed.json
    """
    base_dir = os.path.dirname(test_path) or "."
    base_name = os.path.splitext(os.path.basename(test_path))[0]
    tmp_path = os.path.join(base_dir, f"{base_name}_routed_tmp.json")
    final_path = os.path.join(base_dir, f"{base_name}_routed.json")
    return tmp_path, final_path


def _load_routed_cache(tmp_path: str) -> Dict[str, str]:
    """
    cache: qid -> datasource
    tmp_path lưu list các dict (mỗi dict có qid + datasource + (optional) dữ liệu khác)
    """
    if not os.path.exists(tmp_path):
        return {}

    try:
        with open(tmp_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        cache: Dict[str, str] = {}
        if isinstance(data, list):
            for it in data:
                qid = (it.get("qid") or "").strip()
                ds = normalize_datasource(it.get("datasource"))
                if qid:
                    cache[qid] = ds
        return cache
    except Exception:
        # tmp hỏng thì coi như chưa có
        return {}


def _save_routed_tmp(tmp_path: str, cache: Dict[str, str]) -> None:
    # lưu dạng list để dễ debug
    data = [{"qid": qid, "datasource": ds} for qid, ds in cache.items()]
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_path", default=DEFAULT_TEST_PATH)
    parser.add_argument("--submission_path", default=DEFAULT_SUBMISSION_PATH)
    parser.add_argument("--debug_path", default=DEFAULT_DEBUG_PATH)
    parser.add_argument(
        "--max_calls",
        type=int,
        default=20,
        help="Giới hạn số câu trả lời mỗi lần chạy (quota-friendly).",
    )
    args = parser.parse_args()

    test_path = args.test_path
    submission_path = args.submission_path
    debug_path = args.debug_path

    test_data = load_test(test_path)

    # routed cache (logic classify.py)
    routed_tmp_path, routed_final_path = _derive_routed_paths(test_path)
    routed_cache = _load_routed_cache(routed_tmp_path)

    # resume theo submission.csv
    answered_qids = load_answered_qids(submission_path)
    print(f"Đã có {len(answered_qids)} câu đã trả lời trong {submission_path}")
    if routed_cache:
        print(f"Đã có {len(routed_cache)} câu đã phân loại trong {routed_tmp_path}")

    sub_writer, sub_fh = ensure_csv_writer_2cols(submission_path)
    dbg_writer, dbg_fh = ensure_csv_writer_3cols(debug_path)

    # init small llm for answering
    cfg = {"temperature": 0.0, "top_p": 1.0, "top_k": 20, "max_tokens": 512, "response_format": {"type": "json_object"}}
    llm_small = get_llm(type="large_vnpt", cfg=cfg)

    # router (large) – dùng cho classify/route
    router = Router(type_llm="small_vnpt")
    
    rag = VectorDB(
        EMBEDDED_BOOK_PATH,
        METADATA_BOOK_PATH,
        EMBEDDED_WEB_PATH,
        METADATA_WEB_PATH
    )
    embedder = VNPTAIEmbeddingClient()

    DISPATCH = {
        "Math_Logical_Reasoning": solve_math_logical,
        "Restricted_Questions": solve_restricted,
        "Mandatory_Accuracy_Questions": solve_mandatory_accuracy,
        "Various_Domain": solve_mandatory_accuracy,
        "Long_Text_Questions": solve_long_text,
    }

    calls_made = 0
    total = len(test_data)

    try:
        for idx, item in enumerate(test_data, start=1):
            qid = (item.get("qid") or "").strip()
            if not qid:
                continue

            question = item.get("question", "")
            choices = item.get("choices", [])

            if qid in answered_qids:
                print(f"[SKIP] qid={qid} đã có trong submission.csv")
                continue

            if calls_made >= args.max_calls:
                print(f"Đạt max_calls={args.max_calls}, dừng run.")
                break

            # ====== CLASSIFY (logic classify.py tích hợp) ======
            datasource = routed_cache.get(qid)
            if not datasource:
                try:
                    route_info = router.route(build_router_input(question, choices))
                    datasource = normalize_datasource(route_info.get("datasource", "Various_Domain"))
                except Exception:
                    # router có thể bị policy block -> coi như restricted
                    datasource = "Restricted_Questions"

                routed_cache[qid] = datasource
                _save_routed_tmp(routed_tmp_path, routed_cache)

            # ====== RAG ======
            query_context = []

            if DEBUG:
                print('DEBUG: Loại task', datasource)
                
            if datasource in ['Math_Logical_Reasoning', 'Mandatory_Accuracy_Questions', 'Various_Domain']:
                query = question + '\n' + '\n'.join(choices)
                embedding_query = np.array(embedder.embed(query))
                rag_context = rag.retrieve(embedding_query)
                if DEBUG:
                    print("DEBUG: Hiển thị kết quả RAG")
                    print(f"Số lượng context: {len(rag_context)}")
                    
                for con in rag_context:
                    query_context.append(con.get('text', ''))
                
            else:
                if DEBUG:
                    print("DEBUG: Query không cần RAG")

            # ====== ANSWER ======
            handler = DISPATCH.get(datasource, solve_mandatory_accuracy)
            ans = handler(llm_small, question, choices, query_context, DEBUG)

            # BTC submission (2 cols)
            sub_writer.writerow([qid, ans])
            sub_fh.flush()

            # debug output (3 cols)
            dbg_writer.writerow([qid, ans, datasource])
            dbg_fh.flush()

            answered_qids.add(qid)
            calls_made += 1
            print(f"[OK] {idx}/{total} qid={qid} -> {ans} | route={datasource} | calls={calls_made}")
            if DEBUG:
                print('DEBUG: Kết thúc 1 vòng lặp\n')
    finally:
        sub_fh.close()
        dbg_fh.close()

        # ghi file routed final (giống classify.py)
        try:
            routed_final = [{"qid": q, "datasource": ds} for q, ds in routed_cache.items()]
            with open(routed_final_path, "w", encoding="utf-8") as f:
                json.dump(routed_final, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    print(f"Run này đã xử lý thêm {calls_made} câu mới.")
    print(f"Submission: {submission_path}")
    print(f"Debug CSV : {debug_path}")
    print(f"Routed tmp: {routed_tmp_path}")
    print(f"Routed fin: {routed_final_path}")


if __name__ == "__main__":
    main()
