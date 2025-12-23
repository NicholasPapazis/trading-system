# Data Pipeline 

## Data Module Overview

- **purpose**: The data module handles downloading and storing raw market data for later use in backtesting and future generation.
- **components**:
    - `download_data()` function for fetching ticker data
    - `data/raw/` directory for persistent storage
- **design choice**: Using `pathlib.Path` ensures OS-independent file handling and clean path joining.
- **execution behavior**: The script uses a `__main__` guard so it can be run directly or imported without triggering a download. 


## Data Cleaning and Pipeline Processing

- **skip metadata rows**: The raw Yahoo Finance CSV includes two metadata rows; we load the file using `header=2` to use the correct header row.
- **column normalization**: Columns are renamed to a consistent schema: `close`, `high`, `low`, `open`, `volume`.
- **date parsing**: The index is converted to a proper `DatetimeIndex` for time-series operations.
- **missing data handling**: Rows with missing values are dropped.
- **returns calculation**: A new `returns` column is added using percentage change of the close price.
- **processed output**: Cleaned data is saved to `data/processed/{ticker}_clean.csv`

## Processed Data -> Strategy Input

The processed data pipeline produces standardized price series that are directly comsumed by strategy functions. 

### Guarantees for Strategy Functions
- Index is a proper `DatetimeIndex`
- Columns follows a consistent schema: `open`, `high`, `low`, `close`, `volume`, `returns`
- No missing values
- Cleaned and algiend time series

The `moving_average_crossover` strategy expects a `pd.Series` of cleaned close prices, typically: 
```python
prices = df["close"]
```

## Strategy Output -> Backtesting Input

The backtester requires the processed dataset to include:

- a `returns` column (daily percentage returns)
- a clean `DatetimeIndex`
- aligned price and signal series

Strategy functions generate a `signal` column, and the backtester consumes: 

- **returns** (from the data pipeline)
- **signal** (from the strategy)

These two columns form the core inputs for computing positions and strategy returns.


## Folder Structure
```text
trading-system/
├── data/
|   |-- processed/ #processed CSV files
│   ├── raw/ # raw downloaded CSV files
|   |-- clean_data.py # script to clean and process raw csv file
    |-- download_data.py # script to download data from yfinance
│   
├── docs/
│   └── ... # document files
```
This structure keeps raw data isolated and reproducible.


