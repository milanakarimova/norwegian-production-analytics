import pandas as pd
from pathlib import Path

raw_path = Path("data/raw/field_production_monthly.csv")
processed_path = Path("data/processed/field_production_monthly_clean.csv")

df = pd.read_csv(raw_path)

df = df.rename(columns={
    "prfInformationCarrier": "field",
    "prfYear": "year",
    "prfMonth": "month",
    "prfPrdOilNetMillSm3": "oil_mill_sm3",
    "prfPrdGasNetBillSm3": "gas_bill_sm3",
    "prfPrdNGLNetMillSm3": "ngl_mill_sm3",
    "prfPrdCondensateNetMillSm3": "condensate_mill_sm3",
    "prfPrdOeNetMillSm3": "oe_mill_sm3",
    "prfPrdProducedWaterInFieldMillSm3": "water_mill_sm3",
    "prfNpdidInformationCarrier": "field_id"
})

df["date"] = pd.to_datetime(
    df["year"].astype(str) + "-" + df["month"].astype(str) + "-01"
)

df = df.sort_values(["field", "date"])

processed_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(processed_path, index=False)

print("Cleaned shape:", df.shape)
print("Saved to:", processed_path)
print(df.head())
print(df.columns)
