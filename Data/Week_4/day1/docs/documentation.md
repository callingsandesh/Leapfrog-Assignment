I have used the schema to inside the `schema\*.sql` to create all the tables.
The datas are inside the `data\*.csv`.
I have used the pipeline inside `src\pipelne\extract_csv_files_into_database_tables.py`to populate the date inside the tables created, with the help of function inside `utils.py` and `helper.py`.

### The test script of the given test cases are:
> Check if a single employee is listed twice with multiple ids.

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



> Check if part time employees are assigned other fte_status.

```
SELECT COUNT(*) AS IMPACTED_RECORD_COUNT,
	CASE 
		WHEN COUNT(*)>0 THEN 'FAILED'
		ELSE 'PASSED'
		END AS TEST_RESULT
FROM((

	SELECT CASE WHEN fte=1 THEN 'Full Time' 
		   ELSE 'Part Time'
		   END AS TERM_STATUS
FROM EMPLOYEE
UNION
SELECT fte_status FROM EMPLOYEE)
EXCEPT(
SELECT fte_status FROM EMPLOYEE
INTERSECT
SELECT CASE WHEN fte=1 THEN 'Full Time' 
		   ELSE 'Part Time'
		   END AS TERM_STATUS
FROM EMPLOYEE
)
)RESULT;
```

> Check if termed employees are marked as active.

```
SELECT COUNT(*) AS IMPACTED_RECORD_COUNT,
	CASE 
		WHEN COUNT(*)>0 THEN 'FAILED'
		ELSE 'PASSED'
		END AS TEST_RESULT
FROM(

	SELECT CASE WHEN TERM_DATE='' THEN TRUE 
		   ELSE FALSE
		   END AS TERM_STATUS
FROM EMPLOYEE
EXCEPT 
SELECT IS_ACTIVE FROM EMPLOYEE
)RESULT;


--with CTE
WITH cte_term_status AS(
SELECT CASE WHEN TERM_DATE='' THEN TRUE 
		   ELSE FALSE
		   END AS TERM_STATUS
FROM EMPLOYEE
)
select * from cte_term_status
EXCEPT 
select is_active from employee
```


> Check if the same product is listed more than once in a single bill.


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

> Check if the customer_id in the sales table does not exist in the customer table.

```
select COUNT(*) as total_fail
FROM(
select distinct customer_id from sales s 
except 
select customer_id from customer
)as result;
```

> Check if there are any records where updated_by is not empty but updated_date is empty.


```
select updated_by,updated_date from SALES
where updated_by is not NULL  and updated_date is null
```

> Check if there are any hours worked that are greater than 24 hours.


```
select count(*) as Total_count_more_than_24hr_work
FROM(
select * from timesheet
where hours_worked>24
) as result;

```

> Check if non on-call employees are set as on-call.


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

> Check if the break is true for employees who have not taken a break at all.


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

> Check if the night shift is not assigned to the employees working on the night shift.

```
```


