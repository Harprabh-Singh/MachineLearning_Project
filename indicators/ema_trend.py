import numpy as np

def calculate_ema_trend_score(df):    #exponential moving average trend score

    score = []

    for i in range(len(df)):
        row = df.iloc[i]

        ema8 = row['EMA_8']
        ema21 = row['EMA_21']
        ema50 = row['EMA_50']
        ema200 = row['EMA_200']

        alignment_score = 0

        # Bullish stack
        if ema8 > ema21 > ema50 > ema200:
            alignment_score = 1
        # Bearish stack
        elif ema8 < ema21 < ema50 < ema200:
            alignment_score = -1
        else:
            alignment_score = 0

        # Distance normalization
        distance = abs(ema8 - ema21) / row['Close']

        score.append(alignment_score * distance)

    return np.array(score)
