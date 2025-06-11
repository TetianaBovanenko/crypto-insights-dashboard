# 📊 Crypto Insights Dashboard

An interactive dashboard built with Streamlit that visualizes real-time cryptocurrency data using the CoinGecko API. This app provides up-to-date market insights, price trends, and performance analytics for the top 20 cryptocurrencies by market cap.

![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 🚀 Live App

🔗 **[Launch Crypto Insights Dashboard](https://crypto-insights-dashboard-bssgtzcysoj642gfrvuhtk.streamlit.app)**

No installation required. The app runs entirely in your browser.

---

## ✨ Features

- ✅ Live top 20 cryptocurrencies (via CoinGecko API)
- 📈 Interactive 7-day price trend line chart
- 🔄 24h and 7d percentage change with visual deltas
- 🔍 Dropdown menu to explore individual coins in detail
- 🌙 Streamlit dark theme with custom color palette

---

## 📦 Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/)
- **Data Source:** [CoinGecko API](https://www.coingecko.com/en/api)
- **Visualization:** Seaborn & Matplotlib
- **Language:** Python 3.11+

---

## 🛠 Local Setup

To run the app locally:

```bash
git clone https://github.com/TetianaBovanenko/crypto-insights-dashboard.git
cd crypto-insights-dashboard
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
