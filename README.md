# trading-system

This project implements a modular trading system in Python for developing, backtesting, and evaluating quantitative trading strategies using historical market data.  The system is designed with clear separation between data handling, strategy logic, backtesting, and performance evaluation.

## Project Structure 
```text
trading-system/
├── data/
│   ├── raw/                # Raw historical market data
│   └── processed/          # Cleaned and normalized data
│
├── strategies/             # Trading strategy implementations
│   ├── moving_average.py
│   └── rsi_mean_reversion.py
│
├── backtesting/            # Backtesting engine
│   └── backtester.py
│
├── evaluation/             # Performance evaluation metrics
│   └── metrics.py
│
├── notebooks/              # Sanity checks, backtests, and visualizations
│
├── requirements.txt        # Project dependencies
└── README.md
```

## Data Pipeline

Historical market data is downloaded programmatically and stored in CSV format under the `data/raw` directory. Raw data is never modified.

The data is then cleaned and normalized, including: 
- Parsing dates
- Standardizing column names
- Removing missing values
- Computing daily returns

Processed datasets are stored in `data/processed/` and are used by strategies and the backtesting engine. 

## Strategies

### Moving Average Crossover
The moving average crossover strategy is a trend-following approach that generates trading signals based on the relationship between a short-term and long-tern moving average.
- **Signal = 1**: Short moving average is above long term moving average.
- **Signal = -1**: Short moving average is below long moving average.
- **Signal = 0**: Neutral

### RSI Mean Reversion

The RSI mean reversion strategy is based on the Relative Strength Index (RSI), a momentum indicator that identifies overbought and oversold conditions. 
- **Signal = 1**: RSI below lower threshold (oversold)
- **Signal = -1**: RSI above upper threshold (overbought)
- **Signal = 0**: Neutral

This strategy assumes that prices tend to revert toward a mean following extreme momentum conditions. 

## Backtesting Engine

The backtesting engine is responsible for simulating strategy execution.  It converts trading signals into positions and computes strategy returns while avoiding lookahead bias by shifting signals forward one period.

The backtester outputs a return series that can be evaluating independently using the evaluation module. 

## Evaluation 

Performance evaluation is handled separately from the backtesting engine. The performance module computes common financial metrics, including: 
- Total return
- Sharpe ratio
- Maximum drawdown

These metrics are applied to backtesting results to compare different strategies. 

## Visualization 

Portfolio performance is visualized using equity curve plots generated with Matplotlib. These plots show portfolio value over time and are used to analyze and compare strategy behavior

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Download and clean historical data:
```bash
python data/download_data.py
python data/clean_data.py
```
3. Run strategy backtests and visualizations using the notebooks in the notebooks/ directory. 
