import pandas as pd


# Load Feature Dataset
df = pd.read_csv("data/processed/reliance_features.csv")

df['Date'] = pd.to_datetime(df['Date'])


# Define Future Horizon
future_period = 5  # days


# Calculate Future Return
df['FUTURE_CLOSE'] = df['Close'].shift(-future_period)

df['FUTURE_RETURN'] = (df['FUTURE_CLOSE'] - df['Close']) / df['Close']


# Create Labels
df['LABEL'] = 0  # HOLD

df.loc[df['FUTURE_RETURN'] > 0.03, 'LABEL'] = 1   # BUY
df.loc[df['FUTURE_RETURN'] < -0.03, 'LABEL'] = -1  # SELL


# Remove rows with future leakage
df = df[:-future_period]


# Save labeled dataset
df.to_csv("data/processed/reliance_labeled.csv", index=False)

print("✅ Labels created successfully.")
print(df[['Date', 'Close', 'FUTURE_RETURN', 'LABEL']].head())