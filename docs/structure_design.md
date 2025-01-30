# Structure Design

This file contains the structure design of the program

## File Structure
 
```plaintext
+-- docs/
+-- data/
+-- tests/
+-- src/
|   +-- __init__.py
|   +-- data.py
|   +-- optimization.py
|   +-- portfolio.py
|   +-- performance.py
|   +-- reports.py
+-- main.py
+-- README.md
+-- requirements.txt
```

## Modules

1. `data.py`: This module contains functions to load and preprocess data.
    - Read data from csv files
    - Preprocess data
        - Standardize
        - Missing value imputation
2. `optimization.py`: This module contains functions to optimize the portfolio.
    - Mean variance optimization
    - Constraints
        - Same mktrf exposure with DJIA index
        - High exposure to smb, hml, rmw, cma, umd
3. `portfolio.py`: This module contains functions to build the model.
    - Portfolio class
4. `performance.py`: Performance analysis
    - Ratios
    - Plots
5. `reports.py`: Generate reports
    - Weekly report
6. `main.py`: main script

