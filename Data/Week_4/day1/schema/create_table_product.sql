CREATE TABLE product(
	product_id INTEGER PRIMARY KEY,
	product_name VARCHAR(255),
	description TEXT,
	price FLOAT,
	mrp FLOAT,
	pieces_per_case FLOAT,
	weight_per_piece FLOAT,
	uom VARCHAR(255),
	brand VARCHAR,
	category VARCHAR,
	tax_percent INTEGER,
	active VARCHAR(255),
	created_by VARCHAR(255),
	created_date TIMESTAMP,
	updated_by VARCHAR(255),
	updated_date TIMESTAMP
)