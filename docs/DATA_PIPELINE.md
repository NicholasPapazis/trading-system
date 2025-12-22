# Data Pipeline

## Raw Data Layer

- **data source**: We use the yfinance library to download historical OHLCV market data.
- **storage location**: Raw data is saved under `data/raw{ticker}.csv`.
- **folder creation**: The script automatically creates the `data/raw` directory using `Path.mkdir(parents=True, exists_ok=True)`.
- **defaut parameters**: By default, the script downloads SPY data starting from 2015-01-01 to the most recent available date. 
- **file format**: Data is stored as CSV for simplicity and compatibility with pandas.
            
## Current Workflow

1. Call 'download_data(ticker, start, end)`
2. Fetch data using `yf.download()`
3. Save the resulting DataFrame to `data/raw/`
4. Print a confirmation message

This forms the foundation of the system's data ingestion layer