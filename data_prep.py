import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Load data from a CSV file
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

# Handle missing values
def handle_missing_values(df):
    # Impute numerical columns with mean
    num_imputer = SimpleImputer(strategy='mean')
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = num_imputer.fit_transform(df[num_cols])

    # Impute categorical columns with most frequent
    cat_imputer = SimpleImputer(strategy='most_frequent')
    cat_cols = df.select_dtypes(include=['object']).columns
    df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])

    return df

# Encode categorical variables
def encode_categorical(df):
    le = LabelEncoder()

    # Encode Geography and Gender
    df['Geography'] = le.fit_transform(df['Geography'])
    df['Gender'] = le.fit_transform(df['Gender'])

    return df
