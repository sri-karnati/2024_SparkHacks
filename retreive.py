# to retreive data

import json

import pandas as pd

# this stores all the states and for each state it stores the counties and their coordinates

# Assuming your CSV file is named 'your_file.csv'
file_path = 'src//uscounties.csv'

# Read CSV into a DataFrame
df = pd.read_csv(file_path)

# Create a dictionary to store the organized data
state_county_data = {}

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    state = row['state_name']
    county = row['county_full']
    latitude = row['lat']
    longitude = row['lng']

    # Check if the state is already in the dictionary
    if state not in state_county_data:
        state_county_data[state] = {}

    # Add county data to the state
    state_county_data[state][county] = {'Latitude': latitude, 'Longitude': longitude}
# Print the resulting dictionary
print(state_county_data['Alaska'])
print(f"Number of counties in Alaska: {len(state_county_data['Alaska'])}")










# Sample data to send to JS
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# Convert Python dictionary to JSON string and print it
json_str = json.dumps(data)
print(json_str)
