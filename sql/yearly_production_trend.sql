SELECT
    year,
    ROUND(SUM(oil_mill_sm3), 4) AS yearly_oil_mill_sm3,
    ROUND(SUM(gas_bill_sm3), 4) AS yearly_gas_bill_sm3,
    ROUND(SUM(water_mill_sm3), 4) AS yearly_water_mill_sm3,
    ROUND(SUM(oe_mill_sm3), 4) AS yearly_oe_mill_sm3
FROM field_production
GROUP BY year
ORDER BY year;
