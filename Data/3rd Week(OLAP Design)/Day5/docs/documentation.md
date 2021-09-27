# Proposed ER model of the warehouse
![Image](https://github.com/callingsandesh/Leapfrog-Assignment/blob/ETL-Day5/Data/3rd%20Week(OLAP%20Design)/Day5/docs/warehouse(employee%20and%20timesheet)_1.png )

#  I will describe all the  table creation and respective code to insert the data into the table.
> `schema\create_table_dim_department.sql
```
CREATE TABLE dim_department(
    id SERIAL PRIMARY KEY,
    client_department_id VARCHAR(255),
    department_name VARCHAR(255)

);
```
Used the following query to insert the data from the dump database.
```
INSERT INTO dim_department(client_department_id,department_name)
SELECT DISTINCT department_id,department_name
FROM employee
```

> `schema\create_table_dim_manager.sql`
```
CREATE TABLE dim_manager(
	id SERIAL PRIMARY KEY,
	client_employee_id VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	salary FLOAT
	
);
```
Used the following query to insert the data from the dump database.
```
INSERT INTO dim_manager(client_employee_id,first_name,last_name,salary)
SELECT DISTINCT mgr.employee_id,mgr.first_name,mgr.last_name,mgr.salary
FROM employee e
JOIN employee mgr
	ON e.manager_employee_id = mgr.employee_id
```

> `schema\create_table_dim_period.sql`
```
CREATE TABLE dim_period (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE
)
```
Used the following query to insert the data from the dump database.
```
```

> `schema\create_table_dim_role.sql`
```
CREATE TABLE dim_role (
    role_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
```
Used the following query to insert the data from the dump database.
```
INSERT INTO dim_role(name) 
SELECT DISTINCT employee_role FROM employee
```

> `schema\create_table_dim_shift_type.sql`
```
CREATE TABLE dim_shift_type(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255)
)
```
Used the following query to insert the data from the dump database.
```
INSERT INTO dim_shift_type(name)
SELECT DISTINCT shift_type
FROM timesheet_warehouse t
```

> `schema\create_table_dim_status.sql`
```
CREATE TABLE dim_status (
    status_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
```
Used the following query to insert the data from the dump database.
```
INSERT INTO dim_status(name)
SELECT 
 DISTINCT CASE WHEN terminated_date='01-01-1700' THEN 'active'
	      ELSE 'terminated'
	      END as active_statue
FROM employee
```

> `schema\create_table_fact_employee.sql`
```
CREATE TABLE fact_employee(
    employee_id SERIAL PRIMARY KEY,
    client_employee_id VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department_id VARCHAR(255),
    manager_id VARCHAR(255),
    salary FLOAT,
    hire_date DATE,
    term_date VARCHAR(255),
    term_reason VARCHAR(255),
    dob DATE,
    role_id INTEGER,
    active_status_id INTEGER,
    weekly_hours FLOAT
);
```
Used the following query to insert the data from the dump database.
```

INSERT INTO fact_employee(client_employee_id,first_name,last_name,department_id,manager_id,salary,hire_date,term_date,term_reason,dob,role_id,active_status_id,weekly_hours)
SELECT
	e.employee_id,
	e.first_name,
	e.last_name,
	d.id as department_id,
	mgr.id as manager_id,
	e.salary,
	e.hire_date,
	CASE WHEN e.terminated_date = '01-01-1700' THEN NULL
		 ELSE e.terminated_date
		 END as term_date,
	
	e.terminated_reason as term_reason,
	e.dob,
	r.role_id as role_id,
	CASE WHEN e.terminated_date = '01-01-1700' THEN 1
		 ELSE 2
		 END as active_status_id,
	CAST(fte AS FLOAT)*40 AS weekly_hours
FROM employee e
INNER JOIN dim_role r
	ON e.employee_role = r.name
INNER JOIN dim_department d
	ON e.department_id = d.client_department_id
LEFT JOIN dim_manager mgr
	ON e.manager_employee_id = mgr.client_employee_id
```

> `schema\create_table_fact_timesheet.sql`
```
CREATE TABLE fact_timesheet(
    employee_id INTEGER,
    work_date DATE,
    department_id VARCHAR(255),
    hours_worked FLOAT,
    shift_type_id INTEGER,
    punch_in_time DATE,
    punch_out_time DATE,
    time_period_id INTEGER,
    attendence BOOLEAN,
    has_taken_break BOOLEAN,
    break_hour FLOAT,
    was_charge BOOLEAN,
    charge_hour FLOAT,
    was_on_call BOOLEAN,
    on_call_hours FLOAT,
    is_weekend VARCHAR,
    num_teammates_absent SMALLINT

)
```


I have already made the timesheet_warehouse from previous day,which i will use to fetch the necessary data after and insert into the fact_timesheet after some procession.

### A glimpse of timesheet_warehouse table.

![Image ](https://github.com/callingsandesh/Leapfrog-Assignment/blob/ETL-Day5/Data/3rd%20Week(OLAP%20Design)/Day5/docs/timesheet_warehouse.png )
```
INSERT INTO fact_timesheet(employee_id,work_date,department_id,hours_worked,shift_type_id,punch_in_time,punch_out_time,attendence,has_taken_break,break_hour,was_charge,charge_hour,was_on_call,on_call_hours,is_weekend,num_teammates_absent)
SELECT 
	e.employee_id,
	e.shift_date as work_date,
	e.department_id,
	CASE WHEN e.attendence='0' THEN 0
		 ELSE e.hours_woked
		 END as hours_worked,
	CASE WHEN e.shift_type = NULL THEN 1
		 WHEN e.shift_type ='Morning' THEN 2
		 ELSE 3
		 END as shift_type_id,
	CASE WHEN e.shift_start_time = '[None]' THEN NULL
		 ELSE TO_TIMESTAMP(e.shift_start_time,'HH24:MI:SS')
		 END as punch_in_time,
	CASE WHEN e.shift_end_time = '[None]' THEN NULL
		 ELSE TO_TIMESTAMP(e.shift_end_time,'HH24:MI:SS')
		 END as punch_out_time,
	e.attendence,
	e.has_taken_break,
	e.break_hour,
	e.was_charge,
	e.charge_hour,
	e.was_on_call,
	e.on_call_hour as on_call_hours,
	extract('week' from current_date) as week;
	e.num_teammates_absent

FROM timesheet_warehouse e
```
