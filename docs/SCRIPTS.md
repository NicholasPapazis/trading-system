# Script Documentation

## download_data.py

### Purpose 
Fetches historical price data for a given ticker and saves it locally for use in the trading system.

### Behavior

- Calls `yf.download()` to retrieve OHLCV data.
- Saves the result to `data/raw/{ticker}.csv`.
- Prints a confirmation message after saving. 

### Main Guard

The script includes: 
```python
if __name__ == "__main__":
    download_data()
```

## clean_data.py

### Purpose
Loads raw Yahoo Finance CSVs, cleans them, and outputs standardized processed files.

### Behavior

- uses `header=2` to skip metadata rows.
- ensures consistent naming across tickers by renaming the columns
- adds a `returns` column based on close price.
- Saves cleaned data to `data/processed/{ticker}_clean.csv`.
- includes main guard just like `download_data.py`