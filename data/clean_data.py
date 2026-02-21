import pandas as pd

# Skip first 2 invalid rows (Ticker + Date row)
df = pd.read_csv("data/raw/reliance_daily.csv", skiprows=2)

# Rename columns properly
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Date
df = df.sort_values('Date')

# Drop missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print(df.info())
print(df.head())

# Save cleaned file
df.to_csv("data/processed/reliance_clean.csv", index=False)

print("Cleaned data saved successfully.")
