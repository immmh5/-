import pandas as pd


raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}




df = pd.DataFrame(raw)

df['price'] = df['price'].apply(lambda x: float(x.replace('$', '').replace(',', '')))
df['quantity'] = df['quantity'].fillna(0)
df['total'] = df['price'] * df['quantity']
df['price_category'] = df['price'].apply(lambda x: 'High' if x > 2000 else ('Medium' if x >= 1000 else 'Low'))

print(df)