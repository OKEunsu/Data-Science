# 🏗️ Brazilian E-commerce 데이터 마트 구축

본 리포지토리는 Brazilian E-commerce 공개 데이터를 기반으로 설계한 데이터웨어하우스(DW)로부터,  
분석 목적에 최적화된 데이터 마트(Data Mart)를 구축한 과정을 담고 있습니다.

---

## 📌 목적

- **DW → DM 전환 실습**을 통해 주제 중심 분석 환경 구성
- **판매(Sales), 고객(Customer), 제품(Product)** 관점의 데이터 마트 설계 및 구현
- 실무에서 사용하는 **Star Schema 구조 기반의 데이터 마트 설계 및 SQL 변환 실습**

---

## 1단계: 요구사항 분석 및 계획 수립

- **사용 부서**: 경영진, 리테일팀, 마케팅팀, 물류팀
- **분석 목적**:
  - 월별/카테고리별 매출 추이
  - 셀러(또는 고객) 성과 분석
  - 주문당 평균 매출
  - 배송비 포함 총수익 분석
- **주요 KPI**:
  - 총 매출(GMV), 주문 수, AOV(평균 주문 금액)
  - 판매자별 매출
  - 지역별 주문 건수 및 매출
  - 리뷰 점수 평균

---

## 2단계: 데이터 마트 설계

### ✅ 판매 마트 (Sales Mart)

- **분석 목적**: 전체 매출, 주문 수, 평균 판매가
- **팩트 테이블**: `fact_sales`
  - `order_id`, `order_item_id`, `product_id`, `seller_id`
  - `price`, `freight_value`, `order_status`, `order_date`
- **차원 테이블**:
  - `dim_product`: 제품 정보
  - `dim_seller`: 판매자 위치 정보
  - `dim_order_status`: 주문 상태 그룹화
  - `dim_date`: 날짜 정보
- **KPI 예시**:
  - 총 매출 `SUM(price)`
  - 평균 주문 건당 상품 수
  - 판매자별 매출 랭킹

---

### ✅ 고객 마트 (Customer Mart)

- **분석 목적**: 고객 구매액, 리뷰 점수, 주문 횟수
- **팩트 테이블**: `fact_customer_orders`
  - `customer_id`, `order_id`, `order_date`, `payment_value`, `review_score`
- **차원 테이블**:
  - `dim_customer`: 고객 위치 및 고유 ID 정보
  - `dim_date`: 주문 일자 기준 분석

---

## 3단계: ETL 설계

### 📥 Extract

- 원본 테이블:
  - `orders`, `order_items`
  - `order_payments`, `order_reviews`
  - `products`, `sellers`, `customers`
  - `geolocation`, `product_category_name_translation`

---

### 🔄 Transform & Load

#### 📦 `fact_sales` (판매 중심 팩트 테이블)

```sql
CREATE TABLE fact_sales (
    order_id VARCHAR(50),
    order_item_id INT,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    price FLOAT,
    freight_value FLOAT,
    order_status VARCHAR(50),
    order_date DATE
);

INSERT INTO fact_sales
SELECT
    oi.order_id,
    oi.order_item_id,
    oi.product_id,
    oi.seller_id,
    oi.price,
    oi.freight_value,
    o.order_status,
    DATE(o.order_purchase_timestamp) AS order_date
FROM olist.order_items oi
JOIN olist.orders o ON oi.order_id = o.order_id
WHERE o.order_status IN ('delivered', 'shipped');
```

#### 👤 `fact_customer_orders` (고객 중심 팩트 테이블)
```sql
CREATE TABLE fact_customer_orders (
    customer_id VARCHAR(50),
    order_id VARCHAR(50),
    order_date DATE,
    payment_value FLOAT,
    review_score INT
);

INSERT INTO fact_customer_orders
SELECT
    o.customer_id,
    o.order_id,
    DATE(o.order_purchase_timestamp),
    p.payment_value,
    r.review_score
FROM olist.orders o
JOIN olist.order_payments p ON o.order_id = p.order_id
LEFT JOIN olist.order_reviews r ON o.order_id = r.order_id
WHERE o.order_status IN ('delivered', 'shipped');
```

#### 📚 차원 테이블 정의
##### dim_product
```sql
CREATE TABLE dim_product (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(255),
    product_weight_g FLOAT,
    product_length_cm FLOAT,
    product_height_cm FLOAT,
    product_width_cm FLOAT,
    product_category_name_english VARCHAR(255)
);

INSERT INTO dim_product
SELECT
    p.product_id,
    p.product_category_name,
    p.product_weight_g,
    p.product_length_cm,
    p.product_height_cm,
    p.product_width_cm,
    COALESCE(t.product_category_name_english, 'unknown')
FROM olist.products p
LEFT JOIN olist.product_category_name_translation t
ON p.product_category_name = t.product_category_name;
```
##### dim_seller
```sql
CREATE TABLE dim_seller (
    seller_id VARCHAR(50),
    seller_zip_code_prefix VARCHAR(10),
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(10),
    geolocation_lat DECIMAL(12, 8),
    geolocation_lng DECIMAL(12, 8)
);

INSERT INTO dim_seller
SELECT
    s.seller_id,
    s.seller_zip_code_prefix,
    g.geolocation_city,
    g.geolocation_state,
    g.geolocation_lat,
    g.geolocation_lng
FROM olist.sellers s
LEFT JOIN (
    SELECT
        geolocation_zip_code_prefix,
        geolocation_city,
        geolocation_state,
        AVG(geolocation_lat) AS geolocation_lat,
        AVG(geolocation_lng) AS geolocation_lng
    FROM olist.geolocation
    GROUP BY geolocation_zip_code_prefix, geolocation_city, geolocation_state
) g
ON s.seller_zip_code_prefix = g.geolocation_zip_code_prefix
AND s.seller_city = g.geolocation_city
AND s.seller_state = g.geolocation_state;
```
##### dim_customer
```sql
CREATE TABLE dim_customer (
    customer_id VARCHAR(50),
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix VARCHAR(10),
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(10)
);

INSERT INTO dim_customer
SELECT
    c.customer_id,
    c.customer_unique_id,
    c.customer_zip_code_prefix,
    g.geolocation_city,
    g.geolocation_state
FROM olist.customers c
LEFT JOIN olist.geolocation g
ON c.customer_zip_code_prefix = g.geolocation_zip_code_prefix;
```
##### dim_date
```sql
CREATE TABLE dim_date (
    date DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT,
    weekday INT,
    week INT
);

INSERT INTO dim_date
SELECT
    date,
    YEAR(date),
    MONTH(date),
    DAY(date),
    WEEKDAY(date),
    WEEK(date)
FROM (
    WITH RECURSIVE date_series AS (
        SELECT DATE('2016-09-04') AS date
        UNION ALL
        SELECT DATE_ADD(date, INTERVAL 1 DAY)
        FROM date_series
        WHERE date < '2018-09-03'
    )
    SELECT * FROM date_series
) derived;
```

##### dim_order_status
```sql
CREATE TABLE dim_order_status (
    order_status VARCHAR(50) PRIMARY KEY,
    status_group VARCHAR(50)
);

INSERT INTO dim_order_status
VALUES
  ('delivered', '성공'),
  ('shipped', '성공'),
  ('processing', '진행중'),
  ('created', '진행중'),
  ('canceled', '실패'),
  ('unavailable', '실패'),
  ('invoiced', '성공'),
  ('approved', '진행중');
```

##### dim_geolocation
```sql
CREATE TABLE dim_geolocation (
    geolocation_zip_code_prefix VARCHAR(10),
    geolocation_city VARCHAR(255),
    geolocation_state VARCHAR(10),
    avg_lat DECIMAL(12, 8),
    avg_lng DECIMAL(12, 8),
    PRIMARY KEY (geolocation_zip_code_prefix, geolocation_city, geolocation_state)
);

INSERT INTO dim_geolocation
SELECT
    geolocation_zip_code_prefix,
    geolocation_city,
    geolocation_state,
    AVG(geolocation_lat),
    AVG(geolocation_lng)
FROM olist.geolocation
GROUP BY
    geolocation_zip_code_prefix,
    geolocation_city,
    geolocation_state;
```

---
#### 대시보드용 View
```sql
-- 판매 대시보드
CREATE VIEW vw_sales_dashboard AS
SELECT
    fs.order_id,
    fs.order_date,
    dd.year,
    dd.month,
    dp.product_category_name_english,
    ds.geolocation_state AS seller_state,
    fs.price,
    fs.freight_value,
    dos.status_group
FROM fact_sales fs
JOIN dim_date dd ON fs.order_date = dd.date
JOIN dim_product dp ON fs.product_id = dp.product_id
JOIN dim_seller ds ON fs.seller_id = ds.seller_id
JOIN dim_order_status dos ON fs.order_status = dos.order_status;

-- 고객 대시보드
CREATE VIEW vw_customer_dashboard AS
SELECT
    fco.order_id,
    fco.order_date,
    dc.geolocation_state AS customer_state,
    fco.payment_value,
    fco.review_score,
    dd.year,
    dd.month
FROM fact_customer_orders fco
JOIN dim_customer dc ON fco.customer_id = dc.customer_id
JOIN dim_date dd ON fco.order_date = dd.date;
```