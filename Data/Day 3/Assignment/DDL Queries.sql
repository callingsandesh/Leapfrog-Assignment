CREATE DATABASE ecommerce;

USE ecommerce;

DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
  customer_id int identity (1,1) PRIMARY KEY,
  user_name   varchar(20),
  first_name  varchar(100),
  last_name   varchar(100),
  country     varchar(50),
  town        varchar(50),
  address     varchar(255),
  active      char(1)
)

CREATE TABLE product (
  product_id       int identity (1,1) PRIMARY KEY,
  product_name     varchar(100),
  description      varchar(255),
  price            float,
  mrp              float,
  pieces_per_cASE  float,
  weight_per_piece float,
  uom              varchar(30),
  brand            varchar(100),
  category         varchar(100),
  tax_percent      float,
  active           char(1),
  created_by       varchar(20),
  created_date     datetime DEFAULT GETDATE(),
  updated_by       varchar(20),
  updated_date     datetime DEFAULT GETDATE()
);

CREATE TABLE sales
(
  id             int identity (1,1) PRIMARY KEY,
  transction_id  int,
  bill_no        int,
  bill_date      datetime DEFAULT getdate(),
  bill_location  varchar(30),
  customer_id    int,
  product_id     int,
  qty            int,
  uom            varchar(20),
  price          float,
  gross_price    float,
  tax_pc         float,
  tax_amt        float,
  discount_pc    float,
  discount_amt   float,
  net_bill_amt   float,
  created_by     varchar(20),
  created_date   datetime DEFAULT GETDATE(),
  updated_by     varchar(20),
  updated_date   datetime DEFAULT GETDATE()
  CONSTRAINT fk_product_id FOREIGN KEY(product_id) REFERENCES dbo.product(product_id),
  CONSTRAINT fk_customer_id FOREIGN KEY(customer_id) REFERENCES dbo.customer(customer_id)
)

BULK INSERT dbo.sales
FROM 'sale.csv_file_path'
WITH (
  FIRSTROW = 2,
  FIELDTERMINATOR = ',',
  ROWTERMINATOR ='\n'
)

