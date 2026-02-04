import pandas as pd
import numpy as np


df = pd.read_csv('day11_income.csv')


def winsorize_series(s, lower_q, upper_q):
    lower_limit = s.quantile(lower_q)
    upper_limit = s.quantile(upper_q)

print("-" * 65)
print(f"done\n{df}")
print("-" * 65)
