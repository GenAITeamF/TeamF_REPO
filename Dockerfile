FROM nvidia/cuda:12.6.2-devel-ubuntu22.04

# 시스템 패키지 업데이트 및 필요한 도구 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
RUN pip3 install --no-cache-dir \
    vllm \
    jupyter \
    ray \
    fastapi \
    uvicorn \
    openai \
    gradio \
    pytest \
    black \
    isort \
    flake8

WORKDIR /app

CMD ["/bin/bash"]