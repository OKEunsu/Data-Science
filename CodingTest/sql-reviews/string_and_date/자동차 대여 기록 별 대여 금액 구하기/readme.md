# 문제 : 자동차 대여 기록 별 대여 금액 구하기
### [자동차 대여 기록 별 대여 금액 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/151141)

## 문제 설명
CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬해주세요.

<br/>


### 입력 테이블
1. `CAR_RENTAL_COMPANY_CAR`
   - `CAR_ID`
   - `CAR_TYPE`
   - `DAILY_FEE`
   - `OPTIONS`
2. `CAR_RENTAL_COMPANY_RENTAL_HISTORY`
   - `HISTORY_ID` 
   - `CAR_ID`
   - `START_DATE`
   - `END_DATE`
3. `CAR_RENTAL_COMPANY_DISCOUNT_PLAN`
   - `PLAN_ID` 
   - `CAR_TYPE` 
   - `DURATION_TYPE` 
   - `DISCOUNT_RATE` 

<br/>

### 풀이
#### 1. HISTORY에서 트럭인 빌린 일수 구하기
```SQL
WITH TEMP_01 AS (
    SELECT 
        A.history_id, 
        DATEDIFF(A.end_date, A.start_date) + 1 AS DIFF_DAYS, 
        B.daily_fee
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY A
    JOIN 
        CAR_RENTAL_COMPANY_CAR B
    ON 
        A.car_id = B.car_id
    WHERE 
        B.car_type = '트럭'
)
```

<br/>


#### 2. 기간 숫자로 변경
```SQL
TEMP_02 AS (
    SELECT 
        CASE 
            WHEN DURATION_TYPE = '7일 이상' THEN 7
            WHEN DURATION_TYPE = '30일 이상' THEN 30
            WHEN DURATION_TYPE = '90일 이상' THEN 90
        END AS duration_days, 
        discount_rate
    FROM 
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
    WHERE 
        car_type = '트럭'
)
```

<br/>

#### 3. 각 일수에 맞는 할인율 가져오기
```sql
TEMP_03 AS (
    SELECT 
        T1.HISTORY_ID, 
        T1.DIFF_DAYS, 
        T1.DAILY_FEE,
        CASE 
            WHEN T1.DIFF_DAYS >= 90 THEN (SELECT discount_rate FROM TEMP_02 WHERE duration_days = 90)
            WHEN T1.DIFF_DAYS >= 30 THEN (SELECT discount_rate FROM TEMP_02 WHERE duration_days = 30)
            WHEN T1.DIFF_DAYS >= 7 THEN (SELECT discount_rate FROM TEMP_02 WHERE duration_days = 7)
            ELSE 0
        END AS DISCOUNT_RATE
    FROM 
        TEMP_01 T1
)
```

<br/>

#### 4. 총 금액 계산
```sql
SELECT 
    HISTORY_ID, 
    ROUND((DIFF_DAYS * DAILY_FEE) * (1 - DISCOUNT_RATE / 100)) AS FEE
FROM 
    TEMP_03
ORDER BY 
    FEE DESC, 
    HISTORY_ID DESC;
```

