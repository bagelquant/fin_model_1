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


def _regression() -> None:
    """regress on djia and stocks"""
    stock_returns = pd.read_csv('data/stock_returns.csv', parse_dates=True, index_col=0)
    factor_returns = pd.read_csv('data/factor_returns.csv', parse_dates=True, index_col=0)
    djia = pd.read_csv('data/DJIA.csv', parse_dates=True, index_col=0)

    # djia match the stock_returns index
    concat_data = pd.concat([djia, stock_returns], axis=1, join='inner').sort_index()
    exposure = pd.DataFrame(index=concat_data.columns, columns=['mktrf', 'smb', 'hml', 'rmw', 'cma', 'umd'])
    pvalues = pd.DataFrame(index=concat_data.columns, columns=['mktrf', 'smb', 'hml', 'rmw', 'cma', 'umd'])
    significnant_exposure = pd.DataFrame(index=concat_data.columns, columns=['mktrf', 'smb', 'hml', 'rmw', 'cma', 'umd'])

    for stock in concat_data.columns:
        model = factor_regression(concat_data[stock], factor_returns)  # type: ignore
        exposure.loc[stock] = model.params[1:]
        pvalues.loc[stock] = model.pvalues[1:]
        significnant_exposure.loc[stock] = model.params[1:][model.pvalues[1:] < 0.05]

    print("exposure")
    print(exposure.head(1))
    print("pvalues")
    print(pvalues.head(1))
    print("significnant_exposure")
    print(significnant_exposure.head(1))

    exposure.to_csv('data/regression/exposure.csv')
    pvalues.to_csv('data/regression/pvalues.csv')
    significnant_exposure.to_csv('data/regression/significant_exposure.csv')

if __name__ == '__main__':
    _regression()
