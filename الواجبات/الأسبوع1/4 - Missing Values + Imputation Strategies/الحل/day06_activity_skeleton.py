import pandas as pd

df = pd.read_csv('day06_user_data.csv')

print("Original Data Size:", df.shape)

df = df.dropna()

df = df.drop_duplicates(subset=['email'])


df['signup_date'] = pd.to_datetime(df['signup_date'])


active_users = df[df['is_active'] == True]

active_users.to_csv('cleaned_users.csv', index=False)

print("Cleaned Data Size:", active_users.shape)
print("\nFirst few rows of cleaned data:")
print(active_users.head())