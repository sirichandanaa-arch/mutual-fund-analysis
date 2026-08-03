-- =====================================================
-- Mutual Fund Analysis - SQL Queries
-- =====================================================

-- 1. Total number of mutual fund schemes
SELECT COUNT(*) AS total_schemes
FROM fund_master;

--------------------------------------------------------

-- 2. Number of schemes by fund house
SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM fund_master
GROUP BY fund_house
ORDER BY total_schemes DESC;

--------------------------------------------------------

-- 3. Top 10 schemes by 5-Year Return
SELECT
    scheme_name,
    fund_house,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

--------------------------------------------------------

-- 4. Average NAV of each scheme
SELECT
    amfi_code,
    AVG(nav) AS average_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY average_nav DESC;

--------------------------------------------------------

-- 5. Total Investment Amount by Transaction Type
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;

--------------------------------------------------------

-- 6. State-wise Investment Amount
SELECT
    state,
    SUM(amount_inr) AS total_investment
FROM investor_transactions
GROUP BY state
ORDER BY total_investment DESC;

--------------------------------------------------------

-- 7. Top 10 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;

--------------------------------------------------------

-- 8. Schemes with Expense Ratio greater than 2%
SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct > 2
ORDER BY expense_ratio_pct DESC;

--------------------------------------------------------

-- 9. Average 3-Year Return by Category
SELECT
    category,
    AVG(return_3yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category
ORDER BY avg_return DESC;

--------------------------------------------------------

-- 10. Number of Investors by City Tier
SELECT
    city_tier,
    COUNT(DISTINCT investor_id) AS investors
FROM investor_transactions
GROUP BY city_tier
ORDER BY investors DESC;