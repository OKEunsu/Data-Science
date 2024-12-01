# 문제 : 부모의 형질을 모두 가지는 대장균 찾기
#### [부모의 형질을 모두 가지는 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301647)

## 문제 설명
부모의 형질을 모두 보유한 대장균의 ID(ID), 대장균의 형질(GENOTYPE), 부모 대장균의 형질(PARENT_GENOTYPE)을 출력하는 SQL 문을 작성해주세요. 이때 결과는 ID에 대해 오름차순 정렬해주세요.

### 입력 테이블
1. `ECOLI_DATA `
   - `ID`
   - `PARENT_ID`
   - `SIZE_OF_COLONY`
   - `DIFFERENTIATION_DATE`
   - `GENOTYPE`

### 풀이
#### 1. Data 조회
```sql
SELECT *
FROM ECOLI_DATA
```

<br/>


#### 2. Join

```sql
-- JOIN
SELECT A.ID, A.PARENT_ID, B.ID
FROM ECOLI_DATA A
JOIN ECOLI_DATA B ON A.PARENT_ID = B.ID
-- 부모 노드와 자식 노드 결합
```

<br/>

#### 3. 부모 노드 형질 = 부모 or 자식 형질
```sql
SELECT
    child.ID,
    child.GENOTYPE,
    parent.GENOTYPE AS PARENT_GENOTYPE
FROM
    ECOLI_DATA child
JOIN
    ECOLI_DATA parent
ON
    child.PARENT_ID = parent.ID
WHERE
    (child.GENOTYPE | parent.GENOTYPE) = child.GENOTYPE
ORDER BY
    child.ID;
```
