CREATE VIEW agg_shift AS
select employee_id,shift_date,array_agg(shift_type) AS shift_type
from main_table 
group by employee_id,shift_date
