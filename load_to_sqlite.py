import os
import pandas as pd
from sqlalchemy import create_engine

# Folder containing processed CSVs
PROCESSED_FOLDER = "data/processed"

# SQLite database
DATABASE_NAME = "bluestock_mf.db"

# Create database connection
engine = create_engine(f"sqlite:///{DATABASE_NAME}")

print("=" * 80)
print("LOADING DATA INTO SQLITE")
print("=" * 80)

csv_files = sorted([
    f for f in os.listdir(PROCESSED_FOLDER)
    if f.endswith(".csv")
])

for file in csv_files:

    path = os.path.join(PROCESSED_FOLDER, file)

    df = pd.read_csv(path)

    table_name = file.replace("_processed.csv", "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name} ({len(df)} rows)")

print("\nAll datasets loaded successfully!")

print("\nVerifying row counts...")

for file in csv_files:

    table_name = file.replace("_processed.csv", "")

    query = f"SELECT COUNT(*) AS rows FROM {table_name}"

    rows = pd.read_sql(query, engine)

    print(f"{table_name}: {rows.iloc[0,0]} rows")