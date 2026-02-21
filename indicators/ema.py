import pandas as pd

def calculate_ema(df, period):
    return df['Close'].ewm(span=period, adjust=False).mean()
