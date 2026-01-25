import sys
import pandas as pd

day = int(sys.argv[1])

print(f"Running pipeline for day {day}")

df = pd.DataFrame(
  {
    "A": [1, 2, 3],
    "B": [4, 5, 6]
  }
)

print(df.head())

df.to_parquet(f"day_{day}_output.parquet")

