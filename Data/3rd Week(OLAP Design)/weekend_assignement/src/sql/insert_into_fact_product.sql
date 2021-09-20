INSERT INTO fact_product
SELECT 
	product_id,
	product_name,
	description,
	price,
	mrp,
	pieces_per_case,
	weight_per_piece,
	dim_uom.id AS uom_id,
	dim_brand.id AS brand_id,
	dim_category.id AS category_id,
	tax_percent,
	dim_status.id AS product_status_id,
	created_by,
	created_date,
	updated_by,
	updated_date
FROM product_dump
INNER JOIN dim_uom
	ON product_dump.uom = dim_uom.type
INNER JOIN dim_brand
	ON product_dump.brand = dim_brand.name
INNER JOIN dim_category
	ON product_dump.category = dim_category.name
INNER JOIN dim_status
	ON product_dump.active = dim_status.type