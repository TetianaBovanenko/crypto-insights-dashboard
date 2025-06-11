import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configure Streamlit
st.set_page_config(page_title="Top 20 Cryptos", layout="wide")
st.title("📊 Top 20 Cryptocurrencies by Market Cap")

# --- Fetch top 20 coins ---
@st.cache_data
def fetch_top_coins(vs_currency="usd"):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "24h,7d"
    }
    response = requests.get(url, params=params)
    return pd.DataFrame(response.json())

# --- Fetch 7-day price history ---
@st.cache_data
def fetch_price_history(coin_id, vs_currency="usd"):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": 7}
    response = requests.get(url, params=params)
    prices = response.json()["prices"]
    return pd.DataFrame(prices, columns=["timestamp", "price"])

# --- Load data ---
df = fetch_top_coins()
coin_names = df['name'].tolist()
coin_ids = df.set_index('name')['id'].to_dict()

# --- Display top 20 table with price change ---
st.subheader("📋 Overview with Price Change %")
display_df = df[['market_cap_rank', 'name', 'symbol', 'current_price', 'market_cap',
                 'price_change_percentage_24h_in_currency',
                 'price_change_percentage_7d_in_currency']].copy()

display_df.columns = ['Rank', 'Name', 'Symbol', 'Current Price (USD)', 'Market Cap',
                      '24h Change (%)', '7d Change (%)']

st.dataframe(display_df, use_container_width=True)

# --- Coin selector ---
st.subheader("🔎 View Coin Details")
selected_coin = st.selectbox("Select a coin", coin_names)
coin_id = coin_ids[selected_coin]
selected_row = df[df['id'] == coin_id].iloc[0]

st.markdown(f"**{selected_coin} (Symbol: {selected_row['symbol'].upper()})**")
st.metric("Current Price (USD)", f"${selected_row['current_price']:,.2f}",
          delta=f"{selected_row['price_change_percentage_24h_in_currency']:.2f}% (24h)")

# --- 7-day price chart ---
st.subheader(f"📈 {selected_coin} – 7-Day Price Trend")
history_df = fetch_price_history(coin_id)
history_df['timestamp'] = pd.to_datetime(history_df['timestamp'], unit='ms')

sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#000000", "figure.facecolor": "#000000"})

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=history_df, x='timestamp', y='price', ax=ax, color="#CF1259")
ax.set_title(f"{selected_coin} – Price Over Last 7 Days", color="white")
ax.set_xlabel("Date", color="white")
ax.set_ylabel("Price (USD)", color="white")
ax.tick_params(colors='white')
fig.patch.set_facecolor('black')

st.pyplot(fig)
