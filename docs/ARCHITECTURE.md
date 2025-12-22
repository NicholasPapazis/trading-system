# System Architecture 

## Data Module Overview

- **purpose**: The data module handles downloading and storing raw market data for later use in backtesting and future generation.
- **components**:
    - `download_data()` function for fetching ticker data
    - `data/raw/` directory for persistent storage
- **design choice**: Using `pathlib.Path` ensures OS-independent file handling and clean path joining.
- **execution behavior**: The script uses a `__main__` guard so it can be run directly or imported without triggering a download. 

## Folder Structure
```text
trading-system/
├── data/
│   ├── raw/ # raw downloaded CSV files
    |-- download_data.py # script to download data from yfinance
│   
├── docs/
│   └── ... # document files
```
This structure keeps raw data isolated and reproducible
