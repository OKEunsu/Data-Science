# 📱 토스 CTR 예측 대회

## 📌 개요

- **목표**: 광고 클릭률(CTR) 예측을 위한 이진 분류 모델 개발
- **데이터**: 훈련 10.7M rows × 119 features / 테스트 1.5M rows
- **타겟**: `clicked` (클릭 여부, CTR ≈ 1.9% — 극심한 클래스 불균형)
- **사용 도구**: Python (PyTorch, scikit-learn, XGBoost, CUDA)

---

## 📊 데이터 구성

| 피처 그룹 | 개수 | 설명 |
|-----------|------|------|
| demographic | 2 | gender, age_group |
| contextual | 4 | inventory_id, day_of_week, hour, seq |
| l_feat | 27 | 광고 관련 범주형 피처 |
| feat_a~e | 48 | 익명화된 수치/범주형 피처 |
| history_a | 7 | 사용자 행동 이력 |

---

## ⚙️ 전처리

- **High cardinality 피처 제거**: gender, age_group, inventory_id 등 6개 (unique 추정치 300 초과)
- **범주형 33개**: LabelEncoding (ThreadPoolExecutor 병렬 처리)
- **수치형 79개**: StandardScaler (병렬 처리)
- **결측값**: 96개 컬럼에 결측 존재 → 수치형은 0으로 채움, 범주형은 'missing' 클래스 처리
- **최종 피처 수**: 112개

---

## 🤖 모델링

### DeepCTR Model (메인)

```
입력(112) → BatchNorm → Dense(256) → BN → ReLU → Dropout(0.3)
          → Dense(128) → BN → ReLU → Dropout(0.3)
          → Dense(64)  → BN → ReLU → Dropout(0.3)
          → Dense(1) → Sigmoid
```

- **Loss**: BCEWithLogitsLoss
- **Optimizer**: Adam (lr=0.001, weight_decay=1e-5)
- **Scheduler**: ReduceLROnPlateau
- **학습 최적화**: Mixed Precision (AMP, GradScaler), CUDA
- **배치 크기**: 2048, DataLoader workers: 6

### Baseline (비교)
- Sequence LSTM + MLP 기반 CTR 예측 (`[Baseline]` 노트북)

---

## 📈 결과

| 지표 | 값 |
|------|-----|
| Best Validation AUC | **0.6988** |
| Final Validation AUC | 0.6975 |
| Validation LogLoss | 0.0888 |
| 예측값 평균 (테스트) | 0.0189 |

- 15 에포크 동안 AUC 0.688 → 0.699로 점진적 개선
- 예측 분포가 실제 CTR(~1.9%)과 유사하게 형성됨

---

## 💬 인사이트 및 회고

- **클래스 불균형** (CTR 1.9%)이 핵심 난제 — LogLoss 기준 최적화 시 AUC 트레이드오프 발생
- High cardinality 피처(hour, day_of_week 등)를 제거했으나 이 정보가 CTR 예측에 중요할 수 있음 → 임베딩 처리로 대체 시도 여지 있음
- 10.7M 대용량 데이터 전처리에 ThreadPoolExecutor로 병렬화 적용 — 효과적

---

## 📂 파일 구성

| 파일 | 설명 |
|------|------|
| `CTR_Modeling_Pipeline.ipynb` | 전처리, DeepCTR 모델링, 제출 파일 생성 전체 파이프라인 |
| `[Baseline]_Sequence LSTM + MLP 기반 CTR 예측.ipynb` | 베이스라인 비교 모델 |
| `readme.md` | 본 문서 |
