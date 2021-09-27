INSERT INTO dim_role(name) 
SELECT DISTINCT employee_role FROM employee