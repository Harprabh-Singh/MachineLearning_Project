import pandas as pd
import os
import mplfinance as mpf

# -----------------------------
# Load dataset
# -----------------------------
df_ohlc = pd.read_csv("data/processed/reliance_with_indicators.csv")
df_labels = pd.read_csv("data/processed/reliance_labeled.csv")

# Merge on Date to get OHLC + LABEL
df = pd.merge(df_ohlc, df_labels[['Date', 'LABEL']], on='Date', how='inner')

# -----------------------------
# FIX COLUMN NAMES (VERY IMPORTANT)
# -----------------------------
print("Original Columns:", df.columns)

# Remove spaces if any
df.columns = df.columns.str.strip()

# Ensure correct names
df.rename(columns={
    'open': 'Open',
    'high': 'High',
    'low': 'Low',
    'close': 'Close',
    'volume': 'Volume'
}, inplace=True)

# If columns are already correct but capitalized differently
# enforce correct case
df.columns = [col.capitalize() for col in df.columns]

print("Fixed Columns:", df.columns)

# -----------------------------
# Check required columns
# -----------------------------
required_cols = ['Open', 'High', 'Low', 'Close']

for col in required_cols:
    if col not in df.columns:
        raise Exception(f"❌ Missing column: {col}")

# -----------------------------
# Prepare Data
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# -----------------------------
# Create folders
# -----------------------------
base_dir = "cv/images"

for label in ["buy", "sell", "hold"]:
    os.makedirs(os.path.join(base_dir, label), exist_ok=True)

# -----------------------------
# Parameters
# -----------------------------
window_size = 30
count = 0

# -----------------------------
# Generate images
# -----------------------------
for i in range(window_size, len(df) - 1):

    window = df.iloc[i - window_size:i]

    label = df.iloc[i]['Label']

    if label == 1:
        folder = "buy"
    elif label == -1:
        folder = "sell"
    else:
        folder = "hold"

    filename = os.path.join(base_dir, folder, f"chart_{i}.png")

    print(f"Saving: {filename}")

    try:
        mpf.plot(
            window,
            type='candle',
            style='charles',
            mav=(8, 21),
            volume=False,
            savefig=dict(fname=filename)
        )
        count += 1

    except Exception as e:
        print("Error:", e)
        continue

# -----------------------------
# Done
# -----------------------------
print(f"\n✅ Total images generated: {count}")