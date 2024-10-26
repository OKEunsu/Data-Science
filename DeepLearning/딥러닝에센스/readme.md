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

## 최적화
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

## 최적화

Gradient Descent 문제점
- 모든 파라미터에 대해 동일한 learning rate를 적용함
- Local minimum, Saddle point에서 빠져나오기 어렵
- 무조건 기울어진 방향으로 이동하므로 탐색 경로가 비효율적

![image](https://github.com/user-attachments/assets/137236c9-fa3c-4c7f-9d4b-ba6f1d2aec28)
  







