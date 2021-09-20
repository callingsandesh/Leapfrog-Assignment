CREATE TABLE fact_sales_product(
	id SERIAL PRIMARY KEY,
	date DATE,
	product_id INTEGER,
	total_quantity FLOAT,
	price FLOAT,
	total_gross_price FLOAT,
	total_discount_amt FLOAT,
	total_customers SMALLINT,
	total_tax_amount FLOAT,
	total_new_bill_amount FLOAT,

	CONSTRAINT fk_fact_sales_product
	FOREIGN KEY(product_id) REFERENCES fact_product(product_id)
);