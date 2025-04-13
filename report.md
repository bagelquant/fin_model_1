---
title: "Portfolio Report"
subtitle: "Project for Financial Modeling I"
date: 2025-04-18
author: "Aditri, Yanzhong(Eric) Huang, Vishnu Medagam, Omkar K Vaidya"
output: 
  pdf_document:
    toc: true
    toc_depth: 2
    number_sections: true
---

## Executive Summary

## Introduction and Methodology

-  In recent years, index investing has gained popularity, particularly in the United States.
-  The Dow Jones Industrial Average (DJIA) is one of the most renowned indices globally.
-  Our objective is to construct an enhanced index portfolio based on the DJIA.
-  Common approaches include active management and smart beta strategies.
-  Due to our limited investment horizon, active management may incur high transaction costs, and smart beta strategies may not outperform in the short term.
-  We employ a simple buy-and-hold strategy through a mean-variance optimized portfolio, maintaining the same factor exposure as the DJIA.

## Portfolio Overview

-  Backtesting approach and results
-  Final portfolio:
  - Industry-level allocation (illustrated with a pie chart)
  - Factor exposure (depicted in a time series plot)
  - Stock-level allocation (presented in a table)

TODOs:

-  [ ] Create plots and gather data

## Performance Analysis

### Performance Overview

-  Raw Return (compared to the DJIA index and the overall market):
  - Daily returns (displayed in a time series plot)
  - Cumulative returns
  - Expected annualized return
-  Risk Measures:
  - Volatility
  - Value at Risk (VaR)
  - Maximum Drawdown
-  Risk-adjusted Return:
  - Sharpe Ratio
  - Sortino Ratio
  - Calmar Ratio

TODOs:

-  [ ] Collect daily data for:
  - 20 stocks
  - DJIA index
  - CRSP market index (entire market)
  - Risk-free rate (90-day T-bill)
  - Fama-French 5 factors + momentum
-  [ ] Compute performance ratios

### Style Analysis

-  Industry-level performance
-  Factor exposure (excess return vs. factor return)
-  Stock-level performance

TODOs:

-  [ ] Calculate industry-level performance
-  [ ] Conduct factor exposure regression

### Tariffs Period Review (04/03 - 04/12)

> Date range may not be accurate

-  Impact of tariffs on portfolio performance:
  - Overall market
  - DJIA index
  - Industry impact
  - Factor impact (factor return)

- [ ] Compute performance for the period
- [ ] Analyze impact of tariffs on portfolio performance

## Conclusion


