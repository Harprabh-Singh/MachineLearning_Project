import pandas as pd

# Load Feature Dataset
df = pd.read_csv("data/processed/reliance_features.csv")

df['Date'] = pd.to_datetime(df['Date'])

# Future Horizon
future_period = 5  # days

# Calculate Future Return
df['FUTURE_CLOSE'] = df['Close'].shift(-future_period)

df['FUTURE_RETURN'] = (df['FUTURE_CLOSE'] - df['Close']) / df['Close']

# Create Labels (IMPROVED)
df['LABEL'] = 0  # HOLD

# LOWER thresholds → more balanced dataset
df.loc[df['FUTURE_RETURN'] > 0.01, 'LABEL'] = 1   # BUY
df.loc[df['FUTURE_RETURN'] < -0.01, 'LABEL'] = -1  # SELL

# Remove future leakage rows
df = df[:-future_period]

# Show label distribution
print("Label Distribution:")
print(df['LABEL'].value_counts())

# Save dataset
df.to_csv("data/processed/reliance_labeled.csv", index=False)

print("✅ Labels created successfully.")