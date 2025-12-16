# ------------------------------------------------------------
# BASE IMAGE (CUDA 12.2) + Ubuntu 22.04 (Python 3.10 by default)
# ------------------------------------------------------------
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# ------------------------------------------------------------
# SYSTEM DEPENDENCIES
# ------------------------------------------------------------
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Optional: make `python` point to python3
RUN ln -sf /usr/bin/python3 /usr/bin/python

# ------------------------------------------------------------
# PROJECT SETUP
# ------------------------------------------------------------
WORKDIR /code
COPY . /code

# ------------------------------------------------------------
# INSTALL LIBRARIES
# ------------------------------------------------------------
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# EXECUTION
# ------------------------------------------------------------
CMD ["bash", "inference.sh"]
