import pyowm
import json
import datetime
import requests

# ------------------------------------------------------------------------

# import credentials as json for improved security
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
user_id = input("user id: ")

city_name = input("city name : ")

# base_url + api_key + city_name = final url
final_url = creds['BASE_URL'] + "q=" + city_name + "&appid=" + api_key + "&units=metric"

# capture own api json data
w_data = requests.get(final_url).json()
# ------------------------------------------------------------------------

if w_data["cod"] != "404":
    a = w_data
    city_id = a["id"]
    temp = [a['main']['temp']]
    humidity = [a['main']['humidity']]

    print('temp (celsius) ' + str(temp) + 'city id ' + str(city_id) + 'humidity ' + str(humidity))

else:
    print('not found')

# ------------------------------------------------------------------------
with open("result.json", mode='r', encoding='utf-8') as f:
    f_result = json.load(f)
with open("result.json", mode='w', encoding='utf-8') as f:
    entry = {'CITY_ID': city_id, 'TEMPERATURE': temp, 'HUMIDITY': humidity}
    f_result.append(entry)
    json.dump(f_result, f)

with open("user_id.json", mode='r', encoding='utf-8') as f:
    f2_result = json.load(f)
with open("user_id.json", mode='w', encoding='utf-8') as f2:
    entry = {'USER_ID': user_id, 'REQUEST_DATETIME': json.dumps(d, default=timeconverter)}
    f2_result.append(entry)
    json.dump(f2_result, f2)

