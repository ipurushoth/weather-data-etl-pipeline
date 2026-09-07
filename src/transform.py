import json
import pandas as pd
from pathlib import Path


def transform_weather_data():

    # Read raw weather data
    with open("data/raw/weather.json", "r") as file:
        data = json.load(file)

    # Get current weather
    current = data["current"]

    # Create clean data
    weather = {
        "time": current["time"],
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "pressure": current["surface_pressure"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }

    # Convert to DataFrame
    df = pd.DataFrame([weather])

    # Create processed folder
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    # Save processed data
    df.to_csv("data/processed/weather.csv", index=False)

    print("Data transformed successfully!")
    print(df)


if __name__ == "__main__":
    transform_weather_data()