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