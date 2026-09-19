from portfolio.portfolio import Portfolio
from performance.performance import Performance


class Risk:
    def __init__(self, portfolio: Portfolio, performance: Performance):
        self.portfolio = portfolio
        self.performance = performance

    def portfolio_weights(self):
        return self.portfolio.allocation()

    def largest_position(self):
        data = self.portfolio_weights()

        if len(data) < 1:
            raise ValueError("not enough values")

        largest_value = max(data.values())

        for ticker in data:
            if data[ticker] == largest_value:
                return ticker, largest_value

    def summary(self, risk_free: float):
        largest = self.largest_position()

        largest_position = largest[0]
        largest_weight = largest[1]

        volatility = self.performance.volatility()
        max_drawdown = self.performance.maximum_drawdown()
        sharpe_ratio = self.performance.sharpe_ratio(risk_free)

        return {
            "largest_position": largest_position,
            "largest_weight": largest_weight,
            "volatility": volatility,
            "maximum_drawdown": max_drawdown,
            "sharpe_ratio": sharpe_ratio
        }
