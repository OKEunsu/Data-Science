# 🧪 A/B Testing Casebook: 실전 실험 설계와 데이터 분석

이 프로젝트는 **3가지 실제 시나리오 기반 A/B 테스트 분석**을 통해, 제품 개선, 마케팅 성과 평가, UX 디자인 효과 검증 등 다양한 비즈니스 상황에서의 데이터 기반 의사결정을 연습하고자 합니다.

---

## 📌 프로젝트 개요

| 실험 번호 | 주제 | 분석 대상 | 주요 기술 |
|----------|------|-----------|------------|
| ① | 웹페이지 전환율 테스트 | 기존 vs 신규 페이지 전환율 비교 | `Pandas`, `Z-test`, `Seaborn` |
| ② | 광고 캠페인 퍼널 분석 | Control vs Test 캠페인 성과 비교 | `CTR/CPA`, `Funnel 분석`, `Matplotlib` |
| ③ | UI 변경 사용자 행동 분석 | 배경색 변화가 페이지 뷰/전환에 미치는 영향 | `T-test`, `EDA`, `시각화` |

---

## 🧭 분석 목적

> 실험 설계부터 통계 검정, 세그먼트 분석까지 전 과정 실습을 통해 **데이터 기반의 실질적 인사이트 도출 역량**을 강화합니다.

- A/B Test의 기본 원리와 설계 이해
- 통계적 유의성 검정 (z-test, t-test, chi-square)
- 퍼널 분석과 광고 캠페인 지표 해석
- 사용자 행동 데이터 기반의 UX 개선 제안
- 기기/지역 등 세그먼트별 차이 분석

---

## 📂 폴더 구성

```bash
abtest/
│
├── abtest_01_conversion_page/      # 웹페이지 전환율 비교 실험
│   ├── ab_data.csv
│   ├── countries.csv
│   └── analysis.ipynb
│
├── abtest_02_campaign_funnel/      # 광고 캠페인 퍼널 분석 실험
│   ├── control_group.csv
│   ├── test_group.csv
│   └── analysis.ipynb
│
├── abtest_03_ui_behavior/          # UI 변경에 따른 사용자 행동 변화
│   ├── ab_testing.csv
│   └── analysis.ipynb
│
└── README.md
