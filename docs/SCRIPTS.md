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