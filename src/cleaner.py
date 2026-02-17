import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_column_names(mh):
    mh.columns = mh.columns.str.lower().str.strip().str.replace(' ', '_') # Make column names lowercase and replaces spaces with ' _ '
    return mh

def handle_missing_values(mh):
    # Fill numerical data with median
    numeric_cols = mh.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        mh[col].fillna(mh[col].median(), inplace=True)  # Fills the missing value with the median of the column

    # Fill categorical data with mode
    cat_cols = mh.select_dtypes(include=['object']).columns
    for col in cat_cols:
        mh[col].fillna(mh[col].mode()[0], inplace=True)  # Fills the missing value with mode 

    return mh

def remove_duplicates(mh):
    return mh.drop_duplicates()  # Delete duplicates from the dataset

def clean_data(path):
    mh = load_data(path)
    mh = clean_column_names(mh)
    mh = handle_missing_values(mh)
    mh = remove_duplicates(mh)

    return mh