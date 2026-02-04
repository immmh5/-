import pandas as pd
import numpy as np

def clean_types(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['income'] = pd.to_numeric(df['income'], errors='coerce')
    return df

def clean_missing(df):
    df['age'] = df['age'].fillna(df['age'].median())
    df['income'] = df['income'].fillna(df['income'].median())
    df['city'] = df['city'].fillna('Unknown')
    return df

def handle_outliers(df):
    df['age'] = df['age'].clip(lower=0, upper=100)
    upper_limit = df['income'].quantile(0.95)
    df['income'] = df['income'].clip(upper=upper_limit)
    return df

def clean_strings_and_dates(df):
    df['city'] = df['city'].str.strip().str.upper()
    df['signup_time'] = pd.to_datetime(df['signup_time'], errors='coerce')
    return df

def validate_cleaned(df):
    print("Missing values count:")
    print(df.isnull().sum())
    print("\nData description:")
    print(df.describe())
    return df

def clean_data(df):
    df = clean_types(df)
    df = clean_strings_and_dates(df)
    df = handle_outliers(df)
    df = clean_missing(df)
    df = validate_cleaned(df)
    return df

df_raw = pd.read_csv('day14_users_raw.csv')
df_cleaned = clean_data(df_raw)

print("\nFinal Cleaned Data:")
print(df_cleaned)

df_cleaned.to_csv('final_cleaned_users.csv', index=False)