# 문제 : [Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/description/)

## 문제 설명
Write a solution to find the prices of all products on `2019-08-16`.   
Assume the price of all products before any change is `10`

<br/>

### 입력 테이블
1. `Products `
   - `product_id`
   - `new_price`
   - `change_date`
  

### 풀이 1 서브쿼리
#### 1. 고유 product_id 가져오기
```sql
(SELECT distinct product_id
FROM products) p
```

<br/>


#### 2. 상관 서브쿼리

```sql
select new_price
from products p2
where p.product_id = p2.product_id
  and p2.change_date <= '2019-08-16'
order by p2.change_date desc
limit 1
```

<br/>

#### 3. 2019년 8월 16일 이전 값이 없을 경우 Null값 처리
```sql
coalesce(-- 상관쿼리식
, 0)
```

<br/>


#### 4. 전체 코드
```sql
SELECT p.product_id,
       COALESCE(
           (SELECT new_price
            FROM Products p2
            WHERE p.product_id = p2.product_id
              AND p2.change_date <= '2019-08-16'
            ORDER BY p2.change_date DESC
            LIMIT 1), 
           10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p;
```

<br/>

### 풀이 2 윈도우 함수
#### 1. `2019-08-16`보다 작거나 같은 테이블 생성
```sql
SELECT p.product_id,
        p2.new_price, 
        ROW_NUMBER() OVER (PARTITION BY p.product_id ORDER BY p2.change_date DESC) AS rn -- 제일 최근의 날짜부터 숫자 생성
FROM Products p
LEFT JOIN Products p2
    ON p.product_id = p2.product_id -- 2019년 이후 값을 Null로 받기 위함
    AND p2.change_date <= '2019-08-16' -- change_date가 8월 16일보다 작거나 같은 것만 
```

</br>

#### 2. 결측값 -> 10으로, rn = 1로 최근 값 가져오기
```sql
SELECT product_id,
       COALESCE(new_price, 10) AS price
FROM RankedPrices
WHERE rn = 1;
```

<br/>

#### 3. 전체 코드
```sql
WITH RankedPrices AS (
    SELECT p.product_id,
           p2.new_price,
           ROW_NUMBER() OVER (PARTITION BY p.product_id ORDER BY p2.change_date DESC) AS rn
    FROM Products p
    LEFT JOIN Products p2
        ON p.product_id = p2.product_id
        AND p2.change_date <= '2019-08-16'
)
SELECT product_id,
       COALESCE(new_price, 10) AS price
FROM RankedPrices
WHERE rn = 1;
```
