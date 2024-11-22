# TeamF_REPO

# vllm-env:new 이름으로 이미지 빌드
docker build -t vllm-env:new .

# vllm_container 이름으로 컨테이너 실행, 포트 8888-8888, gpu 사용, volume 사용,
docker run --name vllm_container -it -p 8888:8888 --gpus all -v vllm-data:/app/data -v %cd%:/app/workspace vllm-env:new

# 로컬호스트로 jupyter notebook 실행, 포트 8888
jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root
