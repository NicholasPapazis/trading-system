# Data Pipeline

## Raw Data Layer

- **data source**: We use the yfinance library to download historical OHLCV market data.
- **storage location**: Raw data is saved under `data/raw{ticker}.csv`.
- **folder creation**: The script automatically creates the `data/raw` directory using `Path.mkdir(parents=True, exists_ok=True)`.
- **defaut parameters**: By default, the script downloads SPY data starting from 2015-01-01 to the most recent available date. 
- **file format**: Data is stored as CSV for simplicity and compatibility with pandas.
            
## Processed Data Layer

- **processed data module**: The clean_data.py script transforms raw CSV files into standardized, analysis-ready datasets. 
- **data flow**: `data/raw -> clean_data.py -> data/processed`.
- **consistency guarantees**: All processed files share the same column names, date index, and return calculations.

## Current Workflow

1. Call 'download_data(ticker, start, end)`
2. Fetch data using `yf.download()`
3. Save the resulting DataFrame to `data/raw/`
4. Print a confirmation message

This forms the foundation of the system's data ingestion layer

## Strategy Layer

The project includes a **strategy module** responsible for generating trading signals from processed market data. 

### Moving Average Crossover
The first implemented strategy is the **moving average crossover**, which: 
- consumes cleaned price data from `data/processed/`
- computes short-term and long-term moving averages
- generates directional trading signals 
- outputs a structured DataFrame for downstream components

This strategy layer sits **after the data pipeline** and **before the backtesting engine**