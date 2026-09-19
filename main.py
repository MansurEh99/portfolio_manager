from portfolio.portfolio import Portfolio
from performance.performance import Performance
import statistics
import math

# Test 1: Normal Sharpe ratio
portfolio = Portfolio(10_000)
performance = Performance(portfolio)

performance.history["2026-09-01"] = 10_000
performance.history["2026-09-02"] = 10_200
performance.history["2026-09-03"] = 10_100
performance.history["2026-09-04"] = 10_500

returns = [
    (10_200 - 10_000) / 10_000,
    (10_100 - 10_200) / 10_200,
    (10_500 - 10_100) / 10_100
]

expected_volatility = statistics.stdev(returns)
average_return = sum(returns) / len(returns)
risk_free = 0.01

expected_sharpe = (average_return - risk_free) / expected_volatility

assert math.isclose(
    performance.sharpe_ratio(risk_free),
    expected_sharpe
)


# Test 2: Zero risk-free rate
expected_sharpe = average_return / expected_volatility

assert math.isclose(
    performance.sharpe_ratio(0),
    expected_sharpe
)


# Test 3: Zero volatility
zero_volatility = Performance(Portfolio(10_000))

zero_volatility.history["2026-09-01"] = 10_000
zero_volatility.history["2026-09-02"] = 10_000
zero_volatility.history["2026-09-03"] = 10_000

try:
    zero_volatility.sharpe_ratio(0.01)
    assert False, "Expected ValueError"
except ValueError:
    pass


# Test 4: Not enough observations
one_day = Performance(Portfolio(10_000))
one_day.history["2026-09-01"] = 10_000

try:
    one_day.sharpe_ratio(0.01)
    assert False, "Expected ValueError"
except ValueError:
    pass


print("All Sharpe ratio tests passed!")
