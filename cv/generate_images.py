import pandas as pd
import os
import mplfinance as mpf

# -----------------------------
# Load datasets
# -----------------------------
df_ohlc = pd.read_csv("data/processed/reliance_with_indicators.csv")
df_labels = pd.read_csv("data/processed/reliance_labeled.csv")

# -----------------------------
# Merge OHLC + LABEL
# -----------------------------
df = pd.merge(df_ohlc, df_labels[['Date', 'LABEL']], on='Date', how='inner')

print("Columns:", df.columns)

# -----------------------------
# Ensure required columns exist
# -----------------------------
required_cols = ['Open', 'High', 'Low', 'Close', 'LABEL']

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

    label = df.iloc[i]['LABEL']   # ✅ correct column name

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