# Auto run script - Tự động chạy và đợi 1 giờ rồi chạy tiếp
# Chạy: python auto_process.py

import subprocess
import time
import json
import os
from datetime import datetime

def count_processed():
    """Đếm số câu đã xử lý"""
    if os.path.exists("data/long_text_results.json"):
        with open("data/long_text_results.json", "r", encoding="utf-8") as f:
            return len(json.load(f))
    return 0

def count_total_long_text():
    """Đếm tổng số câu Long Text"""
    with open("data/val_routed.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return len([x for x in data if x.get("datasource") == "Long_Text_Questions"])

def main():
    total = count_total_long_text()
    print(f"Tổng số câu Long Text: {total}")
    
    round_num = 1
    
    while True:
        processed = count_processed()
        remaining = total - processed
        
        print(f"\n{'='*60}")
        print(f"ROUND {round_num}")
        print(f"Đã xử lý: {processed}/{total} câu")
        print(f"Còn lại: {remaining} câu")
        print(f"{'='*60}")
        
        if remaining == 0:
            print("\n🎉 HOÀN TẤT! Đã xử lý hết tất cả câu hỏi Long Text!")
            break
        
        # Chạy handler
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Bắt đầu xử lý...")
        
        result = subprocess.run(
            ["python", "query/long_text_handler.py", "--max-calls", "50"],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        # Kiểm tra lại
        new_processed = count_processed()
        calls_made = new_processed - processed
        
        print(f"\n✅ Round {round_num} xong: Đã xử lý thêm {calls_made} câu")
        
        if new_processed >= total:
            print("\n🎉 HOÀN TẤT!")
            break
        
        # Đợi 1 giờ
        print(f"\n⏰ Đợi 1 giờ để tránh quota...")
        print(f"   Bắt đầu lúc: {datetime.now().strftime('%H:%M:%S')}")
        print(f"   Tiếp tục lúc: {(datetime.now().timestamp() + 3600).__class__(datetime.fromtimestamp(datetime.now().timestamp() + 3600)).strftime('%H:%M:%S')}")
        
        # Đợi 1 giờ (3600 giây)
        for remaining_seconds in range(3600, 0, -60):
            mins = remaining_seconds // 60
            print(f"   Còn {mins} phút...", end="\r")
            time.sleep(60)
        
        print("\n")
        round_num += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Bị ngắt bởi user. Progress đã được lưu.")
        print("Chạy lại script để tiếp tục.")
