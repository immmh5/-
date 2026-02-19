"""
Tasks:

1-Visualizing Distributions: * For each numerical column (income, age, and transactions), create a side-by-side visualization consisting of a Histogram (with 30 bins) and a KDE (Kernel Density Estimate) plot.

    Explain the purpose of comparing both plots together.

2-Summary Statistics: * Generate and display the descriptive statistics (count, mean, std, etc.) for these numerical variables to identify potential outliers or high variability.

3-Data Preprocessing (Handling Skewness):

    Identify if the income variable is right-skewed.

    If the data is positive, apply a Log Transformation (np.log1p) to normalize its distribution.

    Visualize the "Raw Income" vs. "Log-Transformed Income" side-by-side to demonstrate the effect of the transformation.
"""