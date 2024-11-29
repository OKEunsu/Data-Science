# 문제 : 특정 기간동안 대여 가능한 자동차들의 대여 비용 구하기

## 문제 설명
CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액(컬럼명: FEE)을 구하여 대여 기록 ID와 대여 금액 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순 정렬해주세요.


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
3. 'CAR_RENTAL_COMPANY_DISCOUNT_PLAN'
   - `PLAN_ID` 
   - `CAR_TYPE` 
   - `DURATION_TYPE` 
   - `DISCOUNT_RATE` 


### 풀이
#### 1. JOIN 활용 & WHERE 조건절
```SQL

```

#### 2. 



