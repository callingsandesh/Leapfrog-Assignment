## Description of the schema present inside the `schema\*.sql`

* `schema\1_main_table.sql`

```
CREATE OR REPLACE VIEW main_table AS
SELECT
        t.employee_id,
        
        d.id as department_id,
        t.punch_in_time::timestamp::time AS shift_start_time,
        t.punch_out_time ::timestamp :: time AS shift_end_time,
        t.punch_apply_time as shift_date,
        t.hours_worked as hours_worked,
        CASE WHEN t.punch_in_time::timestamp::time BETWEEN '5:00' AND '9:00' THEN 'MORNING'
             WHEN t.punch_in_time::timestamp::time BETWEEN '9:00' AND '17:00' THEN 'DAY'
             WHEN t.punch_in_time::timestamp::time BETWEEN '5:00' AND  '23:59' THEN 'NIGHT'
             ELSE NULL
             END as shift_type,
        CASE WHEN t.paycode <> 'ABSENT' THEN 1
             ELSE 0
             END AS attendence ,
        
        CASE WHEN t.paycode = 'BREAK' THEN 1
             ELSE 0
             END as has_taken_break,

        CASE WHEN t.paycode = 'BREAK' THEN t.hours_worked
             ELSE 0
             END as break_hour,
        
        CASE WHEN t.paycode = 'CHARGE' THEN 1
             ELSE 0
             END as was_charge,
        
        CASE WHEN t.paycode = 'CHARGE' THEN t.hours_worked
             ELSE 0
             END  AS charge_hour,
        
        CASE WHEN t.paycode = 'ON_CALL' THEN 1
             ELSE 0
             END as was_on_call,
        CASE WHEN t.paycode = 'ON_CALL' THEN t.hours_worked
             ELSE 0
             END as on_call_hour
        
        
        FROM timesheet t
        INNER JOIN employee e 
            ON t.employee_id = e.employee_id
        INNER JOIN department d
            ON e.department_id = d.client_department_id
```
  
  The above table will cerate a view from the existing raw_tables.
  
  ` SELECT * FROM main_table `
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/1_main_table.png)
  
  
  
  * `schema\2_main_table_agg.sql`
  ```
  CREATE VIEW main_table_agg AS
SELECT 
	agg_main_table.employee_id,agg_main_table.shift_date ,
	SUM(hours_worked) AS "hours_worked",
	sum(has_taken_break) AS "has_taken_break",
	sum(break_hour) AS "break_hour",
	sum(was_charge) AS "was_charge",
	sum(charge_hour) AS "charge_hour",
	sum(was_on_call) AS "was_on_call",
	sum(on_call_hour) AS "on_call_hour"
	
FROM main_table as agg_main_table
GROUP BY agg_main_table.employee_id,agg_main_table.shift_date

  ```
  It will create aggregate of difference columns like hours_worked,has_taken_break,break_hour,was_charge,charge_hour,was_on_call,on_call_hour FROM the `main_table`
  
  `SELECT * FROM main_table_agg`
  
  ![Image](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/2_main_table_agg.png)
  
  
  * `schema\3_array_agg_shift_type.sql`
  
  ```
  CREATE VIEW agg_shift AS
select employee_id,shift_date,array_agg(shift_type) AS shift_type
from main_table 
group by employee_id,shift_date
  ```
 
 It will create the array of aggregates of shift types from the column by grouping by the employee_id and shift_date
  
  `SELECT * FROM agg_shift`
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/3_array_agg_shift_type.png)
  
  
  
  * `schema\4_attendence_view.sql`
  
  ```
  CREATE OR REPLACE VIEW attendence_view AS 
	SELECT 
	DISTINCT main_table.employee_id,shift_date,
	attendence
	FROM main_table
  ```
  `SELECT * FROM attendence_view`
  
  ![Image](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/4_attendence_view.png)
  
  
  
  * `schema\5_department_view.sql`
  ```
  CREATE VIEW department_view AS
	SELECT attendence_view.employee_id,attendence_view.shift_date,attendence_view.attendence,d.id as department_id
	FROM attendence_view
	INNER JOIN employee e
 		ON attendence_view.employee_id = e.employee_id
	INNER JOIN department d
		ON e.department_id = d.client_department_id
  ```
  `SELECT * FROM department_view`
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/5_department_view.png)
  
  
  
  * `schema\6_num_teammates_absent.sql`
  ```CREATE VIEW num_teammate_absent AS
	SELECT 
	demo.shift_date,demo.department_id,COUNT(*)-SUM(attendence) AS num_teammates_absent
	FROM (
	SELECT attendence_view.employee_id,attendence_view.shift_date,attendence_view.attendence,d.id as department_id
	FROM attendence_view
	INNER JOIN employee e
 		ON attendence_view.employee_id = e.employee_id
	INNER JOIN department d
		ON e.department_id = d.client_department_id
	) AS demo
	GROUP BY demo.shift_date,demo.department_id
  ```
  `SELECT * FROM num_teammate_absent`
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/6_num_teammates_absent.png)
  
  

  
  
  * `schema\7_semi_final_view.sql`
  ```
  CREATE VIEW semi_final_table AS
  SELECT 
	mt.employee_id,
	d.department_id,
	mt.shift_date,
	agg_shift.shift_type,
	mt.hours_worked,
	d.attendence,
	mt.has_taken_break,
	mt.break_hour,
	mt.was_charge,
	mt.charge_hour,
	mt.was_on_call,
	mt.on_call_hour,
	num_teammate_absent.num_teammates_absent 

FROM main_table_agg mt
INNER JOIN department_view d
	ON (mt.employee_id,mt.shift_date)=(d.employee_id,d.shift_date)
INNER JOIN agg_shift
	ON (mt.employee_id,mt.shift_date) = (agg_shift.employee_id,agg_shift.shift_date)
LEFT JOIN num_teammate_absent 
	ON (mt.shift_date,d.department_id) = (num_teammate_absent.shift_date,num_teammate_absent.department_id)
  ```
  `SELECT * FROM semi_final_view`
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/7_semi_final_view.png)
  
  
  * `schema\8_array_agg_shift_times.sql`
  ```
  CREATE VIEW array_agg_shift_times AS
	SELECT employee_id,shift_date,array_agg(shift_start_time) AS shift_start_time,array_agg(shift_end_time) AS 	   shift_end_time
	FROM main_table
	GROUP BY employee_id,shift_date
  ```
  `SELECT * FROM array_agg_shift_times`
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/8_arr_shift_times.png)
  
    * `schema\9_final_table.sql`
  ```
CREATE VIEW final_table AS
SELECT 
mt.employee_id,
mt.department_id,
ag.shift_start_time,
ag.shift_end_time,
mt.shift_date,
mt.shift_type,
mt.hours_worked,
mt.attendence,
mt.has_taken_break,
mt.break_hour,
mt.was_charge,
mt.charge_hour,
mt.was_on_call,
mt.on_call_hour,
mt.num_teammates_absent 
FROM semi_final_table mt
INNER JOIN array_agg_shift_times ag
	ON (mt.employee_id,mt.shift_date) = (ag.employee_id,ag.shift_date)
  ```
  `SELECT * FROM final_table`
  
  ![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/elt-day4/Data/3rd%20Week(OLAP%20Design)/Day4/docs/SS%20of%20tables/9_final_table.png)
