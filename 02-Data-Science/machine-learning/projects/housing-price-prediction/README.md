# 🏠 보스턴 주택 가격 예측 프로젝트

## 📌 개요

- **목표**: 보스턴 지역 주택 특성 데이터로 중위 주택 가격(MEDV) 예측
- **데이터**: Boston Housing 데이터셋 (506 samples, 13 features)
- **문제 유형**: 회귀(Regression)
- **사용 도구**: Python (scikit-learn, XGBoost, LightGBM, seaborn)

---

## 📊 분석 프로세스

### 1. 데이터 구성

| 주요 변수 | 설명 |
|-----------|------|
| RM | 주택당 평균 방 수 |
| LSTAT | 하위 계층 인구 비율(%) |
| PTRATIO | 학생-교사 비율 |
| CRIM | 범죄율 |
| MEDV | 중위 주택 가격 (타겟) |

### 2. 모델 비교 (5-Fold CV RMSE 기준)

| 모델 | RMSE |
|------|------|
| Decision Tree (max_depth=5) | 5.394 |
| Linear Regression | 4.829 |
| Random Forest (n=100) | 3.819 |
| XGBoost (n=100) | 3.625 |
| **Gradient Boosting (n=100)** | **3.526** |
| LightGBM (n=100) | 3.725 |

### 3. Random Forest 하이퍼파라미터 튜닝

- GridSearchCV로 `n_estimators`, `max_depth`, `max_leaf_nodes` 탐색
- 최적 파라미터: `n_estimators=100`, `max_depth=20`, `max_leaf_nodes=30`
- **최종 Test 성능: RMSE 2.905, R² 0.885**

### 4. 변수 중요도 (Random Forest 기준)

| 변수 | 중요도 |
|------|--------|
| RM | 0.519 |
| LSTAT | 0.317 |
| DIS | 0.058 |
| CRIM | 0.033 |

---

## 💬 인사이트

- 방 수(RM)와 하위 계층 비율(LSTAT) 두 변수가 전체 예측의 80% 이상을 설명
- 트리 수를 1000 → 100으로 줄여도 성능 차이 거의 없음 (연산 효율 우선)
- Gradient Boosting이 CV RMSE 기준 가장 낮았으나, RF도 튜닝 후 테스트 성능 좋음

---

## 📂 파일 구성

| 파일 | 설명 |
|------|------|
| `Housing.ipynb` | 전체 EDA, 모델 비교, 튜닝 코드 |
| `housing.csv` | 보스턴 주택 데이터 |
| `README.md` | 본 문서 |
