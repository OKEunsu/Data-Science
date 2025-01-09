# RandomForest

![image](https://github.com/user-attachments/assets/c3e3c852-5dbe-4618-8efe-326e80f041ca)


## 앙상블의 정의

약한 분류기들을 결합하여 강한 분류기를 만드는 것

1. bagging
2. boosting
3. stacking

## Bagging

- Bootstrap + Aggregation
- 약한 분류기들을 결합하여 강 분류기로 만드는 것

## Bootstrap

- Train Data에서 여러 번 복원 추출하는 Random Sampling 기법
- 추출된 샘플들을 부트스트랩 샘플이라고 부른다

![image](https://github.com/user-attachments/assets/59745b5f-c2c3-415f-8eef-40efec1ee95d)


### OOB(Out-Of-Bag) 평가

추출되지 않은 샘플을 이용해 Cross Validation(교차 검증)에서 Valid 데이터로 사용할 수 있다.

### 약분류기 생성

추출된 부트스트랩 샘플마다 약분류기를 학습시킨다

![image](https://github.com/user-attachments/assets/e7202f1a-d812-425e-9362-17dddecdecf1)


### Aggregation

생성된 약 분류기들의 예측 결과를 Voting을 통해 결합한다.

1. Hard Voting

예측한 결과값 중 다수의 분류기가 결정한 값을 최종 예측값으로 결정

![image](https://github.com/user-attachments/assets/cf7e4d39-9c82-4da2-aacc-fb5a428bf250)


1. Soft Voting

분류기가 예측한 확률 값의 평균으로 결정

![image](https://github.com/user-attachments/assets/35a291aa-3886-408e-9d64-59fc7b3c4786)


## Bagging의 장점

- 분산을 줄이는 효과가 있음
    - 원래 추정 모델이 불안정하면 분산 감소 효과를 얻을 수 있다
    - 과대 적합이 심한(High Variance)모델에 적합

## Random Forest의 정의

- Decision Tree + Bagging
- 분산이 큰 Decision Tree + 분산을 줄일 수 있는 Bagging

## Random Forest와 무작위성(Randomness)

- 무작위성을 더 강조하여서 의사결정나무들이 서로 조금씩 다른 특성을 갖음
- 변수가 20개가 있다면 5개의 변수만 선택해서 의사결정나무를 생성
- 의사결정나무의 예측들이 비상관화되어 일반화 성능을 향상시킨다.

## Random Forest 학습방법

1. Bootstrap 방법으로 T개의 부트스트랩 샘플을 생성한다.
2. T개의 의사결정나무들을 만든다.
3. 의사결정나무 분류기들을 하나의 분류기로 결합한다.

## 장점

- 의사결정나무의 단점인 Overfitting을 해결한다
- 노이즈 데이터에 영향을 크게 받지 않는다.
- 의사결정나무 모델보다 복잡도가 적다

## 단점

- 모델의 예측 결과를 해석하고 이해하기 어렵다.

# Catboost

- CatBoost 는 범주가 많은 범주형 Feature 를 포함하는 데이터셋에 매우 효율적이다.
- CatBoost 는 범주형 데이터를 숫자형으로 변환하게 되고, 기본 설정으로 Mean Encoding 을 사용하는데 단순하게 평균을 사용하게 되면 Data Leakage 문제(우리가 예측해야 하는 값이 훈련 데이터의 Feature 에 들어가는 문제) 가 나타나게 되는데 이전 데이터들의 평균을 활용하는 방법을 사용하여 이를 해결해 준다
- Pool 을 사용하여 학습 데이터를 CatBoost 에 맞게 변환해 준다
- CatBoost 는 Ordered Boosting 과 Random Permutation 등의 Overfitting 을 방지하기 위한 내장 알고리즘이 있어서, 비교적 다른 Gradient Boosting 방법들에 비해 Hyper Parameter Tuning 에 자유로운 알고리즘
