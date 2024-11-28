# 문제
- USER_INFO 테이블과 ONLINE_SALE 테이블에서 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율(=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력하는 SQL문을 작성해주세요.  
- 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림하고, 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬해주세요.  

## 데이터
### 입력 테이블
1. `Customers`
   
| Column Name | Type       | Nullable |
|-------------|------------|----------|
| USER_ID     | INTEGER    | FALSE    |
| GENDER      | TINYINT(1) | TRUE     |
| AGE         | INTEGER    | TRUE     |
| JOINED      | DATE       | FALSE    |
  
2. `Orders`
   
| Column Name    | Type       | Nullable |
|----------------|------------|----------|
| ONLINE_SALE_ID | INTEGER    | FALSE    |
| USER_ID        | INTEGER    | FALSE    |
| PRODUCT_ID     | INTEGER    | FALSE    |
| SALES_AMOUNT   | INTEGER    | FALSE    |
| SALES_DATE     | DATE       | FALSE    |

## 풀이과정
### 1. 2021년에 가입한 회원, LEFT JOIN

```
SELECT UI.JOINED, OS.SALES_DATE, UI.USER_ID AS JOIN_ID, OS.USER_ID AS SALE_ID
FROM USER_INFO UI 
    LEFT JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
WHERE YEAR(UI.JOINED) = '2021'
```  
  
### 2. 연도별, 월별로 구입한 고유한 회원수 구하기  

```
SELECT YEAR(OS.SALES_DATE) AS YEAR, MONTH(OS.SALES_DATE) AS YEAR, COUNT(DISTINCT OS.USER_ID) AS PURCHASED_USERS
FROM USER_INFO UI 
    LEFT JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
WHERE YEAR(UI.JOINED) = '2021'
GROUP BY 1, 2 
HAVING YEAR IS NOT NULL; # NULL 값도 같이 그룹화 됨
```  
### 3. 2021년에 가입한 전체 회원수 구하기  
```
SELECT COUNT(DISTINCT UI.USER_ID) AS TOTAL_USER
FROM USER_INFO UI 
WHERE YEAR(UI.JOINED) = '2021'
```  

### 4. 비율 구하기  
```
SELECT YEAR(OS.SALES_DATE) AS YEAR, MONTH(OS.SALES_DATE) AS MONTH, COUNT(DISTINCT OS.USER_ID) AS PURCHASED_USERS,
       ROUND(COUNT(DISTINCT OS.USER_ID) / (SELECT COUNT(DISTINCT UI.USER_ID) 
                                            FROM USER_INFO UI 
                                            WHERE YEAR(UI.JOINED) = '2021'), 1) AS PURCHASE_RATE
FROM USER_INFO UI
LEFT JOIN ONLINE_SALE OS ON UI.USER_ID = OS.USER_ID
WHERE YEAR(UI.JOINED) = '2021'
GROUP BY 1, 2
HAVING YEAR IS NOT NULL
ORDER BY 1, 2
```
