--FINAL TABLE
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
