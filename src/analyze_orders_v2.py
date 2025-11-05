import pandas as pd
from pathlib import Path # Path class to handle file paths in a portable way (not break with location change)

# ✅ Define relative paths to input/output files to avoid Windows hard-coding
DATA_PATH = Path("data/orders_cities.xlsx")
OUTPUT_PATH = Path("output/totals_by_city.csv")

# Check the existance of input file > stop if not > print defined error
try:
    df = pd.read_excel(DATA_PATH, engine='openpyxl') # specify engine in case not installed on OS
except FileNotFoundError:
    raise SystemExit(f"❌ Input file not found: {DATA_PATH}")

# ✅ Validate required columns > stop if not > print defined error
required_cols = {"city", "cost"} # Create a set with column names required for script
if not required_cols.issubset(df.columns): # all in required_cols is in df.columns
    raise SystemExit(f"❌ Missing required columns: {required_cols - set(df.columns)}") # displays the missing columns (required but not found in DataFrame)

def main(): # separate function > can import script in another file without it auto-running

    # ✅ Calculations
    num_rows = len(df)
    total_cost = df["cost"].sum()
    totals_df = df.groupby("city", as_index=False)["cost"].sum() # group by 'city' + sum 'cost' + DF [.reset_index()]
    totals_df.columns = ["City", "Total Costs"]  # rename DF columns for clean output

    # ✅ Make sure output folder exists > create it if not
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # ✅ Export new file
    totals_df.to_csv(OUTPUT_PATH, index=False)

    print("✅ Done!")
    print(f"Orders: {num_rows}")
    print(f"Total Cost: {total_cost} €")
    print(f"➡️ Exported: {OUTPUT_PATH}")
if __name__ == "__main__":
    main()