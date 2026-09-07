from src.extract import extract_weather_data
from src.transform import transform_weather_data
from src.load import load_weather_data


print("Starting Weather ETL Pipeline...")

print("\n1. Extracting weather data...")
extract_weather_data()

print("\n2. Transforming weather data...")
transform_weather_data()

print("\n3. Loading data into PostgreSQL...")
load_weather_data()

print("\nWeather ETL Pipeline completed successfully! ✅")