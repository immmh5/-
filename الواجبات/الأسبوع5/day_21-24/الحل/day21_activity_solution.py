import pandas as pd
import numpy as np

df = pd.read_csv("data/day21_housing.csv")

df["price_per_sqft"] = df["price"] / df["sqft"].replace(0, np.nan)
df["price_per_sqft"] = df["price_per_sqft"].fillna(df["price_per_sqft"].median())

df["bedrooms_per_sqft"] = (df["bedrooms"] / df["sqft"].replace(0, np.nan)).fillna(0.0)

df["bathrooms_per_bedroom"] = df["bathrooms"] / df["bedrooms"].replace(0, np.nan)
df["bathrooms_per_bedroom"] = df["bathrooms_per_bedroom"].fillna(df["bathrooms_per_bedroom"].median())

print(df[["price", "sqft", "price_per_sqft", "bedrooms_per_sqft", "bathrooms_per_bedroom"]].head())