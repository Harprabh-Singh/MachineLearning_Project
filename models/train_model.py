import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Load Dataset
df = pd.read_csv("data/processed/reliance_labeled.csv")

# Feature Columns
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

X = df[feature_columns]
y = df['LABEL']

# Label Distribution (Check)
print("\nLabel Distribution:")
print(y.value_counts())

# Time-based Train-Test Split
split_index = int(len(df) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Model (Phase 7 Standard)
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

print("📊 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))