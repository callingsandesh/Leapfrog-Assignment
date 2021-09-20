INSERT INTO dim_uom(type)
SELECT DISTINCT uom
FROM product_dump