import pandas as pd

# Create additional features
def create_features(df):
    # Add additional features here...
    return df

# Select features for modeling
def select_features(df):
    features = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    target = 'Exited'
    return df[features], df[target]


