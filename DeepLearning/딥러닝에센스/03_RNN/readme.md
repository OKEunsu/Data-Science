# Time Series(시계열)
일정 시간 간격으로 배치된 데이터들의 수열
- 과거의 데이터가 현재, 미래까지 영향을 미침
- 머신러닝에서 배운 회귀분석은 시점은 고려하지 않으나 Time Series(시계열)분석은 시간을 고려함
- 시계열 분석의 목적 : 시계열 데이터를 보고 앞으로 일어날 미래의 일을 예측

## Sequence Model
모델의 입력이나 출력이 Sequence data인 상황을 다루는 모델

Sequential data란?
- 텍스트 스트림, 오디오 클립, 비디오 클립, 시계열 데이터
- 음성 인식 : 음성 스펙트럼 -> 나는 밥을 먹었다
- 감정 분석 : 그 영화는 5번 더 보고 싶을 정도로 기억에 남는다 -> 별 5점
- 비디오 행동 인식 : 넘어지는 frame들로 이루어진 영상 -> 쓰러졌다

## Sequence Model : 다양한 구조  
![image](https://github.com/user-attachments/assets/295a6bb3-e293-4ffb-9f36-bacd9774c773)  

1. Non sequential : ex) 이미지 분류
   - 입력 : 이미지
   - 출력 : label
2. Many to One : ex) 감정분류, 영화 평점 예측
   - 입력 : 단어 sequence
   - 출력 : 별점, 평점
   - 이 영화는 5번은 더 보고 싶을 정도이다 -> 5점
3. One to Many : ex) 이미지 캡셔닝
   - 입력 : 이미지
   - 출력 : 이미지에 대한 설명
4. Many to Many : ex) DNA 순서 분석
   - 입력 : DNA sequence
   - 출력 : 염기 서열
5. Many to Many : ex) 번역
   - 입력 : 한국어 단어 sequence
   - 출력 : 영어 단어 sequence
   - 나는 이 집에 살고 싶어 -> I hope to live this house

# RNN(Recurrnet Neural Network) : 대표적인 Sequence Model
사용 : 시간에 의존적인 Time Series 분석을 하거나 순차적인(Sequential) 데이터 학습에 활용

## Nerual Network vs RNN
일반적인 Neural Network
- 이전의 입력값에 영향을 받지 않음  
RNN
- h(t-1) 이라는 정보가 추가되어 이전의 입력값에 영향을 받게됨  

## RNN 예시
Input x :[h,e,l,o] 일 경우 다음 나올 character 예측하여 hello 만들기
- 'h', 'e', 'l', 'o' -> [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1] : one hot encoding

## RNN : BPTT
BackPropagation Through Time : 시간 방향으로 펼친 Neural Network의 역전파 수행  
![image](https://github.com/user-attachments/assets/61c51e72-37f9-4e37-8844-985848aac733)  


## RNN : 단점
1. 신경망이 깊어질 수록 Gradient Vanishing(or Exploding0 문제가 일어날 수 있음
   - RNN은 가까이 있는 정보(입력)에 영향을 더 많이 받음
   - 몇몇 사례에서 초반부 데이터에 영향을 받는 경우가 많다
   - Gradient Vanishing/Exploding이 일어나면 기울기가 중간에 소멸하여 정보가 남아있지 않게 되며 학습이 안됨
2. 장기적인 의존성을 확인하는 데 효과적이지 않음

# LSTM(Long short Term Memory Network)
장기적인 의존성을 요구하는 학습을 할 수 있음  
RNN에 비해 부가적인 연산들이 추가됨  
![image](https://github.com/user-attachments/assets/49683272-f278-4ce2-afc8-a184351ba569)  
![image](https://github.com/user-attachments/assets/7a624ad9-f9b4-499d-b4e3-a7e598dfe210)  
### Cell State
- LSTM의 핵심 아이디어
- 이전의 정보가 잘 흐를 수 있는 구조
- Cell State에 어떠한 값을 곱하거나 더해줌으로써 정보를 적절히 다음 state로 전달
- 곱하거나 더해지는 정도는 여러 gate에 의해 조정됨
### Forget Gate
- 과거의 정보를 얼마나 잊을것인가
- 이전 hidden state와 현재 input를 받아 sigmoid를 취함
- 0에 가까울 수록 이전의 많은 정보를 잊고 1에 가까울 수록 유지
### Input Gate
- 현재 정보를 얼마나 기억할 것인가
- 이전 hidden state와 현재 input를 받아 sigmoid를 취함으로써 i_t를 구함
- tanh를 통해 새로운 벡터 ct를 만듦
- i_t와 c_t를 곱한 값을 cell state를 업데이트하기 위해 사용
### Cell State Update
- 이전 Cell State에 적절한 값을 고합고 더함으로써 새로운 Cell State를 업데이트
### Output Gate
- 다음 State로 보낼 output를 구함
- 이전 hidden sate와 현재 input를 받아 sigmoid를 취함으로써 o_t를 구함
- Cell state에 tanh를 취한 것과 ot를 곱함으로써 output으로 보냄
  

