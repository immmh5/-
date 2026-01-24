import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

train_df = pd.read_csv('day07_train.csv')
test_df = pd.read_csv('day07_test.csv')

print("Columns:", train_df.columns)

X_train = train_df[['x']] 
y_train = train_df['y']

X_test = test_df[['x']]
y_test = test_df['y']

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)

print(f"Model Coefficient (Slope): {model.coef_[0]}")
print(f"Mean Squared Error: {mse}")

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
print("\nComparison (First 5 rows):")
print(comparison.head())