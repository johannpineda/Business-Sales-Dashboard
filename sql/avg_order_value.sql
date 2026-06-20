SELECT
    SUM(revenue) / COUNT(order_id) AS average_order_value
FROM sales;