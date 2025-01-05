# 문제 : Challenges
### [Challenges](https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true)

## 문제 설명
Julia은 학생들에게 몇가지 코딩 챌린지를 만들도록 요청.  
1. 각 학생이 만든 챌린지의 총 개수와 함께 hacker_id, 이름
2. 생성된 챌린지의 총 개수를 기준으로 내림차순, hacker_id 기준으로 오름차순 정렬
3. 동일한 챌린지 개수를 만든 학생이 여러명, 해당 개수가 가장 많이 생성된 챌린지 개수보다 적다면, 그 학생들은 결과에서 제외

<br/>

### 입력 테이블
1. `Hackers`
   - `hacker_id`
   - `name`
2. `Challenges`
   - `challenge_id` 
   - `hacker_id`

<br/>

### 풀이
#### 1. 각 학생이 만든 챌린지 총 개수 구하기
```SQL
SELECT h.hacker_id, h.name, COUNT(*) cnt
FROM hackers h
     INNER JOIN challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
```
<br/>

#### 2. 생성된 챌린지 개수가 max이면 모두 다 출력, 
```SQL
HAVING cnt = (SELECT max(sub.cnt) as maxcnt
                FROM (
                    SELECT hacker_id, count(*) as cnt
                    FROM challenges
                    GROUP BY hacker_id
                ) sub)
```

<br/>

#### 3. 생성된 챌린지 개수가 같을 경우 제외
```SQL
OR cnt IN (SELECT sub.cnt
                FROM (
                    select hacker_id, count(*) as cnt
                    from challenges
                    group by hacker_id
                ) sub
                GROUP BY sub.cnt
                HAVING count(*) = 1)
```

<br/>

#### 4. 정렬 생성된 챌린지의 총 개수를 기준으로 내림차순, hacker_id 기준으로 오름차순 정렬
```sql
ORDER BY cnt DESC, h.hacker_id
```

#### 5. 총 정리
```sql
SELECT h.hacker_id, h.name, COUNT(*) cnt
FROM hackers h
     INNER JOIN challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING cnt = (SELECT max(sub.cnt) as maxcnt
                FROM (
                    SELECT hacker_id, count(*) as cnt
                    FROM challenges
                    GROUP BY hacker_id
                ) sub)
OR cnt IN (SELECT sub.cnt
                FROM (
                    select hacker_id, count(*) as cnt
                    from challenges
                    group by hacker_id
                ) sub
                GROUP BY sub.cnt
                HAVING count(*) = 1)
ORDER BY cnt DESC, h.hacker_id
```
