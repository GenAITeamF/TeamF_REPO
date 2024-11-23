FROM nvidia/cuda:12.6.2-devel-ubuntu22.04

# 시스템 패키지 업데이트 및 필요한 도구 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt /app/requirements.txt

# Python 패키지 설치
RUN pip3 install --no-cache-dir -r /app/requirements.txt
WORKDIR /app

CMD ["/bin/bash"]