# 문제 : 15 Days of Learning SQL
### [15 Days of Learning SQL](https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true)

## 문제 설명
줄리아씨.. 15일 동안 SQL 학습 대회를 진행했습니다..
대회 시작일은 2016년 3월 1일이었고, 종료일은 2016년 3월 15일이었습니다.

1. 매일 최소 제출 횟수를 기록한 고유 해커의 총 수를 출력
2. 매일 최대 제출 횟수를 기록한 해커의 hacker_id와 이름을 찾기
3. 해커가 최대 제출 횟수를 두 번 이상 기록한 경우, 가장 낮은 hacker_id 출력
4. 대회를 날짜별로 정렬

<br/>


### 입력 테이블
1. `Hackers`
   - `hacker_id`
   - `name`
2. `Submissions`
   - `submission_date` 
   - `submission_id`
   - `hacker_id`
   - `score`

<br/>

### 예제
#### Hackers Table
![image](https://github.com/user-attachments/assets/a008921e-3dba-40b9-9ab7-d103ce657d27)  
#### Submissions Table  
![image](https://github.com/user-attachments/assets/f37791e8-21e5-41cd-89da-ab533c532149)

### Sample Output
```
2016-03-01 4 20703 Angela
2016-03-02 2 79722 Michael
2016-03-03 2 20703 Angela
2016-03-04 2 20703 Angela
2016-03-05 1 36396 Frank
2016-03-06 1 20703 Angela
```

<br/>

### 설명





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


