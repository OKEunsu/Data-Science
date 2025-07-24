# 🧠 딥러닝 & 컴퓨터 비전 실습 모음

이 저장소는 TensorFlow, OpenCV, Darknet-YOLO를 활용하여 딥러닝 및 컴퓨터 비전 핵심 개념을 실습한 Jupyter Notebook들을 모아놓은 프로젝트입니다. 기초적인 인공신경망부터 시작해 CNN, 자연어 처리, 하이퍼파라미터 튜닝, 객체 탐지, 차량 추적까지 다양한 내용을 포함하고 있습니다.

---

## 📚 실습 목록

### 📌 딥러닝 기초 및 전이 학습
| No. | 파일명 | 설명 |
|-----|--------|------|
| 01 | `01_Basic_DeepLearning.ipynb` | 기본적인 신경망 구조 (Sequential API) |
| 02 | `02_Convolutional_Neural_Network.ipynb` | CNN을 활용한 MNIST 이미지 분류 |
| 03 | `03_TextClassification.ipynb` | IMDB 텍스트 감성 분류 (Embedding 포함) |
| 04 | `04_TextClassificationTFHub.ipynb` | TensorFlow Hub 기반 텍스트 분류 (전이학습) |
| 05 | `05_Flower_Classfication.ipynb` | 꽃 이미지 분류 (데이터셋 + 전이학습) |
| 06 | `06_Karas_tuner.ipynb` | Keras Tuner를 활용한 하이퍼파라미터 최적화 |

### 🎨 OpenCV 기반 영상 처리
| No. | 파일명 | 설명 |
|-----|--------|------|
| 08 | `08_OpenCVBasic.ipynb` | OpenCV 기초 (이미지 읽기, 채널 처리 등) |
| 09 | `09_OpenCVDraw.ipynb` | 도형 그리기 및 영상 출력 |
| 10 | `10_OpenCVDNN.ipynb` | OpenCV DNN 모듈을 활용한 사전학습 모델 사용 |
| 11 | `11_Harr-cascade.ipynb` | Haar-Cascade를 이용한 얼굴 탐지 |
| 12 | `12_Dog_Cat_Classfication.ipynb` | 개 vs 고양이 이미지 분류 |
| 13 | `13_YOLO.ipynb` | YOLO 객체 탐지 기초 실습 |
| 14 | `14_CustomYOLOPreparation.ipynb` | 커스텀 YOLO 데이터셋 준비 |
| 15 | `15_YOLO_darknet.ipynb` | Darknet 기반 YOLO 실행 |
| 16 | `16_Detect_Car_Plate.ipynb` | 차량 번호판 탐지 |
| 17 | `17_Detect Line.ipynb` | 차선 인식 (Hough Line) |
| 18 | `18_Darknet_Viedeo.ipynb` | 동영상 기반 YOLO 탐지 |
| 19 | `19_carTracker.ipynb` | 차량 객체 추적 |
| 20 | `20_CarTrackerAdaptiveCruiseControl.ipynb` | 어댑티브 크루즈 컨트롤 시뮬레이션 |
| 21 | `21_Traffic_Yolo_Darknet.ipynb` | Darknet 기반 교통 객체 탐지 |
| 22 | `22_trafficCustomYoloDetection.ipynb` | 커스텀 YOLO 모델로 교통 객체 탐지 |
| 23 | `Darknet YOLOv4 - Google Colab (Firearm Detection).ipynb` | Google Colab 기반 총기 탐지 실습 |
| 24 | `faceTracker.ipynb` | 얼굴 추적 알고리즘 구현 |
| 25 | `YOLO.ipynb` | YOLO 객체 탐지 재정리 버전 |

---

## 🛠️ 사용 기술 및 도구

- **Python 3.10+**
- **TensorFlow / Keras**
- **OpenCV (cv2)**
- **Darknet (YOLOv4)**
- **Keras Tuner**
- **TensorFlow Hub**
- **Jupyter Notebook**

---
