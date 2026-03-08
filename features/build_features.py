import pandas as pd

# Load Data With Indicators
df = pd.read_csv("data/processed/reliance_with_indicators.csv")

df['Date'] = pd.to_datetime(df['Date'])

# EMA Features

df['EMA_DIFF_8_21'] = df['EMA_8'] - df['EMA_21']

df['EMA_DIFF_21_50'] = df['EMA_21'] - df['EMA_50']

df['EMA_DISTANCE_CLOSE_21'] = (df['Close'] - df['EMA_21']) / df['Close']


# Trend Features

df['EMA_SLOPE_21'] = df['EMA_21'].diff()

df['EMA_TREND_STRENGTH'] = df['EMA_TREND_SCORE']


# Momentum Features

df['RSI'] = df['RSI_14']

df['RSI_SLOPE'] = df['RSI_14'].diff()

df['SMI_SLOPE'] = df['SMI'].diff()


# Volatility Feature

df['PRICE_RANGE'] = (df['High'] - df['Low']) / df['Close']


# Drop NaN rows from diff()

df = df.dropna()


# Select ML Feature Columns

feature_columns = [
    'EMA_DIFF_8_21',
    'EMA_DIFF_21_50',
    'EMA_DISTANCE_CLOSE_21',
    'EMA_SLOPE_21',
    'EMA_TREND_STRENGTH',
    'RSI',
    'RSI_SLOPE',
    'SMI',
    'SMI_SLOPE',
    'PRICE_RANGE'
]

features_df = df[['Date', 'Close'] + feature_columns]


# Save Feature Dataset

features_df.to_csv("data/processed/reliance_features.csv", index=False)

print("✅ Feature engineering complete.")
print(features_df.head())