SELECT
    field,
    ROUND(SUM(oil_mill_sm3), 4) AS total_oil_mill_sm3,
    ROUND(SUM(gas_bill_sm3), 4) AS total_gas_bill_sm3,
    COUNT(*) AS monthly_records
FROM field_production
GROUP BY field
ORDER BY total_oil_mill_sm3 DESC
LIMIT 10;
