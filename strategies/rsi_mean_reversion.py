import pandas as pd
import numpy as np

def rsi_mean_reversion(
    prices: pd.Series,
    window: int = 14,
    lower_thresh: int = 30,
    upper_thresh: int = 70
) -> pd.DataFrame:
    """
    RSI-Based Mean Reversion Strategy

    Parameters
    ----------
    prices : pd.Series
        Historical price series (adjusted close)
    window : int
        Lookback period for RSI calculation
    lower_thresh : int
        RSI threshold below which asset is considered oversold
    upper_thresh : int
        RSI threshold above which asset is considered overbought

    Returns
    -------
    pd.DataFrame
        DataFrame with price, RSI, and trading signals
    """

    #create new dataframe
    df = pd.DataFrame(index=prices.index)
    df["price"] = prices

    #price changes between rows 
    delta = prices.diff() #Pandas Series

    #gains and losses
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)

    #rolling averages for window size
    avg_gain = pd.Series(gain, index=prices.index).rolling(window).mean()
    avg_loss = pd.Series(loss, index=prices.index).rolling(window).mean()

    #rsi calculation
    rs = avg_gain / avg_loss
    df["rsi"] = 100 - (100 / (1 + rs))

    # Signals
    df["signal"] = 0
    df.loc[df["rsi"] < lower_thresh, "signal"] = 1    # Buy
    df.loc[df["rsi"] > upper_thresh, "signal"] = -1   # Sell

    return df
