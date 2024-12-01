# 문제 : [특정 세대의 대장균 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/301650)
3세대의 대장균의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 이때 결과는 대장균의 ID 에 대해 오름차순 정렬해주세요.

<br/>


### 입력 테이블
1. `ECOLI_DATA `
   - `ID`
   - `PARENT_ID`
   - `SIZE_OF_COLONY`
   - `DIFFERENTIATION_DATE`
   - `GENOTYPE`

### 풀이

#### 1. Join

```sql
-- JOIN 이용
SELECT F.ID
FROM ECOLI_DATA AS F
JOIN ECOLI_DATA AS S ON F.PARENT_ID = S.ID
JOIN ECOLI_DATA AS T ON S.PARENT_ID = T.ID
WHERE T.PARENT_ID IS NULL
ORDER BY F.ID ASC;
```

<br/>

#### 2. 재귀식 사용
```sql
-- 재귀식 이용
WITH RECURSIVE GENERATION AS (
	-- 초기 조건 : 첫 번째 세대 (PARENT_ID가 NULL인 개체)
	SELECT ID, PARENT_ID, 1 AS GEN
	FROM ECOLI_DATA
	WHERE PARENT_ID IS NULL
	
	UNION ALL
	
	-- 재귀적 조건 : 다음 세대 찾기
	SELECT E.ID, E.PARENT_ID, G.GEN + 1 AS GEN
	FROM ECOLI_DATA E
	INNER JOIN GENERATION G ON E.PARENT_ID = G.ID
)
-- 최종 결과 선택 : 3세대 개체의 ID
SELECT ID
FROM GENERATION
WHERE GEN = 3
ORDER BY ID;
```

### 재귀 CTE
- 재귀 CTE를 사용하는 것은 **계층적 데이터**를 다룰 때 매우 강력한 도구
- 복잡한 부모-자식 관계를 간결하고 이해하기 쉽게 표현할 수 있음
- 각 재귀 단계에서 새로운 세대는 **바로 이전 세대의 결과**를 참조하여 생성되지만, 이전 모든 단계의 결과는 `Generation` CTE 내에 계속 축적됨

---

1. **CTE 시작 (WITH RECURSIVE Generation AS (...))**: 재귀적으로 사용될 CTE를 정의. `Generation`은 각 세대의 대장균을 추적.
2. **초기 조건**:
    - 첫 번째 `SELECT` 문은 초기 조건을 설정. 여기서는 `PARENT_ID`가 **NULL**인 대장균, 즉 첫 세대를 선택.
    - `Gen`이라는 열을 추가하여, 현재 세대를 나타냄 (첫 세대는 1).
3. **재귀적 조건**:
    - `UNION ALL`을 사용하여 초기 조건의 결과와 재귀적으로 생성된 결과를 결합.
    - 두 번째 `SELECT` 문에서는 `ECOLI_DATA` 테이블의 각 행(`e`)을 `Generation` CTE의 결과(`g`)와 조인. 여기서 `e.PARENT_ID = g.ID`는 자식 대장균을 부모와 연결.
    - `Gen + 1`은 각 반복에서 세대를 하나씩 증가시킴. 즉, 부모의 세대에서 자식 세대로 넘어갈 때마다 세대 수가 증가.
4. **최종 결과 선택**:
    - `WHERE Gen = 3`을 통해 3세대의 대장균만 선택.
    - 결과는 `ID`에 대해 오름차순으로 정렬.

참고) 재귀 CTE에 관한 개념 설명 : [RECURSIVE CTE](https://ddunddan.tistory.com/30)
