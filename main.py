import pandas as pd
import json
from datetime import datetime, timedelta
import openmeteo_requests
import requests_cache
from retry_requests import retry
import numpy as np

def get_user_input_state():
    state_name = input("Enter the name of the state you want to scrape data for: ")
    return state_name

def get_user_input_crop():
    crop_name = input("Enter the name of the crop you are interested in: ").capitalize()
    return crop_name

cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

file_path = 'C:/Users/dwij/Downloads/uscounties.csv'
df = pd.read_csv(file_path)

state_name = get_user_input_state()
crop_name = get_user_input_crop()

df = df[df['state_name'] == state_name]

soil_data_by_county = {}

start_date = (datetime.now() - timedelta(days=367)).strftime('%Y-%m-%d')
end_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

ideal_conditions = {
    'Corn': {'soil_moisture': 0.23, 'precipitation': 20},
    'Potatoes': {'soil_moisture': 0.2, 'precipitation': 25},
    'Wheat': {'soil_moisture': 0.12, 'precipitation': 15},
    'Strawberries': {'soil_moisture': 0.25, 'precipitation': 30},
    'Tomatoes': {'soil_moisture': 0.18, 'precipitation': 35},
    'Cucumbers': {'soil_moisture': 0.3, 'precipitation': 40},
    'Onions': {'soil_moisture': 0.15, 'precipitation': 10},
}

if crop_name not in ideal_conditions:
    print(f"{crop_name} is not supported or incorrect. Please add it to the ideal_conditions dictionary.")
    exit()

county_scores = []

for index, row in df.iterrows():
    county = row['county_full']
    latitude = row['lat']
    longitude = row['lng']

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "soil_moisture_0_to_7cm,precipitation"
    }

    responses = openmeteo.weather_api("https://archive-api.open-meteo.com/v1/archive", params=params)

    if responses:
        response = responses[0]
        hourly = response.Hourly()
        soil_moisture = hourly.Variables(0).ValuesAsNumpy()
        precipitation = hourly.Variables(1).ValuesAsNumpy()  # Assuming second variable is precipitation
        average_moisture = float(np.nanmean(soil_moisture))
        average_precipitation = float(np.nanmean(precipitation))

        soil_data_by_county[county] = {
            "average_soil_moisture_0_to_7cm": average_moisture,
            "average_precipitation": average_precipitation
        }
    else:
        print(f"No data available for {county}")

conditions = ideal_conditions[crop_name]
for county, data in soil_data_by_county.items():
    moisture_diff = abs(data["average_soil_moisture_0_to_7cm"] - conditions['soil_moisture'])
    precipitation_diff = abs(data["average_precipitation"] - conditions['precipitation'])
    score = moisture_diff + precipitation_diff
    county_scores.append((county, score))

county_scores.sort(key=lambda x: x[1])

print(f"Counties sorted from best to worst for {crop_name}:")
for county, score in county_scores:
    print(f"{county}")