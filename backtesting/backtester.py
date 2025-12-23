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

    #computes the total return of the strategy over the whole period, as a percentage
    def total_return(self):
        #extracts the strategy's return series.
        return (1 + self.results["strategy_returns"]).prod() - 1

    #computes the annualized Sharpe ratio of the strategy.
    def sharpe_ratio(self, risk_free_rate=0.0, periods_per_year=252):
        excess_returns = self.results["strategy_returns"] - risk_free_rate / periods_per_year
        return np.sqrt(periods_per_year) * excess_returns.mean() / excess_returns.std()

    #computes the maximum drawdown of the strategy, the worst peak to trough loss. 
    def max_drawdown(self):
        cumulative = (1 + self.results["strategy_returns"]).cumprod() #cumulative equity
        peak = cumulative.cummax() #your highest equity during the time frame
        drawdown = (cumulative - peak) / peak #peak to pit decline. 
        return drawdown.min() #the most negative drawdown
