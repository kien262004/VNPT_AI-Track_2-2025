import json
import csv
import argparse
from typing import Dict, Tuple


def load_val_answers(val_json_path: str) -> Dict[str, str]:
    with open(val_json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    ans = {}
    for item in data:
        qid = (item.get("qid") or "").strip()
        a = (item.get("answer") or "").strip().upper()
        if qid:
            ans[qid] = a
    return ans


def load_predictions(csv_path: str) -> Dict[str, tuple[str, str]]:
    # qid -> (pred, route)
    preds = {}
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            qid = (row.get("qid") or "").strip()
            a = (row.get("answer") or "").strip().upper()
            route = (row.get("route") or "").strip() or "UNKNOWN"
            if qid:
                preds[qid] = (a, route)
    return preds

from collections import defaultdict

def score_by_route(val: Dict[str, str], pred: Dict[str, tuple[str, str]]):
    # route -> [correct, total, missing]
    stats = defaultdict(lambda: {"correct": 0, "total": 0, "missing": 0})
    for qid, gt in val.items():
        if qid not in pred:
            stats["MISSING"]["missing"] += 1
            continue
        p, r = pred[qid]
        stats[r]["total"] += 1
        if p == gt:
            stats[r]["correct"] += 1
    return stats



def score(val: Dict[str, str], pred: Dict[str, str]) -> Tuple[int, int, int, int]:
    correct = 0
    total = len(val)
    missing = 0
    wrong = 0

    for qid, gt in val.items():
        if qid not in pred:
            missing += 1
            continue
        if pred[qid] == gt:
            correct += 1
        else:
            wrong += 1

    extra = sum(1 for qid in pred.keys() if qid not in val)
    return correct, wrong, missing, extra

def dump_mismatches(val, pred, out_path):
    rows = []
    for qid, gt in val.items():
        if qid not in pred:
            continue
        p, r = pred[qid]
        if p != gt:
            rows.append((qid, gt, p, r))
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["qid", "gold", "pred", "route"])
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--val_json", default="data/val.json")
    ap.add_argument("--pred_csv", default="result_val.csv")
    ap.add_argument("--mismatch_csv", default="mismatches_val.csv")
    args = ap.parse_args()

    val = load_val_answers(args.val_json)
    pred = load_predictions(args.pred_csv)

    correct, wrong, missing, extra = score(val, pred)
    total = len(val)
    attempted = total - missing

    acc_all = correct / total if total else 0.0
    acc_attempted = correct / attempted if attempted else 0.0

    print(f"Val size        : {total}")
    print(f"Pred size       : {len(pred)}")
    print(f"Correct         : {correct}")
    print(f"Wrong           : {wrong}")
    print(f"Missing (no pred): {missing}")
    print(f"Extra (pred not in val): {extra}")
    print(f"Accuracy (over all val)      : {acc_all:.4f} ({acc_all*100:.2f}%)")
    print(f"Accuracy (over attempted only): {acc_attempted:.4f} ({acc_attempted*100:.2f}%)")

    dump_mismatches(val, pred, args.mismatch_csv)
    print(f"Saved mismatches to: {args.mismatch_csv}")

    stats = score_by_route(val, pred)
    print("\n=== Accuracy by route ===")
    for r, s in sorted(stats.items(), key=lambda x: x[0]):
        total = s["total"]
        correct = s["correct"]
        acc = correct / total if total else 0.0
        print(f"{r:24s}  total={total:4d}  correct={correct:4d}  acc={acc*100:6.2f}%")


if __name__ == "__main__":
    main()
