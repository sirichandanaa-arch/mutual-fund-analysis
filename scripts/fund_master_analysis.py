import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nTotal Schemes:")
print(df.shape[0])

print("\nUnique Fund Houses:")
print(df["fund_house"].nunique())
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Grades:")
print(df["risk_category"].value_counts())

print("\nTop 10 Fund Houses:")
print(df["fund_house"].value_counts().head(10))