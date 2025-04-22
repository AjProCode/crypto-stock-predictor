import streamlit as st
from data_fetcher import fetch_stock_data, fetch_crypto_data
from predictor import forecast_prices
from investment_suggester import suggest_investment

st.title("📈 Crypto & Stock Market Predictor")

ticker = st.text_input("Enter Stock Ticker (e.g. AAPL):", "AAPL")
crypto = st.text_input("Enter Crypto ID (e.g. bitcoin):", "bitcoin")
investment = st.number_input("Investment Amount ($):", 1000)
risk = st.selectbox("Risk Level", ['low', 'medium', 'high'])

if st.button("Analyze & Predict"):
    stock_data = fetch_stock_data(ticker)
    crypto_data = fetch_crypto_data(crypto)

    st.subheader("📊 Stock Forecast")
    stock_forecast = forecast_prices(stock_data)
    st.line_chart(stock_forecast.set_index('ds')['yhat'])

    st.subheader("💰 Crypto Forecast")
    crypto_forecast = forecast_prices(crypto_data, column="price")
    st.line_chart(crypto_forecast.set_index('ds')['yhat'])

    st.subheader("💡 Investment Suggestion")
    suggestion = suggest_investment(investment, risk)
    st.write(suggestion)