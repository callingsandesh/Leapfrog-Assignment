CREATE TABLE fact_product(
	product_id INTEGER PRIMARY KEY,
	product_name VARCHAR(255),
	description TEXT,
	price FLOAT,
	mrp FLOAT,
	pieces_per_case FLOAT,
	weight_per_piece FLOAT,
	uom_id INTEGER,
	brand_id INTEGER,
	category_id INTEGER,
	tax_percent INTEGER,
	product_status_id INTEGER,
	created_by VARCHAR(255),
	created_date TIMESTAMP,
	updated_by VARCHAR(255),
	updated_date TIMESTAMP,
	
	CONSTRAINT fk_fact_product_dim_uom
	FOREIGN KEY(uom_id) REFERENCES dim_uom(id),
	CONSTRAINT fk_fact_product_dim_brand
	FOREIGN KEY(brand_id) REFERENCES dim_brand(id),
	CONSTRAINT fk_fact_product_dim_category
	FOREIGN KEY(category_id) REFERENCES dim_category(id),
	CONSTRAINT fk_fact_product_dim_status
	FOREIGN KEY(product_status_id) REFERENCES dim_status(id)
);