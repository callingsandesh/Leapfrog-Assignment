CREATE TABLE fact_sales(
	id SERIAL PRIMARY KEY,
	client_sales_id VARCHAR(255),
	transaction_id VARCHAR(255),
	bill_no VARCHAR(255),
	bill_date TIMESTAMP,
	bill_location VARCHAR(255),
	customer_id INTEGER,
	product_id INTEGER,
	qty SMALLINT,
	uom_id INTEGER,
	price FLOAT,
	gross_price FLOAT,
	tax_pc FLOAT,
	tax_amount FLOAT,
	discount_pc FLOAT,
	discount_amt FLOAT,
	net_bill_amt FLOAT,
	created_by VARCHAR,
	updated_by VARCHAR(255),
	created_date VARCHAR(255),
	updated_date VARCHAR(255),
	
	CONSTRAINT fk_fact_sales_customer_customer_id
	FOREIGN KEY(customer_id) REFERENCES dim_customer(customer_id),
	
	CONSTRAINT fk_fact_sales_product_product_id
	FOREIGN KEY(product_id) REFERENCES fact_product(product_id),
	
	CONSTRAINT fk_fact_sales_uom_uom_id 
	FOREIGN KEY(uom_id) REFERENCES dim_uom(id)
)