CREATE VIEW main_table_agg AS
SELECT 
	agg_main_table.employee_id,agg_main_table.shift_date ,
	SUM(hours_worked) AS "hours_worked",
	sum(has_taken_break) AS "has_taken_break",
	sum(break_hour) AS "break_hour",
	sum(was_charge) AS "was_charge",
	sum(charge_hour) AS "charge_hour",
	sum(was_on_call) AS "was_on_call",
	sum(on_call_hour) AS "on_call_hour"
	
FROM main_table as agg_main_table
GROUP BY agg_main_table.employee_id,agg_main_table.shift_date
