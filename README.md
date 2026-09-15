# Weather Data ETL Pipeline

## 📌 Project Overview

This project is an end-to-end Weather Data ETL Pipeline developed using Python.

The pipeline collects weather data from the Open-Meteo API, stores the raw response as JSON, transforms the data using Pandas, and loads the processed data into PostgreSQL.

The complete pipeline can be executed using a single Python command.

## 🏗️ ETL Architecture

Weather API
     ↓
Extract
     ↓
Raw JSON
     ↓
Transform using Pandas
     ↓
Processed CSV
     ↓
Load into PostgreSQL
     ↓
Weather Database

## 🛠️ Technologies Used

- Python
- REST API
- Requests
- Pandas
- PostgreSQL
- Psycopg2
- python-dotenv
- Git
- GitHub
- VS Code

## ⚙️ ETL Process

### 1. Extract

Weather data is collected from the Open-Meteo API.

The pipeline retrieves:

- Temperature
- Humidity
- Surface Pressure
- Wind Speed
- Weather Code
- Time

The raw API response is stored as:

`data/raw/weather.json`

### 2. Transform

The raw JSON data is processed using Pandas.

The required weather fields are extracted and converted into a structured DataFrame.

The transformed data is saved as:

`data/processed/weather.csv`

### 3. Load

The processed CSV data is loaded into PostgreSQL.

Database table:

`weather_data`

The table stores:

- Time
- Temperature
- Humidity
- Pressure
- Wind Speed
- Weather Code

## 📂 Project Structure

```text
weather-data-etl-pipeline/
│
├── data/
│   ├── raw/
│   │   └── weather.json
│   │
│   └── processed/
│       └── weather.csv
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── README.md