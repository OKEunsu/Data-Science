# 문제 : 조건에 맞는 개발자 찾기
### [조건에 맞는 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276034)

## 문제 설명
DEVELOPERS 테이블에서 Python이나 C# 스킬을 가진 개발자의 정보를 조회하려 합니다. 조건에 맞는 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요.

결과는 ID를 기준으로 오름차순 정렬해 주세요.

### 입력 테이블
1. `SKILLCODES`
   - `NAME`
   - `CATEGORY`
   - `CODE`
2. `DEVELOPERS`
   - `ID` 
   - `FIRST_NAME` 
   - `order_amount`
   - `LAST_NAME`
   - `EMAIL`
   - `SKILL_CODE`

### 풀이
#### 1. JOIN 활용
`SKILL_CODE`와 `CODE`를 비트 연산자로 JOIN

```SQL
SELECT *
FROM DEVELOPERS D
   JOIN SKILLCODES S ON (D.SKILL_CODE & S.CODE) = S.CODE
WHERE FIRST_NAME = 'Jerami'
```

##### 예시  
ID가 `D165`인 Edwards Jerami 개발자는 `SKILL CODE`가 400이다.  
400을 비트 연산으로 하면 110010000 이다.
400은 256 + 128 + 16 이므로 Python, Java, JavaScript가 되어야 한다.

<br/>

| ID   | FIRST_NAME | LAST_NAME | EMAIL                     | SKILL_CODE | NAME       | CATEGORY  | CODE |
|------|------------|-----------|---------------------------|------------|------------|-----------|------|
| D165 | Jerami     | Edwards   | jerami_edwards@grepp.co   | 400        | JavaScript | Front End | 16   |
| D165 | Jerami     | Edwards   | jerami_edwards@grepp.co   | 400        | Java       | Back End  | 128  |
| D165 | Jerami     | Edwards   | jerami_edwards@grepp.co   | 400        | Python     | Back End  | 256  |

<br/>

#### 2. WHERE 조건절 Python, C# 가져오기

```sql
WHERE S.NAME = 'C#' OR S.NAME = 'Python'
```

<br/>

#### 3. 전체 코드 - 중복 제거 DISTINCT ID 사용
```sql
SELECT DISTINCT
    D.ID,
    D.EMAIL,
    D.FIRST_NAME,
    D.LAST_NAME
FROM
    DEVELOPERS D
JOIN
    SKILLCODES S
ON
    (D.SKILL_CODE & S.CODE) = S.CODE
WHERE S.NAME = 'C#' OR S.NAME = 'Python'
ORDER BY D.ID ASC;
```
