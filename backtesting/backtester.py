"""
Backtesting Engine

This module defines a simple backtesting engine that converts trading
signals into positions and evaluates strategy performance using common
financial metrics.
"""


import pandas as pd
import numpy as np

# a Backtester object will hold data, run the backtest, and compute metrics like returns, Sharpe, drawdown.
class Backtester:
    # initializer creates a new Backtester object
    def __init__(self, data: pd.DataFrame, signal_col: str = "signal"):
        """
        Parameters
        ----------
        data : pd.DataFrame
            DataFrame containing prices, returns, and signals
        signal_col : str
            Column name containing trading signals
        """
        self.data = data.copy() # stores a copy of the input DataFrame inside the object so the original is not mutated. 
        self.signal_col = signal_col # saves the name of the column that contains trading signals for later use.

    def run(self):
        """
        Run the backtest:
        - Convert signals to positions
        - Compute strategy returns
        """
        #short hand reference so we can write df[...] instead of self.data[...]
        df = self.data

        # Position = yesterday's signal (no lookahead bias). You cannot trade todays signal with todays close, that would be cheating.
        #yesterdays signals becomes today's position
        df["position"] = df[self.signal_col].shift(1).fillna(0)

        # Strategy returns.  This is the underlying asset's return series (e.g., daily returns of SPY), PnL stream of the strategy
        df["strategy_returns"] = df["position"] * df["returns"]

        self.results = df # saves the DataFrame with positions and strategy returns as an attribute of the object. 
        return df #return the DataFrame

    
