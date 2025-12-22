import pandas as pd

#define function for the strategy
def moving_average_crossover(
        #param name : expected type
        prices: pd.Series, # usually the closing prices
        short_window: int = 20, #fast moving average
        long_window: int = 50 #slow moving average
) -> pd.DataFrame: # returns a DataFrame
    """
    Moving Average Crossover Strategy

    Parameters
    ----------
    prices : pd.Series
        Historical price series (e.g. adjusted close prices)
    short_window : int 
        Window size for short term moving average
    long_window : int
        Window size for long-term moving average

    Returns 
    -------
    pd.DataFrame
        DataFrame containing prices, moving averages, and trading signals

    """

    #safety check, the short MA must be shorter than the long MA
    if short_window >= long_window:
        raise ValueError("short_window must be less than long_window")
    
    # here is where the new dataframe starts getting built. Will will return it once we add the signals
    df = pd.DataFrame(index=prices.index) #create new dataframe with the same index (dates) as the price series
    df["price"] = prices # adds the raw price data into 

    #compute moving averages and add a column for them
    df["short_ma"] = prices.rolling(window=short_window).mean() #.rolling(window=n) creates a sliding window of size n
    df["long_ma"] = prices.rolling(window=long_window).mean() #.mean() computes the average inside each window

    #generate signals and add a column for them
    df["signal"] = 0 #initializes new column with zeroes
    df.loc[df["short_ma"] > df["long_ma"], "signal"] = 1 # set signal column to 1 wherever short_ma > long_ma. Trend is bullish, go long
    df.loc[df["short_ma"] < df["long_ma"], "signal"] = -1 # set signal column to -1 wherever short_ma < long_ma. Trend is bearish, go short

    #return the full DataFrame containing price, short moving average, long moving average, trading signals. 
    return df # the signals can be used for backtesting, plotting, or live trading logic
