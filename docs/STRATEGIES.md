# Moving Average Crossover Strategy

## Overview 
The **moving average crossover strategy** is a classic trend-following technique. It compares a short-term moving average to a long-term moving average to determine market direction

- **Short MA above Long MA** -> bullish trend -> long signal
- **Short MA below Long MA** -> bearish trend -> short signal

This strategy operates on **processed price data** produced by the data pipeline.

## Function Definition
```python
moving_average_crossover(
    prices: pd.Series,
    short_window: int = 20,
    long_window: int = 50
) -> pd.DataFrame
```

### Inputs 
- **prices (pd.Series)** - Cleaned historical price series (usually close prices).
- **short_window (int)** - Fast moving average window. 
- **long_window (int)** - Slow moving average window. 

### Outputs 
- A DataFrame containing price, short moving average, long moving average, trading signals

---
> **Note:** This strategy is most effective in trending markets and can produce "whipsaws" (false signals) in sideways/ranging markets.
