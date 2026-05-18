# 📈 ML-Driven Stock Analysis — Updated

This repository provides a reproducible, offline pipeline that converts raw OHLCV data into labeled datasets and (optionally) CV images for downstream modeling and backtesting.


## Quick Start — Run the full preprocessing pipeline

run pip install -r requirements.txt and then - 

1. Place your raw CSV (OHLCV) file somewhere accessible.
2. From the repository root run:

```bash
python run_pipeline.py --raw-csv path/to/your_dataset.csv
```

Notes:
- If `--raw-csv` is omitted, the pipeline expects `data/raw/reliance_daily.csv`.
- The script runs these steps in order:
	- `data/clean_data.py`
	- `indicators/build_indicators.py`
	- `features/build_features.py`
	- `labels/create_labels.py`
	- `cv/generate_images.py`

After completion the main labeled dataset is saved to `data/processed/reliance_labeled.csv` and images (if generated) are under `cv/images/`.

---

## Project layout (current)

stock_ml_project/
├── backtest/
│   └── simple_backtest.py
├── cv/
│   ├── generate_images.py
│   ├── train_cnn.py
│   └── images/
│       ├── buy/
│       ├── hold/
│       └── sell/
├── data/
│   ├── raw/
│   │   └── reliance_daily.csv (example)
│   └── processed/
│       └── reliance_labeled.csv
├── features/
│   └── build_features.py
├── indicators/
│   ├── build_indicators.py
│   ├── ema.py
│   ├── ema_trend.py
│   ├── rsi.py
│   └── smi.py
├── labels/
│   └── create_labels.py
├── models/
│   └── train_model.py
├── fusion/
│   └── simple_fusion.py
├── run_pipeline.py
├── main.py
├── README.md

---

## Dependencies

Install the typical data science stack (adjust versions as needed):

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
```

Add any other packages shown by import errors (e.g., CV libraries) as needed.

---

## Useful commands

- Run full preprocessing pipeline:

```bash
python run_pipeline.py --raw-csv data/raw/reliance_daily.csv
```

- Run individual pipeline steps (examples):

```bash
python data/clean_data.py
python indicators/build_indicators.py
python features/build_features.py
python labels/create_labels.py
python cv/generate_images.py
```

---

## Outputs

- Labeled CSV: `data/processed/reliance_labeled.csv`
- CV images: `cv/images/` (subfolders: `buy`, `hold`, `sell`)

---

## Notes & Caveats

- This is a research / learning project — not investment advice.
- The pipeline scripts are designed to be run locally and expect realistic, cleaned OHLCV CSVs.

## Authors - 

- Harprabh Singh Nanda and Hridayjit Singh Nanda