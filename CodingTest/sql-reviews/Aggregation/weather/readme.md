# 문제 : Weather Observation Station 20 / LAT_N 중앙값 구하기
### [Weather Observation Station 20](https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true)

## 문제 설명
A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  4decimal places

<br/>


### 입력 테이블
1. `STATION`
   - `ID`
   - `CITY`
   - `STATE`
   - `LAT_N`
   - `LONG_W`

<br/>

### 풀이
#### 1. LAT_N WINDOW FUNTION으로 넘버링
```SQL
SELECT
  LAT_N,
  ROW_NUMBER() OVER (ORDER BY LAT_N) AS RN
FROM STATION
```

<br/>


#### 2. 전체 ROW 갯수 구하기
```SQL
SELECT COUNT(*) AS CNT FROM STATION
```

<br/>

#### 3. 홀수 -> cast((CNT + 1) / 2 as int) , 짝수 -> cast((CNT + 2) / 2)
(cnt + 1) / 2 -> 특정 문맥에서 값을 암묵적으로 내림하여 정수로 처리할 수 있음
(cnt + 1) / 2 == cast((cnt + 1) / 2 as int)

```sql
with loc as (
  select LAT_N,
        row_number() over (order by LAT_N) as rn
  from station
),
shape as (
  select count(*) as row_cnt from station
)
select round(avg(lat_n), 4)
from loc, shape
where rn in ((row_cnt + 1) / 2, (row_cnt + 2) / 2)
```


