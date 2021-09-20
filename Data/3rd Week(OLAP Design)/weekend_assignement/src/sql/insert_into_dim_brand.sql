INSERT INTO dim_brand(name)
SELECT DISTINCT brand
FROM product_dump