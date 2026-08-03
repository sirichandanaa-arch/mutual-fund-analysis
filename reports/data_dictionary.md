# Mutual Fund Analysis - Data Dictionary

## 1. fund_master

| Column | Description |
|--------|-------------|
| amfi_code | Unique AMFI scheme code |
| scheme_name | Mutual fund scheme name |
| fund_house | Asset Management Company |
| category | Fund category |
| sub_category | Fund sub-category |
| plan | Direct/Regular plan |
| option_type | Growth/IDCW option |
| launch_date | Scheme launch date |
| benchmark | Benchmark index |
| risk_category | Risk classification |

---

## 2. nav_history

| Column | Description |
|--------|-------------|
| amfi_code | Scheme code |
| date | NAV date |
| nav | Net Asset Value |

---

## 3. scheme_performance

| Column | Description |
|--------|-------------|
| return_1yr_pct | 1-Year Return (%) |
| return_3yr_pct | 3-Year Return (%) |
| return_5yr_pct | 5-Year Return (%) |
| alpha | Alpha |
| beta | Beta |
| sharpe_ratio | Sharpe Ratio |
| sortino_ratio | Sortino Ratio |
| expense_ratio_pct | Expense Ratio (%) |
| aum_crore | Assets Under Management (₹ Crore) |

---

## 4. investor_transactions

| Column | Description |
|--------|-------------|
| investor_id | Investor ID |
| transaction_date | Transaction Date |
| transaction_type | SIP / Lumpsum / Redemption |
| amount_inr | Investment Amount (₹) |
| state | Investor State |
| city | Investor City |
| city_tier | Tier 1 / Tier 2 / Tier 3 |
| annual_income_lakh | Annual Income (Lakhs) |
| payment_mode | Payment Method |
| kyc_status | KYC Verification Status |

---

## Database

SQLite Database:
`bluestock_mf.db`