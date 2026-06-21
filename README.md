# Portfolio Analytics Toolkit

Portfolio Analytics Toolkit is an open-source Python project for portfolio performance analysis, risk measurement, benchmark comparison, and investment analytics.

This project was built to learn quantitative finance, portfolio analytics, Git, GitHub workflows, automated testing, and open-source software development.

---

## Features


## Screenshots

### Portfolio vs Benchmark

![Portfolio vs Benchmark](docs/images/portfolio-vs-benchmark.png)

### Correlation Heatmap

![Correlation Heatmap](docs/images/correlation-heatmap.png)

### Asset Allocation

![Asset Allocation](docs/images/allocation-chart.png)

### Portfolio Analytics

* Daily Returns
* Portfolio Returns
* CAGR
* Sharpe Ratio
* Volatility
* Maximum Drawdown
* Correlation Matrix
* Benchmark Comparison
* Beta
* Alpha

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
Portfolio CAGR: 19.36%
Benchmark CAGR: 14.82%
Portfolio Beta: 1.05
Portfolio Alpha: 3.20%
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
