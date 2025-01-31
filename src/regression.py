"""
multi-regression

regressor: factor_returns

factor_returns columns:
    - Excess return on the Market (mktrf)
    - Small-Minus-Big (smb)
    - High-Minus-Low (hml)
    - Robust Minus Weak (rmw)
    - Conservative Minus Aggressive (cma)
    - Momentum (umd)
    - Risk-Free Rate (rf)
"""

import pandas as pd
from statsmodels.formula.api import ols


def factor_regression(data: pd.DataFrame,
                      factor_returns: pd.DataFrame):
    """
    :param data: pd.DataFrame, data to be regressed
    :param factor_returns: pd.DataFrame
    :return: model

    data and factor_returns format:
        index: date (datetime)
        columns: factor names
        values: returns
    """
    # calculate excess returns
    factors: list[str] = factor_returns.columns.tolist()  # type: ignore
    reg_data = pd.concat([data, factor_returns], axis=1, join='inner').sort_index()
    reg_data.columns = ['excess_return'] + factors
    reg_data['excess_return'] = reg_data['excess_return'] - reg_data['rf']

    # regression
    return ols('excess_return ~ mktrf + smb + hml + rmw + cma + umd', data=reg_data).fit()


if __name__ == '__main__':
    # quick test
    factor_returns = pd.read_csv('data/factor_returns.csv', parse_dates=True, index_col=0)
    djia = pd.read_csv('data/DJIA.csv', parse_dates=True, index_col=0)

    model = factor_regression(data=djia, 
                              factor_returns=factor_returns)
    print(model.summary())

