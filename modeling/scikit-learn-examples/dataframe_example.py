# Pandas DataFrame with Scikit-learn Example
# This example demonstrates how to use pandas DataFrames with scikit-learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create a sample DataFrame
np.random.seed(42)
n_samples = 100

# Generate synthetic data
X = np.random.rand(n_samples, 3)  # 3 features
y = 2 * X[:, 0] + 0.5 * X[:, 1] - 1.5 * X[:, 2] + np.random.normal(0, 0.2, n_samples)  # Target with noise

# Convert to pandas DataFrame
df = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3'])
df['target'] = y

print("Sample DataFrame:")
print(df.head())
print("\nDataFrame info:")
print(df.info())
print("\nDataFrame statistics:")
print(df.describe())

# Split the data into features and target
X = df.drop('target', axis=1)
y = df['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set shape: {X_train.shape}")
print(f"Testing set shape: {X_test.shape}")

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

print(f"\nModel Evaluation:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Example of using the DataFrame for feature engineering
print("\nFeature Engineering Example:")
df['feature1_squared'] = df['feature1'] ** 2
df['feature1_feature2_interaction'] = df['feature1'] * df['feature2']

print(df.head())

print("\nThis example demonstrates how to:")
print("1. Create and manipulate pandas DataFrames")
print("2. Use DataFrames with scikit-learn's machine learning models")
print("3. Perform basic feature engineering with DataFrames")
