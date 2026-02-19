"""
Task:
    You are provided with a dataset containing user session data (pages_viewed, session_minutes, basket_value, city, and device_type). Your goal is to build a robust machine learning pipeline following these requirements:

    
1-Feature Interaction: Create at least two new engineered features:

    A ratio feature named pages_per_min to capture "engagement intensity".

    A composite feature named is_mobile_high_spend that combines categorical and numerical data.

    
2-Model Pipeline:

    Define a Baseline set of features and an Enhanced set of features.

    Split the data into training and testing sets to avoid feature leakage.

    Train a LogisticRegression model and evaluate its performance using the AUC score.


    
3-Ethical Evaluation: * Perform a Subgroup Performance check to evaluate the model's fairness across different device_type categories.

    Ensure the code flags if performance differs significantly between groups
"""