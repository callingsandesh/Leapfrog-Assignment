INSERT INTO dim_status(type)
SELECT DISTINCT active
FROM product_dump