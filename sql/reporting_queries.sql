-- For ETL
SELECT COUNT(*) FROM sales_report_etl;

SELECT * FROM sales_report_etl LIMIT 10;

SELECT category, SUM(total_amount) AS total_revenue
FROM sales_report_etl
GROUP BY category
ORDER BY total_revenue DESC;

SELECT city, COUNT(*) AS total_orders
FROM sales_report_etl
GROUP BY city
ORDER BY total_orders DESC;

-- For ELT
SELECT COUNT(*) FROM sales_report_elt;

SELECT * FROM sales_report_elt LIMIT 10;

SELECT category, SUM(total_amount) AS total_revenue
FROM sales_report_elt
GROUP BY category
ORDER BY total_revenue DESC;

SELECT city, COUNT(*) AS total_orders
FROM sales_report_elt
GROUP BY city
ORDER BY total_orders DESC;