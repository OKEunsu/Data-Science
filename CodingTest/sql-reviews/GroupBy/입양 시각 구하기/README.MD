# 문제
- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.  

## 데이터  
### 입력 테이블  
1. `ANIMAL_OUTS`  
  
| **NAME**              | **TYPE**   | **NULLABLE** |
|-----------------------|------------|--------------|
| ANIMAL_ID             | VARCHAR(N) | FALSE        |
| ANIMAL_TYPE           | VARCHAR(N) | FALSE        |
| DATETIME              | DATETIME   | FALSE        |
| NAME                  | VARCHAR(N) | TRUE         |
| SEX_UPON_OUTCOME      | VARCHAR(N) | FALSE        |


## 풀이과정
### 1. RECURSIVE 학습  


```SQL
WITH RECURSIVE recursive_name AS (
    -- 기본 쿼리 (Anchor Member)
    SELECT columns
    FROM table
    WHERE condition
    UNION ALL
    -- 재귀 쿼리 (Recursive Member)
    SELECT columns
    FROM table
    JOIN recursive_name ON condition
)
SELECT * FROM recursive_name;
```  
  
1. 'WITH RECURSIVE' : 재귀 쿼리를 시작하는 키워드.
2. 'RECURSIVE_NAME' : 재귀 쿼리의 결과를 임시 테이블처럼 사용할 이름  
3. 기본 쿼리 : 재귀 쿼리가 시작되는 기본 데이터를 반환하는 부분.
4. 재귀 쿼리 : 기본 쿼리에서 반환된 데이터를 기반으로 반복적으로 데이터를 검색하는 부분  
5. 'UNION ALL' : 기본 쿼리와 재귀 쿼리의 결과를 결합합니다.  
6. 'SELECT' : 재귀 쿼리의 결과를 선택하여 반환합니다.
  
  
### 2. 
