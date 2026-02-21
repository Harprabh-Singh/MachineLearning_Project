import pandas as pd

from ema import calculate_ema
from ema_trend import calculate_ema_trend_score
from rsi import calculate_rsi
from smi import calculate_smi


# -----------------------------
# Load Cleaned Data
# -----------------------------
df = pd.read_csv("data/processed/reliance_clean.csv")

# Ensure Date is datetime
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# Calculate EMAs
# -----------------------------
df['EMA_8'] = calculate_ema(df, 8)
df['EMA_21'] = calculate_ema(df, 21)
df['EMA_50'] = calculate_ema(df, 50)
df['EMA_200'] = calculate_ema(df, 200)

# -----------------------------
# Calculate EMA Trend Score
# -----------------------------
df['EMA_TREND_SCORE'] = calculate_ema_trend_score(df)

# -----------------------------
# Calculate RSI
# -----------------------------
df['RSI_14'] = calculate_rsi(df, 14)

# -----------------------------
# Calculate SMI
# -----------------------------
df['SMI'] = calculate_smi(df, period=14, smooth=3)

# -----------------------------
# Drop NaNs from indicator warm-up periods
# -----------------------------
df = df.dropna()

# -----------------------------
# Quick sanity check
# -----------------------------
print(df[['Date', 'Close', 'EMA_TREND_SCORE', 'RSI_14', 'SMI']].head())

# -----------------------------
# Save Updated File
# -----------------------------
df.to_csv("data/processed/reliance_with_indicators.csv", index=False)

print("✅ Indicators calculated and saved successfully.")
