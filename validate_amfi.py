import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = nav_codes - master_codes

print("=" * 60)
print("AMFI VALIDATION")
print("=" * 60)

print("Codes in Fund Master :", len(master_codes))
print("Codes in NAV History :", len(nav_codes))

if len(missing) == 0:
    print("\nAll NAV AMFI codes exist in fund_master.")
else:
    print("\nMissing Codes:")
    print(missing)