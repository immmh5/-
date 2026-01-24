"""
Day 10 Activity: Outliers Practice
Tasks:
1) Implement IQR-based outlier detection
2) Implement z-score detection
3) Compare strategies: no handling, IQR capping, log1p transform
"""

import numpy as np
import pandas as pd

# Sample heavy-tailed data
np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])

df = pd.DataFrame({"income": values})

# TODO: Implement iqr_bounds and detect_outliers_iqr
# TODO: Implement detect_outliers_zscore
# TODO: Apply capping and log1p transformation
