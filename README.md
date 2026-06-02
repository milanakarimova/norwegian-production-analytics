
# Norwegian Production Analytics

Real-world data science project analyzing Norwegian oil and gas field production data using Python, Pandas, SQL, Matplotlib, and scikit-learn.

## Dataset

Source: Norwegian Offshore Directorate monthly field production dataset.

The dataset contains monthly production records for Norwegian petroleum fields, including oil, gas, NGL, condensate, oil equivalent, and produced water.

## Project Goals

* Clean real petroleum production data
* Analyze production trends by year and field
* Run SQL-based production aggregation queries
* Visualize oil, gas, and water production patterns
* Engineer time-series features
* Build a baseline next-month oil production forecasting model

## Tech Stack

Python, SQL, Pandas, NumPy, Matplotlib, scikit-learn, SQLite, Git, GitHub

## Project Workflow

1. Load raw monthly production data
2. Clean and standardize column names
3. Create a monthly date feature
4. Save processed dataset
5. Run SQL analysis queries
6. Generate EDA visualizations
7. Train a baseline forecasting model

## How to Run

Install dependencies:

```
pip install -r requirements.txt
```

Run data cleaning:

```
python src/clean_data.py
```

Run SQL analysis:

```
python src/run_sql_analysis.py
```

Run exploratory data analysis:

```
python src/eda.py
```

Run forecasting model:

```
python src/model.py
```

## SQL Analysis

The project includes SQL queries for production analytics:

| Query                                  | Purpose                                                          |
| -------------------------------------- | ---------------------------------------------------------------- |
| `sql/top_fields_by_oil_production.sql` | Finds top fields by total oil production                         |
| `sql/yearly_production_trend.sql`      | Aggregates yearly oil, gas, water, and oil-equivalent production |
| `sql/field_level_aggregation.sql`      | Creates field-level production summaries                         |

SQL output files are saved in:

```
reports/sql_results/
```

## Model Results

The baseline next-month oil production forecasting model achieved:

| Metric |              Value |
| ------ | -----------------: |
| MAE    | 0.0172 million Sm³ |
| R²     |             0.9486 |

## Visualizations

### Total Oil Production by Year

![Total Oil Production by Year](reports/figures/total_oil_production_by_year.png)

### Total Gas Production by Year

![Total Gas Production by Year](reports/figures/total_gas_production_by_year.png)

### Top 10 Fields by Oil Production

![Top 10 Fields by Oil Production](reports/figures/top_10_fields_by_oil_production.png)

### Oil vs Produced Water by Year

![Oil vs Produced Water by Year](reports/figures/oil_vs_water_by_year.png)

### Actual vs Predicted Oil Forecast

![Actual vs Predicted Oil Forecast](reports/figures/actual_vs_predicted_oil_forecast.png)

### Feature Importance

![Feature Importance](reports/figures/feature_importance.png)

## Project Structure

```
data/
  raw/
  processed/
sql/
  top_fields_by_oil_production.sql
  yearly_production_trend.sql
  field_level_aggregation.sql
src/
  clean_data.py
  run_sql_analysis.py
  eda.py
  model.py
reports/
  figures/
  sql_results/
  model_results.txt
requirements.txt
README.md
```

## Portfolio Value

This project demonstrates applied data science for petroleum production analytics, combining geoscience domain knowledge with Python-based data cleaning, SQL analysis, visualization, feature engineering, and machine learning.
