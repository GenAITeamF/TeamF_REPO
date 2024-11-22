FROM nvidia/cuda:12.6.2-devel-ubuntu22.04

# �ý��� ��Ű�� ������Ʈ �� �ʿ��� ���� ��ġ
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Python ��Ű�� ��ġ
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