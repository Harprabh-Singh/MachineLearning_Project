# 📈 ML-Driven Stock Analysis with Indicator Fusion

## 🚀 Project Overview

This project is a machine learning–based stock analysis system that generates **Buy / Sell / Hold signals** using technical indicators and data-driven modeling.

Unlike traditional rule-based trading systems, this project:
- Learns patterns from historical data
- Uses engineered features instead of raw indicators
- Avoids data leakage and unrealistic assumptions
- Is fully offline and reproducible

---

## 🎯 Objectives

- Analyze stock data using technical indicators
- Convert indicators into machine learning features
- Generate supervised learning labels using future returns
- Build a clean ML pipeline for stock signal classification

---

## 🧠 Key Features

- 📊 EMA Trend Meter (custom implementation)
- 📉 RSI (Relative Strength Index)
- ⚡ SMI (Stochastic Momentum Index)
- 🧮 Feature engineering pipeline
- 🏷️ Buy/Sell/Hold label generation (no leakage)
- 📁 Fully modular and structured codebase

---

## 🏗️ Project Structure

stock_ml_project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── indicators/
│   ├── ema.py
│   ├── ema_trend.py
│   ├── rsi.py
│   ├── smi.py
│   └── build_indicators.py
│
├── features/
│   └── build_features.py
│
├── labels/
│   └── create_labels.py
│
├── docs/
│   └── problem_definition.md
│
├── .gitignore
└── README.md

---

# ✅ Completed Phases

### 🔵 Phase 1 — Problem Definition
- Defined system scope and limitations
- Offline ML-based stock signal system

### 🔵 Phase 2 — Data Collection
- Historical OHLCV data collected
- Stored locally for reproducibility

### 🔵 Phase 3 — Data Cleaning
- Removed missing values and duplicates
- Sorted data chronologically
- Addressed bias considerations

### 🔵 Phase 4 — Indicator Computation
- EMA (8, 21, 50, 200)
- EMA Trend Score
- RSI (14)
- SMI

### 🔵 Phase 5 — Feature Engineering
- Trend, momentum, and volatility features created
- Converted indicators → ML-ready features

### 🔵 Phase 6 — Label Generation
- Buy/Sell/Hold labels based on future returns
- No data leakage

---

# ⚙️ Setup Instructions (Run on Any Laptop)

## 🔹 Step 1 — Clone Repository

git clone https://github.com/YOUR_USERNAME/stock-ml-analysis.git
cd stock-ml-analysis

---

## 🔹 Step 2 — Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

---

## 🔹 Step 3 — Install Dependencies

pip install pandas numpy yfinance scikit-learn matplotlib

---

## 🔹 Step 4 — Add Data

Download from Yahoo Finance and place in:
data/raw/reliance_daily.csv

---

## 🔹 Step 5 — Clean Data

python data/clean_data.py

---

## 🔹 Step 6 — Build Indicators

python indicators/build_indicators.py

---

## 🔹 Step 7 — Generate Features

python features/build_features.py

---

## 🔹 Step 8 — Create Labels

python labels/create_labels.py

---

# 📊 Pipeline Overview

Raw Data → Clean Data → Indicators → Features → Labels

---

# ⚠️ Important Notes

- This project does NOT guarantee profits
- Not financial advice
- Intended for learning and research

---

# 🔜 Upcoming Work

- Machine Learning Models
- Backtesting
- Computer Vision Integration

---

# 🧰 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn

---

# 👨‍💻 Authors

Harprabh Singh Nanda and Hridayjit Singh Nanda