"""
Day 3 Activity: Use lambda and .apply() to clean a dataset.
Tasks:
1) Clean price (remove $ and commas)
2) Fill missing quantity with 0
3) Create total = price * quantity
4) Categorize price: low / med / high
"""

import pandas as pd

# Sample dataset
raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}

df = pd.DataFrame(raw)

# TODO: Clean price column using .apply with lambda.
# TODO: Fill missing quantity with 0.
# TODO: Create total column.
# TODO: Add price_category column (low/med/high).

# print(df)
