"""Risk-based mutual fund recommender."""
from pathlib import Path
import argparse
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "processed" / "07_scheme_performance_processed.csv"


def recommend(risk_appetite, top_n=3):
    """Return top funds by Sharpe ratio for Low/Moderate/High risk."""
    valid = {"low": "Low", "moderate": "Moderate", "high": "High"}
    key = str(risk_appetite).strip().lower()
    if key not in valid:
        raise ValueError("Risk appetite must be Low, Moderate, or High.")

    df = pd.read_csv(DATA_FILE)
    required = {"scheme_name", "risk_grade", "sharpe_ratio"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    df["sharpe_ratio"] = pd.to_numeric(df["sharpe_ratio"], errors="coerce")
    result = df[df["risk_grade"].astype(str).str.strip().str.lower() == key]
    result = result.dropna(subset=["sharpe_ratio"]).sort_values("sharpe_ratio", ascending=False).head(top_n)
    cols = [c for c in ["scheme_name", "fund_house", "category", "plan", "risk_grade", "sharpe_ratio", "return_3yr_pct", "max_drawdown_pct"] if c in result.columns]
    return result[cols].reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser(description="Recommend mutual funds by risk appetite.")
    parser.add_argument("--risk", choices=["Low", "Moderate", "High"])
    parser.add_argument("--top", type=int, default=3)
    args = parser.parse_args()
    risk = args.risk or input("Enter risk appetite (Low / Moderate / High): ").strip()
    result = recommend(risk, args.top)
    print(f"\nTop {args.top} recommendations for {risk} risk appetite:\n")
    print(result.to_string(index=False) if not result.empty else "No matching funds found.")


if __name__ == "__main__":
    main()
