# 📚 Data Science Portfolio Repository

이 저장소는 데이터 사이언스 학습 및 프로젝트 수행 과정을 체계적으로 정리한 포트폴리오입니다.  
데이터 분석, 머신러닝, 딥러닝, 웹 크롤링, 시각화 등 다양한 주제의 실습과 프로젝트가 포함되어 있으며, 실제 경진대회 수상 및 문제 해결 사례도 다수 담고 있습니다.

---

## 🗂️ 디렉토리 구조

```
01-Python-Basics/              👉 파이썬 기초 학습
├── basic-library/             기초 라이브러리 활용 예제
├── coding-test/               코딩 테스트 문제 풀이
├── django/                    Django 프레임워크 실습
├── functions/                 함수 문법 실습
├── oop/                       객체지향 프로그래밍 기초
├── pandas-practice/           판다스 실무형 데이터 분석 (13개 실습)
├── 디렉토리 처리/              파일 입출력 및 디렉토리 자동화
└── 자료구조_알고리즘/           기본 알고리즘 및 자료구조 실습

02-Data-Science/               👉 데이터 사이언스 핵심 학습
├── ab-testing/                A/B 테스트 실습 및 분석 (3개 시리즈)
├── data-processing/           EDA, 결측값 처리, 프레임 결합 등 전처리
├── data-visualization/        matplotlib, Streamlit 시각화 예제
├── machine-learning/
│   ├── study/                 지도/비지도 학습, 모델 평가
│   └── projects/              금융예측, 자전거수요, 호텔예약 등 8개 프로젝트
├── deep-learning/
│   ├── basics/                딥러닝 기초, Tensorflow
│   ├── applications/          EasyOCR, 주식 예측
│   ├── 딥러닝에센스/            뉴럴네트워크, CNN, RNN 학습
│   └── 머신러닝_딥러닝/         Numpy, Step1 실습
├── computer-vision/
│   ├── opencv-basics/         OpenCV 기초, 드로잉, DNN, Haar-cascade
│   ├── image-classification/  이미지 분류 (꽃, 개/고양이 등)
│   └── object-detection/      YOLO, Darknet, 차량 추적 등 13개 노트북
├── nlp/                       자연어 처리 (LIME, 정규식, 텍스트 분석)
├── crawling/                  웹 크롤링, 네이버 카페 자동화, 병렬 크롤러
├── recommendation-system/     추천 시스템 (협업 필터링)
└── llm-rag/                   RAG + n8n 워크플로우 파이프라인

03-Data-Engineering/           👉 데이터 엔지니어링
├── e-commerce-data-warehouse/ 이커머스 DW → DM 구축 프로젝트
└── 학습자료/                   데이터 엔지니어링 학습자료

04-Projects/                   👉 프로젝트 모음
├── 🏆 소방안전AI공모전/        2022 제2회 소방안전 AI예측 경진대회 우수상 수상작
├── dacon-e-commerce/          Dacon 이커머스 고객 세분화
├── toss-ctr-prediction/       Toss CTR 예측 모델링
├── busan-commute-analysis/    부산시 출퇴근 교통 분석
├── sonocam-review-analysis/   소노캄 거제 리뷰 분석
├── housing-price-prediction/  주택 가격 예측
├── london-bicycle-demand/     런던 자전거 수요 예측
├── wine-classification/       와인 품질 분류
├── 카드거래이력_분석/           카드 거래 이력 분석
├── pixelbay-crawler/          Pixelbay 이미지 크롤러
├── bigquery-upload/           BigQuery 연동 스크립트
└── bootcamp/
    ├── sparta-coding/         스파르타코딩 프로젝트
    └── wanted-analyst/        Wanted 데이터 분석 챌린지

05-Interview-Prep/             👉 기술 면접 준비 자료

configs/                       👉 환경 설정 및 유틸
├── ColabSetting.ipynb         Colab 환경 설정
├── colabSetting.py            Colab 설정 스크립트
├── github.md                  GitHub 가이드
└── utils/                     유틸리티 함수
```

---

## 🏆 대표 프로젝트

### 🔥 소방안전 AI예측 경진대회 (2022 우수상)
- **목표**: 원주시 격자별 사고 유형 예측
- **기술**: GeoPandas, Scikit-Learn, 시계열 + 공간 정보 처리
- **성과**: 외부 데이터 수집 및 지리 분석 기반 정밀한 예측 모델 개발

### 📊 A/B 테스트 분석 시리즈
- conversion, 캠페인 퍼널, UI 테스트 등 실무형 A/B 실험 분석

### 🎯 추천 시스템 개발
- 사용자 기반, 아이템 기반 협업 필터링 구현

### 🏗️ 이커머스 Data Warehouse 구축
- Brazilian E-commerce 데이터 기반 DW → DM 파이프라인

### 🤖 LLM RAG 파이프라인
- Pinecone + n8n 기반 RAG 워크플로우 및 에이전트 구현

---

## ⚙️ 기술 스택

- **Language**: Python, SQL
- **Data**: Pandas, NumPy, Scikit-learn
- **Deep Learning**: Tensorflow, Keras, OpenCV
- **Visualization**: Seaborn, Matplotlib, Streamlit, Folium
- **Geo/Spatial**: GeoPandas
- **Infra**: BigQuery, Selenium, FastAPI
- **LLM/AI**: LangChain, Pinecone, n8n

---

## 📎 사용법

각 디렉토리의 `README.md` 또는 노트북 상단의 마크다운 셀을 통해 사용 방법, 코드 설명, 프로젝트 배경 등을 확인하실 수 있습니다.

---

## 🙋‍♂️ 작성자

- **이름**: 옥은수 (OK Eunsu)
- **목표**: 데이터로 의미를 만드는 분석가
- **연락처**: esok0617@gmail.com

---

이 저장소는 지속적으로 업데이트되며, 실무 중심의 데이터 분석 및 AI 응용 역량 강화를 목표로 합니다.
