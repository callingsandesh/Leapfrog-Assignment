INSERT INTO fact_sales_product(date,product_id,total_quantity,price,total_gross_price,total_discount_amt,total_customers,total_tax_amount,total_new_bill_amount)
SELECT 
    CASE WHEN bill_date='2017-02-30 11:00:00' THEN DATE(TO_TIMESTAMP('2017-02-28 11:00:00','YYYY-MM-DD'))
	     ELSE DATE(TO_TIMESTAMP(bill_date,'YYYY-MM-DD'))
	     END AS date,
    product_id ,
	SUM(CAST(qty AS INT)) AS total_quantity,
	ROUND(AVG(CAST(price AS FLOAT))::NUMERIC,2) AS price, 
	ROUND(SUM(CAST(gross_price AS FLOAT))::NUMERIC,2) AS total_gross_price,
	SUM(CAST(discount_amt AS FLOAT)) AS total_discount_amt,
	COUNT(customer_id) AS total_customers,
	ROUND(sum(CAST(tax_amount AS FLOAT))::NUMERIC,2) AS total_tax_amount,
	ROUND(sum(CAST(net_bill_amt AS FLOAT))::NUMERIC,2) AS total_new_bill_amount
FROM sales_dump
GROUP BY date,product_id
ORDER BY date ASC , total_new_bill_amount DESC