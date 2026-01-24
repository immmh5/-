"""
Day 7 Activity: Imputation Practice
Tasks:
1) Implement fit_imputer(train_df) returning medians/modes
2) Implement transform_imputer(df, params)
3) Add missing indicators optionally
4) Compare behavior with/without indicators
"""

import pandas as pd

# Sample dataset
train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})

test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})

# TODO: Implement fit_imputer
# def fit_imputer(train_df, num_cols, cat_cols):
#     ...

# TODO: Implement transform_imputer
# def transform_imputer(df, params, add_indicators=True):
#     ...
