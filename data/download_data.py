import yfinance as yf

ticker = "RELIANCE.NS"  # Example Indian stock

data = yf.download(
    ticker,
    start="2022-01-01",
    end="2024-01-01",
    interval="1d"
)

data.to_csv("data/raw/reliance_daily.csv")

print("Download complete")
