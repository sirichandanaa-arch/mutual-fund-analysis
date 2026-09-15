-- ==========================================
-- Mutual Fund Analysis Database Schema
-- ==========================================

-- 1. Fund Master
CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    option_type TEXT,
    launch_date DATE,
    benchmark TEXT,
    risk_category TEXT
);

-- 2. NAV History
CREATE TABLE nav_history (
    amfi_code INTEGER,
    date DATE,
    nav REAL,
    PRIMARY KEY (amfi_code, date),
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- 3. AUM by Fund House
CREATE TABLE aum_by_fund_house (
    fund_house TEXT,
    month DATE,
    aum_crore REAL
);

-- 4. Monthly SIP Inflows
CREATE TABLE monthly_sip_inflows (
    month DATE,
    sip_inflow_crore REAL,
    yoy_growth_pct REAL
);

-- 5. Category Inflows
CREATE TABLE category_inflows (
    month DATE,
    category TEXT,
    inflow_crore REAL
);

-- 6. Industry Folio Count
CREATE TABLE industry_folio_count (
    month DATE,
    folio_count BIGINT
);

-- 7. Scheme Performance
CREATE TABLE scheme_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    benchmark_3yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    std_dev_ann_pct REAL,
    max_drawdown_pct REAL,
    aum_crore REAL,
    expense_ratio_pct REAL,
    morningstar_rating INTEGER,
    risk_grade TEXT,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- 8. Investor Transactions
CREATE TABLE investor_transactions (
    investor_id INTEGER,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- 9. Portfolio Holdings
CREATE TABLE portfolio_holdings (
    amfi_code INTEGER,
    company_name TEXT,
    sector TEXT,
    instrument_type TEXT,
    holding_pct REAL,
    market_value_crore REAL,
    FOREIGN KEY (amfi_code) REFERENCES fund_master(amfi_code)
);

-- 10. Benchmark Indices
CREATE TABLE benchmark_indices (
    date DATE,
    index_name TEXT,
    close_value REAL,
    PRIMARY KEY (date, index_name)
);