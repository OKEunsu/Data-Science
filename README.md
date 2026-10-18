# 📚 Data Science Portfolio Repository

이 저장소는 데이터 사이언스 학습 및 프로젝트 수행 과정을 체계적으로 정리한 포트폴리오입니다.  
데이터 분석, 머신러닝, 딥러닝, 웹 크롤링, 시각화 등 다양한 주제의 실습과 프로젝트가 포함되어 있으며, 실제 경진대회 수상 및 문제 해결 사례도 다수 담고 있습니다.

---

## 🏆 대표 프로젝트

| 프로젝트 | 문제 | 방법 | 결과 |
|---|---|---|---|
| [이커머스 Data Warehouse 구축](03-Data-Engineering/e-commerce-data-warehouse) | 주문·결제·리뷰 등 8개 테이블로 흩어진 이커머스 데이터를 분석 가능한 구조로 | 스타 스키마 DW → 데이터마트 설계, SQL ETL | KPI 대시보드 배포 ([Streamlit](https://olist-ecommerce-dashboard-eunsu.streamlit.app/)) |
| [이커머스 RFM 고객 세분화](04-Projects/ecommerce-rfm-segmentation) | 동일 가중치 RFM이 매출 목표와 맞지 않는 세분화를 만드는 문제 | 변동계수(CV) 기반 가중치 RFM, KMeans, ANOVA, 코호트·연관규칙 | 5등급 10세그먼트, 세그먼트 간 차이 유의(p < 0.001), 세그먼트별 액션 플랜 |
| [소방안전 AI예측 경진대회](04-Projects/소방안전AI공모전) | 원주시 격자별 구급출동 사고 유형 예측 (3인 팀) | 기상·공간정보 외부 데이터 수집, GeoPandas, 유형별 이진 분류 | **2022 우수상** |

그 밖에 [A/B 테스트 시리즈](02-Data-Science/ab-testing), [Toss CTR 예측](04-Projects/toss-ctr-prediction)(1,070만 행), [LLM RAG 파이프라인](02-Data-Science/llm-rag), [추천 시스템](02-Data-Science/recommendation-system)이 있습니다.

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
├── ecommerce-rfm-segmentation/ 이커머스 RFM 가중치 고객 세분화
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

> 최상단의 `Data-Engineering/`, `Data_Science/`, `ProjectFiles/`, `Python/`은 구조 정리 전 링크를 위한 **이동 안내 폴더**입니다. 안의 README가 현재 위치로 안내합니다.

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
