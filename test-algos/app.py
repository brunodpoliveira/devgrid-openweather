import pyowm
import json
import datetime
import asyncio
import pprint
import numpy as np
import aiofiles
import aiohttp
from aiohttp import ClientSession
import logging
import re
import sys
import os
from urllib.error import HTTPError
from typing import IO

# ------------------------------------------------------------------------
# TESTING PURPOSES ONLY - DEACTIVATE IN PRODUCTION ENVIRON
ENV = 'dev'

if ENV == 'dev':
    logging.basicConfig(
        format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
        level=logging.DEBUG,
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )
    logger = logging.getLogger("areq")
    logging.getLogger("chardet.charsetprober").disabled = True
else:
    print('production mode')

# import credentials as json for improved security
with open('api_key.json', 'r') as file:
    creds = json.load(file)
    api_key = creds['API_KEY']
    # instantiate object
    owm_obj = pyowm.OWM(api_key)

# time converter
d = {'date': datetime.datetime.now()}

# TODO SEE IF C_ID CAN BE PUT IN OTHER .PY FILE

c_id_array = np.array(
    ["3439525",
     "3439781",
     "3440645"])

"""
c_id_array = np.array(
    ["3439525", "3439781", "3440645", "3442098", "3442778", "3443341", "3442233", "3440781", "3441572",
     "3441575", "3443207", "3442546", "3441287", "3441242", "3441686", "3440639", "3441354", "3442057",
     "3442585", "3442727", "3439705", "3441890", "3443411", "3440054", "3441684", "3440711", "3440714",
     "3440696", "3441894", "3443173", "3441702", "3442007", "3441665", "3440963", "3443413", "3440033",
     "3440034", "3440571", "3443025", "3441243", "3440789", "3442568", "3443737", "3440771", "3440777",
     "3442597", "3442587", "3439749", "3441358", "3442980", "3442750", "3443352", "3442051", "3441442",
     "3442398", "3442163", "3443533", "3440942", "3442720", "3441273", "3442071", "3442105", "3442683",
     "3443030", "3441011", "3440925", "3440021", "3441292", "3480823", "3440379", "3442106", "3439696",
     "3440063", "3442231", "3442926", "3442050", "3440698", "3480819", "3442450", "3442584", "3443632",
     "3441122", "3441475", "3440791", "3480818", "3439780", "3443861", "3440780", "3442805", "7838849",
     "3440581", "3440830", "3443756", "3443758", "3443013", "3439590", "3439598", "3439619", "3439622",
     "3439652", "3439659", "3439661", "3439725", "3439748", "3439787", "3439831", "3439838", "3439902",
     "3440055", "3440076", "3440394", "3440400", "3440541", "3440554", "3440577", "3440580", "3440596",
     "3440653", "3440654", "3440684", "3440705", "3440747", "3440762", "3440879", "3440939", "3440985",
     "3441074", "3441114", "3441377", "3441476", "3441481", "3441483", "3441577", "3441659", "3441674",
     "3441803", "3441954", "3441988", "3442058", "3442138", "3442206", "3442221", "3442236", "3442238",
     "3442299", "3442716", "3442766", "3442803", "3442939", "3443061", "3443183", "3443256", "3443280",
     "3443289", "3443342", "3443356", "3443588", "3443631", "3443644", "3443697", "3443909", "3443928",
     "3443952", "3480812", "3480820", "3480822", "3480825"])
"""


def timeconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


# TODO ASYNC CALL TO API
# TODO HOLD FOR TIME IN CASE OWN HALTS US
# TODO LIMIT REQUEST TO 60/MIN


async def fetch_url(city_id, session):
    """create and fetch urls in array"""
    # iterate through list
    for i in range(len(c_id_array)):
        element = str(c_id_array[i])
    # base_url + group_id + api_key +  = final url (units changed to metric - standard is kelvin)
    url = creds['BASE_URL'] + f"group?id={element}" + "&appid=" + api_key + "&units=metric"
    print(url)
    try:
        response = await session.request(method='GET', url=url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response status ({url}): {response.status}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


def extract_fields_from_response(response):
    """Extract fields from API's response"""
    list_a = response.get("list", [{}])[0]
    main_a = list_a.get("main")
    c_name = list_a.get("name")
    c_id = list_a.get("id")
    temp = main_a.get("temp")
    humidity = main_a.get("humidity")

    return (
        c_name,
        c_id,
        temp,
        humidity
    )


async def run_program(city_id, session):
    try:
        response = await fetch_url(city_id, session)
        parsed_response = extract_fields_from_response(response)
        print(f"Response: {json.dumps(parsed_response, indent=2)}")
    except Exception as err:
        print(f"Exception occured: {err}")
        pass


async def main():
    async with ClientSession() as session:
        await asyncio.gather(*[run_program(city_id, session) for city_id in c_id_array])


if __name__ == '__main__':
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
