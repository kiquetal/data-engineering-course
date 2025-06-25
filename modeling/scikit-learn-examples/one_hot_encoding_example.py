# One-Hot Encoding with Scikit-learn Example
# This example demonstrates how to use one-hot encoding for categorical features

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Create a sample DataFrame with categorical features
np.random.seed(42)
n_samples = 200

# Generate synthetic data
categories = ['red', 'green', 'blue', 'yellow']
sizes = ['small', 'medium', 'large']
shapes = ['circle', 'square', 'triangle']

# Create random categorical features
color = np.random.choice(categories, size=n_samples)
size = np.random.choice(sizes, size=n_samples)
shape = np.random.choice(shapes, size=n_samples)

# Create a numerical feature
numerical_feature = np.random.rand(n_samples)

# Create a target variable (binary classification)
# Let's say red circles are more likely to be class 1
target = np.zeros(n_samples, dtype=int)
for i in range(n_samples):
    if color[i] == 'red' and shape[i] == 'circle':
        target[i] = 1 if np.random.rand() < 0.8 else 0
    elif color[i] == 'blue' and size[i] == 'large':
        target[i] = 1 if np.random.rand() < 0.7 else 0
    else:
        target[i] = 1 if np.random.rand() < 0.3 else 0

# Create DataFrame
df = pd.DataFrame({
    'color': color,
    'size': size,
    'shape': shape,
    'numerical_feature': numerical_feature,
    'target': target
})

print("Sample DataFrame with categorical features:")
print(df.head())
print("\nFeature value counts:")
print("Color values:", df['color'].value_counts())
print("Size values:", df['size'].value_counts())
print("Shape values:", df['shape'].value_counts())
print("Target distribution:", df['target'].value_counts())

# Method 1: Using OneHotEncoder directly
print("\nMethod 1: Using OneHotEncoder directly")
encoder = OneHotEncoder(sparse_output=False)
encoded_features = encoder.fit_transform(df[['color', 'size', 'shape']])
feature_names = encoder.get_feature_names_out(['color', 'size', 'shape'])

# Create a new DataFrame with encoded features
encoded_df = pd.DataFrame(encoded_features, columns=feature_names)
encoded_df['numerical_feature'] = df['numerical_feature']
encoded_df['target'] = df['target']

print("\nDataFrame after one-hot encoding (first 5 rows, first 10 columns):")
print(encoded_df.iloc[:5, :10])
print(f"Shape after encoding: {encoded_df.shape}")

# Method 2: Using ColumnTransformer and Pipeline
print("\nMethod 2: Using ColumnTransformer and Pipeline")
# Define which columns should be encoded
categorical_features = ['color', 'size', 'shape']
numerical_features = ['numerical_feature']

# Create preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(sparse_output=False), categorical_features),
        ('num', 'passthrough', numerical_features)
    ])

# Create a pipeline with preprocessing and model
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Split the data
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nThis example demonstrates how to:")
print("1. Handle categorical features using one-hot encoding")
print("2. Use OneHotEncoder directly on selected columns")
print("3. Use ColumnTransformer and Pipeline for a more streamlined workflow")
print("4. Train a model with encoded categorical features")
