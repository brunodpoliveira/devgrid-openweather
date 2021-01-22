import pyowm
import json
import time
import requests
from pprint import pprint

# ------------------------------------------------------------------------

# import credentials as json for improved security
with open('api_key.json', 'r') as file:
    creds = json.load(file)
api_key = creds['API_KEY']
# instantiate object
owm_obj = pyowm.OWM(api_key)
# ------------------------------------------------------------------------
#user_id = input("user id: ")

city_name = input("city name : ")

# base_url + api_key + city_name = final url
final_url = creds['BASE_URL'] + "appid=" + api_key + "&q" + city_name

# capture own api json data
w_data = requests.get(final_url).json()
pprint(w_data)
# ------------------------------------------------------------------------
#city_id = w_data["id"]
#temp = w_data('celsius')["temp"]
#humidity = w_data["humidity"]
#print('temp (celsius)' + str(temp) + 'city id' + str(city_id) + 'humidity' + str(humidity))
# ------------------------------------------------------------------------
"""
if w_data["cod"] != "404":
    a = w_data
    b = w_data["weather"]

    print('temp (celsius)' + str(temp) + 'city id' + str(city_id) + 'humidity' + str(humidity))

else:
    print('not found')
# ------------------------------------------------------------------------

# TODO: STORE UNIQUE USER ID AND Datetime of request
u_id_json = {}
u_id_json['USER_ID'] = user_id
u_id_json['REQUEST_DATETIME'] = ""

# ------------------------------------------------------------------------

s_result = {}
s_result['CITY_ID'] = city_id
s_result['TEMPERATURE'] = temp
s_result['HUMIDITY'] = humidity

with open("result.json", "w") as file:
    json.dump(s_result, file)
with open("user_id.json", "w") as file2:
    json.dump(u_id_json, file2)
"""