from flask import Flask, request, jsonify
import pandas as pd
import json
from datetime import datetime, timedelta
import openmeteo_requests
import requests_cache
from retry_requests import retry
import numpy as np


from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/process_selection', methods=['POST'])
def process_selection():
    data = request.json
    crop_name = data['crop'].capitalize()
    state_name = data['state']

    # Your existing Python code with modifications to use `crop_name` and `state_name` directly
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    file_path = 'src/uscounties.csv'
    df = pd.read_csv(file_path)

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
        return jsonify({"error": f"{crop_name} is not supported or incorrect. Please add it to the ideal_conditions dictionary."}), 400

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
            precipitation = hourly.Variables(1).ValuesAsNumpy()
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

    # Simplified response for demonstration purposes
    top_counties = [county for county, score in county_scores[:5]]  # Return top 5 counties as an example
    print(f'top counties: {top_counties}')
    print(request.json)  # Add this line to debug the incoming JSON data
    return jsonify({"Top Counties": top_counties})
if __name__ == '__main__':
    app.run(debug=True)
