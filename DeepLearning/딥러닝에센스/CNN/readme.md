# 이미지 분류
이미지를 넣었을 때 그 이미지의 CLASS를 분류해내는 작업

## Rule Based
- 개의 눈, 코, 입, 귀 등과 같은 특징들의 존재여부 등으로 규칙을 세우고 그 규칙에 부합하는가의 여부로 개를 분류함
- 단점
  - 불안정
  - 분류를 위한 규칙을 정하기 어려움
  - 각 class를 분류하는 모델을 따로 만들어야 함 - 각 class마다 rule을 따로 정해야 함
    
## Data Driven
- 데이터를 기반으로 모델을 만들어 문제 해결

- 사람은 쉽게 분류할 수 있는 작업이 컴퓨터에게는 어려울 수 있음
- 사람은 이미지 전체를 한 눈에 보고 전반적인 경험에 비추어 물체를 분류해 냄
- 컴퓨터는 이미지를 구성하고 있는 pixel값들을 받아 분류하며 관측한 위치, 빛, 자세, 가려짐, 생김새의 차이등에 따라 다르게 볼 수 있음

- 단순 pixel값 만으로 물체를 분류하는 것은 바람직하지 않을 수 있음
- 물체를 분류하는 데 필요한 특징들 이외에 배경 등에 영향을 많이 받게 됨
- 사람이 물체를 인식하는 데 필요한 여러 특성들을 많은 데이터를 통해 축적하며 이를 바탕으로 물체를 분류함 - 딥러닝

# 데이터 증강기법
## 데이터 증강
- 원본 데이터에 변화를 가하여 학습에 활용할 수 있는 새로운 데이터를 만드는 기법
- Overfitting을 막기 위한 방법으로 Regularization/Normalization 등 이외에 데이터 수를 늘리는 방법이 있음
- Data Augmentation도 데이터 수를 늘림으로써 Overfitting을 막기 위한 방법 중 하나

## 기법
![image](https://github.com/user-attachments/assets/06589cb6-35ff-4c1d-91d9-d8d74afd771a)  
너무 과한 Data Augmentation 기법을 적용할 경우 오히려 학습에 혼동을 줄 수 있음

# CNN 기본 개념
## Spatial/Locality
- 단순히 눈 2개, 코 1개, 입 1개가 있다는 사실을 인지하는 것 뿐 아니라 두 눈이 코 위에 있으며 입이 코 아래에 있다는 공간 정보를 네트워크가 인지하길 바람
- 이미지를 구상하는 특징들은 이미지 전체가 아닌 일부 지역에 근접한 픽셀들로만 구성되며 근접한 픽셀들끼리만 의존성을 가짐
- 위와 같은 insightt를 통해 나온 방법이 CNN(Convolutional Neural Network)
- CNN 구조
  - CONV layer - ReLU - CONV layer - ReLU - Pooling layer - CONY layer - FC Layer
 
- Filter와 Input Feature map간의 convolution 연산이 이루어 짐
- Filter가 이미지를 슬라이드 하며 filter 단위로 내적을 함  

![image](https://github.com/user-attachments/assets/9b03d92f-14e3-49f6-92de-a7830559a505)
- Filter가 이미지를 슬라이드 하며 filter 단위로 내적함
- 차원은 input feature map과 filter가 동일해야 함
- Filter의 수는 Output feature map의 차원이 됨
- Convolution Layer에서 Filter는 해당 이미지의 특징들의 위치를 찾기 위해 사용
- 여러 Feature를 풍부하게 뽑기 위해 여러 개의 filter를 사용  

## Convolution Layer : stride
![image](https://github.com/user-attachments/assets/ba0b0b0e-6152-45cd-b019-a484f57d77f1)
- 모든 sparial locations에 대해 convolution 연산 진행
- 한칸 씩 움직인다 했을 경우
  - 파란색 filter가 5x5 output feature map을 만듦
  - 이 때 1칸 씩을 stride라고 함
- 7x7 input feature map에 3x3 filter를 적용
- stride = 2 일 경우
  - 파란색 filter가 3x3 output feature map을 만듦
