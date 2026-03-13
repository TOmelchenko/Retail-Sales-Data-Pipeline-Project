CREATE DATABASE retail_project;

-- Create table for reporting
CREATE TABLE IF NOT EXISTS sales_report_etl (
    order_id INTEGER,
    order_date DATE,
    customer_id INTEGER,
    customer_name TEXT,
    city TEXT,
    product_id INTEGER,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price NUMERIC(10,2),
    total_amount NUMERIC(10,2)
);

CREATE TABLE IF NOT EXISTS category_summary (
    category TEXT,
    total_revenue NUMERIC(10,2)
);

INSERT INTO category_summary (category, total_revenue)
SELECT category, SUM(total_amount)
FROM sales_report
GROUP BY category;

CREATE TABLE IF NOT EXISTS raw_customers (
    customer_id TEXT,
    customer_name TEXT,
    city TEXT,
    signup_date TEXT
);

CREATE TABLE IF NOT EXISTS raw_orders (
    order_id TEXT,
    customer_id TEXT,
    product_id TEXT,
    quantity TEXT,
    order_date TEXT
);

CREATE TABLE IF NOT EXISTS raw_products (
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    price TEXT
);

CREATE TABLE IF NOT EXISTS sales_report_elt (
    order_id INTEGER,
    order_date DATE,
    customer_id INTEGER,
    customer_name TEXT,
    city TEXT,
    product_id INTEGER,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    price NUMERIC(10,2),
    total_amount NUMERIC(10,2)
);