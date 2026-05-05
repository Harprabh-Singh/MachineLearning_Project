import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/processed/reliance_labeled.csv")

# -----------------------------
# Features (same as Phase 7)
# -----------------------------
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

# -----------------------------
# Split same as training
# -----------------------------
split_index = int(len(df) * 0.8)

test_df = df.iloc[split_index:].copy()

# -----------------------------
# Load trained model
# -----------------------------
# Instead of re-training, we simulate predictions again

from sklearn.ensemble import RandomForestClassifier

X = df[feature_columns]
y = df['LABEL']

X_train = X.iloc[:split_index]
y_train = y.iloc[:split_index]

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Generate Predictions
# -----------------------------
X_test = test_df[feature_columns]
test_df['PREDICTION'] = model.predict(X_test)

# -----------------------------
# Backtesting Logic
# -----------------------------
future_period = 5

test_df['EXIT_PRICE'] = test_df['Close'].shift(-future_period)

# Remove last rows (no future data)
test_df = test_df[:-future_period]

# Calculate returns
test_df['RETURN'] = (test_df['EXIT_PRICE'] - test_df['Close']) / test_df['Close']

# Apply trading logic
def calculate_profit(row):
    if row['PREDICTION'] == 1:
        return row['RETURN']   # Long
    elif row['PREDICTION'] == -1:
        return -row['RETURN']  # Short
    else:
        return 0  # No trade

test_df['STRATEGY_RETURN'] = test_df.apply(calculate_profit, axis=1)

# -----------------------------
# Performance Metrics
# -----------------------------
total_return = test_df['STRATEGY_RETURN'].sum()
win_rate = (test_df['STRATEGY_RETURN'] > 0).mean()

print("\n📊 BACKTEST RESULTS:\n")
print(f"Total Return: {total_return:.4f}")
print(f"Win Rate: {win_rate:.2%}")
print(f"Number of Trades: {(test_df['PREDICTION'] != 0).sum()}")

# -----------------------------
# Preview trades
# -----------------------------
print("\nSample Trades:\n")
print(test_df[['Date', 'Close', 'PREDICTION', 'STRATEGY_RETURN']].head())