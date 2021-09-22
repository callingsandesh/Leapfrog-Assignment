## Customer
1. Checking if the manager employee is not in the employee id.
```
select COUNT(*) as total_impacted_records,
       case when COUNT(*)>0 then 'failed'
       else 'passed'
       end as results
       FROM(

select distinct(manager_employee_id) from employee where manager_employee_id !=''
except
select client_employee_id from employee
) R
```
|total_impacted_records|results|
|----------------------|-------|
|0|passed|


2. checking if the hire_date of the employee is in the future
```
select count(*) total_impacted_count,
	case when count(*)>0 then 'failed'
	else 'pass'
	end as c
FROM(
select hire_date from employee e 
where hire_date > localtimestamp 
)result

```
|total_impacted_count|c|
|--------------------|-|
|0|pass|


3. checking if the manager has the  role not as manager
```
select COUNT(*) as total_impacted_count,
		case when COUNT(*)>0 then 'failed'
		else 'pass'
		end c
from(
select 
 distinct m.client_employee_id,m.role
from employee e 
inner join employee m 
 on e.manager_employee_id  = m.client_employee_id 
where 
m.role !='Manager'
 )R
```
|total_impacted_count|c|
|--------------------|-|
|0|pass|



4.  Checking if the weekly_hours is less than fte
```
 with cte_check as (
 select fte*40 as fte_hours_weekly,weekly_hours 
 from employee
 )
select COUNT(*) as total_impacted_weekly_hours_rows
from
cte_check
WHERE
fte_hours_weekly < weekly_hours
```

## Timesheet
1. checking if the total hours_worked has excluded break_hour
```
with cte_hours as ( 
select extract(hours from shift_end_time -shift_start_time) total_hours ,hours_worked -break_hour as worked_hours
from timesheet t 
)
select COUNT(*) as total_impacted_count,
		case when count(*)>0 then 'failed'
		else 'passed'
		end as label
from cte_hours
where total_hours <worked_hours and total_hours is not null
```
|total_impacted_count|label|
|--------------------|-----|
|0|passed|


2. checking if the employees has shift_in_time  when he/she is absent.
```
select COUNT(*) as total_impacted_count,
       case when COUNT(*)>0 then 'Failed'
       else 'Passed'
       end as label
from timesheet t 
where attendance =false and shift_start_time != NULL
```
|total_impacted_count|label|
|--------------------|-----|
|0|Passed|


3. checking if the employee has different department_id through out the timesheet
```
select case when count>1 then 'failed'
       else 'passed'
       end as label,count(*) as total_employee
from (
with cte_e_d as (
select distinct employee_id ,department_id ,
COUNT(*) over (partition by employee_id,department_id) as ccc
from timesheet t
)
select employee_id,COUNT(*)
from cte_e_d
group by employee_id
)r
group by label
```
|label|total_employee|
|-----|--------------|
|passed|29|

4. cheking if the employee has break more than 1 hours
```
select COUNT(*) as total_employee_count from timesheet t 
where break_hour >=1

```
|total_employee_count|
|--------------------|
|15|

5. checking if the on_call employee has attendence as false
```
select COUNT(*) as total_impacted_count from timesheet t 
where t.was_on_call =true and t.attendance = False

```
|total_impacted_count|
|--------------------|
|0|

## Products

1.  checking if the same product is listed twice and deleting it before proceeding to another test cases
```
delete from product p1 USING(
	select MIN(product_id) as pid,product_name
	from product
	group by product_name 
	having COUNT(*)>1
)p2
where p1.product_name=p2.product_name
and p1.product_id <> pid
```
2. check if the price is greater than mrp
```
select COUNT(*) as total_impacted_product from product
where price>mrp

--2)checking if the brand has less than 5 products
select COUNT(*) as total_brand_count_less_than_5
from (
select brand,COUNT(*) as ct from product p 
group by brand
having COUNT(*)<5
)r
```
|total_brand_count_less_than_5|
|-----------------------------|
|4|


3. checking if the peices is less that 10
```
select COUNT(*) as total_product_count__pieces_less_than_5
from (
select pieces_per_case,COUNT(*) as pc from product p 
group by pieces_per_case
having COUNT(*)<10
)r
```
|total_product_count__pieces_less_than_5|
|---------------------------------------|
|23|

4. checking if the weight of the product is 0

```
select COUNT(*) total_impacted_count
from product p 
where weight_per_piece <=0

```
|total_impacted_count|
|--------------------|
|0|


## Sales

1. checking if the created_by and updated_by are different person
```

select COUNT(*) as total_impacted_count from sales
where LOWER(created_by) != lower(updated_by) 
AND updated_by !=NULL and updated_by != NULL
```
|total_impacted_count|
|--------------------|
|18|


2. checking if the same bill_no is associated with different time or customer.
```
with cte_bill as (
select bill_no,COUNT(*) as bill_count FROM(
select distinct bill_no,bill_date,customer_id,COUNT(*) from sales s 
group by bill_no,bill_date,customer_id
)r
group by bill_no
) select COUNT(*)
from cte_bill
where bill_count>1
```
|count|
|-----|
|80|


3. checking if the total_net_bill amount is not equal to gross_price  + tax_amount 
```
select COUNT(*) as total_impacted_count
from sales
where gross_price+tax_amount <> net_bill_amt 
```
|total_impacted_count|
|--------------------|
|0|

