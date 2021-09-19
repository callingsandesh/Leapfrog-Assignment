--This is a view

CREATE OR REPLACE VIEW main_table AS
SELECT
        t.employee_id,
        
        d.id as department_id,
        t.punch_in_time::timestamp::time AS shift_start_time,
        t.punch_out_time ::timestamp :: time AS shift_end_time,
        t.punch_apply_time as shift_date,
        t.hours_worked as hours_worked,
        CASE WHEN t.punch_in_time::timestamp::time BETWEEN '5:00' AND '9:00' THEN 'MORNING'
             WHEN t.punch_in_time::timestamp::time BETWEEN '9:00' AND '17:00' THEN 'DAY'
             WHEN t.punch_in_time::timestamp::time BETWEEN '5:00' AND  '23:59' THEN 'NIGHT'
             ELSE NULL
             END as shift_type,
        CASE WHEN t.paycode <> 'ABSENT' THEN 1
             ELSE 0
             END AS attendence ,
        
        CASE WHEN t.paycode = 'BREAK' THEN 1
             ELSE 0
             END as has_taken_break,

        CASE WHEN t.paycode = 'BREAK' THEN t.hours_worked
             ELSE 0
             END as break_hour,
        
        CASE WHEN t.paycode = 'CHARGE' THEN 1
             ELSE 0
             END as was_charge,
        
        CASE WHEN t.paycode = 'CHARGE' THEN t.hours_worked
             ELSE 0
             END  AS charge_hour,
        
        CASE WHEN t.paycode = 'ON_CALL' THEN 1
             ELSE 0
             END as was_on_call,
        CASE WHEN t.paycode = 'ON_CALL' THEN t.hours_worked
             ELSE 0
             END as on_call_hour
        
        
        FROM timesheet t
        INNER JOIN employee e 
            ON t.employee_id = e.employee_id
        INNER JOIN department d
            ON e.department_id = d.client_department_id
	
