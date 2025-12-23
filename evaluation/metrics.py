"""
Performance Metrics

This module contains functions for evaluating trading strategy performance
using common financial metrics such as total return, Sharpe ratio, and 
maximum drawdown.
"""

import numpy as np
import pandas as pd


def total_return(returns: pd.Series) -> float:
    return (1 + returns).prod() - 1


def sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    periods_per_year: int = 252
) -> float:
    excess_returns = returns - risk_free_rate / periods_per_year
    return np.sqrt(periods_per_year) * excess_returns.mean() / excess_returns.std()


def max_drawdown(returns: pd.Series) -> float:
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    return drawdown.min()