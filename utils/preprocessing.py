import pandas as pd
import numpy as np


# Clean installs column
# Example:
# 1,000+ -> 1000

def clean_installs(value):
    value = str(value)
    value = value.replace(',', '')
    value = value.replace('+', '')

    try:
        return int(value)
    except:
        return np.nan


# Clean size column
# Example:
# 12M -> 12
# 500k -> 0.48
def clean_size(value):
    value = str(value)

    if 'M' in value:
        return float(value.replace('M', ''))

    elif 'k' in value:
        return float(value.replace('k', '')) / 1024

    return np.nan


# Clean price
# Example:
# $5.99 -> 5.99

def clean_price(value):
    value = str(value).replace('$', '')
    try:
        return float(value)
    except:
        return 0


# Clean reviews

def clean_reviews(value):
    try:
        return int(value)
    except:
        return np.nan


# Main preprocessing function

def preprocess_data(df):

    df = df.copy()

    # Apply cleaning
    df['Installs'] = df['Installs'].apply(clean_installs)
    df['SizeMB'] = df['Size'].apply(clean_size)
    df['Price'] = df['Price'].apply(clean_price)
    df['Reviews'] = df['Reviews'].apply(clean_reviews)

    # Revenue calculation
    df['Revenue'] = df['Installs'] * df['Price']

    # Convert dates
    df['Last Updated'] = pd.to_datetime(
        df['Last Updated'],
        errors='coerce'
    )

    # Extract Android version
    df['Android Ver Numeric'] = (
        df['Android Ver']
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')[0]
        .astype(float)
    )

    return df