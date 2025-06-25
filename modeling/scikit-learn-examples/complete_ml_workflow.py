# Complete Machine Learning Workflow with Scikit-learn
# This example demonstrates a full ML workflow including data preprocessing,
# feature engineering, model training, and evaluation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.datasets import fetch_openml

# Load a real dataset (Titanic dataset)
print("Loading Titanic dataset...")
try:
    # Try to load from scikit-learn datasets
    titanic = fetch_openml(name='titanic', version=1, as_frame=True)
    df = titanic.data
    df['survived'] = titanic.target
except:
    # If that fails, create a synthetic version with similar properties
    print("Could not load Titanic dataset, creating synthetic data instead...")
    np.random.seed(42)
    n_samples = 891  # Same as original Titanic dataset

    # Generate synthetic data
    age = np.random.normal(30, 14, n_samples)
    age[np.random.choice(n_samples, size=int(n_samples*0.2))] = np.nan  # Add missing values

    fare = np.random.exponential(30, n_samples)
    sex = np.random.choice(['male', 'female'], size=n_samples, p=[0.65, 0.35])
    pclass = np.random.choice([1, 2, 3], size=n_samples, p=[0.25, 0.2, 0.55])
    embarked = np.random.choice(['C', 'Q', 'S'], size=n_samples, p=[0.2, 0.1, 0.7])
    embarked[np.random.choice(n_samples, size=2)] = np.nan  # Add missing values

    # Create synthetic target based on features (similar to Titanic survival patterns)
    survived = np.zeros(n_samples, dtype=int)
    for i in range(n_samples):
        survival_prob = 0.3  # Base survival rate
        if sex[i] == 'female':
            survival_prob += 0.5  # Women had higher survival rates
        if pclass[i] == 1:
            survival_prob += 0.3  # First class had higher survival rates
        elif pclass[i] == 2:
            survival_prob += 0.1  # Second class had moderate survival rates
        if age[i] < 10 and not np.isnan(age[i]):
            survival_prob += 0.3  # Children had higher survival rates

        survived[i] = 1 if np.random.rand() < min(survival_prob, 0.95) else 0

    # Create DataFrame
    df = pd.DataFrame({
        'pclass': pclass,
        'sex': sex,
        'age': age,
        'fare': fare,
        'embarked': embarked,
        'survived': survived
    })

# Display dataset information
print("\nDataset Overview:")
print(f"Shape: {df.shape}")
print("\nSample data:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nTarget distribution:")
print(df['survived'].value_counts(normalize=True))

# Data Preprocessing
print("\n--- Data Preprocessing ---")

# Select features and target
X = df.drop('survived', axis=1)
y = df['survived']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set shape: {X_train.shape}")
print(f"Testing set shape: {X_test.shape}")

# Define preprocessing for numerical and categorical features
numerical_features = ['age', 'fare']
categorical_features = ['pclass', 'sex', 'embarked']

# Create preprocessing pipelines
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create the full pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Model Training and Evaluation
print("\n--- Model Training and Evaluation ---")

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Cross-validation
cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')
print(f"\nCross-validation scores: {cv_scores}")
print(f"Mean CV accuracy: {cv_scores.mean():.4f}")

# Hyperparameter Tuning
print("\n--- Hyperparameter Tuning ---")
print("(This would normally be a more extensive grid, but we're keeping it simple for this example)")

param_grid = {
    'classifier__n_estimators': [50, 100],
    'classifier__max_depth': [None, 10]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.4f}")

# Evaluate the best model
best_model = grid_search.best_estimator_
y_pred_best = best_model.predict(X_test)
accuracy_best = accuracy_score(y_test, y_pred_best)
print(f"Best model accuracy on test set: {accuracy_best:.4f}")

# Feature Importance
print("\n--- Feature Importance ---")
# Get feature names after preprocessing
feature_names = []
for name, transformer, features in preprocessor.transformers_:
    if name == 'cat':
        # Get the one-hot encoded feature names
        feature_names.extend(transformer.named_steps['onehot'].get_feature_names_out(features))
    else:
        # Add the numerical feature names
        feature_names.extend(features)

# Get feature importances from the model
importances = best_model.named_steps['classifier'].feature_importances_

# Sort feature importances
indices = np.argsort(importances)[::-1]

print("Feature ranking:")
for i, idx in enumerate(indices[:10]):  # Print top 10 features
    if i < len(feature_names):
        print(f"{i+1}. {feature_names[idx]} ({importances[idx]:.4f})")

print("\nThis example demonstrates a complete machine learning workflow:")
print("1. Data loading and exploration")
print("2. Handling missing values")
print("3. Preprocessing numerical and categorical features")
print("4. Model training and evaluation")
print("5. Cross-validation")
print("6. Hyperparameter tuning")
print("7. Feature importance analysis")
