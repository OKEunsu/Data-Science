# 문제 : [Average Selling Price](https://leetcode.com/problems/average-selling-price/description/)
## 문제 
Write a solution to find the average selling price for each product. 
average_price should be rounded to 2 decimal places.   
If a product does not have any sold units, its average selling price is assumed to be 0.  
Return the result table in any order.

<br/>

### 입력 테이블
1. `Prices`
   - `product_id`
   - `start_date`
   - `end_date`
   - `price`
2. `UnitsSold`
   - `product_id` 
   - `purchase_date` 
   - `units`

<br/>

### 풀이
#### 1. JOIN 활용(between date, id)
`prices`와 `UnitsSold`를 `customer_id`와 `purchase_date` between `start_date` and `end_date`를 기준으로 조인합니다.

```sql
select p.product_id, p.price * u.units as total, u.units
    from prices p
        left join unitssold u on u.purchase_date
        between p.start_date and p.end_date -- 해당 팔린 날짜에만 
        and u.product_id = p.product_id -- product_id가 같은 것만
```

<br/>


#### 2. 집계함수, null 값 처리
`round(coalesce(sum(total) / sum(units), 0), 2)` 

```sql
select product_id, round(COALESCE(sum(total) / sum(units),0), 2) as average_price 
from temp_01
group by 1
```
