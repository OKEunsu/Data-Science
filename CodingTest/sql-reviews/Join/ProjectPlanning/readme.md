# 문제 : Project Planning
### [Project Planning](https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true)

## 문제 설명
1. Start_date ~ End_date의 차이는 항상 1일임이 보장된다.
2. End_date가 연속적이라면, 해당 작업들은 같은 프로젝트의 일부로 간주
3. 완료된 프로젝트의 총 개수를 확인
4. 프로젝트 완료 까지 걸린 일수 기준으로 오름차순 정렬
5. 프로젝트 시작일을 기준으로 오름차순 정렬


<br/>

### 입력 테이블
1. `Project`
   - `Task_ID`
   - `Start_Date`
   - `End_Date`


<br/>

### 풀이
#### 1. End_Date가 연속된 프로젝트 그룹화
- 1일 차이나는 end_date
- 2025-01-06 첫번쨰 -1 2025-01-05
- 2025-01-07 두번째 -2 2025-01-05
Row_number() 사용

<br/>

```SQL
(
select *,
   end_date - row_number() over (order by end_date) as project_group
from Projects
order by end_date asc
)
```
<br/>

#### 2. 프로젝트 그룹화 중 최솟값, 최대값, 정렬
```SQL
select min(start_date), max(end_date)
from 
(
   select *,
      end_date - row_number() over (order by end_date) as project_group
   from Projects
   order by end_date asc
) a
group by a.project_group
order by max(end_date) - min(start_date) asc, min(start_date) asc
```



