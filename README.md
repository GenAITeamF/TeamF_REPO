vLLM : Colab에서 L4 GPU로 gpu-uyillization 0.8 옵션으로 수행함, chat template (jinja) 은 lms에 업로드된 예제 jinja를 사용함.

Gradio : FAISS-GPU를 사용하므로 GPU가 있는 컴퓨터에서 사용하면 성능 향상 있음; Colab에서 T4로 가동.
        Gradio는 Colab에서 작동하면 Colab을 자동으로 감지하여 share=True 옵션(Public URL) 으로 호스팅을 해줌.


vLLM <-> Gradio : Colab간 OpenAI 형식으로 통신, ngrok의 도메인을 사용하여 로컬호스트를 Public URL에서 접속 가능하게 함.

발표시 사용한 Prompt engineering 기법과 Prompt txt는 첨부된 Prompt.txt를 참고해 주세요.