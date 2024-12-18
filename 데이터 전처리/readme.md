[How to Handle Missing Data](https://towardsdatascience.com/how-to-handle-missing-data-8646b18db0d4)

1. MAR(Missing at Random) : 임의적으로 누락된다는 것은 데이터 포인트가 누락되는 경향이 누락된 데이터와 관련이 없지만 일부 관측 데이터와 관련이 있음을 의미합니다.
2. MCAR(Missing Completely at Random) : 특정 값이 누락되었다는 사실은 가상 값 및 다른 변수의 값과 관련이 없습니다.
3. MNAR(Missing not at Random) : 두 가지 가능한 이유는 누락된 값이 가상 값에 따라 달라지거나 누락된 값이 다른 변수의 값에 따라 달라지기

→ 처음 두 경우에는 발생에 따라 결측값이 있는 데이터를 제거하는 것이 안전하지만 세번째 경우에는 결측값이 있는 관측값을 제거하면 모델에 편향이 생길수 있습니다. 제거 하기 전에는 정말 조심해야 한다.

![image](https://github.com/user-attachments/assets/10acb180-fcbc-4803-bf44-460118cba747)


## 제거

### **Listwise**

목록별 삭제는 하나 이상의 결측값이 있는 관찰에 대한 모든 데이터를 제거합니다. 결과적으로 목록별 삭제 방법은 편향된 매개 변수와 추정치를 생성합니다.

```python
df.dropna(inplace = True)
```

### Pairwise

관심 변수가 존재하는 모든 경우를 분석하여 분석 기준으로 사용 가능한 모든 데이터를 최대화합니다. 장점은 분석의 검정력을 증가시키는 점, 단점은 모델의 다른 부분에 기여하는 다른 수의 관측치가 생겨 해석이 어려울 수 있습니다.

|  | ageNA | DV1 | DV2 |
| --- | --- | --- | --- |
| 1, | 18 | NA | 9 |
| 2, | NA | 1 | 4 |
| 3, | 27 | 5 | 2 |
| 4, | 22 | -3 | 7 |

case 1 : 3, 4은 ageNa, DV1의 공분산을 찾는데 사용할 수 있습니다.

case 2 : 2,3,4은 DV1, DV2의 공분산을 찾는데 사용할 수 있습니다.

### Drop Variance

경우에 따라 60%이상의 관측치에 대해 데이터가 누락되었지만 해당 변수가 중요하지 않은 경우에만 변수를 삭제할 수 있다. (왠만해서는 삭제하지 말자)

## 시계열 특정 방법

### LOCF(Last Observation Carried Forward) 및 NOCB(Next Observation Carried Backward)

일부 후속 관찰이 누락될 수 있는 종단 반복 측정 데이터 분석에 대한 일반적인 통계적 접근 방식

이 두가지 방법은 분석에 편향을 가져올 수 있으며 데이터에 대한 가시적인 추세가 있을 때 성능이 저하될 수 있다.

### Linear Interpolation

이 방법은 추세가 있는 시계열에는 적합하지만 계절 데이터에는 적합하지 않다.

### 계절 조정 + 선형 보간

이 방법은 추세와 계절성이 모두 있는 데이터에 적합합니다.

![image](https://github.com/user-attachments/assets/70873593-8661-415f-9a34-82c0d726c4a5)
![image](https://github.com/user-attachments/assets/3355aa75-6c7a-4dd4-9115-bb66157b7224)
![image](https://github.com/user-attachments/assets/be6a8d75-939c-4b8f-897f-46bffd74d106)
![image](https://github.com/user-attachments/assets/b3cae13e-61ac-44a6-b1e6-e829e8e829e7)


데이터 : tsAirgap 양식 라이브러리(imputeTs), 빨간색 보간 데이터

### 평균, 중앙값 및 최빈값

전체 평균, 중앙값 또는 최빈값을 계산하는 것은 매우 기본적인 대치 방법이며 시계열 특성 또는 변수 간의 관계를 활용하지 않은 유일한 테스트 함수입니다. 단점은 평균 전가가 데이터 세트의 분산을 감소시킨다는 것입니다.

### 선형회귀

변수의 여러 예측 변수가 상관 행렬을 사용하여 식별됩니다. 최상의 예측 변수가 선택되어 회귀 방정식에는 독립 변수로 사용됩니다. 누락된 값이 있는 변수는 종속 변수로 사용됩니다. 장점은 누락된 값에 대한 좋은 추정치를 제공합니다. 단점은 1. 대체된 값이 다른 변수에서 예측되었기 때문에 서로 잘 맞는 경향이 있어 표준 오류가 줄어듭니다. 회귀 방정식에 사용된 변수가 없을 때 선형 관계가 있다고 가정해야 합니다.

### 다중 대치

1. **대치** **: 불완전한 데이터 세트의 누락된 항목을 m번 대치합니다귀속된 값은 분포에서 가져온 것입니다. 무작위 추첨 시뮬레이션에는 모델 매개변수의 불확실성이 포함되지 않습니다. 더 나은 접근 방식은 Markov Chain Monte Carlo(MCMC) 시뮬레이션을 사용하는 것입니다. 이 단계는 m개의 완전한 데이터 세트를 생성합니다.
2. **분석 :** *m개의* 완성된 데이터 세트 각각을 분석합니다 .
3. **Pooling :** *m* 분석 결과를 최종 결과로 통합

![image](https://github.com/user-attachments/assets/0c3804e3-9bb8-4c37-81af-96d258a46bc6)


이것은 다음과 같은 이유로 전가에 가장 선호되는 방법입니다.

- 사용하기 쉬움
- 편향 없음(전가 모델이 올바른 경우)

### 범주형 변수의 대치

1. 확실히 편향을 도입
2. 누락된 값을 그 자체로 별도의 범주로 취급
3. 예측 모델 : 로지스틱 회귀, ANOVA
4. 다중 대치

### KNN(K 최근접 이웃)

: 데이터 대체를 위한 XGBoost 및 Random Forest와 같은 다른 기계 학습 기술이 있지만 널리 사용되는 KNN에 대해 논의 

1. 연속 데이터 : 이 경우 일반적으로 유클리드, 맨하튼, 코사인 거리를 이용
2. 범주형 데이터 : 이 경우 해밍 거리를 이용, 모든 범주 속성을 사용하고 각각에 대해 두 지점 간에 값이 동일하지 않으면 1로 계산합니다.

장점 : 데이터가 매우 비정상적일 수 있는 특정 설정에서 이점이 있습니다.

단점 : 전체 데이터 세트를 통해 유사한 인스턴스르 검색하기 때문에 큰 데이터 세트를 분석할 때 시간이 많이 걸린다는 것입니다.

### 보간법 대치

```python
DataFrame.interpolate(method='linear', axis=0, limit=None, inplace=False, limit_direction='forward', limit_area=None, downcast=None)
```

### 주요 매개변수

- **method**: 보간 방법을 지정합니다. 기본값은 `'linear'`입니다. `'linear'` 외에도 `'polynomial'`, `'spline'`, `'quadratic'` 등 다양한 방법을 사용할 수 있습니다.
- **axis**: 보간을 적용할 축을 지정합니다.
    - `0` 또는 `'index'`: 각 열을 독립적으로 위에서 아래로 보간합니다.
    - `1` 또는 `'columns'`: 각 행을 독립적으로 왼쪽에서 오른쪽으로 보간합니다.
- **limit**: 최대 보간할 결측값의 개수를 지정합니다.
- **inplace**: `True`로 설정하면 원본 DataFrame을 수정하며, `None`을 반환합니다. `False`로 설정하면 수정된 새로운 DataFrame을 반환합니다.
- **limit_direction**: 보간을 적용할 방향을 지정합니다. `'forward'` (기본값), `'backward'`, `'both'` 중 선택할 수 있습니다.

### Pad 사용

```sql
DataFrame.pad(axis=None, inplace=False, limit=None, downcast=None)
```

### 매개변수

- **axis**: {0 or ‘index’, 1 or ‘columns’}, default None
    - 데이터를 채울 방향을 지정합니다.
    - `0` 또는 `'index'`: 각 열을 독립적으로 위에서 아래로 채웁니다.
    - `1` 또는 `'columns'`: 각 행을 독립적으로 왼쪽에서 오른쪽으로 채웁니다.
    - 기본값은 `None`이며, `DataFrame`의 메서드인 경우 `0`이 기본값입니다.
- **inplace**: bool, default False
    - `True`로 설정하면 원본 데이터프레임을 수정하며, `None`을 반환합니다.
    - `False`로 설정하면 수정된 새로운 DataFrame을 반환합니다.
- **limit**: int, default None
    - 채울 최대 결측값의 개수를 지정합니다. 기본값은 `None`으로, 제한 없이 채웁니다.
- **downcast**: dict, default None
    - 결과를 지정된 타입으로 다운캐스팅합니다. 예를 들어, `downcast='infer'`로 설정하면 가능한 경우 데이터 타입을 더 낮은 크기로 변환합니다.

### 반환값

- 결측값이 앞선 값으로 채워진 DataFrame 또는 Series를 반환합니다. `inplace=True`로 설정하면 `None`을 반환합니다.

# Scaling
- `StandardScaler`: 기본 스케일, 각 피처의 평균을 0, 표준편차를 1로 변환
- `RobustScaler`: 위와 유사하지만 평균 대신 중간값(median)과 일분위, 삼분위값(quartile)을 사용하여 이상치 영향을 최소화
- `MinMaxScaler`: 모든 피처의 최대치와 최소치가 각각 1, 0이 되도록 스케일 조정
- `Normalizer`: 피처(컬럼)이 아니라 row마다 정규화되며, 유클리드 거리가 1이 되도록 데이터를 조정하여 빠르게 학습할 수 있게 함

스케일 조정을 하는 이유는 데이터의 값이 너무 크거나 작을 때 학습이 제대로 되지 않을 수도 있기 때문입니다. 또한 스케일의 영향이 절대적인 분류기(예: knn과 같은 거리기반 알고리즘)의 경우, 스케일 조정을 필수적으로 검토해야 합니다.

반면 어떤 항목은 원본 데이터의 분포를 유지하는 것이 나을 수도 있습니다. 예를 들어, 데이터가 거의 한 곳에 집중되어 있는 feature를 표준화시켜 분포를 같게 만들었을 때, 작은 단위의 변화가 큰 차이를 나타내는 것처럼 학습될 수도 있습니다. 또한 스케일의 영향을 크게 받지 않는 분류기(예: 트리 기반 앙상블 알고리즘)를 사용할 경우에도 성능이 준수하게 나오거나 과대적합(overfitting)의 우려가 적다면 생략할 수도 있습니다.

스케일 조정시 유의해야할 점은 원본 데이터의 의미를 잃어버릴 수 있다는 것입니다. 최종적으로 답을 구하는 것이 목적이 아니라 모델의 해석이나 향후 다른 데이터셋으로의 응용이 더 중요할 때 원 피처에 대한 설명력을 잃어버린다면 모델 개선이 어려울 수도 있습니다. 이 점을 함께 고려하시면 좋겠습니다.
