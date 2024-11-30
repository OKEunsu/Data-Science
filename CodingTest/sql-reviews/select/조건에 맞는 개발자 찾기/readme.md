# 문제 : 조건에 맞는 개발자 찾기
### [조건에 맞는 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276034)

## 문제 설명
DEVELOPERS 테이블에서 Python이나 C# 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.

결과는 ID를 기준으로 오름차순 정렬해 주세요.

### 입력 테이블
1. `SKILLCODES`
   - `NAME`
   - `CATEGORY`
   - `CODE`
2. `DEVELOPERS`
   - `ID` 
   - `FIRST_NAME` 
   - `order_amount`
   - `LAST_NAME`
   - `EMAIL`
   - `SKILL_CODE`

### 풀이
#### 1. JOIN 활용
`Orders`와 `Customers`를 `customer_id`를 기준으로 조인합니다.

#### 2. GROUP BY 및 집계 함수 사용
`SUM(order_amount)`를 사용해 고객별 총 주문 금액을 계산합니다.

```sql
SELECT
    c.customer_name,
    SUM(o.order_amount) AS total_amount
FROM
    Customers c
JOIN
    Orders o ON c.customer_id = o.customer_id
GROUP BY
    c.customer_name;
