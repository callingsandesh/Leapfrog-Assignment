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
