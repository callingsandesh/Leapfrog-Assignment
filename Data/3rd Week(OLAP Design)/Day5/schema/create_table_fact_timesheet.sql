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