"""
Evaluate script - So sánh đáp án dự đoán với đáp án chuẩn
"""

import json
import sys
import os


def evaluate(ground_truth_file: str, prediction_file: str):
    """
    So sánh đáp án dự đoán với ground truth
    
    Args:
        ground_truth_file: File có đáp án đúng (val_routed.json)
        prediction_file: File đáp án dự đoán (long_text_results.json)
    """
    # Đọc ground truth
    with open(ground_truth_file, "r", encoding="utf-8") as f:
        ground_truth = json.load(f)
    
    # Tạo dict mapping qid -> answer đúng
    gt_dict = {item["qid"]: item["answer"] for item in ground_truth}
    
    # Đọc predictions
    with open(prediction_file, "r", encoding="utf-8") as f:
        predictions = json.load(f)
    
    # So sánh
    total = 0
    correct = 0
    wrong = 0
    missing = 0
    
    details = []
    
    for pred in predictions:
        qid = pred["qid"]
        pred_answer = pred["answer"]
        
        if qid not in gt_dict:
            print(f"[WARN] qid={qid} không có trong ground truth")
            missing += 1
            continue
        
        true_answer = gt_dict[qid]
        total += 1
        
        is_correct = (pred_answer.upper() == true_answer.upper())
        
        if is_correct:
            correct += 1
            status = "✓"
        else:
            wrong += 1
            status = "✗"
        
        details.append({
            "qid": qid,
            "predicted": pred_answer,
            "true": true_answer,
            "correct": is_correct,
            "status": status
        })
    
    # Tính accuracy
    accuracy = (correct / total * 100) if total > 0 else 0
    
    # In kết quả
    print("=" * 60)
    print("EVALUATION RESULTS")
    print("=" * 60)
    print(f"Ground Truth File: {ground_truth_file}")
    print(f"Prediction File:   {prediction_file}")
    print("-" * 60)
    print(f"Total Questions:   {total}")
    print(f"Correct:           {correct} ✓")
    print(f"Wrong:             {wrong} ✗")
    print(f"Missing in GT:     {missing}")
    print("-" * 60)
    print(f"ACCURACY:          {accuracy:.2f}%")
    print("=" * 60)
    
    # In chi tiết các câu sai
    if wrong > 0:
        print("\nCÂU TRẢ LỜI SAI:")
        print("-" * 60)
        for detail in details:
            if not detail["correct"]:
                print(f"{detail['status']} qid={detail['qid']}: "
                      f"Predicted={detail['predicted']}, "
                      f"True={detail['true']}")
    
    # Lưu report
    report_file = prediction_file.replace('.json', '_report.json')
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total": total,
                "correct": correct,
                "wrong": wrong,
                "missing": missing,
                "accuracy": accuracy
            },
            "details": details
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\nĐã lưu báo cáo chi tiết: {report_file}")
    
    return accuracy


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Evaluate predictions against ground truth")
    parser.add_argument(
        "--ground-truth",
        default="data/val_routed.json",
        help="File có đáp án đúng"
    )
    parser.add_argument(
        "--prediction",
        default="data/long_text_results.json",
        help="File đáp án dự đoán"
    )
    
    args = parser.parse_args()
    
    # Check files exist
    if not os.path.exists(args.ground_truth):
        print(f"[ERROR] File không tồn tại: {args.ground_truth}")
        sys.exit(1)
    
    if not os.path.exists(args.prediction):
        print(f"[ERROR] File không tồn tại: {args.prediction}")
        sys.exit(1)
    
    # Evaluate
    evaluate(args.ground_truth, args.prediction)


if __name__ == "__main__":
    main()
