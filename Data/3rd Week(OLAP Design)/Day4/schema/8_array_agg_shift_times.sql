CREATE VIEW array_agg_shift_times AS
SELECT employee_id,shift_date,array_agg(shift_start_time) AS shift_start_time,array_agg(shift_end_time) AS shift_end_time
from main_table
GROUP BY employee_id,shift_date
