import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

data_path = Path("data/processed/field_production_monthly_clean.csv")
figures_path = Path("reports/figures")
figures_path.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(data_path)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(["field", "date"])

# Feature engineering
df["oil_lag_1"] = df.groupby("field")["oil_mill_sm3"].shift(1)
df["oil_lag_3"] = df.groupby("field")["oil_mill_sm3"].shift(3)
df["oil_rolling_3"] = (
    df.groupby("field")["oil_mill_sm3"]
    .shift(1)
    .rolling(3)
    .mean()
)
df["target_next_month_oil"] = df.groupby("field")["oil_mill_sm3"].shift(-1)

features = [
    "year",
    "month",
    "gas_bill_sm3",
    "ngl_mill_sm3",
    "condensate_mill_sm3",
    "oe_mill_sm3",
    "water_mill_sm3",
    "oil_lag_1",
    "oil_lag_3",
    "oil_rolling_3",
]

model_df = df.dropna(subset=features + ["target_next_month_oil"])

# Time-based split
cutoff_date = model_df["date"].quantile(0.8)
train = model_df[model_df["date"] <= cutoff_date]
test = model_df[model_df["date"] > cutoff_date]

X_train = train[features]
y_train = train["target_next_month_oil"]
X_test = test[features]
y_test = test["target_next_month_oil"]

model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)

mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print("Next-month oil production forecasting")
print(f"MAE: {mae:.4f} million Sm3")
print(f"R2: {r2:.4f}")

with open("reports/model_results.txt", "w", encoding="utf-8") as f:
    f.write("Next-month oil production forecasting\n")
    f.write(f"MAE: {mae:.4f} million Sm3\n")
    f.write(f"R2: {r2:.4f}\n")

# Plot actual vs predicted
plt.figure(figsize=(7, 6))
plt.scatter(y_test, preds, alpha=0.5)
plt.title("Actual vs Predicted Next-Month Oil Production")
plt.xlabel("Actual oil production, million Sm3")
plt.ylabel("Predicted oil production, million Sm3")
plt.tight_layout()
plt.savefig(figures_path / "actual_vs_predicted_oil_forecast.png")
plt.close()

# Feature importance
importance = pd.Series(model.feature_importances_, index=features).sort_values()

plt.figure(figsize=(8, 5))
importance.plot(kind="barh")
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig(figures_path / "feature_importance.png")
plt.close()

print("Model results saved to reports/model_results.txt")
print("Figures saved to reports/figures/")
