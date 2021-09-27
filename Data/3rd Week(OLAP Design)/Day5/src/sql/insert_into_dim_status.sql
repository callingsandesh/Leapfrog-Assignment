INSERT INTO dim_status(name)
SELECT 
 DISTINCT CASE WHEN terminated_date='01-01-1700' THEN 'active'
	      ELSE 'terminated'
	      END as active_statue
FROM employee