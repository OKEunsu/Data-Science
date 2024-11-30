# 문제 : 특정 기간동안 대여 가능한 자동차들의 대여 비용 구하기
### [특정 기간동안 대여 가능한 자동차들의 대여비용 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/157339)

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
#### 1. 대여 가능 여부 확인
```SQL
-- 대여 가능 여부 확인
WITH AVAILABLE_CARS AS (
    SELECT C.CAR_ID, C.CAR_TYPE, C.DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR C
    LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    ON C.CAR_ID = H.CAR_ID 
    AND (
        (H.START_DATE <= '2022-11-30' AND H.END_DATE >= '2022-11-01')
    )
    WHERE H.CAR_ID IS NULL
    AND C.CAR_TYPE IN ('세단', 'SUV')
)
```
<br/>

#### 2. 11-1 ~ 11-30 에 예약하지 않는 테이블
```SQL
-- 할인 요금 테이블
DISCOUNTED_CARS AS (
    SELECT 
        A.CAR_ID, 
        A.CAR_TYPE, 
        A.DAILY_FEE,
        DP.DISCOUNT_RATE / 100 AS DISCOUNT_RATE
    FROM AVAILABLE_CARS A
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN DP
    ON A.CAR_TYPE = DP.CAR_TYPE
```

<br/>

#### 3. 해당 CAR_ID 할인 요금(30일 이상) 조인
```SQL
-- 조건 필터링
CAR_FEES AS (
    SELECT 
        CAR_ID, 
        CAR_TYPE, 
        ROUND((DAILY_FEE * 30) * (1 - DISCOUNT_RATE)) AS FEE
    FROM DISCOUNTED_CARS
)
-- 정렬
SELECT 
    CAR_ID, 
    CAR_TYPE, 
    FEE
FROM CAR_FEES
WHERE FEE >= 500000 
AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;
```

