--creating table sales
CREATE TABLE sales(
    user_id INTEGER,
    username VARCHAR(45) NOT NULL,
    product_id INTEGER,
    category_id INTEGER,
    category_name VARCHAR(45),
    current_price DOUBLE PRECISION NOT NULL,
    sold_price DOUBLE PRECISION,
    sold_quantity INTEGER,
    remaining_quantity INTEGER,
    sales_date TIMESTAMP

);