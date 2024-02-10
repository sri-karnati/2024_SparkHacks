# to retreive data

import json










# Sample data to send to JS
data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}


# Convert Python dictionary to JSON string and print it
json_str = json.dumps(data)
print(json_str)
