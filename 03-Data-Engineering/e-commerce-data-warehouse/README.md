## 1. 프로젝트 개요
- **목표**: 이커머스 데이터를 활용하여 데이터 웨어하우스 설계 및 구축, 복잡한 SQL 쿼리 최적화, 데이터 마트 구성을 목표로 합니다.
- **사용 데이터셋**: Brazilian E-commerce 실제 이커머스 데이터 (Kaggle 제공)

- **핵심 내용**:
    - 데이터 웨어하우스 설계 및 구축
    - 복잡한 SQL 쿼리 최적화 (인덱스, 조인, 서브쿼리 등)
    - Window Function, CTE 활용
    - 데이터 마트 구성

## 2. 데이터 [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data)
<img width="2486" height="1496" alt="image" src="https://github.com/user-attachments/assets/67126f74-d9bb-415e-afb6-958e4457691a" />

<br/>

## Data Schema
`olist_order_payments_dataset`  
`olist_products_dataset`  
`olist_order_reviews_dataset`    
`olist_orders_dataset`  
`olist_order_items_dataset`  
`olist_sellers_dataset`   
`olist_customers_dataset`   
`olist_geolocation_dataset`  

<br/>

### 배경
이 데이터셋은 브라질 마켓플레이스에서 가장 큰 백화점인 Olist가 아낌없이 제공했습니다.  
Olist는 브라질 전역의 소규모 사업체를 번거로움 없이 단일 계약으로 채널에 연결합니다.  
이 판매자들은 Olist 스토어를 통해 제품을 판매하고 Olist 물류 파트너를 이용하여 고객에게 직접 배송할 수 있습니다. 

고객이 Olist 스토어에서 제품을 구매하면 판매자에게 해당 주문을 처리하라는 알림이 전송됩니다.  
고객이 제품을 받거나 예상 배송일이 되면, 고객은 이메일로 만족도 설문조사를 받아 구매 경험에 대한 평가를 제공하고 의견을 작성할 수 있습니다.  

<br/>

### 주의사항
하나의 주문에 여러 개의 상품이 있을 수 있습니다.

각 상품은 다른 판매자가 처리할 수 있습니다.

상점과 파트너를 식별하는 모든 텍스트는 '왕좌의 게임'에 나오는 위대한 가문의 이름으로 대체되었습니다.

마켓플레이스에 등록된 제품의 예시가 제공됩니다.

<br/>

---
# 📊 이커머스 DW 설계 실습 정리 (PPT 3장 분량)

---

## 슬라이드 1: 데이터 탐색 및 준비

### 1.1 테이블 구조 및 관계 이해
- 주요 테이블:
  - `orders`, `order_items`, `customers`, `products`, `sellers`, `order_payments`, `order_reviews`, `geolocation`
- 핵심 컬럼 예시:
  - `orders`: order_id, customer_id, order_status, purchase_timestamp
  - `order_items`: order_id, product_id, seller_id, price
  - `customers`: customer_id, customer_city, customer_state

### 1.2 테이블 간 관계 정의
- 고객 → 주문 (`customer_id`)
- 주문 → 주문상품 (`order_id`)
- 주문상품 → 제품, 판매자 (`product_id`, `seller_id`)
- 주문 → 결제/리뷰/배송 (`order_id`)
- 고객 ↔ 지역 정보 (`geolocation`)

### 1.3 데이터 품질 점검
- 결측치 예시: review_comment_title, review_comment_message
- 이상치 예시: 배송 소요일 음수, price=0
- 데이터 타입 점검 및 변환 여부 확인

### 1.4 키 및 정규화 구조 확인
- 기본키 예시: `orders.order_id`
- 복합키 예시: `order_items.order_id + order_item_id`
- 외래키 후보: customer_id, product_id, seller_id
- 정규화 점검: 1NF(원자성), 2NF(부분 종속성), 3NF(전이 종속성)

---

## 슬라이드 2: 요구사항 분석 및 분석 단위 설계

### 🛍2.1 비즈니스 흐름 요약
- 주문 생성 → 결제 → 배송 → 수령 → 리뷰
- 각 단계에 연결되는 테이블 및 필드 정리

### 2.2 OLTP vs OLAP 구분

| 항목 | OLTP | OLAP |
|------|------|------|
| 목적 | 실시간 트랜잭션 처리 | 전략적 데이터 분석 |
| 예시 | 주문 등록, 결제 기록 | 월별 매출, 고객 LTV |
| 쿼리 | INSERT, UPDATE | SELECT, JOIN, GROUP BY |

### 2.3 분석 단위(Grain) 정의
- 주문 단위 (`order_id`)
- 주문상품 단위 (`order_item_id`)
- 고객 단위 (`customer_id`)
- 날짜 단위 (`order_purchase_date`)
- 제품 단위 (`product_id`)

### 2.4 KPI 정의
- 총 매출, 주문 수, 고객 수
- 월별 매출 추이
- 배송 지연률 = 실제 배송일 > 예상 배송일
- 고객별 LTV = 누적 결제 금액

---

## 슬라이드 3: DW 물리 모델 및 마트 설계

### 3.1 스타 스키마 구성

- 팩트 테이블:
  - `fact_order_items`: 주문상품 기준 매출/수량/할인 등
  - `fact_payments`: 결제 방식별 금액
  - `fact_reviews`: 평점, 리뷰 작성일 등
- 차원 테이블:
  - `dim_customer`, `dim_seller`
  - `dim_product`, `dim_category`
  - `dim_geolocation`, `dim_time`

### 3.2 인덱싱 전략
- 조인용: `order_id`, `product_id`, `customer_id`
- 필터링용: `order_status`, `review_score`, `payment_type`

### 3.3 데이터 흐름 요약 (ETL)
```
┌────────────┐
│  Raw CSV   │  ← olist_customers.csv, olist_orders.csv ...
└────┬───────┘
     │
     ▼
┌────────────┐
│  Extract   │  ← Pandas로 CSV 읽기
└────┬───────┘
     │
     ▼
┌────────────┐
│ Transform  │  ← 결측치 제거, 데이터 타입 변환, 조인
│            │     - 주문 + 고객 + 결제 + 상품 + 리뷰
└────┬───────┘
     │
     ▼
┌────────────┐
│   Load     │  ← SQLite / PostgreSQL / BigQuery 적재
│            │     - fact_order_items, dim_customer ...
└────┬───────┘
     │
     ▼
┌────────────────────────┐
│ Fact & Dimension Table │  ← Star Schema 기반 DW 설계
└────┬───────────────────┘
     │
     ▼
┌─────────────────────┐
│   분석 및 시각화     │  ← SQL / Pandas / Tableau 등
│                     │     - KPI 리포트, 대시보드
└─────────────────────┘

```

