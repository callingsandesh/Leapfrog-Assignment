--Creating timesheet table
CREATE TABLE timesheet(
    employee_id VARCHAR(7),
    cost_center CHAR(5),
    punch_in_time TIMESTAMP,
    punch_out_time TIMESTAMP,
    punch_apply_time DATE,
    hours_worked NUMERIC(3,1),
    paycode VARCHAR(7)
);