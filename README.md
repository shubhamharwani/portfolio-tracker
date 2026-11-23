# ⚡ Momentum Portfolio Tracker

> 📦 **Part of the Momentum Investing Suite**  
> **Part 1:** [Momentum Rank Screener](https://github.com/shubhamharwani/<screener-repo-name>) (Screen & size positions) → **Part 2:** **Portfolio Tracker** *(You are here — track P&L & trade metrics)*

A portfolio performance and trade-analytics web app built with **Python**, **Streamlit**, and **yfinance**. Upload a CSV of shortlisted stock tickers to evaluate equal-weighted portfolio returns, stock-wise P&L, win rate, and average risk-to-reward ratio over any custom trading-day lookback window.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-Market%20Data-6001D2)

---

## 📌 Overview

Built as the second half of a systematic momentum workflow, **Momentum Portfolio Tracker** picks up where the screener leaves off. Once you have a basket of stocks, this app eliminates manual spreadsheet tracking by:

1. Ingesting your portfolio ticker list via CSV upload.
2. Pulling 5 years of daily historical closing prices from Yahoo Finance.
3. Computing stock-level P&L, overall equal-weighted portfolio gain, and key trading performance metrics (Win Rate, Avg Win, Avg Loss, and Avg Risk-to-Reward Ratio) over any configurable lookback period.

---

## ✨ Key Features

- **CSV Portfolio Upload:** Upload any watchlist or exported screener file containing a `Ticker` column (e.g., `RELIANCE.NS`, `TCS.NS`).
- **Custom Trading-Day Lookback:** Dynamically adjust the lookback window (default: `20` trading days) to evaluate short-term or long-term holding periods.
- **Side-by-Side Price Verification:** Displays closing prices on both the start date and the latest trading date for transparent auditability.
- **Ranked Stock-Wise P&L:** Automatically sorts holdings from top performer to worst performer alongside the overall equal-weighted portfolio return.
- **Automated Trade Analytics:** Calculates Win Trades, Loss Trades, Win Rate (`%`), Average Win (`%`), Average Loss (`%`), and Average Risk-to-Reward (`Avg RR`) with built-in zero-division protection.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Language** | Python |
| **Frontend / UI** | Streamlit |
| **Market Data** | `yfinance` (Yahoo Finance) |
| **Data Processing** | Pandas, NumPy |

---

## ⚙️ How It Works

1. **Input Parsing:** Reads the uploaded CSV file, sorts tickers alphabetically, and extracts the `Ticker` column into a list.
2. **Historical Data Retrieval:** Calls `yf.download(..., period="5y", interval="1d")` to fetch daily `Close` prices.
3. **Performance & Risk Metrics:**
   - **Stock P&L (%):**
     $$\text{P\&L (\%)} = \left(\frac{\text{Latest Close} - \text{Lookback Close}}{\text{Lookback Close}}\right) \times 100$$
   - **Win Rate (%):**
     $$\text{Win Rate} = \left(\frac{\text{Winning Trades}}{\text{Total Trades}}\right) \times 100$$
   - **Average Risk-to-Reward (Avg RR):**
     $$\text{Avg RR} = \frac{\text{Avg Win (\%)}}{-\text{Avg Loss (\%)}}$$

### Expected CSV Format
```csv
Ticker
RELIANCE.NS
TCS.NS
HDFCBANK.NS
INFY.NS
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/shubhamharwani/](https://github.com/shubhamharwani/)<tracker-repo-name>.git
   cd <tracker-repo-name>
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas numpy yfinance
   ```
   *(Or if using a `requirements.txt` file: `pip install -r requirements.txt`)*

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 🗺️ Roadmap & Planned Enhancements

- [ ] **Weighted Portfolio Returns:** Support custom share quantities (`Qty`) and actual entry prices from the uploaded CSV for capital-weighted P&L.
- [ ] **Excel & CSV Support:** Add native `.xlsx` parsing via `openpyxl` alongside `.csv` uploads.
- [ ] **Benchmark Comparison:** Overlay Nifty 50 / Nifty 500 returns over the same lookback period to measure alpha.
- [ ] **Visual Equity Curve:** Plot cumulative portfolio growth and drawdown charts using Plotly or Streamlit native charts.

---

## ⚠️ Disclaimer

This tool is built for educational and research purposes only and does not constitute financial or investment advice.

---

## 👤 Author

**Shubham Harwani**  
- GitHub: [@shubhamharwani](https://github.com/shubhamharwani)  
- Twitter/X: [@oyesindhi_](https://twitter.com/oyesindhi_)
