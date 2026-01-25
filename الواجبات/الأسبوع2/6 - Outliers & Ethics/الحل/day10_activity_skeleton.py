import numpy as np
import pandas as pd

np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])

df = pd.DataFrame({"income": values})

def get_iqr_bounds(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return lower_bound, upper_bound

lower, upper = get_iqr_bounds(df['income'])
df['is_outlier_iqr'] = (df['income'] < lower) | (df['income'] > upper)

def detect_outliers_zscore(data, threshold=3):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = (data - mean) / std
    return np.abs(z_scores) > threshold

df['is_outlier_z'] = detect_outliers_zscore(df['income'])

df['income_capped'] = df['income'].clip(lower, upper)

df['income_log'] = np.log1p(df['income'])

print(f"IQR Outliers found: {df['is_outlier_iqr'].sum()}")
print(f"Z-score Outliers found: {df['is_outlier_z'].sum()}")
print(df.head())