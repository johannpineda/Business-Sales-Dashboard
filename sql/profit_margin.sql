SELECT
    ROUND(
        (SUM(profit) * 100.0) / SUM(revenue),
        2
    ) AS profit_margin_percentage
FROM sales;