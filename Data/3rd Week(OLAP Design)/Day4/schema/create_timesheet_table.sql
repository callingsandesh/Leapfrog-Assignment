CREATE TABLE timesheet(
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(255), 
    department_id INTEGER,
    shift_start_time VARCHAR(50),
    shift_end_time VARCHAR(50),
    shift_date VARCHAR(255),
    shift_type VARCHAR(255),
    hours_woked FLOAT,
    attendence VARCHAR(50),
    has_taken_break BOOLEAN,
    break_hour FLOAT,
    was_charge BOOLEAN,
    charge_hour FLOAT,
    was_on_call BOOLEAN,
    on_call_hour FLOAT,
    num_teammates_absent SMALLINT,

    CONSTRAINT fk_timesheet_department_department_id
    FOREIGN KEY(department_id) REFERENCES department(id)

);