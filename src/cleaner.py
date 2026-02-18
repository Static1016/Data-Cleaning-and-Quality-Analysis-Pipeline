import pandas as pd
import numpy as np
from datetime import datetime

# Load path of the dataset
def load_data(path):
    mh = pd.read_csv(path)
    return mh

# Normalize column names by making them lowercase and replacing spaces with underscores
def clean_column_names(mh):
    mh.columns = mh.columns.str.lower().str.strip().str.replace(' ', '_') # Make column names lowercase and replaces spaces with ' _ '
    return mh

# Naam padke samaj jao
def handle_missing_values_and_types(mh):

    # Replace common missing value indicators with np.nan
    mh.replace(['N/A', 'na', '', 'null'], np.nan, inplace=True)

    # Stating the numeric columns to convert to numeric type
    numeric_cols = [
        "area_sqft",
        "bedrooms",
        "bathrooms",
        "year_built",
        "price"
    ]

    # Convert columns to numeric tyoe
    for col in numeric_cols:
        mh[col] = pd.to_numeric(mh[col], errors='coerce') # Convert to numeric and corece errors to NaN

    # Fill missing numeric values with median
    for col in numeric_cols:
        mh[col].fillna(mh[col].median(), inplace=True)

    return mh

# Standardize location
def standardize_location(mh):

    # Convert location to string, lowercase and strip white spaces
    mh["location"] = (mh["location"].astype(str).str.lower().str.strip())

    # Map various location names to a standard format using the location_map dictionary
    location_map = {
        "austin": "austin",
        "san francisco": "san francisco",
        "sf": "san francisco",
        "la": "los angeles",
        "l.a.": "los angeles",
        "los angeles": "los angeles",
        "nyc": "new york",
        "new york city": "new york",
        "chicago": "chicago",
        "boston": "boston",
        "miami": "miami"
    }

    mh["location"] = mh["location"].replace(location_map)

    return mh

# Remove rows with invalid values such as negatives, zeros, etc
def remove_invalid_rows(mh):
    current_year = datetime.now().year

    mh = mh[mh["area_sqft"] > 0]
    mh = mh[mh["bedrooms"] > 0]
    mh = mh[mh["bathrooms"] > 0]
    mh = mh[mh["price"] > 0]
    mh = mh[mh["year_built"] <= current_year]

    return mh

# Remove outliers
def remove_outliers(mh):

    # Useing IQR method to remove outliers from price column
    q1 = mh["price"].quantile(0.25)
    q3 = mh["price"].quantile(0.75)
    iqr = q3 - q1

    # Upper and Lower bounds for outliers
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    # Filter the dataset to include only rows where price is within the upper and lower bounds
    mh = mh[(mh["price"] >= lower) & (mh["price"] <= upper)]

    return mh

# Determine house age and price per square feet
def house_age_and_ppsqft(mh):

    # Get the current year
    current_year = datetime.now().year

    mh["house_age"] = current_year - mh["year_built"]  #Calculate house age
    mh["price_per_sqft"] = mh["price"] / mh["area_sqft"]  #Calculate price per square feet

    return mh

# remove duplicates 
def remove_duplicates(mh):
    return mh.drop_duplicates()  # Delete duplicates from the dataset

def clean_data(input_path, output_path):

    mh = load_data(input_path)

    mh = clean_column_names(mh)
    mh = handle_missing_values_and_types(mh)
    mh = standardize_location(mh)
    mh = remove_invalid_rows(mh)
    mh = remove_outliers(mh)
    mh = house_age_and_ppsqft(mh)
    mh = remove_duplicates(mh)

    # Save the cleaned dataset 
    mh.to_csv(output_path, index=False) 

    print("Cleaning completed and dataset saved to: ", output_path)
    print("Final dataset shape: ", mh.shape)

    return mh