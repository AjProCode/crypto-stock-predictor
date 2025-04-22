import yfinance as yf
import requests
import pandas as pd

def fetch_stock_data(ticker, period="6mo", interval="1d"):
    data = yf.download(ticker, period=period, interval=interval)
    return data

def fetch_crypto_data(crypto_id="bitcoin", currency="usd", days="180"):
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
    params = {"vs_currency": currency, "days": days}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises HTTPError if response code isn't 200

        data = response.json()
        if 'prices' not in data:
            print(f"[Error] 'prices' key not found in response: {data}")
            return pd.DataFrame()  # Return empty DataFrame if data is invalid

        prices = data['prices']
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df

    except requests.RequestException as e:
        print(f"[Request Error] Failed to fetch data: {e}")
        return pd.DataFrame()

    except ValueError as e:
        print(f"[Value Error] Invalid response format: {e}")
        return pd.DataFrame()
