# 문제
REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.

## 데이터  

| Column Name  | Type       | Nullable |
|--------------|------------|----------|
| REST_ID      | VARCHAR(5) | FALSE    |
| REST_NAME    | VARCHAR(50)| FALSE    |
| FOOD_TYPE    | VARCHAR(20)| TRUE     |
| VIEWS        | NUMBER     | TRUE     |
| FAVORITES    | NUMBER     | TRUE     |
| PARKING_LOT  | VARCHAR(1) | TRUE     |
| ADDRESS      | VARCHAR(100)| TRUE     |
| TEL          | VARCHAR(100)| TRUE     |


  
### 문제풀이
