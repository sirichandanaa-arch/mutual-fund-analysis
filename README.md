# Bluestock Mutual Fund Analytics

A data analytics project on mutual funds covering data ingestion, cleaning, SQL analysis, exploratory data analysis, fund performance, advanced analytics, and Power BI dashboarding.

## Project Structure

- `data/raw/` — original datasets
- `data/processed/` — cleaned datasets and advanced analytics outputs
- `notebooks/` — EDA, performance, and advanced analytics notebooks
- `charts/` — analysis charts
- `sql/` — database schema and analytical queries
- `dashboard/` — Power BI dashboard
- `reports/` — final report, presentation, dashboard PDF, and page images

## Scripts

- `data_ingestion.py` — loads and processes the raw datasets
- `live_nav_fetch.py` — retrieves NAV data
- `load_to_sqlite.py` — loads processed data into SQLite
- `validate_amfi.py` — validates AMFI scheme codes
- `fund_master_analysis.py` — explores fund-house and scheme information
- `recommender.py` — recommends top funds based on risk appetite
- `run_pipeline.py` — runs the main project pipeline

## Analysis

The project covers:

- Daily returns and CAGR
- Sharpe and Sortino ratios
- Alpha and Beta
- Maximum drawdown
- Fund scoring and ranking
- Benchmark comparison
- VaR and CVaR
- Rolling Sharpe ratio
- Investor cohort analysis
- SIP continuity analysis
- Sector concentration using HHI

## Power BI Dashboard

The Power BI dashboard contains four pages:

1. Industry Overview
2. Fund Performance
3. Investor Analytics
4. SIP & Market Trends

Open `dashboard/bluestock_mf_dashboard.pbix` using Power BI Desktop to view the dashboard.

## Fund Recommender

The recommender can be run from the project root:

```bash
python recommender.py --risk Low
python recommender.py --risk Moderate
python recommender.py --risk High
```

It returns the top funds for the selected risk category.

## Running the Project

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Then run:

```bash
python run_pipeline.py
```

## Notes

The project uses the supplied Bluestock mutual-fund datasets for analysis. Generated database files are kept out of GitHub where required by the project instructions.