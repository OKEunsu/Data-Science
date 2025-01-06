# 문제 : Symmetric Pairs
### [Symmetric Pairs](https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true)

## 문제 설명
(X1, Y1), (X2, Y2) 에서 X1=Y1이고 X2=Y1일 때 대칭 쌍이라고 합니다.  
모든 대칭 쌍을 X 오름차순 정렬, X1 <= Y1 형식으로 

<br/>

### 입력 테이블
1. `Functions`
   - `X`
   - `Y`


<br/>

### 풀이
#### 1. X1 <= Y1을 만족하는 쌍 대칭 쌍 X 기준으로 모으기
```SQL
select if(X <= Y, X, Y) as X, if(X <= Y, Y, X) as Y
from Functions
```
<br/>

#### 2. 쌍이 두개인 것만 출력
```SQL
select *
from (
   select if(X <= Y, X, Y) as X, if(X <= Y, Y, X) as Y
   from Functions
) a
group by a.X, a.Y
having count(*) >= 2
```

<br/>

#### 3. X 오름차순으로 정렬
```SQL
select *
from (
   select if(X <= Y, X, Y) as X, if(X <= Y, Y, X) as Y
   from Functions
) a
group by a.X, a.Y
having count(*) >= 2
order by a.X asc;
```


