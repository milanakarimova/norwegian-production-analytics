import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path("data/processed/field_production_monthly_clean.csv")
figures_path = Path("reports/figures")
figures_path.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])

print("Shape:", df.shape)
print(df.head())
print(df.describe())

# 1. Total oil production by year
yearly_oil = df.groupby("year")["oil_mill_sm3"].sum()

plt.figure(figsize=(10, 5))
yearly_oil.plot()
plt.title("Total Oil Production by Year")
plt.xlabel("Year")
plt.ylabel("Oil Production, million Sm3")
plt.tight_layout()
plt.savefig(figures_path / "total_oil_production_by_year.png")
plt.close()

# 2. Top 10 fields by oil production
top_fields = (
    df.groupby("field")["oil_mill_sm3"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 5))
top_fields.plot(kind="bar")
plt.title("Top 10 Fields by Oil Production")
plt.xlabel("Field")
plt.ylabel("Oil Production, million Sm3")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(figures_path / "top_10_fields_by_oil_production.png")
plt.close()

# 3. Total gas production by year
yearly_gas = df.groupby("year")["gas_bill_sm3"].sum()

plt.figure(figsize=(10, 5))
yearly_gas.plot()
plt.title("Total Gas Production by Year")
plt.xlabel("Year")
plt.ylabel("Gas Production, billion Sm3")
plt.tight_layout()
plt.savefig(figures_path / "total_gas_production_by_year.png")
plt.close()

# 4. Oil vs water production by year
yearly = df.groupby("year")[["oil_mill_sm3", "water_mill_sm3"]].sum()

plt.figure(figsize=(10, 5))
plt.plot(yearly.index, yearly["oil_mill_sm3"], label="Oil")
plt.plot(yearly.index, yearly["water_mill_sm3"], label="Water")
plt.title("Oil vs Produced Water by Year")
plt.xlabel("Year")
plt.ylabel("Production, million Sm3")
plt.legend()
plt.tight_layout()
plt.savefig(figures_path / "oil_vs_water_by_year.png")
plt.close()

print("EDA figures saved to reports/figures/")
