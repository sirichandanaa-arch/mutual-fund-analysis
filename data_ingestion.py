import os
import pandas as pd

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)

print("=" * 80)
print("DATA INGESTION REPORT")
print("=" * 80)

csv_files = sorted([
    f for f in os.listdir(RAW_FOLDER)
    if f.endswith(".csv") and f != "live_nav.csv"
])

for file in csv_files:

    print(f"\nDataset: {file}")
    print("-" * 80)

    path = os.path.join(RAW_FOLDER, file)

    # Read dataset
    df = pd.read_csv(path)

    # ---------------------------------------------------
    # Basic Cleaning (Applied to all datasets)
    # ---------------------------------------------------

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert date columns
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col], errors="coerce")
            except:
                pass

    # ---------------------------------------------------
    # Dataset Specific Cleaning
    # ---------------------------------------------------

    # NAV History
    if file == "02_nav_history.csv":

        df = df.sort_values(["amfi_code", "date"])

        df["nav"] = df.groupby("amfi_code")["nav"].ffill()

        df = df[df["nav"] > 0]

    # Investor Transactions
    elif file == "08_investor_transactions.csv":

        # Standardize transaction type
        df["transaction_type"] = (
            df["transaction_type"]
            .astype(str)
            .str.strip()
            .str.title()
        )

        valid_types = ["Sip", "Lumpsum", "Redemption"]
        df = df[df["transaction_type"].isin(valid_types)]

        # Amount should be positive
        df = df[df["amount_inr"] > 0]

        # Standardize KYC Status
        df["kyc_status"] = (
            df["kyc_status"]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # Scheme Performance
    elif file == "07_scheme_performance.csv":

        return_columns = [
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct",
            "benchmark_3yr_pct"
        ]

        for col in return_columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df["expense_ratio_pct"] = pd.to_numeric(
            df["expense_ratio_pct"],
            errors="coerce"
        )

        # Flag expense ratio anomalies
        df["expense_ratio_valid"] = (
            (df["expense_ratio_pct"] >= 0.1)
            &
            (df["expense_ratio_pct"] <= 2.5)
        )

    # ---------------------------------------------------
    # Save Processed Dataset
    # ---------------------------------------------------

    processed_file = file.replace(".csv", "_processed.csv")

    processed_path = os.path.join(
        PROCESSED_FOLDER,
        processed_file
    )

    df.to_csv(processed_path, index=False)

    # ---------------------------------------------------
    # Report
    # ---------------------------------------------------

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nData Quality Summary:")

    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("No missing values found.")
    else:
        print("\nMissing Values:")
        print(missing[missing > 0])

    duplicates = df.duplicated().sum()

    print("Duplicate Rows:", duplicates)

    print("\nProcessed file saved to:")
    print(processed_path)

    print("=" * 80)

print("\nAll datasets processed successfully.")