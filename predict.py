import os
import sys
import json
import csv
import argparse
from typing import List, Set, Tuple

# Cho phép chạy `python3 predict.py` từ root mà import được src/...
sys.path.append(os.path.abspath("."))

from src.core.llm import get_llm, Router

# Handlers: mỗi handler chịu trách nhiệm xử lý logic đặc thù + tự chống policy block
from src.query.math_logical_reasoning import solve_math_logical
from src.query.restricted import solve_restricted
from src.query.mandatory_accuracy import solve_mandatory_accuracy
from src.query.long_text_questions import solve_long_text


DEFAULT_TEST_PATH = os.path.join("data", "test.json")
DEFAULT_SUBMISSION_PATH = "submission.csv"


def load_test(test_path: str) -> List[dict]:
    with open(test_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_answered_qids(submission_path: str) -> Set[str]:
    answered = set()
    if os.path.exists(submission_path):
        with open(submission_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                qid = (row.get("qid") or "").strip()
                if qid:
                    answered.add(qid)
    return answered


def ensure_csv_writer(submission_path: str) -> Tuple[csv.writer, "TextIO"]:
    existed = os.path.exists(submission_path)
    fh = open(submission_path, "a", newline="", encoding="utf-8")
    writer = csv.writer(fh)
    if not existed:
        writer.writerow(["qid", "answer", "route"])
        fh.flush()
    return writer, fh


def build_router_input(question: str, choices: List[str]) -> str:
    # Router nhận 1 string; gộp cả choices để phân loại tốt hơn.
    lines = [question, "", "Choices:"]
    for i, c in enumerate(choices):
        letter = chr(ord("A") + i)
        lines.append(f"{letter}. {c}")
    return "\n".join(lines)


def normalize_datasource(ds: str) -> str:
    # Chuẩn hoá label router để dispatch thống nhất.
    if not ds:
        return "Various_Domain"
    ds = ds.strip()
    if ds in ("Restricted", "Restricted_Questions"):
        return "Restricted_Questions"
    return ds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test_path", default=DEFAULT_TEST_PATH)
    parser.add_argument("--submission_path", default=DEFAULT_SUBMISSION_PATH)
    parser.add_argument("--max_calls", type=int, default=50, help="Số câu tối đa xử lý mỗi lần chạy (quota-friendly).")
    args = parser.parse_args()

    test_data = load_test(args.test_path)
    answered_qids = load_answered_qids(args.submission_path)
    print(f"Đã có {len(answered_qids)} câu đã trả lời trong {args.submission_path}")

    writer, fh = ensure_csv_writer(args.submission_path)

    # Small LLM để trả lời (handlers có quyền tự dùng / hoặc bỏ qua)
    small_cfg = {"temperature": 0.0, "top_p": 1.0, "top_k": 20, "max_tokens": 128}
    llm_small = get_llm(type="small_vnpt", cfg=small_cfg)

    # Router (large) – tự tạo large llm bên trong theo llm.py
    router = Router(type_llm="large_vnpt")

    # Dispatch table (predict chỉ điều phối)
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
            qid = item.get("qid")
            question = item.get("question", "")
            choices = item.get("choices", [])

            if not qid:
                continue

            if qid in answered_qids:
                print(f"[SKIP] qid={qid} đã có trong submission.csv")
                continue

            if calls_made >= args.max_calls:
                print(f"Đạt max_calls={args.max_calls}, dừng run.")
                break

            # 1) Route trước (predict chỉ route; fallback policy/router error xử lý trong handler)
            try:
                route_info = router.route(build_router_input(question, choices))
                datasource = normalize_datasource(route_info.get("datasource", "Various_Domain"))
            except Exception as e:
                # Router có thể bị policy block trên câu nhạy cảm.
                # predict không phân tích e; chỉ fallback sang Restricted handler.
                datasource = "Restricted_Questions"

            # 2) Dispatch handler
            handler = DISPATCH.get(datasource, solve_mandatory_accuracy)

            # 3) Handler tự chịu trách nhiệm: heuristics, policy block, fallback answer...
            # Quy ước: handler luôn trả về 'A'/'B'/... hoặc '' (rỗng) nếu quyết định không trả lời.
            ans = handler(llm_small, question, choices)

            writer.writerow([qid, ans, datasource])
            fh.flush()
            answered_qids.add(qid)
            calls_made += 1

            print(f"[OK] {idx}/{total} qid={qid} -> {ans} | route={datasource} | calls={calls_made}")

    finally:
        fh.close()

    print(f"Run này đã xử lý thêm {calls_made} câu mới. Bạn có thể chạy lại để resume.")


if __name__ == "__main__":
    main()
