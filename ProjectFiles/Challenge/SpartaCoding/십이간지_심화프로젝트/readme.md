# 🎧 십이간지 프로젝트 – Mood 따라 Music 따라 (feat. Mr.Cluster)

> **음악 데이터를 비지도학습 기반으로 클러스터링하고, 감성 기반 플레이리스트 추천으로 확장한 프로젝트입니다.**

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/324d2a25-6a4b-4215-ac8d-d93609ce04c8" />

---

## 📅 기간
**2024.12 ~ 2025.01 (약 4주)**  
데이터 분석 트랙 팀 프로젝트 (총 4인 구성)

---

## ✅ 프로젝트 개요

- Spotify 음원 데이터를 활용하여 감정 기반 클러스터링 수행
- K-means보다 **비선형 데이터에 적합한 Spectral Clustering**을 적용
- 클러스터별 감성 특징을 분석하고, 이에 기반한 **테마별 플레이리스트 제작**
- **Silhouette Score**, **Davies–Bouldin Index** 등 정량적 지표와  
  실제 **사용자 설문조사 기반 정성 평가** 병행

---

## 👥 역할 분담

| 역할 | 기여도 |
|------|--------|
| 데이터 전처리 및 분석 파이프라인 구성 | 60% |
| 클러스터링 모델 설계 및 하이퍼파라미터 튜닝 | ✅ 직접 주도 |
| 군집 평가 지표 선정 및 분석 | ✅ 직접 수행 |
| 사용자 대상 설문 설계 및 결과 해석 | 참여 |
| 프로젝트 발표자료 및 문서화 | 작성 및 정리 |

---

## 📈 주요 성과

- **Spectral Clustering** 기반 4개 감성 클러스터 도출  
- **Silhouette Score > 0.4**, **DBI 낮음** → 클러스터 품질 우수
- 설문 응답자 중 **80% 이상이 플레이리스트 만족**  
- **정량 지표 + 정성 지표 병행 평가**로 실무 적용 가능성 확인

---

## 🛠️ 주요 기술 스택 및 도구

- Python (Pandas, Scikit-learn, Matplotlib, UMAP, TSNE 등)
- Spectral Clustering, K-means 비교 실험
- 차원 축소 및 시각화: PCA, t-SNE, UMAP  
- 사용자 기반 플레이리스트 구성 및 설문 피드백 분석
- 커스텀 시각화 함수: [`dimensionality_visaul.py`](./dimensionality_visaul.py)

---

## 🗂️ 핵심 파일 목록

| 파일명 | 설명 |
|--------|------|
| `십이간지_심화프로젝트.ipynb` | 전체 프로젝트 워크플로우 정리 |
| `dimensionality_visaul.py` | 3D 차원 축소 시각화 함수 모듈 |
| `README.md` | 프로젝트 소개 및 문서화 (본 파일) |

---

## 🧾 발표 및 문서

- 📄 발표자료: [[12팀] 십이간지](https://www.notion.so/12-1962dc3ef51480df9c8ff6b3a28b6d32?pvs=21)
- 🎬 소개 콘텐츠: [ONAIR](https://www.notion.so/ONAIR-1854fe3aca3080eba58bd881a34a7518?pvs=21)
- 🍨 부가자료: [투게더](https://www.notion.so/1992dc3ef5148055ab51e4a7dc72b537?pvs=21)
- ✍ 블로그 후기: [2025-02-07 TIL(일기, 프로젝트 회고)](https://okbublewrap.tistory.com/222)

---

## 💬 피드백 요약

### 🟩 긍정적 피드백

- K-means 외 **Spectral Clustering** 활용 → **차별화 우수**
- **사용자 설문 기반 정성적 평가** 포함 → 실용성 높음
- **필터링 기준 명확**, 발표자료 구성이 직관적
- 제한된 기간 내 **심화 모델 적용 및 평가 체계 구축** 노력 인상적

### 🔧 개선점 제안

- **EDA 및 탐색적 분석 내용 부족** (데이터 특징 및 분포 시각화 필요)
- **지표 간 해석 논리 연결 강화** (예: 클러스터 수 조정 과정)
- **지표 설명의 직관성 보완 필요** (일반 청중 대상 전달력 개선)
- **기획 의도와 최종 결과 간 명확한 연결성 강조 필요**

---

## 🔚 총평

> "단기간 프로젝트임에도 불구하고, 일반적인 군집화에서 벗어나 **비선형 모델 실험**,  
> 실제 사용자 평가를 통한 **현실 적용성 검증**까지 시도한 점이 매우 인상적입니다." 👏👏

---

## 📜 라이선스

본 프로젝트는 학습 및 비상업적 목적에 한하여 자유롭게 활용 가능합니다.
