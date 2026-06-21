# Portfolio Analytics Toolkit

An open-source Python project for portfolio analysis, risk measurement, and investment performance evaluation.

This project was built to learn quantitative finance, portfolio analytics, Git, GitHub workflows, automated testing, and open-source software development.

---

## Features

### Portfolio Analytics

* Daily return calculation
* Portfolio return aggregation
* Compound Annual Growth Rate (CAGR)
* Sharpe Ratio
* Annualized Volatility
* Maximum Drawdown
* Correlation Matrix

### Visualizations

* Portfolio Growth Chart
* Asset Allocation Pie Chart
* Correlation Heatmap

### Software Engineering

* Unit testing with pytest
* Automated CI testing with GitHub Actions
* Feature branch workflow
* Pull request workflow

---

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* yfinance
* pytest
* GitHub Actions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/paeezan61-pixel/portfolio-analytics-toolkit-2.git
cd portfolio-analytics-toolkit-2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the application:

```bash
python src/main.py
```

Example portfolio:

```python
tickers = ["AAPL", "MSFT", "SPY"]
weights = [0.4, 0.3, 0.3]
```

Example metrics:

```text
Portfolio Sharpe Ratio: 1.24
Annualized Volatility: 15.16%
Maximum Drawdown: -16.11%
CAGR: 19.36%
```

---

## Project Structure

```text
PortfolioAnalyticsToolkit
│
├── src
│   ├── data_loader.py
│   ├── metrics.py
│   ├── portfolio.py
│   └── main.py
│
├── tests
│   ├── test_metrics.py
│   └── test_portfolio.py
│
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
├── requirements.txt
└── .github
    └── workflows
```

---

## Roadmap

Planned future features:

* Benchmark comparison
* Alpha and Beta calculations
* Information Ratio
* Portfolio optimization
* ETF analytics
* Additional automated testing
* Enhanced visual reporting

---

## Learning Goals

This repository is part of a broader effort to develop practical skills in:

* Portfolio Management
* Financial Analytics
* Python Development
* Git and GitHub
* Open Source Software Development
* Quantitative Finance
