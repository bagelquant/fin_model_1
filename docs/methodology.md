# Methodology

Our goal is to constructing a portfolio from Dow Jones Industrial Average (DJIA) stocks that exceeds the performance of the DJIA index in 12 weeks. Since we are only allowed to trade once a week, with 20 basis points of transaction cost, we will use a buy and hold strategy throughout the 12 weeks. Our success will highly depend on the initial portfolio selection. We will use following methodology to select the initial portfolio:

1. (Mean variance optimization) We will use the mean variance optimization to select the optimal weights for the stocks in the portfolio.
1. (Factor exposure) A multi-factor regression model to identify the exposure of each stock to the factors. Then we will construct a portfolio with excess exposure to the factors.

> In general, we will construct a mean-variance optimized portfolio with constraints of high factor exposure.

## Steps

1. **Data Collection**
    - DJIA daily returns: 30 stocks + 1 index
    - Fama French 5 Factors plus momentum - Daily Frequency
        - Excess return on the Market (mktrf)
        - Small-Minus-Big (smb)
        - High-Minus-Low (hml)
        - Robust Minus Weak (rmw)
        - Conservative Minus Aggressive (cma)
        - Momentum (umd)
        - Risk-Free Rate (rf)
2. **Regression Analysis**
    - Regress DJIA index against factors
    - Regress each stock against factors
3. **Mean variance optimization**
    - Constraints: 
        1. Same mktrf exposure with DJIA index
        2. High exposure to smb, hml, rmw, cma, umd
            - How much to overweight each factor? TBD
    - Objective: Maximize Sharpe Ratio


## Further Improvements

For now, we will only consider a simple long-only buy and hold strategy. In the future, we can consider the following improvements:

- Run time series trading strategy upon the stocks we selected
- Rebalance portfolio

