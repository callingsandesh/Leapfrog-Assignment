I have used the schema to inside the `schema\*.sql` to create all the tables.
The datas are inside the `data\*.csv`.
I have used the pipeline inside `src\pipelne\extract_csv_files_into_database_tables.py`to populate the date inside the tables created, with the help of function inside `utils.py` and `helper.py`.

### The test script of the given test cases are:
### Check if a single employee is listed twice with multiple ids.

```
--Here I assume that the client has different full_names,hire_date and dob
SELECT
	CASE
		WHEN S.TOTAL_NAMES = 1 THEN 'PASS'
		ELSE 'FAIL'
	END AS TOTAL_RESULT,
		COUNT(*)
FROM
	(
	SELECT
		CONCAT(FIRST_NAME, ' ', LAST_NAME),
		HIRE_DATE,
		DOB,
		COUNT(*) AS TOTAL_NAMES,
		CASE
			WHEN COUNT(*)>1 THEN 'FAILED'
			ELSE 'PASS'
		END AS TEST_RESULT
	FROM
		EMPLOYEE
	GROUP BY
		CONCAT(FIRST_NAME, ' ', LAST_NAME),
		HIRE_DATE,
		DOB) AS S
GROUP BY
	TOTAL_RESULT
```
|total_result|count|
|------------|-----|
|PASS|30|



### Check if part time employees are assigned other fte_status.

```
with cte_status as (SELECT CASE WHEN fte=1 THEN 'Full Time' 
		   ELSE 'Part Time'
		   END AS term_status,
		   fte_status
		   FROM employee
) select case when term_status=fte_status then 'correct'
		 else 'part_time_employees_assigned_as full time'
		 end as c,COUNT(*)
from cte_status
group by c
```
|c|count|
|-|-----|
|part_time_employees_assigned_as full time|6|
|correct|24|




### Check if termed employees are marked as active.

```
with cte_term_status AS(
	SELECT CASE WHEN TERM_DATE='' THEN TRUE 
		   ELSE FALSE
		   END AS term_status,
		   is_active
		 from employee
)
select case when term_status = is_active then 'CORRECT'
		else 'INCORRECT'
		end as label,
		COUNT(*)
from cte_term_status
group by label
```
|label|count|
|-----|-----|
|CORRECT|30|



### Check if the same product is listed more than once in a single bill.


```
select case when c.product_listed_in_bill = 1 then 'PASS'
	   else 'FAIL'
	   end as result,
COUNT(*)
FROM(
select bill_no,product_id,COUNT(*) as product_listed_in_bill
from SALES   
group by bill_no,product_id
) as c
group by result
```
|result|count|
|------|-----|
|PASS|915|



### Check if the customer_id in the sales table does not exist in the customer table.
```
select COUNT(*) as impacted_record_count,
		case when COUNT(*)>0 THEN 'Failed'
		else 'Passed'
		end as test_status
FROM(
select distinct customer_id from sales s 
except 
select customer_id from customer
)as result;
```
|impacted_record_count|test_status|
|---------------------|-----------|
|0|Passed|




### Check if there are any records where updated_by is not empty but updated_date is empty.


```
select COUNT(*) as Failed
FROM(
select updated_by,updated_date from SALES
where updated_by !=''  and updated_date is null
) R
```
|failed|
|------|
|57|



### Check if there are any hours worked that are greater than 24 hours.


```
select count(*) as Total_count_more_than_24hr_work
FROM(
select * from timesheet
where hours_worked>24
) as result;

```
|total_count_more_than_24hr_work|
|-------------------------------|
|0|




### Check if non on-call employees are set as on-call.


```
select 
COUNT(*) as impacted_record_count,
case when COUNT(*)>0 THEN 'failed'
	else 'passed'
	end as test_status
from timesheet t  
inner join timesheet_raw tr 
on t.employee_id =tr.employee_id 
and t.shift_date =tr.punch_apply_time
and tr.paycode !='ON_CALL'
and t.was_on_call =true
```
|impacted_record_count|test_status|
|---------------------|-----------|
|176|failed|





### Check if the break is true for employees who have not taken a break at all.

```
select 
COUNT(*) as impacted_record_count,
case when COUNT(*)>0 THEN 'failed'
	else 'passed'
	end as test_status
from timesheet t  
inner join timesheet_raw tr 
on t.employee_id =tr.employee_id 
and t.shift_date =tr.punch_apply_time
and tr.paycode !='BREAK'
and t.has_taken_break =true
```
|impacted_record_count|test_status|
|---------------------|-----------|
|523|failed|





### Check if the night shift is not assigned to the employees working on the night shift.

```
```


