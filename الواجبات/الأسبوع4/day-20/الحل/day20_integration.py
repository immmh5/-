import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
import os

df20 = pd.read_csv("day20_integration.csv")

df20["pages_per_min"] = df20["pages_viewed"] / (df20["session_minutes"] + 1e-3)

median_basket = df20["basket_value"].median()
df20["is_mobile_high_spend"] = (
    (df20["device_type"] == "mobile") & (df20["basket_value"] > median_basket)
).astype(int)

base_features = ["pages_viewed", "session_minutes", "basket_value"]
engineered_features = base_features + ["pages_per_min", "is_mobile_high_spend"]
target = "converted"

X_train, X_test, y_train, y_test = train_test_split(
    df20[engineered_features], df20[target], test_size=0.3, random_state=42
)

clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
auc_score = roc_auc_score(y_test, clf.predict_proba(X_test)[:, 1])

print(f"\nAUC مع الميزات المهندسة: {auc_score:.3f}")

print("\n--- تقييم العدالة (Subgroup Performance) ---")

test_results = X_test.copy()
test_results[target] = y_test
test_results["pred"] = clf.predict_proba(X_test)[:, 1]

test_results["device_type"] = df20.loc[X_test.index, "device_type"]

for device in test_results["device_type"].unique():
    mask = test_results["device_type"] == device

    if len(test_results.loc[mask, target].unique()) > 1:
        auc_sub = roc_auc_score(test_results.loc[mask, target], test_results.loc[mask, "pred"])
        print(f"Device {device}: AUC = {auc_sub:.3f}")
    else:
        print(f"Device {device}: لا توجد بيانات كافية للحساب")