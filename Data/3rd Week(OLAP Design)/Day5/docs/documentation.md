#Proposed ER model of the warehouse
![Image](https://github.com/callingsandesh/Leapfrog-Assignment/blob/ETL-Day5/Data/3rd%20Week(OLAP%20Design)/Day5/docs/warehouse(employee%20and%20timesheet).png )

#  I will describe all the table table creation and respective code to insert the data into the table.
> `schema\create_table_dim_department.sql
```
CREATE TABLE dim_department(
    id SERIAL PRIMARY KEY,
    client_department_id VARCHAR(255),
    department_name VARCHAR(255)

);
```
Used the following query to insert the data from the dump database.
``

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
``

> `schema\create_table_dim_period.sql`
```
CREATE TABLE dim_period (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE
)
```
Used the following query to insert the data from the dump database.
`INSERT INTO dim_department(client_department_id,department_name)
SELECT DISTINCT department_id,department_name
FROM employee`

> `schema\create_table_dim_role.sql`
```
CREATE TABLE dim_role (
    role_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
```
Used the following query to insert the data from the dump database.
``

> `schema\create_table_dim_shift_type.sql`
```
CREATE TABLE dim_shift_type(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255)
)
```
Used the following query to insert the data from the dump database.
``

> `schema\create_table_dim_status.sql`
```
CREATE TABLE dim_status (
    status_id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
```
Used the following query to insert the data from the dump database.
``

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
``

> `schema\create_table_fact_timesheet.sql`
```
CREATE TABLE fact_employee(
    employee_id INTEGER,
    work_date DATE,
    department_id VARCHAR(255),
    hours_worked FLOAT,
    shift_type_id INTEGER,
    punch_in_time DATE,
    punch_out_time DATE,
    time_period_id INTEGER,
    attendence BOOLEAN,
    work_code VARCHAR(255),
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
Used the following query to insert the data from the dump database.
``

