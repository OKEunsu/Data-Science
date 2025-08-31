# 📣 광고 캠페인 퍼널 성과 비교 A/B 테스트

이 프로젝트는 두 가지 광고 캠페인 전략(컨트롤 그룹 vs 테스트 그룹)이 사용자의 행동 및 구매 전환에 어떤 영향을 미치는지를 분석하기 위한 A/B 테스트입니다.  
실험은 실제 디지털 광고 집행 데이터를 기반으로 캠페인 성과를 퍼널 관점에서 비교하는 방식으로 진행됩니다.

---

## 📌 프로젝트 목적

> “어떤 캠페인이 더 높은 전환율, 낮은 비용, 효과적인 퍼널 구조를 갖고 있는가?”

---

## 📊 데이터 설명

| 컬럼명           | 설명                         |
| ---------------- | ---------------------------- |
| `campaign_name`  | 캠페인 이름 (Control / Test) |
| `date`           | 일자                         |
| `spent`          | 광고 지출 비용 ($)           |
| `impressions`    | 광고 노출 수                 |
| `reach`          | 고유 노출 수                 |
| `website_clicks` | 웹사이트 클릭 수             |
| `searches`       | 웹사이트 내 검색 수          |
| `view_content`   | 콘텐츠 조회 수               |
| `add_to_cart`    | 장바구니 추가 수             |
| `purchases`      | 구매 건수                    |

---

## 🧪 향후 분석 계획

- 캠페인별 주요 지표 계산:
  - CTR (클릭률)
  - Conversion Rate (전환율)
  - CPA (구매당 비용)
  - ROI 추정
- 퍼널 단계별 전환율 분석
- 시각화를 통한 병목 구간 파악 및 캠페인 비교
- 통계적 검정을 통한 유의미성 확인

---

## 📂 현재 파일 구성

```bash
abtest_02_campaign_funnel/
├── control_group.csv
├── test_group.csv
├── README.md
├── analysis.ipynb 
└── claude_anlysis.ipynb
```

## 📌 데이터 출처

- 📦 Kaggle: https://www.kaggle.com/datasets/amirmotefaker/ab-testing-dataset

