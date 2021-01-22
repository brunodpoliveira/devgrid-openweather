import json

# Enter key below as string
credentials = {}
credentials['API_KEY'] = ''
credentials['BASE_URL'] = 'http://api.openweathermap.org/data/2.5/weather?'
# Save to file
with open("api_key.json", "w") as file:
    json.dump(credentials, file)
