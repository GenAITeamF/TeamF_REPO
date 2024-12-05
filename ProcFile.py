import semchunk
from pdfplumber import open as open_pdf
import os
import pandas as pd
import json
from bs4 import BeautifulSoup
import re

def process_file(file):
    #global text_faiss_index, chunk_data, chunk_metadata

    if file is None:
        return "No file uploaded."

    file_name = os.path.basename(file.name)
    file_ext = os.path.splitext(file_name)[-1].lower()

    text_chunks = []
    metadata_chunks = []

    if file_ext == ".pdf":
        with open_pdf(file.name) as pdf:
            for page_num, page in enumerate(pdf.pages, start=1):
                page_text = page.extract_text()
                if page_text:
                    page_chunks = semchunk.chunkerify('gpt-4', chunk_size=200)(page_text)
                    for chunk in page_chunks:
                        chunks, metadata = process_chunks(chunk, file_name, "PDF", "page", page_num)
                        text_chunks.extend(chunks)
                        metadata_chunks.extend(metadata)
    elif file_ext in [".csv", ".xlsx"]:
        data = pd.read_csv(file.name) if file_ext == ".csv" else pd.read_excel(file.name)
        for i, row in data.iterrows():
            chunks, metadata = process_chunks(row.to_string(index=False), file_name, "CSV/Excel", "row", i + 1)
            text_chunks.extend(chunks)
            metadata_chunks.extend(metadata)
    elif file_ext == ".txt":
        with open(file.name, "r", encoding="utf-8") as txt_file:
            lines = txt_file.readlines()
            for i, line in enumerate(lines):
                chunks, metadata = process_chunks(line, file_name, "Text", "line", i + 1)
                text_chunks.extend(chunks)
                metadata_chunks.extend(metadata)
    elif file_ext == ".json":
        with open(file.name, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                chunks, metadata = process_chunks(f"{key}: {value}", file_name, "JSON", "key", key)
                text_chunks.extend(chunks)
                metadata_chunks.extend(metadata)
    elif file_ext in [".html", ".htm"]:
        with open(file.name, "r", encoding="utf-8") as html_file:
            soup = BeautifulSoup(html_file, "html.parser")
            for i, paragraph in enumerate(soup.get_text().split("\n")):
                if paragraph.strip():
                    chunks, metadata = process_chunks(paragraph, file_name, "HTML", "paragraph", i + 1)
                    text_chunks.extend(chunks)
                    metadata_chunks.extend(metadata)
    else:
        print("Unsupported file format. Supported formats: PDF, CSV, Excel, Text, JSON, HTML.")
        return None

    if not text_chunks:
        print("No valid chunks found in the file.")
        return None
    
    else:
        return file_name, text_chunks, metadata_chunks


    # chunk_data.extend(text_chunks)
    # chunk_metadata.extend(metadata_chunks)

    # embeddings = embedding_model.encode(text_chunks, batch_size=32, show_progress_bar=True)
    # embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

    # if text_faiss_index is None:
    #     if(GPU_FLAG):
    #         # GPU용 인덱스 생성
    #         flat_config = faiss.GpuIndexFlatConfig()
    #         flat_config.device = 0  # 사용할 GPU 장치 ID 설정 (보통 0번부터 시작)
    #         text_faiss_index = faiss.GpuIndexFlatL2(res, d, flat_config)
    #     else:
    #         d = embeddings.shape[1]
    #         text_faiss_index = faiss.IndexFlatL2(d)
    # text_faiss_index.add(embeddings)

    # return f"{file_name} processed successfully. {len(text_chunks)} chunks indexed."
    



# 텍스트 전처리 함수
def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # 다중 공백 제거
    text = re.sub(r'[^\w\s.,!?]', '', text)  # 불필요한 특수 문자 제거
    return text.strip()

# 텍스트 청크화 함수
def split_text_into_chunks(text, chunk_size=100):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

# 텍스트 청크 처리 통합 함수
def process_chunks(text, file_name, file_type, identifier_key, identifier_value, chunk_size=50):
    text = preprocess_text(text)
    chunks = split_text_into_chunks(text, chunk_size)
    metadata = [{
        "file": file_name,
        "type": file_type,
        identifier_key: identifier_value,
        "chunk_text": chunk
    } for chunk in chunks]
    return chunks, metadata
