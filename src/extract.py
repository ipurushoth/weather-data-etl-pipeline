import requests
import json
from pathlib import Path


def extract_weather_data():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "current": "temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m,weather_code",
    "timezone": "Asia/Kolkata"
}

    response = requests.get(url, params=params)

    print("API Status:", response.status_code)

    if response.status_code == 200:

        data = response.json()

        Path("data/raw").mkdir(parents=True, exist_ok=True)

        with open("data/raw/weather.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data extracted successfully!")
        print("weather.json created.")

    else:
        print("Failed to extract data")


if __name__ == "__main__":
    extract_weather_data()