FROM nvidia/cuda:12.6.2-devel-ubuntu22.04

# �ý��� ��Ű�� ������Ʈ �� �ʿ��� ���� ��ġ
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt ������ �����̳ʷ� ����
COPY requirements.txt /app/requirements.txt

# Python ��Ű�� ��ġ
RUN pip3 install --no-cache-dir -r /app/requirements.txt
WORKDIR /app

CMD ["/bin/bash"]