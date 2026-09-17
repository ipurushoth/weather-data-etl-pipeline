import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()


def load_weather_data():

    df = pd.read_csv("data/processed/weather.csv")

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    cursor = connection.cursor()

    for _, row in df.iterrows():

        
        cursor.execute(
            """
            INSERT INTO weather_data
            (time, temperature, humidity, pressure, wind_speed, weather_code)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (time) DO NOTHING
            """,
            (
                row["time"],
                row["temperature"],
                row["humidity"],
                row["pressure"],
                row["wind_speed"],
                row["weather_code"]
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("Data loaded successfully into PostgreSQL!")


if __name__ == "__main__":
    load_weather_data()