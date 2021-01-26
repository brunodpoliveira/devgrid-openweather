import pyowm
import json
import datetime
import asyncio
from aiohttp import ClientSession
import logging
import sys
from urllib.error import HTTPError
import time
from ratelimit import limits, RateLimitException, sleep_and_retry
from backoff import on_exception, expo
from progress.bar import IncrementalBar
import app
# ------------------------------------------------------------------------
logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True

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


"""
c_id_array = [
    "3439525", "3439781", "3440645", "3442098", "3442778", "3443341", "3442233", "3440781", "3441572",
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
    "3443952", "3480812", "3480820", "3480822", "3480825"]
"""

c_id_array = [
    "3439525", "3439781", "3440645", "3442098"]


async def fetch_url(city_id, session):
    """create and fetch urls, using array to store the cities ids"""
    # base_url + group_id + api_key +  = final url (units changed to metric - standard is kelvin)
    url = creds['BASE_URL'] + "group?id=" + city_id + "&appid=" + api_key + "&units=metric"
    try:
        response = await session.request(method='GET', url=url)
        response.raise_for_status()
        print(f"Response status ({url}): {response.status}")
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


one_min = 60


# TODO FIX RATE LIMIT EXCEPTION W/OUT RAISING CALLS/MIN (CALLS=167 SOLVES IT, BUT
#  OWM WILL BAN YOU)


#@on_exception(expo, RateLimitException, max_tries=8)
@sleep_and_retry
@limits(calls=60, period=one_min)
# TODO CHANGE THIS DEF TO ASYNC
def extract_fields_from_response(u_id, response):
    """Extract fields from API's response"""
    # TODO CHANGE .GET() TO .REQUEST()
    res = response.get("list", [{}])[0]
    # TODO UNIQUE ID FOR EACH REQUEST
    user_id_search = u_id + str(' user')
    main_a = res.get("main")
    c_name = res.get("name")
    c_id = res.get("id")
    temp = main_a.get("temp")
    humidity = main_a.get("humidity")
    save_to_json(c_id, user_id_search, temp, humidity)
    return (
        user_id_search,
        c_name,
        c_id,
        temp,
        humidity
    )


def save_to_json(c_id, u_id, temp, humidity):
    with open("result.json", mode='r', encoding='utf-8') as f:
        f_result = json.load(f)
    with open("result.json", mode='w', encoding='utf-8') as f:
        entry = {'CITY_ID': c_id, 'TEMPERATURE': temp, 'HUMIDITY': humidity}
        f_result.append(entry)
        json.dump(f_result, f)
    with open("user_id.json", mode='r', encoding='utf-8') as f:
        f2_result = json.load(f)
    with open("user_id.json", mode='w', encoding='utf-8') as f:
        entry = {'USER_ID': u_id, 'REQUEST_DATETIME': json.dumps(d, default=timeconverter)}
        f2_result.append(entry)
        json.dump(f2_result, f)


async def run_program(city_id, session):
    try:
        response = await fetch_url(city_id, session)
        parsed_response = extract_fields_from_response(app.user_id, response)
        print(f"Response: {json.dumps(parsed_response, indent=2)}")
    except Exception as err:
        print(f"Exception occured: {err}")
        pass


async def main():
    # percentage of progress
    bar = IncrementalBar('progress', max=len(c_id_array))
    async with ClientSession() as session:
        tasks = []
        for city_id in c_id_array:
            bar.next()
            task = asyncio.create_task(run_program(city_id, session))
            time.sleep(1)
            bar.finish()
        tasks.append(task)

        return await asyncio.gather(*tasks, return_exceptions=True), bar


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
