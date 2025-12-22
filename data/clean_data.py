import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

def clean_data(ticker="SPY"):
    df = pd.read_csv(RAW_DATA_PATH / f"{ticker}.csv", header=2, index_col=0)

    
    df.columns = ["close", "high", "low", "open", "volume"]
    # Basic cleaning
    df = df.dropna()


    # converts the DataFrame's index into actual datetime objects instead of plain strings
    df.index = pd.to_datetime(df.index)

    # Add useful columns
    df["returns"] = df["close"].pct_change()

    #export to csv file
    df.to_csv(PROCESSED_DATA_PATH / f"{ticker}_clean.csv")
    
    #print confirmation
    print(f"Cleaned data saved for {ticker}")

if __name__ == "__main__":
    clean_data()

