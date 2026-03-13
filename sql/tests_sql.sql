
SELECT COUNT(*) FROM sales_report;

SELECT * FROM sales_report LIMIT 10;

SELECT category, SUM(total_amount) AS total_revenue
FROM sales_report_etl
GROUP BY category
ORDER BY total_revenue DESC;

SELECT city, COUNT(*) AS total_orders
FROM sales_report
GROUP BY city
ORDER BY total_orders DESC;


SELECT * FROM category_summary;