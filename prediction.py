import os
import pandas as pd
import mplfinance as mpf
from sklearn.ensemble import RandomForestClassifier

FEATURE_COLUMNS = [
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

LABEL_NAME = {
    1: 'BUY',
    0: 'HOLD',
    -1: 'SELL'
}

PREDICTION_IMAGE_PATH = os.path.join('cv', 'prediction_latest.png')


def load_data():
    labeled_path = os.path.join('data', 'processed', 'reliance_labeled.csv')
    features_path = os.path.join('data', 'processed', 'reliance_features.csv')
    indicators_path = os.path.join('data', 'processed', 'reliance_with_indicators.csv')

    missing = [p for p in [labeled_path, features_path, indicators_path] if not os.path.exists(p)]
    if missing:
        raise FileNotFoundError(f'Missing required dataset file(s): {missing}')

    df_labeled = pd.read_csv(labeled_path)
    df_features = pd.read_csv(features_path)
    df_indicators = pd.read_csv(indicators_path)

    return df_labeled, df_features, df_indicators


def train_classifier(df):
    X = df[FEATURE_COLUMNS]
    y = df['LABEL']

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X, y)
    return model


def build_prediction_image(window_df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    window_df = window_df.copy()
    window_df['Date'] = pd.to_datetime(window_df['Date'])
    window_df.set_index('Date', inplace=True)

    mpf.plot(
        window_df[['Open', 'High', 'Low', 'Close']],
        type='candle',
        style='charles',
        mav=(8, 21),
        volume=False,
        savefig=dict(fname=output_path)
    )


def main():
    df_labeled, df_features, df_indicators = load_data()

    model = train_classifier(df_labeled)

    latest_feature_window = df_features.tail(5).reset_index(drop=True)
    latest_window = df_indicators.tail(5).reset_index(drop=True)

    predictions = model.predict(latest_feature_window[FEATURE_COLUMNS])
    latest_window = latest_window.copy()
    latest_window['PREDICTION'] = [LABEL_NAME[p] for p in predictions]

    current_prediction = latest_window.loc[len(latest_window) - 1, 'PREDICTION']
    current_date = latest_window.loc[len(latest_window) - 1, 'Date']

    print('=== Latest 5-Day Prediction Window ===')
    print(latest_window[['Date', 'Close', 'PREDICTION']].to_string(index=False))
    print()
    print(f'Current recommendation for {current_date}: {current_prediction}')
    print(f'Prediction image saved at: {PREDICTION_IMAGE_PATH}')

    build_prediction_image(latest_window, PREDICTION_IMAGE_PATH)


if __name__ == '__main__':
    main()
