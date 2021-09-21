create table timesheet(
	employee_id VARCHAR(255),
	department_id VARCHAR(255),
	shift_start_time VARCHAR(255),
	shift_end_time VARCHAR(255),
	shift_date DATE,
	shift_type VARCHAR(255),
	hours_worked FLOAT,
	attendence BOOLEAN,
	has_taken_break BOOLEAN,
	break_hour FLOAT,
	was_charge BOOLEAN,
	charge_hour FLOAT,
	was_on_call BOOLEAN,
	on_call_hour FLOAT,
	num_teammates_absent SMALLINT
)