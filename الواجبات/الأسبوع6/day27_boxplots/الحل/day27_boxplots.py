"""
Day 27 Activity Solution: Histograms & Boxplots
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "day27_boxplots.csv")
df = pd.read_csv(csv_path)

print("Data loaded successfully:")
print(df.head())

plt.figure(figsize=(6, 3))
df["score"].hist(bins=20, edgecolor="black")
plt.title("Score Histogram")
plt.tight_layout()
plt.savefig("score_histogram.png")
plt.close()
print("Saved score_histogram.png")

plt.figure(figsize=(6, 3))
sns.boxplot(x="group", y="score", data=df)
plt.title("Score by Group")
plt.tight_layout()
plt.savefig("score_boxplot.png")
plt.close()
print("Saved score_boxplot.png")

print("\nData Summary:")
print(df)