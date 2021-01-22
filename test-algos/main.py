import pyowm
import json
import datetime
from array import *


# ------------------------------------------------------------------------


# import credentials as json for improved security
def read_api():
    with open('api_key.json', 'r') as file:
        creds = json.load(file)
    api_key = creds['API_KEY']
    # instantiate object
    owm_obj = pyowm.OWM(api_key)


# time converter
d = {'date': datetime.datetime.now()}


def timeconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


# ------------------------------------------------------------------------
# TODO POST - Receives a user defined ID, collect weather data from Open Weather API
user_id = input("user id: ")

a = group_id_array_loop().w_data
if a["cod"] != "404":
    city_id = a["id"]
    temp = [a['main']['temp']]
    humidity = [a['main']['humidity']]

else:
    print('not found')

# ------------------------------------------------------------------------

if __name__ == "__main__":
    with open("result.json", mode='r', encoding='utf-8') as f:
        f_result = json.load(f)
    with open("result.json", mode='w', encoding='utf-8') as f:
        entry = {'CITY_ID': city_id, 'TEMPERATURE': temp, 'HUMIDITY': humidity}
        f_result.append(entry)
        json.dump(f_result, f)
    with open("user_id.json", mode='r', encoding='utf-8') as f:
        f2_result = json.load(f)
    with open("user_id.json", mode='w', encoding='utf-8') as f:
        entry = {'USER_ID': user_id, 'REQUEST_DATETIME': json.dumps(d, default=timeconverter)}
        f2_result.append(entry)
        json.dump(f2_result, f)
