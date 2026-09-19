# Mini Portfolio Manager

A Python-based mini portfolio management system built as a learning project.

The project simulates a basic investment portfolio and tracks holdings, cash, portfolio value, performance, and risk metrics. It also includes automated tests and a formatted portfolio report.

The main goal of this project was to learn how to structure a small Python application while applying basic quantitative-finance concepts.

---

## Features

### Portfolio Management

The portfolio supports:

- Buying assets
- Selling assets
- Tracking cash
- Tracking holdings
- Calculating average cost
- Recording transactions
- Updating current market prices

### Portfolio Accounting

The system calculates:

- Total portfolio value
- Unrealized profit/loss
- Portfolio allocation
- Cash allocation

### Performance Analysis

The system tracks portfolio values through time and calculates:

- Period returns
- Total return
- Cumulative performance
- Consecutive returns
- Volatility
- Sharpe ratio
- Drawdown
- Maximum drawdown

### Risk Analysis

The risk module calculates:

- Portfolio weights
- Largest portfolio position
- Largest position weight
- Volatility
- Maximum drawdown
- Sharpe ratio

### Reporting

The report module produces a formatted portfolio report containing:

- Portfolio value
- Cash
- Holdings
- Position values
- Total return
- Volatility
- Maximum drawdown
- Sharpe ratio
- Largest position
- Largest position weight

### Testing

The project includes tests for:

- Portfolio functionality
- Performance calculations
- Risk calculations
- Report generation
- Invalid inputs
- Edge cases

All tests can be run with a single command.

---

## Project Structure

```text
portfolio_manager/
│
├── portfolio/
│   └── portfolio.py
│
├── performance/
│   ├── performance.py
│   └── risk.py
│
├── tests/
│   ├── __init__.py
│   ├── test_portfolio.py
│   ├── test_performance.py
│   ├── test_risk.py
│   └── test_report.py
│
├── report.py
├── main.py
├── test.sh
└── README.md
