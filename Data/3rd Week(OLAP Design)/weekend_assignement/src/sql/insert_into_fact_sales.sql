SELECT 
	sales_dump.id,
	transaction_id,
	bill_no,
	CASE WHEN bill_date='2017-02-30 11:00:00' THEN TO_TIMESTAMP('2017-02-28 11:00:00','YYYY-MM-DD HH24:MI:SS')
	     ELSE TO_TIMESTAMP(bill_date,'YYYY-MM-DD HH24:MI:SS')
		 END bill_date_corrected,
	bill_location,
	CAST(customer_id AS INT),
	CAST(product_id AS INT),
	CAST(qty AS INT),
	dim_uom.id,
	CAST(price AS FLOAT),
	CAST(gross_price AS FLOAT),
	CAST(tax_pc AS FLOAT),
	CAST(tax_amount AS FLOAT),
	CAST(discount_pc AS FLOAT),
	CAST(discount_amt AS FLOAT),
	CAST(net_bill_amt AS FLOAT),
	created_by,
	updated_by,
	CASE WHEN created_date='2017-02-30 11:00:00' THEN TO_TIMESTAMP('2017-02-28 11:00:00','YYYY-MM-DD HH24:MI:SS')
	     ELSE TO_TIMESTAMP(created_date,'YYYY-MM-DD HH24:MI:SS')
		 END created_date_corrected,
	CASE WHEN updated_date='2017-02-30 11:00:00' THEN TO_TIMESTAMP('2017-02-28 11:00:00','YYYY-MM-DD HH24:MI:SS')
	     WHEN updated_date='-' THEN NULL
	     ELSE TO_TIMESTAMP(updated_date,'YYYY-MM-DD HH24:MI:SS')
		 END updated_date_corrected
FROM sales_dump
INNER JOIN dim_uom
	ON sales_dump.uom=dim_uom.type