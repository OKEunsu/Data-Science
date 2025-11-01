# LangGraph RAG 워크플로우

이 저장소는 OpenAI LLM과 Pinecone 벡터 스토어를 이용해 FAQ 기반 RAG(Retrieval Augmented Generation) 워크플로우를 구성하는 예제입니다. 데이터 전처리부터 Pinecone 업로드, LangGraph 기반 워크플로우 실행까지 노트북 3개로 나뉘어 있으며, `rag_n8n/README.md`에 각 노트북의 세부 설명이 포함되어 있습니다.

## 주요 노트북
- **1_data_processing.ipynb**: 원본 Markdown 문서 정리, 텍스트 클리닝, 후속 단계에서 사용할 JSON/Markdown 파일 생성.
- **2_upload_to_pinecone.ipynb**: 전처리된 문서를 임베딩하여 Pinecone 인덱스(`inhouse-python-index`)에 업서트하고, 샘플 쿼리로 업로드 결과 검증.
- **3_workflow.ipynb**: LangGraph `StateGraph`로 FAQ 여부 판별 → 문서 선택 → 답변 생성 파이프라인 구성 및 테스트.

## 빠른 시작
1. **Python 3.11+** 환경을 준비하고 가상환경을 활성화합니다.
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate      # Windows
   ```
   uv를 사용한다면 `uv venv`로 대체할 수 있습니다.
2. **의존성 설치**
   ```bash
   uv sync                      # uv 사용 시
   # 또는
   pip install -r requirements.txt
   ```
3. **환경 변수 설정**: 루트에 `.env` 파일을 만들고 다음 값을 채웁니다.
   ```env
   OPENAI_API_KEY=sk-...
   PINECONE_API_KEY=pc-...
   PINECONE_INDEX_NAME=inhouse-python-index
   # 필요 시 PINECONE_ENV, PINECONE_REGION, PINECONE_HOST 등을 추가
   ```
4. **Jupyter 실행**
   ```bash
   uv run jupyter lab    # 또는 python -m jupyter lab
   ```
5. **노트북 실행 순서**
   1. `1_data_processing.ipynb`
   2. `2_upload_to_pinecone.ipynb`
   3. `3_workflow.ipynb`

## 핵심 구성요소
- **OpenAI LLM**: `ChatOpenAI`로 `gpt-4.1`, `gpt-4.1-mini` 등을 사용하며 temperature는 0으로 설정해 일관된 결과를 얻습니다.
- **OpenAI 임베딩**: `text-embedding-3-large` (3072차원). Pinecone 인덱스 차원과 반드시 일치해야 합니다.
- **Pinecone**: 이미 생성된 인덱스를 `Pinecone.from_existing_index()`로 불러와 `.as_retriever()`로 검색기를 구성합니다.
- **LangGraph**: `StateGraph(AgentState)`를 사용해 노드를 정의하고, FAQ 여부에 따라 다른 답변 경로로 분기합니다.

## 디렉터리 구조 (발췌)
```
project-root/
├─ 1_data_processing.ipynb
├─ 2_upload_to_pinecone.ipynb
├─ 3_workflow.ipynb
├─ rag_n8n/
│  └─ README.md            # 세부 가이드
├─ output/                 # 전처리 결과 및 참고 문서
├─ requirements.txt
└─ README.md (현재 파일)
```

## 참고
- 세부 절차와 트러블슈팅 팁은 `rag_n8n/README.md`를 참고하세요.
- Pinecone 인덱스를 새로 만들 경우, 임베딩 모델과 동일한 차원(예: 3072)을 지정한 뒤 업서트해야 합니다.
- LangChain, LangGraph, Pinecone API 사용법은 각 공식 문서를 확인하세요.
