CREATE OR REPLACE VIEW attendence_view AS 
SELECT 
DISTINCT main_table.employee_id,shift_date,
attendence
FROM main_table
