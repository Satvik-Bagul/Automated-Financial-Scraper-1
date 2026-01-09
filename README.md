# Automated-Financial-Tracker-1
<pre>
A Python-based quantitative finance analysis pipeline that retrieves historical equity data, computes return and risk metrics, implements a moving-average crossover strategy, generates trading signals, exports structured datasets, and visualizes market behavior using technical indicators.

Features:

  Market Data Ingestion:
    Fetches historical stock price data programmatically using yfinance
    Supports any valid equity ticker symbol

  Quantitative Metrics:
    Daily returns
    Annualized returns (simple & compounded)
    Annualized volatility (risk estimation)
  
  Technical Analysis:
    50-day and 200-day moving averages
    Moving-average crossover strategy
    Automated buy/sell signal generation

  Data Engineering:
    Stores historical price data as CSV for further analysis
    Uses Pandas for efficient time-series manipulation

  Visualization:
    Plots price trends with technical indicators
    Highlights buy/sell signals on the chart
    Custom dark-themed Matplotlib styling

Strategy Overview:

  The trading logic is based on a moving-average crossover strategy:
    Buy Signal: 50-day MA crosses above 200-day MA
    Sell Signal: 50-day MA crosses below 200-day MA
This strategy is commonly used in quantitative finance to identify momentum and trend direction.

Technologies Used:
  Python
  YFinance
  Pandas
  Matplotlib


Intended Output:
  Enter a valid stock ticker (e.g., AAPL) when prompted.
  Latest price
  Annualized returns
  Volatility
  Moving averages
  CSV file containing historical price data
  Interactive price chart with indicators and trading signals

Project Motivation:

  This project demonstrates:
    Quantitative finance fundamentals
    Time-series data processing
    Algorithmic trading logic
    Clean Python program design

It is intended as a foundation for more advanced extensions such as backtesting, portfolio optimization, and risk modeling. To further facilitate this, I have started learnign about the Monte Carlo Simulation that will help in risk assessment.

Possible Extensions:
  Backtesting framework
  Sharpe ratio and drawdown analysis
  Multi-asset portfolio support
  Strategy parameter optimization
  Integration with live market data APIs
</pre>
