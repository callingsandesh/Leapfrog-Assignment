CREATE VIEW num_teammate_absent AS
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
