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
	e.was_on_call,
	e.on_call_hour as on_call_hours,
	e.num_teammates_absent

FROM timesheet_warehouse e