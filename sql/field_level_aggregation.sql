SELECT
    field,
    MIN(date) AS first_month,
    MAX(date) AS last_month,
    COUNT(*) AS monthly_records,
    ROUND(SUM(oil_mill_sm3), 4) AS total_oil_mill_sm3,
    ROUND(AVG(oil_mill_sm3), 4) AS avg_monthly_oil_mill_sm3,
    ROUND(SUM(gas_bill_sm3), 4) AS total_gas_bill_sm3,
    ROUND(SUM(water_mill_sm3), 4) AS total_water_mill_sm3,
    ROUND(SUM(oe_mill_sm3), 4) AS total_oe_mill_sm3
FROM field_production
GROUP BY field
ORDER BY total_oe_mill_sm3 DESC;
