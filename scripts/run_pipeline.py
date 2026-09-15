"""Master execution script for the Bluestock project."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
STEPS = [
    ("Data ingestion", "data_ingestion.py"),
    ("Load SQLite database", "load_to_sqlite.py"),
    ("Validate AMFI codes", "validate_amfi.py"),
]


def main():
    print("Bluestock Mutual Fund Analytics Pipeline")
    for name, filename in STEPS:
        script = ROOT / filename
        if not script.exists():
            print(f"[SKIP] {filename} not found.")
            continue
        print(f"\n--- {name} ---")
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if result.returncode != 0:
            raise SystemExit(f"{name} failed with exit code {result.returncode}.")
        print(f"[OK] {name}")
    print("\nPipeline completed.")


if __name__ == "__main__":
    main()
