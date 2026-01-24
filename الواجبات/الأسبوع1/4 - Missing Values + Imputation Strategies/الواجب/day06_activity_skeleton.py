"""
Day 6 Activity: Missing Values Practice
Tasks:
1) Load/define a partially observed dataset
2) Normalize missing tokens to NaN
3) Produce missingness summary (per-column %, per-row)
4) Build Version A: drop rows with missing in key cols
5) Build Version B: impute + indicators
6) Compare basic metrics between A and B
"""

import numpy as np
import pandas as pd

# Sample raw dataset (replace or load your own)
raw = {
    "age": [25, "N/A", 40, 33, "?"],
    "income": [50000, 60000, None, "unknown", 80000],
    "churned": [0, 1, 0, 1, 0],
}

df_raw = pd.DataFrame(raw)

# TODO: Normalize custom missing tokens to NaN
# df = df_raw.replace(["N/A", "NA", "not reported", "unknown", "?"], np.nan)

# TODO: Create missing_summary(df) returning per-column and per-row missingness

# TODO: Version A: drop rows with missing in key columns (e.g., age, income)

# TODO: Version B: impute numeric columns + add missing indicators

# TODO: Compare basic statistics or a simple model between A and B
