# 🍷 와인 품종 분류 프로젝트

## 📌 개요

- **목표**: 와인의 화학적 성분 데이터를 기반으로 품종(0, 1, 2) 분류
- **데이터**: sklearn 내장 wine 데이터셋 (178 samples, 13 features, 3 classes)
- **사용 도구**: Python (scikit-learn, pandas, seaborn, missingno)

---

## 📊 분석 프로세스

### 1. EDA

- 결측값 없음
- 각 변수의 분포 및 boxplot으로 이상치 확인 (`malic_acid` 상위 3개 이상치 발견)
- 상관계수 히트맵으로 변수 간 관계 파악

### 2. 피처 선택

- Decision Tree의 `feature_importances_`를 기준으로 상위 7개 변수 선택
- 선택 변수: `proline`, `od280/od315_of_diluted_wines`, `flavanoids`, `hue`, `color_intensity`, `alcohol`, `malic_acid`

### 3. 모델 비교

| 모델 | 전처리 | Accuracy |
|------|--------|----------|
| Decision Tree | 없음 | 0.87 |
| Decision Tree (튜닝: min_samples_leaf=4) | 없음 | 0.81 |
| SVM (linear, C=1) | StandardScaler | 0.96 |
| **SVM (GridSearch 최적)** | **StandardScaler** | **0.98** |

### 4. 최적 모델

- **SVM (kernel=linear, C=10, gamma=scale)**
- GridSearchCV (cv=5) 기준 Best Score: 0.99
- Test Accuracy: **0.98**

---

## 💬 인사이트

- 표준화(StandardScaler)가 SVM 성능에 결정적 영향을 줌
- Decision Tree 단독보다 SVM이 이 데이터셋에 더 적합
- `proline`, `flavanoids`가 품종 구분에 가장 중요한 변수

---

## 📂 파일 구성

| 파일 | 설명 |
|------|------|
| `Wine.ipynb` | EDA, 피처 선택, 모델링 전체 코드 |
| `README.md` | 본 문서 |
