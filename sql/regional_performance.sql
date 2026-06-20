SELECT
    region,
    SUM(revenue) AS total_revenue,
    SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;