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
이 판매자들은 Olist 스토어를 통해 제품을 판매하고 Olist 물류 파트너를 이용하여 고객에게 직접 배송할 수 있습니다. 자세한 내용은 저희 웹사이트(www.olist.com)에서 확인할 수 있습니다. 

고객이 Olist 스토어에서 제품을 구매하면 판매자에게 해당 주문을 처리하라는 알림이 전송됩니다.  
고객이 제품을 받거나 예상 배송일이 되면, 고객은 이메일로 만족도 설문조사를 받아 구매 경험에 대한 평가를 제공하고 의견을 작성할 수 있습니다.  

<br/>

### 주의사항
하나의 주문에 여러 개의 상품이 있을 수 있습니다.

각 상품은 다른 판매자가 처리할 수 있습니다.

상점과 파트너를 식별하는 모든 텍스트는 '왕좌의 게임'에 나오는 위대한 가문의 이름으로 대체되었습니다.

마켓플레이스에 등록된 제품의 예시가 제공됩니다.

## 3. 폴더 구조
📁 abtest_01_dw_design
  ↳ 데이터베이스 설계 / 스키마 구조 / 논리-물리 모델
📁 abtest_02_sql_optimization
  ↳ 복잡한 쿼리, CTE, 인덱스 활용 사례
📁 abtest_03_data_mart
  ↳ 마케팅 마트 뷰 구성 및 KPI 시각화
📁 docs
  ↳ 회고, 설계 노트, ERD 이미지 등

  
