CREATE VIEW department_view AS
SELECT attendence_view.employee_id,attendence_view.shift_date,attendence_view.attendence,d.id as department_id
FROM attendence_view
INNER JOIN employee e
 	ON attendence_view.employee_id = e.employee_id
INNER JOIN department d
	ON e.department_id = d.client_department_id
