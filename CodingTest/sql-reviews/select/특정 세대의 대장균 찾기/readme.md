# 문제 : [특정 세대의 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301650)
3세대의 대장균의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 이때 결과는 대장균의 ID 에 대해 오름차순 정렬해주세요.

<br/>

## 문제 설명
대장균들은 일정 주기로 분화하며, 분화를 시작한 개체를 부모 개체, 분화가 되어 나온 개체를 자식 개체라고 합니다.
  
다음은 실험실에서 배양한 대장균들의 정보를 담은 `ECOLI_DATA` 테이블입니다. `ECOLI_DATA` 테이블의 구조는 다음과 같으며, `ID`, `PARENT_ID`, `SIZE_OF_COLONY`, `DIFFERENTIATION_DATE`, `GENOTYPE` 은 각각 대장균 개체의 ID, 부모 개체의 ID, 개체의 크기, 분화되어 나온 날짜, 개체의 형질을 나타냅니다.

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
