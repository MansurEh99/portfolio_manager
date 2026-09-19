import math

from portfolio.portfolio import Portfolio
from performance.performance import Performance
from performance.risk import Risk


def create_risk():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 50, 100)
    portfolio.buy("2026-01-01", "MSFT", 30, 100)

    portfolio.holdings["AAPL"].current_price = 100
    portfolio.holdings["MSFT"].current_price = 100

    performance = Performance(portfolio)

    performance.history["2026-01-01"] = 10_000
    performance.history["2026-01-02"] = 10_500
    performance.history["2026-01-03"] = 9_800
    performance.history["2026-01-04"] = 10_300
    performance.history["2026-01-05"] = 10_400
    performance.history["2026-01-06"] = 11_000

    risk = Risk(portfolio, performance)

    return portfolio, performance, risk


def test_portfolio_weights():
    portfolio, performance, risk = create_risk()

    weights = risk.portfolio_weights()

    assert math.isclose(weights["CASH"], 0.20)
    assert math.isclose(weights["AAPL"], 0.50)
    assert math.isclose(weights["MSFT"], 0.30)

    assert math.isclose(sum(weights.values()), 1.0)


def test_largest_position():
    portfolio, performance, risk = create_risk()

    ticker, weight = risk.largest_position()

    assert ticker == "AAPL"
    assert math.isclose(weight, 0.50)


def test_cash_is_largest_position():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 10, 100)
    portfolio.holdings["AAPL"].current_price = 100

    performance = Performance(portfolio)
    risk = Risk(portfolio, performance)

    ticker, weight = risk.largest_position()

    assert ticker == "CASH"
    assert math.isclose(weight, 0.90)


def test_tied_largest_positions():
    portfolio = Portfolio(10_000)

    portfolio.buy("2026-01-01", "AAPL", 40, 100)
    portfolio.buy("2026-01-01", "MSFT", 40, 100)

    portfolio.holdings["AAPL"].current_price = 100
    portfolio.holdings["MSFT"].current_price = 100

    performance = Performance(portfolio)
    risk = Risk(portfolio, performance)

    ticker, weight = risk.largest_position()

    assert ticker in ["AAPL", "MSFT"]
    assert math.isclose(weight, 0.40)


def test_empty_portfolio():
    portfolio = Portfolio(0)

    performance = Performance(portfolio)
    risk = Risk(portfolio, performance)

    try:
        risk.largest_position()
        assert False
    except ValueError:
        assert True


def test_risk_summary():
    portfolio, performance, risk = create_risk()

    summary = risk.summary(0.01)

    assert summary["largest_position"] == "AAPL"
    assert math.isclose(summary["largest_weight"], 0.50)

    expected_volatility = performance.volatility()
    expected_drawdown = performance.maximum_drawdown()
    expected_sharpe = performance.sharpe_ratio(0.01)

    assert math.isclose(
        summary["volatility"],
        expected_volatility
    )

    assert math.isclose(
        summary["maximum_drawdown"],
        expected_drawdown
    )

    assert math.isclose(
        summary["sharpe_ratio"],
        expected_sharpe
    )


print("All risk tests passed!")
