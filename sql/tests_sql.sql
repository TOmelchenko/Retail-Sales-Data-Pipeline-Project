-- Test ETL and ELT loads
-- If both tables sales_report_elt and sales_report_etl are the same
-- the query shouldn't return any row

SELECT * 
FROM(    
    SELECT 
        order_id,
        order_date,
        customer_id,
        customer_name,
        city,
        product_id,
        product_name,
        category,
        quantity,
        price,
        total_amount
    FROM sales_report_elt 
    EXCEPT
    SELECT 
        order_id,
        order_date,
        customer_id,
        customer_name,
        city,
        product_id,
        product_name,
        category,
        quantity,
        price,
        total_amount
    FROM sales_report_etl
    UNION ALL
    SELECT 
        order_id,
        order_date,
        customer_id,
        customer_name,
        city,
        product_id,
        product_name,
        category,
        quantity,
        price,
        total_amount
    FROM sales_report_etl 
    EXCEPT
    SELECT 
        order_id,
        order_date,
        customer_id,
        customer_name,
        city,
        product_id,
        product_name,
        category,
        quantity,
        price,
        total_amount
    FROM sales_report_elt
);

