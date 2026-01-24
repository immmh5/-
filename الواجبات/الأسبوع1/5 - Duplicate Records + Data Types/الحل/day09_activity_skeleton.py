import pandas as pd

df = pd.read_csv('day09_schema_raw.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-zA-Z0-9_]', '', regex=True)

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()

df = df.drop_duplicates()

df = df.dropna()

print(df.info())
print(df.head())

df.to_csv('day09_cleaned.csv', index=False)