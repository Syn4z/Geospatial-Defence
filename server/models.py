import pickle
import numpy as np
import pandas as pd

def predict_ndmi(weather_data: pd.DataFrame) -> pd.DataFrame:

    model = pickle.load(open("model_ndmi.pkl", "rb"))

    weather_data = weather_data.reset_index()
    # print(weather_data)
    weather_data['date'] = pd.to_datetime(weather_data['date'])
    weather_data['Week'] = weather_data['date'].dt.month * 4 + weather_data['date'].dt.day // 7

    weather_data.rename(columns={
        "date": "Date",
        "temperature_2m": "Temperature (°C)", 
        "relative_humidity_2m": "Humidity (%)", 
        "precipitation": "Rainfall (mm)"
    }, inplace=True)

    X = weather_data.drop(['Date'], axis=1)
    y = model.predict(X)

    weather_data['NDMI'] = y

    return weather_data

def predict_seed_rate(weather_data: pd.DataFrame) -> pd.DataFrame:

    model = pickle.load(open("model_seed.pkl", "rb"))

    print(weather_data)

    # Expected order
    expected_order = ['Date', 'Temperature (°C)', 'Humidity (%)', 'Rainfall (mm)', 'NDMI', 'Week']

    # Reorder the columns
    weather_data = weather_data[expected_order]


    X = weather_data.drop(['Date'], axis=1).copy()
    y = model.predict(X)

    weather_data['Seed Rate'] = y

    return weather_data
