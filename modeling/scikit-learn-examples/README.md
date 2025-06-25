# Scikit-learn Examples

This folder contains examples demonstrating how to use scikit-learn for machine learning tasks, with a focus on working with pandas DataFrames and categorical data encoding.

## Index

1. [Creating a Python Environment](#1-creating-a-python-environment)
2. [Requirements](#2-requirements)
3. [Running the Examples](#3-running-the-examples)
4. [Examples Overview](#4-examples-overview)
   - [DataFrame Example](#41-dataframe-example-dataframe_examplepy)
   - [One-Hot Encoding Example](#42-one-hot-encoding-example-one_hot_encoding_examplepy)
   - [Complete ML Workflow](#43-complete-ml-workflow-complete_ml_workflowpy)

## 1. Creating a Python Environment

Follow these steps to set up a Python virtual environment for running the examples:

```bash
# Create a virtual environment
python3 -m venv venv

# Add virtual environment directory to .gitignore
echo "venv/" >> .gitignore

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
# Or install packages individually:
# pip install scikit-learn pandas numpy matplotlib
```

## 2. Requirements

To run these examples, you'll need:
- Python 3.6+
- scikit-learn
- pandas
- numpy
- matplotlib

You can create a `requirements.txt` file with the following content:

```
scikit-learn>=1.0.0
pandas>=1.3.0
numpy>=1.20.0
matplotlib>=3.4.0
```

Then install the requirements using:

```bash
pip install -r requirements.txt
```

## 3. Running the Examples

Each example can be run as a standalone Python script:

```bash
python dataframe_example.py
python one_hot_encoding_example.py
python complete_ml_workflow.py
```

The examples include print statements that explain what's happening at each step, making them suitable for educational purposes.

## 4. Examples Overview

### 4.1 DataFrame Example (`dataframe_example.py`)

This example demonstrates how to use pandas DataFrames with scikit-learn:
- Creating and manipulating DataFrames
- Using DataFrames with scikit-learn's machine learning models
- Basic linear regression with synthetic data
- Feature engineering with DataFrames

**Key concepts covered:**
- DataFrame creation and manipulation
- Train-test splitting with pandas data
- Linear regression modeling
- Model evaluation metrics
- Basic feature engineering

### 4.2 One-Hot Encoding Example (`one_hot_encoding_example.py`)

This example shows how to handle categorical features using one-hot encoding:
- Creating a dataset with categorical features
- Two methods for one-hot encoding:
  - Using OneHotEncoder directly
  - Using ColumnTransformer and Pipeline
- Training a RandomForest classifier with encoded data

**Key concepts covered:**
- Categorical data handling
- One-hot encoding implementation
- Pipeline creation for preprocessing
- Classification with encoded features
- Model evaluation

### 4.3 Complete ML Workflow (`complete_ml_workflow.py`)

This comprehensive example demonstrates a full machine learning workflow:
- Data loading and exploration (using the Titanic dataset)
- Handling missing values
- Preprocessing numerical and categorical features
- Model training and evaluation
- Cross-validation
- Hyperparameter tuning
- Feature importance analysis

**Key concepts covered:**
- End-to-end ML pipeline creation
- Data preprocessing for mixed data types
- Missing value imputation
- Feature scaling
- Model selection and evaluation
- Hyperparameter optimization
- Feature importance interpretation

