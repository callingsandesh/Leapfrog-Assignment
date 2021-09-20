CREATE TABLE dim_customer(
	customer_id INTEGER PRIMARY KEY,
	user_name VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	country VARCHAR(255),
	town VARCHAR(255),
	active CHAR
);