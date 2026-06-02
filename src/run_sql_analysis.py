import sqlite3
from pathlib import Path

import pandas as pd

data_path = Path("data/processed/field_production_monthly_clean.csv")
sql_path = Path("sql")
output_path = Path("reports/sql_results")
output_path.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path)

conn = sqlite3.connect(":memory:")
df.to_sql("field_production", conn, index=False, if_exists="replace")

queries = {
    "top_fields_by_oil_production": sql_path / "top_fields_by_oil_production.sql",
    "yearly_production_trend": sql_path / "yearly_production_trend.sql",
    "field_level_aggregation": sql_path / "field_level_aggregation.sql",
}

for name, query_file in queries.items():
    query = query_file.read_text(encoding="utf-8")
    result = pd.read_sql_query(query, conn)
    result.to_csv(output_path / f"{name}.csv", index=False)

    print(f"\n{name}")
    print(result.head(10))

conn.close()
print("\nSQL analysis results saved to reports/sql_results/")
