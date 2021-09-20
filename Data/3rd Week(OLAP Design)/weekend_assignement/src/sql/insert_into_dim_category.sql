INSERT INTO dim_category(name)
SELECT DISTINCT category
FROM product_dump