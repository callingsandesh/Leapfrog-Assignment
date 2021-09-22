create table employee(
	client_employee_id VARCHAR(255),
	department_id VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	manager_employee_id VARCHAR(255),
	salary FLOAT,
	hire_date TIMESTAMP,
	term_date VARCHAR(255),
	term_reason VARCHAR(255),
	dob TIMESTAMP,
	fte FLOAT,
	fte_status VARCHAR(255),
	weekly_hours smallint,
	role VARCHAR(255),
	is_active BOOLEAN
)