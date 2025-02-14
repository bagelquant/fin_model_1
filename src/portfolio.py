"""
Portfolio class
"""

import pandas as pd
from dataclasses import dataclass


@dataclass(slots=True)
class Portfolio:

    cash: float
    positions: pd.Series

    def nav(self, prices: pd.Series) -> float:
        """Net asset value of the portfolio"""
        if not self._match_positions_prices(prices):
            raise ValueError('Prices do not match positions')
        return self.cash + (self.positions * prices).sum()

    def values(self, prices: pd.Series) -> pd.Series:
        """Value of the portfolio"""
        if not self._match_positions_prices(prices):
            raise ValueError('Prices do not match positions')
        
        stock_values = self.positions * prices
        stock_values.name = 'value'
        cash = pd.Series(data=[self.cash], index=['cash'], name='value')
        return pd.concat([cash, stock_values])  # type: ignore

    def _match_positions_prices(self, prices: pd.Series) -> bool:
        """Check if positions and prices have the same index"""
        return self.positions.index.equals(prices.index)
    

if __name__ == '__main__':
    portfolio = Portfolio(cash=1000, positions=pd.Series(data=[10, 20, 30], index=['AAPL', 'GOOGL', 'MSFT']))
    prices = pd.Series(data=[100, 200, 300], index=['AAPL', 'GOOGL', 'MSFT'])

    print(portfolio.nav(prices))
    print(portfolio.values(prices))

