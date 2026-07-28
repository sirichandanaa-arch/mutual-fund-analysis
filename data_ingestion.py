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

    df = pd.read_csv(path)

    # --------------------------
    # Basic Cleaning
    # --------------------------

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
    )

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Convert date columns if present
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col])
            except:
                pass

    # --------------------------
    # Save processed dataset
    # --------------------------

    processed_file = file.replace(".csv", "_processed.csv")
    processed_path = os.path.join(PROCESSED_FOLDER, processed_file)

    df.to_csv(processed_path, index=False)

    # --------------------------
    # Print information
    # --------------------------

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