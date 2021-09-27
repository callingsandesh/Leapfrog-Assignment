INSERT INTO dim_shift_type(name)
SELECT DISTINCT shift_type
FROM timesheet_warehouse t