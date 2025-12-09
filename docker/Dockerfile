# BASE IMAGE
# ------------------------------------------------------------
FROM nvidia/cuda:12.2.0-devel-ubuntu20.04

# ------------------------------------------------------------
# SYSTEM DEPENDENCIES
# Cài đặt Python, Pip và các gói hệ thống cần thiết
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y \
   python3 \
   python3-pip \
   git \
   && rm -rf /var/lib/apt/lists/*

# Link python3 thành python nếu cần
RUN ln -s /usr/bin/python3 /usr/bin/python

# ------------------------------------------------------------
# PROJECT SETUP
# ------------------------------------------------------------
# Thiết lập thư mục làm việc (có thể thay thành tên thư mục dự án của bạn)
WORKDIR /code

# Sao chép toàn bộ source code từ thư mục gốc của dự án vào container
COPY ./ /code

# ------------------------------------------------------------
# INSTALL LIBRARIES
# ------------------------------------------------------------
# Nâng cấp pip và cài đặt các thư viện từ requirements.txt
RUN pip3 install --no-cache-dir --upgrade pip && \
   pip3 install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# EXECUTION
# Lệnh chạy mặc định khi container khởi động
# Pipeline sẽ đọc private_test.json và xuất ra submission.csv
# ------------------------------------------------------------
CMD ["bash", "inference.sh"]
