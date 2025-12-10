import os
import json
import csv
from typing import List, Set

from src.core.llm import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

# Số câu tối đa xử lý mỗi lần chạy để tránh đụng quota 60 req/giờ
MAX_CALLS_PER_RUN = 50

SYSTEM_PROMPT = (
    "Bạn là trợ lý làm bài trắc nghiệm nhiều lựa chọn.\n"
    "Với mỗi câu hỏi và danh sách các lựa chọn A, B, C, D, ... "
    "hãy chọn ĐÚNG MỘT đáp án.\n\n"
    "QUY TẮC BẮT BUỘC:\n"
    "- CHỈ trả về duy nhất MỘT ký tự là chữ cái của đáp án (A, B, C, D, ...).\n"
    "- KHÔNG giải thích, không thêm bất kỳ ký tự hay câu chữ nào khác.\n"
    "- Không trả về nội dung của phương án, chỉ trả về chữ cái.\n"
)

def build_question_prompt(question_text: str, choices: List[str]) -> str:
    """Tạo prompt cho 1 câu hỏi với các lựa chọn A, B, C, ..."""
    lines = [f"Câu hỏi: {question_text}", "", "Các lựa chọn:"]
    for idx, choice in enumerate(choices):
        letter = chr(ord("A") + idx)
        lines.append(f"{letter}. {choice}")
    lines.append("")
    lines.append("Hãy trả lời CHỈ MỘT ký tự là chữ cái của đáp án đúng (A, B, C, ...).")
    return "\n".join(lines)


def parse_answer(raw_answer: str, num_choices: int) -> str:
    """
    Chuẩn hóa câu trả lời từ LLM thành một chữ cái A, B, C, ...
    Nếu không parse được thì fallback về 'A' (cho an toàn, không crash).
    """
    if not raw_answer:
        return "A"

    text = raw_answer.strip().upper()

    # Nếu chỉ có 1 ký tự và là A..Z thì dùng luôn
    if len(text) == 1 and "A" <= text <= "Z":
        idx = ord(text) - ord("A")
        if 0 <= idx < num_choices:
            return text

    # Nếu model trả kiểu 'Đáp án: C', 'Tôi chọn phương án D', ...
    for ch in text:
        if "A" <= ch <= "Z":
            idx = ord(ch) - ord("A")
            if 0 <= idx < num_choices:
                return ch

    # Fallback an toàn
    return "A"


def load_answered_qids(submission_path: str) -> Set[str]:
    """Đọc submission.csv nếu có, trả về tập các qid đã được trả lời."""
    answered = set()
    if os.path.exists(submission_path):
        with open(submission_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                qid = row.get("qid")
                if qid:
                    answered.add(qid)
    return answered


def main():
    # Đường dẫn trong container (WORKDIR đã là /code)
    test_path = os.path.join("data", "test.json")
    submission_path = "submission.csv"

    # Load dữ liệu test
    with open(test_path, "r", encoding="utf-8") as f:
        test_data = json.load(f)

    # Đọc các qid đã trả lời (nếu có)
    answered_qids = load_answered_qids(submission_path)
    print(f"Đã có {len(answered_qids)} câu đã trả lời trong submission.csv")

    # Chuẩn bị writer cho submission.csv (append nếu file đã tồn tại)
    file_exists = os.path.exists(submission_path)
    csv_file = open(submission_path, "a", newline="", encoding="utf-8")
    writer = csv.writer(csv_file)

    # Nếu file mới tạo, ghi header
    if not file_exists:
        writer.writerow(["qid", "answer"])

    # Khởi tạo LLM small VNPT
    # Nếu get_llm của bạn có thêm tham số cfg/router, chỉnh lại dòng dưới cho khớp
    small_cfg = {
        "temperature": 0.0,
        "top_p": 1.0,
        "top_k": 20,
        "max_tokens": 64,
    }

    # Thử gọi với cfg (router version mới), nếu project cũ không nhận cfg thì fallback
    try:
        llm = get_llm("large_vnpt", cfg=small_cfg)
    except TypeError:
        # Trường hợp hàm get_llm cũ, không có tham số cfg
        llm = get_llm("large_vnpt")

    calls_made = 0
    total_questions = len(test_data)

    try:
        for idx, item in enumerate(test_data, start=1):
            qid = item["qid"]

            # Nếu đã có câu trả lời cho qid này thì bỏ qua
            if qid in answered_qids:
                print(f"[SKIP] qid={qid} đã có trong submission.csv")
                continue

            # Nếu đã đạt giới hạn cho run này thì dừng
            if calls_made >= MAX_CALLS_PER_RUN:
                print(f"Đã đạt MAX_CALLS_PER_RUN = {MAX_CALLS_PER_RUN}, dừng run hiện tại.")
                break

            question = item["question"]
            choices = item["choices"]

            prompt = build_question_prompt(question, choices)

            messages = [
                SystemMessage(content=SYSTEM_PROMPT),
                HumanMessage(content=prompt),
            ]

            try:
                ai_msg = llm.invoke(messages)
                raw_answer = getattr(ai_msg, "content", str(ai_msg))

                # Nếu API trả về nội dung từ chối (nhạy cảm)
                if "không thể trả lời" in raw_answer.lower() or "không thể phản hồi" in raw_answer.lower():
                    print(f"[SENSITIVE] VNPT từ chối câu qid={qid}. Ghi answer rỗng.")
                    writer.writerow([qid, ""])
                    csv_file.flush()
                    calls_made += 1
                    continue

            except Exception as e:
                # Nếu lỗi là dạng "VNPT API logical error response: {...}" → API từ chối
                msg = str(e)
                if "VNPT API logical error response" in msg and "BadRequestError" in msg:
                    print(f"[SENSITIVE-ERROR] VNPT từ chối qid={qid}. Ghi answer rỗng.")
                    writer.writerow([qid, ""])
                    csv_file.flush()
                    calls_made += 1
                    continue

                # còn lại là lỗi thật → dừng run
                print(f"[ERROR] Lỗi khi gọi LLM cho qid={qid}: {e}")
                break

            answer_letter = parse_answer(raw_answer, num_choices=len(choices))

            writer.writerow([qid, answer_letter])
            csv_file.flush()  # Đảm bảo ghi ngay ra đĩa

            calls_made += 1
            print(
                f"[{idx}/{total_questions}] qid={qid} -> {answer_letter} "
                f"(raw: {raw_answer!r}) | calls_made={calls_made}"
            )
    finally:
        csv_file.close()

    print(
        f"Run này đã xử lý thêm {calls_made} câu mới. "
        f"Tổng số câu đã có trong submission.csv bây giờ sẽ là ~{len(answered_qids) + calls_made}."
    )
    print("Bạn có thể chạy lại script sau khi qua giới hạn 60 req/giờ để tiếp tục.")


if __name__ == "__main__":
    main()
