import pandas as pd

def calculate_ema(df, period):  #Exponential Moving Average
    return df['Close'].ewm(span=period, adjust=False).mean()
