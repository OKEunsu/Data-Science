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


