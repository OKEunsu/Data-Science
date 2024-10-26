# Deep Learning
#### 인공지능 Artificaial Intelligence

- A technique which enables machines to mimic human behaviour

#### 머신러닝 Machine Learning

- Subset of AI technique which use statistical methods to enable machines to improve with experience

#### 딥러닝 Deep Learning

- Subset of ML which make the computation of multi-layer neural network feasible

##### MLP(Multi-Layer Perceptron = Fully Connected Layer = Dense Layer

활성화 함수 역활 : 최종 출력값을 다음 레이어로 보낼지 말지 결정하는 역할

## 비선형 함수
1. Sigmoid함수  
![image](https://github.com/user-attachments/assets/ffe2ea44-e04f-4fa0-a5e6-3b66c73ee4c4)  
- Logistic function
- 0과1 사이의 값을 가짐
- 중심이 0.5
- 주로 히든 레이어에 대한 활성화 함수보다는 2개의 카테고리를 예측하는 출력 레이어에서 사용
2. Tanh 함수  
![image](https://github.com/user-attachments/assets/e7889098-8cb0-4556-b241-298906d507a7)  
- -1과 1사이의 값을 가짐
- 중심이 0
3. ReLu  
![image](https://github.com/user-attachments/assets/890cdc57-fc47-4743-a022-f7140b0d95f2)
- 0보다 작은 값을 0으로 설정
- Sigmoid나 tanh보다 학습이 빠름
- 가장 많이 쓰임
4. Leaky ReLU  
![image](https://github.com/user-attachments/assets/b4bd3cbb-2b64-46ae-a7ca-0f32c6477d08)
- x가 음수일 때 미분값이 0이 되는 ReLU를 변형하여 약간의 미분값을 갖게 만듬
5. Softmax  
![image](https://github.com/user-attachments/assets/7b4b4248-238d-4122-8b30-e81f97ee7652)
- 주로 레이어 간의 activation보다는 마지막 layer에서 클래스를 분류하기 위해 쓰임
- 입력 값을 0~1 사이의 값으로 정규화하여 합이 1인 확률 분포로 만듦

## 손실함수
- 손실 함수 값이 작은 방향으로 모델을 학습 시키는 것이 목표
- 크게는 회귀를 위한 손실 함수와 분류를 위한 손실 함수로 나뉨

1. 평균 절대 오차  
![image](https://github.com/user-attachments/assets/a3ba4667-e822-45d2-812d-95df5ccca828)
- 모든 데이터에 대해 예측 값과 실제 정답 값의 차이에 절댓값을 취한 후 평균
- 이상치에 조금 덜 예민함
2. 평균 제곱 오차  
![image](https://github.com/user-attachments/assets/288aa3f2-7a0a-4293-a193-a49ba000d17f)
- 모든 데이터에 대해 예측값과 실제 정답 값의 차이에 제곱을 취한 후 평균
- 이상치에 예민함
- 오차가 커질수록 손실 함수가 빠르게 증가
3. 이진 교차 엔트로피  
![image](https://github.com/user-attachments/assets/3cefde90-1338-462f-917f-4af2f23fdd57)
- 이진 분류에 사용
- 예측값은 0과 1 사이의 확률값
- 예측값이 1에 가까우면 True일 확류이 크고 0에 가까우면 False일 확률이 큼
4. 범주 교차 엔트로피  
![image](https://github.com/user-attachments/assets/78239a11-fea3-4b4b-99b1-a31827cbc6a6)
- Class의 수가 3이상인 분류에 사용
- 예측값은 0과 1 사이의 확률 값
- 레이블 y는 원-핫 인코딩 형태

## 최적화 1
최적화 : 손실 함수를 최소화 하는 Weight(W)를 찾는 과정

- 현재 위치에서 손실 함수의 출력값이 감소하는 방향으로 조금씩 Weights(W)를 움직여 나가는 것
- 산을 내려가는 원리와 같음
  - 한 걸음 내딛은 후 그 위치에서 어느 방향이 내리막 길인지 찾아 그 방향으로 한 걸음을 내딛음
  - 위의 과정을 더 이상 내려갈 수 없는 곳에 도달할 때까지 반복
- 어떤 방향이 내리막 길인가?
- 한 걸음이란 얼마정도를 의미하는가?

 Gradient Descent : 손실 함수를 최소화 하는 Weights(W)를 찾기 위해 기울기(gradient)를 이용하는 방법
 - 어떤 방향이 내리막 길인가?
 - 한 걸음이란 얼마 정도를 의미하는 가?
 - 기울기가 양수면 w를 감소시키고, 음수면 w를 증가시키는 방식으로 손실 함수가 최소가 되는 지점을 찾음
- 임의의 함수의 임의의 점에서의 gradient를 계산하면 w로부터 움직였을 때, L값의 변화량을 표현하는 벡터가 나옴
- 이 벡터는 가장 가파르게 L값이 증가하는 방향을 가리킴
- 따라서 반대방향으로 W를 업데이트 해주면 최솟값을 찾는 방법이 됨
   
## 역전파
Input에 대한 Output을 가장 잘 예측하는 Weights를 찾기 위해 W를 조정하는 방법

#### simoid 미분
- sigmoid는 0과 1 사이의 값을 가지며, 반복되서 곱해지면 거의 0에 가까운 값이 됨
- 이러한 현상을 Gradient Vanishing이라 함 이를 피하기 위해 ReLU, Normalization등 방법이 존재

## 최적화 2

Gradient Descent 문제점
- 모든 파라미터에 대해 동일한 learning rate를 적용함
- Local minimum, Saddle point에서 빠져나오기 어렵
- 무조건 기울어진 방향으로 이동하므로 탐색 경로가 비효율적

![image](https://github.com/user-attachments/assets/137236c9-fa3c-4c7f-9d4b-ba6f1d2aec28)
![image](https://github.com/user-attachments/assets/0e26e452-073c-4a73-9545-691317a2ecb7)

- Gradient Descent를 통해 이동하는 과정에 관성을 더함
- 파라미터를 업데이트 할 때 현재 뿐만 아니라 이전 gradient도 계산에 포함하여 업데이트
- 과거에 이동했던 방식을 기억하면서 그 방향으로 일정 정도를 추가적으로 이동
- Gradient들의 지수평균을 업데이트 하는 데 이용

#### Adagrad(Adaptive Gradient)
- 각 변수마다 step size를 다르게 설정해서 이동하는 방식
- Gradient가 커서 많이 변화했던 변수들은 step size를 작게
- 많이 변화한 변수들은 그만큼 학습이 더 많이 되었을 것으로 가정
- 단점 : 학습을 계속 진행하면 step size가 너무 줄어듦 - 학습을 오래 할 경우 거의 움직이지 않게 됨

#### RMSProp
- AdaGrad의 학습이 오래 진행할 경우 step size가 너무 줄어들어 학습이 더 이상 되지 않는 문제를 해결하기 위함
- Gradient의 제곱값을 더해가며 구한 g 부분을 합이 아닌 지수 평균으로 대체
- 변수간 상대적 크기 차이 유지 가능

#### Adam(Adaptive Moment Estimation)
- RMSProp + Momentum
- 가장 많이 사용되는 최적화 방법
- 지금까지 계산해 온 gradient의 지수평균 저장
- Gradient의 제곱갑스이 지수평균을 저장

## Overfitting
Regularzation이 필요한 이유 : 과적합 문제를 해결하기 위함

### 과적합
- 학습 데이터에는 성능이 높지만 검증/테스트 데이터에는 성능이 잘 나오지 않는 경우
- 모델이 복잡하고 데이터가 적을수록 과적합이 일어나기 쉬움
- 학습 데이터가 검증/테스트 데이터를 충분히 대표하지 못할 경우 많이 일어남
- Training loss는 감소하지만 Validation loss는 증가하는 구간
- 모델을 데이터에 과하게 맞추려 하는 경우 - 학습 보다 암기에 가까움

Mini-batch : 전체 데이터를 동일한 크기를 가진 그룹으로 나눈 것
Iteration : 한 배치 단위의 데이터를 학습하는 단위
Epoch : 모든 데이터를 한 번 학습하는 단위

## Regularization 기법
### Early Stopping
- 이전 epoch과 비교하여 validation loss가 감소하지 않으면 학습을 중단
- 바로 전 epoch의 validation loss 뿐 아니라 일정한 epoch 수를 거듭하며 validation loss가 감소하지 않으면 학습 중단
  
### Dropout
- 모델이 복잡할 수록, 뉴럴 네트워크가 커질수록 overfitting에 빠질 가능성이 높음
- 네트워크에 있는 모든 weight에 대해 학습을 하는 것이 아니라 layer에 포함된 weight중 일부만 학습
- 학습시 뉴런을 임의의 비율만큼 삭제하며 삭제된 뉴런의 값은 순전파, 역전파를 하지 않음
- 하나의 feature에 의존하지 않게 하기 위함

## Batch Normalization

