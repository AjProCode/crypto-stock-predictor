from prophet import Prophet
import pandas as pd

def forecast_prices(df, column="Close", periods=30):
    df = df[[column]].reset_index()
    df.columns = ['ds', 'y']
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]