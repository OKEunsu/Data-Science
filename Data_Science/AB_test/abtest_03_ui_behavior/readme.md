# 🖥️ UI 변경에 따른 사용자 행동 변화 A/B 테스트 (준비 중)

이 프로젝트는 웹사이트의 **배경색(UI 요소)** 변경이 사용자 행동에 어떤 영향을 미치는지 분석하기 위한 A/B 테스트 실험입니다.  
현재는 데이터 이해 및 분석 구조 설계 단계이며, 추후 분석을 통해 실질적인 UX 개선 인사이트를 도출할 예정입니다.

---

## 📌 프로젝트 목적

> “웹사이트 배경색 변경이 사용자 참여(조회수, 체류 시간, 전환)에 실질적인 영향을 주는가?”

---

## 📊 데이터 설명

본 데이터는 **합성된 A/B 테스트 데이터셋**으로, Numpy 기반의 무작위 샘플링 기법을 통해 생성되었으며, 영국 전역의 가상 소매 웹사이트를 시뮬레이션한 것입니다.

| 컬럼명 | 설명 |
|--------|------|
| `user_id` | 사용자 ID |
| `group` | A: 흰색 배경 (기존), B: 검정 배경 (테스트) |
| `page_views` | 세션 중 사용자 페이지 조회 수 |
| `time_spent` | 사이트 체류 시간 (초) |
| `converted` | 전환 여부 (Yes / No) |
| `device` | 접속 장치 (Mobile / Desktop 등) |
| `location` | 사용자 지역 (영국 내 지역 단위) |

---

## 🧪 향후 분석 계획

- 그룹 A vs B 간 행동 지표 평균 비교
- 통계 검정 (t-test, proportion z-test 등) 적용
- 기기(device) 및 지역(location) 기반 세그먼트 분석
- 시각화를 통해 결과 해석 (boxplot, histplot 등)
- UX/UI 개선 방향 제안 도출

---

## 📂 현재 파일 구성

```bash
abtest_03_ui_behavior/
├── ab_testing.csv
├── README.md
└── analysis.ipynb  ← 향후 분석 노트북 작성 예정
```

## 📌 데이터 출처

- 📦 Kaggle: https://www.kaggle.com/datasets/adarsh0806/ab-testing-practice

