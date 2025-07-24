# 🧼 데이터 전처리 & EDA 실습

이 디렉토리는 Pandas 및 다양한 도구를 활용한 **데이터 전처리 및 결측값 처리, EDA, 병렬 처리(MODIN)** 등에 관한 실습 및 이론 자료를 담고 있습니다.

---

## 📁 파일 구성

| 파일명 | 설명 |
|--------|------|
| `EDA Profiling.ipynb` | `pandas_profiling`을 이용한 자동 EDA 리포트 생성 |
| `MissingValues.md` | 결측치 처리에 대한 이론, 보간법, 회귀 대치 등 상세 설명 |
| `데이터_프레임_생성_삭제_결측값.ipynb` | 데이터프레임 생성, 삭제, 결측값 처리 등 기본 조작 |
| `데이터_추출_정렬.ipynb` | 행/열 조건 추출, 정렬 등 데이터 필터링 실습 |
| `데이터_프레임_결합.ipynb` | `merge`, `concat` 등을 이용한 데이터프레임 병합 방법 |
| `modin.md` | 대용량 데이터를 빠르게 처리하는 Pandas 대체 라이브러리 **MODIN** 소개 및 설치법 정리 |

---

## 📌 주요 학습 포인트

### ✅ 결측값 처리 전략

- MCAR / MAR / MNAR 개념 정리
- Listwise vs Pairwise 삭제
- 평균/중앙값 대치, 회귀 대치, KNN 대치, 다중 대치(MICE)
- 시계열 결측값 처리 (LOCF, Linear Interpolation, 계절 보정 등)

### ✅ 스케일링 개념 정리

- `StandardScaler`, `MinMaxScaler`, `RobustScaler`, `Normalizer`
- 트리 기반 모델 vs 거리 기반 모델에서의 스케일링 영향 차이

### ✅ 자동 EDA 도구 활용

- `pandas_profiling`으로 데이터 분포, 상관관계, 결측 분석 자동화

### ✅ 대용량 데이터 프레임 병렬 처리: MODIN

- Pandas API와 동일하게 사용할 수 있는 고속 라이브러리
- CPU 코어 병렬 활용
- 설치 방법 및 작동 방식, Pandas와의 성능 비교

```python
# 기존 Pandas 코드에서 아래처럼 한 줄만 변경
import modin.pandas as pd
