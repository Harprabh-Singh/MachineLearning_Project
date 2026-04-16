import pandas as pd

def calculate_smi(df, period=14, smooth=3):   #Stochastic Momentum Index

    high_max = df['High'].rolling(period).max()
    low_min = df['Low'].rolling(period).min()

    midpoint = (high_max + low_min) / 2
    distance = df['Close'] - midpoint

    distance_ema = distance.ewm(span=smooth, adjust=False).mean()
    range_ema = (high_max - low_min).ewm(span=smooth, adjust=False).mean()

    smi = 100 * (distance_ema / (range_ema / 2))

    return smi
