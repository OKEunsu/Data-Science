**개요**
- 이 폴더는 RAG 파이프라인을 노트북으로 운영하기 위한 요약 문서입니다.
- 순서는 데이터 전처리 → 벡터DB 업로드 → 워크플로우 실행입니다.

**구성 파일**
- `data_processing.ipynb`: 원문 수집/정리, 청크 분할, 메타데이터 부여
- `upload_to_pinecone.ipynb`: 임베딩 생성 후 Pinecone 인덱스에 업서트
- `workflow.ipynb`: 검색기(retriever) + LLM + LangGraph로 질의응답 실행

**파일명 피드백**
- 현재 이름은 충분히 명확합니다. 그대로 사용해도 무방합니다.
- 권장(선택): 실행 순서 명시를 위해 접두어 번호를 붙이면 가독성이 더 좋아집니다.
  - `01_data_processing.ipynb`, `02_upload_to_pinecone.ipynb`, `03_workflow.ipynb`

**사전 준비**
- Python 3.11+ 권장, 가상환경 사용 권장(예: `.venv`)
- 필수 패키지(예): `langchain-openai`, `langchain-pinecone`, `pinecone`, `langgraph`, `python-dotenv`, `jupyter`
- OpenAI/Pinecone 자격 정보
  - OpenAI: `OPENAI_API_KEY`
  - Pinecone: `PINECONE_API_KEY`, `PINECONE_INDEX_NAME` (필요시 `PINECONE_ENV` 또는 `PINECONE_REGION`/`PINECONE_HOST`)

**.env 예시**
```
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=pc-...
PINECONE_INDEX_NAME=inhouse-python-index
# 필요 시
# PINECONE_ENV=gcp-starter
# PINECONE_REGION=us-east-1
# PINECONE_HOST=https://...pinecone.io
```

**임베딩/인덱스 규칙(중요)**
- 인덱스 차원은 임베딩 모델과 반드시 일치해야 합니다.
- 본 저장소 예시: `text-embedding-3-large`(3072차원) 사용 → Pinecone 인덱스도 `dimension=3072`여야 합니다.

**실행 순서**
1) `data_processing.ipynb`
   - 원문 로딩 → 청크 분할 → 메타데이터(예: `source`, `filename`) 확인
   - 업서트 시 사용할 `namespace`, `metadata` 키/값을 결정합니다.

2) `upload_to_pinecone.ipynb`
   - 임베딩 모델 설정: `text-embedding-3-large`(3072)
   - Pinecone 인덱스 이름(`PINECONE_INDEX_NAME`) 확인/생성
   - 문서 업서트(필요 시 `namespace` 지정, `metadata` 포함)

3) `workflow.ipynb`
   - `OpenAIEmbeddings(model="text-embedding-3-large")`로 검색기 초기화
   - `Pinecone.from_existing_index(index_name, embedding)`로 벡터스토어 연결
   - LangGraph 노드
     - `check_faq`: FAQ 포함 여부 판별(필요 시 `filter`와 `namespace` 적용)
     - `answer_faq`: 컨텍스트 기반 답변
     - `answer_general`: 일반 답변
   - 테스트: `app.invoke({"question": "..."})`

**FAQ 필터 팁**
- 업서트했던 `metadata` 키/값과 정확히 일치해야 합니다.
  - 예: `filter={"source": "employee_benefits_and_welfare_faq"}`
  - 또는 `filter={"filename": {"$eq": "employee_benefits_and_welfare_faq.md"}}`
- 업서트 시 `namespace`를 사용했다면 조회에도 동일 `namespace`를 지정하세요.

**자주 겪는 이슈**
- 벡터 차원 오류: `1536 != 3072` 등 → 임베딩 모델과 인덱스 차원을 맞추세요.
- 필터 결과 없음: `metadata` 키/값, `namespace`가 업서트와 다르면 빈 결과가 나옵니다.
- 응답 형식 제어: LLM 프롬프트에서 Yes/No만 반환하도록 명시하세요.

**빠른 실행(요약)**
- 가상환경 활성화 후 의존성 설치
  - `pip install -r requirements.txt` 또는 `uv sync`
- `.env` 설정
- 노트북 실행 순서: `data_processing` → `upload_to_pinecone` → `workflow`

**폴더 구조 예시**
- 루트
  - `data_processing.ipynb`
  - `upload_to_pinecone.ipynb`
  - `workflow.ipynb`
  - `rag_n8n/README.md`(현재 문서)

**라이선스/기여**
- 내부 프로젝트 기준에 따르세요. 외부 공개 전 민감정보 제거를 권장합니다.

