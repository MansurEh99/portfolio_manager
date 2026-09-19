from portfolio.portfolio import Portfolio
import statistics

class Performance:
    def __init__(self, portfolio: Portfolio):
        self.history = {}
        self.portfolio = portfolio

    def record(self, date):
        if date not in self.history:
            self.history[date] = self.portfolio.value()
        else:
            raise ValueError("date already recorded")

    def period_return(self, current_date, previous_date):
        if current_date in self.history and previous_date in self.history and self.history[previous_date] != 0:
            current_value = self.history[current_date]
            previous_value = self.history[previous_date]
            return (current_value - previous_value) / previous_value
        else:
            raise ValueError("invalid dates or previous value is zero")

    def total_return(self, start_date, end_date):
        return self.period_return(end_date, start_date)

    def cumulative_performance(self):
        cumulative_performance = {}
        if len(self.history) < 1:
            raise ValueError("not enough values")
        else:
            first_value = next(iter(self.history.values()))
            for date in self.history:
                perf = (self.history[date] / first_value) - 1
                cumulative_performance[date] = round(perf, 2)
        return cumulative_performance

    def consecutive_returns(self):
        if len(self.history) < 2:
            raise ValueError("not enough values")

        returns = []
        previous_date = next(iter(self.history.keys()))

        for date in list(self.history.keys())[1:]:
            returns.append(self.period_return(date, previous_date))
            previous_date = date

        return returns

    def volatility(self):
        data = self.consecutive_returns()
        if len(data) < 2:
            raise ValueError("not enough values")
        return statistics.stdev(data)

    def drawdown(self):
        if len(self.history) < 1:
            raise ValueError("not enough values")
        drawdown = {}
        peak = next(iter(self.history.values()))
        for date in self.history:
            if self.history[date] > peak:
                peak = self.history[date]
            if peak == 0:
                raise ValueError("peak cannot be 0")
            ddt = (self.history[date] - peak) / peak
            drawdown[date] = ddt
        return drawdown

    def maximum_drawdown(self):
        drawdowns = self.drawdown()
        maximum_drawdown = min(drawdowns.values())
        return maximum_drawdown

    # make sure the risk free is on the same time scale
    def sharpe_ratio(self, risk_free: float):
        volatility = self.volatility()
        if volatility == 0:
            raise ValueError("cannot devide by 0")
        returns = self.consecutive_returns()
        portfolio_return = sum(returns) / len(returns)
        ratio = (portfolio_return - risk_free) / volatility
        return ratio
