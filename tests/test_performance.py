import math

from portfolio.portfolio import Portfolio
from performance.performance import Performance


def create_performance():
    portfolio = Portfolio(10_000)
    performance = Performance(portfolio)

    performance.history["2026-01-01"] = 10_000
    performance.history["2026-01-02"] = 10_500
    performance.history["2026-01-03"] = 9_800
    performance.history["2026-01-04"] = 10_300
    performance.history["2026-01-05"] = 10_400
    performance.history["2026-01-06"] = 11_000

    return performance


def test_record():
    portfolio = Portfolio(10_000)
    performance = Performance(portfolio)

    performance.record("2026-01-01")

    assert performance.history["2026-01-01"] == 10_000


def test_record_duplicate_date():
    portfolio = Portfolio(10_000)
    performance = Performance(portfolio)

    performance.record("2026-01-01")

    try:
        performance.record("2026-01-01")
        assert False
    except ValueError:
        assert True


def test_period_return():
    performance = create_performance()

    result = performance.period_return(
        "2026-01-02",
        "2026-01-01"
    )

    assert math.isclose(result, 0.05)


def test_period_return_loss():
    performance = create_performance()

    result = performance.period_return(
        "2026-01-03",
        "2026-01-02"
    )

    expected = (9_800 - 10_500) / 10_500

    assert math.isclose(result, expected)


def test_total_return():
    performance = create_performance()

    result = performance.total_return(
        "2026-01-01",
        "2026-01-06"
    )

    assert math.isclose(result, 0.10)


def test_cumulative_performance():
    performance = create_performance()

    result = performance.cumulative_performance()

    assert math.isclose(result["2026-01-01"], 0.00)
    assert math.isclose(result["2026-01-02"], 0.05)
    assert math.isclose(result["2026-01-03"], -0.02)
    assert math.isclose(result["2026-01-06"], 0.10)


def test_consecutive_returns():
    performance = create_performance()

    result = performance.consecutive_returns()

    expected = [
        (10_500 - 10_000) / 10_000,
        (9_800 - 10_500) / 10_500,
        (10_300 - 9_800) / 9_800,
        (10_400 - 10_300) / 10_300,
        (11_000 - 10_400) / 10_400
    ]

    assert len(result) == 5

    for actual, expected_value in zip(result, expected):
        assert math.isclose(actual, expected_value)


def test_volatility():
    performance = create_performance()

    result = performance.volatility()

    expected_returns = performance.consecutive_returns()

    import statistics
    expected = statistics.stdev(expected_returns)

    assert math.isclose(result, expected)


def test_volatility_not_enough_data():
    portfolio = Portfolio(10_000)
    performance = Performance(portfolio)

    performance.history["2026-01-01"] = 10_000

    try:
        performance.volatility()
        assert False
    except ValueError:
        assert True


def test_drawdown():
    performance = create_performance()

    drawdowns, maximum = performance.drawdown()

    assert math.isclose(drawdowns["2026-01-01"], 0)
    assert math.isclose(drawdowns["2026-01-02"], 0)

    expected_drawdown = (9_800 - 10_500) / 10_500

    assert math.isclose(
        drawdowns["2026-01-03"],
        expected_drawdown
    )

    assert math.isclose(maximum, expected_drawdown)


def test_maximum_drawdown():
    performance = create_performance()

    result = performance.maximum_drawdown()

    expected = (9_800 - 10_500) / 10_500

    assert math.isclose(result, expected)


def test_drawdown_empty_history():
    portfolio = Portfolio(10_000)
    performance = Performance(portfolio)

    try:
        performance.drawdown()
        assert False
    except ValueError:
        assert True


def test_sharpe_ratio():
    performance = create_performance()

    risk_free = 0.01

    result = performance.sharpe_ratio(risk_free)

    returns = performance.consecutive_returns()

    expected_return = sum(returns) / len(returns)

    import statistics
    volatility = statistics.stdev(returns)

    expected = (expected_return - risk_free) / volatility

    assert math.isclose(result, expected)


def test_sharpe_ratio_zero_volatility():
    portfolio = Portfolio(10_000)
    performance = Performance(portfolio)

    performance.history["2026-01-01"] = 10_000
    performance.history["2026-01-02"] = 10_000
    performance.history["2026-01-03"] = 10_000

    try:
        performance.sharpe_ratio(0.01)
        assert False
    except ValueError:
        assert True


print("All performance tests passed!")
