INSERT INTO dim_manager(client_employee_id,first_name,last_name,salary)
SELECT DISTINCT mgr.employee_id,mgr.first_name,mgr.last_name,mgr.salary
FROM employee e
JOIN employee mgr
	ON e.manager_employee_id = mgr.employee_id