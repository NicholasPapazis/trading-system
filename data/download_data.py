import yfinance as yf
import pandas as pd
from pathlib import Path # makes working with file paths cleaner and OS-independent

# Create directories if they don't exist
RAW_DATA_PATH = Path("data/raw") # creates a path object pointing to the folder data/raw. It does not create the folder, just represents that path
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True) # creates the directory and any missing parent directories. Avoids errors if the folder already exists. Ensures the script never crashes because of missing folders. 

# define the function that downloads data
def download_data(ticker="SPY", start="2015-01-01", end=None):
    df = yf.download(ticker, start=start, end=end) # uses yfinance to download historical price data, returns a pandas DataFrame containing OHLCV data. 
    df.to_csv(RAW_DATA_PATH / f"{ticker}.csv") # saves the DataFrame as a CSV file
    print(f"Downloaded {ticker} data") # prints confirmation method so you know the download succeeded. 

# this block only runs when you execute the file directly, e.g, python script.py
# it does not run when the file is imported as a module. 
if __name__ == "__main__":
    download_data() # calls the function with default parameters, downloads SPY data from the year specified above to today, and saves it. 
