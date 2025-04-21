"""
Optimize portfolio

goal: maximize sharpe ratio
constraints: 
    - sum of weights = 1
    - weights >= 0
    - mktrf = djia['mktrf']
    - smb > djia['smb']
    - hml > djia['hml']
    - rmw > djia['rmw']
    - cma > djia['cma']
"""

import pandas as pd
import numpy as np
from scipy.optimize import minimize


def sharpe_ratio(weights: pd.Series,
                 stock_returns: pd.DataFrame,
                 rf: pd.Series) -> float:
    """Sharpe ratio of the portfolio"""
    portfolio_returns = stock_returns.dot(weights)
    excess_returns = portfolio_returns - rf
    lg_excess_returns = np.log(1 + excess_returns)

    annualized_return = np.exp(lg_excess_returns.mean() * 52) - 1
    annualized_volatility = np.sqrt(52) * lg_excess_returns.std()
    sharpe = annualized_return / annualized_volatility
    return sharpe


def _optimize() -> None:
    # read data
    exposure = pd.read_csv('data/regression/significant_exposure.csv', index_col=0)
    stock_returns = pd.read_csv('data/stock_returns.csv', parse_dates=True, index_col=0)['2020-12-31':]  # type: ignore
    djia_exposure = exposure.loc['djia']
    exposure = exposure.drop('djia').fillna(0)
    rf = pd.read_csv('data/factor_returns.csv', parse_dates=True, index_col=0)['rf']  # type: ignore
    rf: pd.Series = pd.concat([rf, stock_returns], axis=1, join='inner').sort_index()['rf']  # type: ignore

    # initial weights
    initial_weights = pd.Series(np.repeat(1 / len(exposure), len(exposure)), index=exposure.index)

    # constraints
    constraints = [{'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
                   # weights >= 0
                   {'type': 'ineq', 'fun': lambda x: x},
                   {'type': 'ineq', 'fun': lambda x: 0.1 - x},
                   {'type': 'eq', 'fun': lambda x: djia_exposure['mktrf'] - x.dot(exposure['mktrf'])},
                   {'type': 'ineq', 'fun': lambda x: x.dot(exposure['smb'] - djia_exposure['smb'])},
                   {'type': 'ineq', 'fun': lambda x: x.dot(exposure['hml'] - djia_exposure['hml'])},
                   {'type': 'ineq', 'fun': lambda x: x.dot(exposure['rmw'] - djia_exposure['rmw'])},
                   {'type': 'ineq', 'fun': lambda x: x.dot(exposure['cma'] - djia_exposure['cma'])}
                   ]

    # optimization
    result = minimize(lambda x: - sharpe_ratio(x, stock_returns, rf), initial_weights, constraints=constraints)  # type: ignore
    weights = pd.Series(result.x, index=exposure.index)
    # round weights
    weights = weights.round(4)
    print("====== optimized weights ======")
    print(weights)
    print("====== performance ======")
    print(f'sharpe ratio: {sharpe_ratio(weights, stock_returns, rf)}')  # type: ignore
    print(f'expected return: {np.exp(np.log(1 + stock_returns.mean()).dot(weights) * 52) - 1}')
    print(f'expected volatility: {np.sqrt(52) * np.log(1 + stock_returns).std().dot(weights)}')
    # exposure
    print("====== exposure difference ======")
    print(f'mktrf: {weights.dot(exposure["mktrf"]) - djia_exposure["mktrf"]: .4f}')  # type: ignore
    print(f'smb: {weights.dot(exposure["smb"]) - djia_exposure["smb"]: .4f}')  # type: ignore
    print(f'hml: {weights.dot(exposure["hml"]) - djia_exposure["hml"]: .4f}')  # type: ignore
    print(f'rmw: {weights.dot(exposure["rmw"]) - djia_exposure["rmw"]: .4f}')  # type: ignore
    print(f'cma: {weights.dot(exposure["cma"]) - djia_exposure["cma"]: .4f}')  # type: ignore
    
    exposure = pd.DataFrame({"DJIA": [djia_exposure["mktrf"], djia_exposure["smb"], djia_exposure["hml"], djia_exposure["rmw"], djia_exposure["cma"]],
                            "Portfolio": [weights.dot(exposure["mktrf"]), weights.dot(exposure["smb"]), weights.dot(exposure["hml"]), weights.dot(exposure["rmw"]), weights.dot(exposure["cma"])]},
                           index=["mktrf", "smb", "hml", "rmw", "cma"])
    exposure["difference"] = exposure["Portfolio"] - exposure["DJIA"]
    exposure = exposure.round(3)
    print(exposure)
    exposure.to_csv('data/exposure_difference.csv')

    weights.to_csv('data/optimized_weights.csv')

    

if __name__ == '__main__':
    _optimize()
