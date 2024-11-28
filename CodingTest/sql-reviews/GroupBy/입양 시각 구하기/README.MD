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
### 1. 2021년에 가입한 회원, LEFT JOIN

```SQL

```
