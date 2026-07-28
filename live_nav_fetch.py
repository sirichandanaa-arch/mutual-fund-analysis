import requests
import pandas as pd
from pathlib import Path

# AMFI scheme code
scheme_code = "125497"

# API URL
url = f"https://api.mfapi.in/mf/{scheme_code}"

print("Fetching live NAV data...")

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    print("Successfully fetched data!")

    # Save complete JSON
    raw_folder = Path("data/raw")
    raw_folder.mkdir(parents=True, exist_ok=True)

    json_file = raw_folder / "live_nav.json"

    with open(json_file, "w", encoding="utf-8") as f:
        import json
        json.dump(data, f, indent=4)

    # NAV history
    nav_df = pd.DataFrame(data["data"])

    csv_file = raw_folder / "live_nav.csv"

    nav_df.to_csv(csv_file, index=False)

    print(f"CSV saved to {csv_file}")

    print("\nScheme Information")
    print("-----------------------")
    print("Scheme Name:", data["meta"]["scheme_name"])
    print("Fund House :", data["meta"]["fund_house"])

    print("\nLatest NAV")
    print(nav_df.head())

else:
    print("Failed to fetch data.")
    print("Status Code:", response.status_code)