from flask import Flask, render_template, request
import json
import os
import owm_async
from owm_async import d, timeconverter

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False


# TODO IMPLEMENT IT IN THE LOOP
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


@app.route("/")
def home():
    return render_template("index.html")


# TODO Receives a user defined ID, collect weather data from Open Weather API(done) and store:
# USER DEFINED ID, DATETIME OF REQUEST, JSON DATA W/ CITY ID,TEMP(C),HUMIDITY

@app.route('/submit', methods=['GET', 'POST'])
def main_loop():
    if request.method == 'POST':
        pass
        # Receives user id (created in html file)
        # activate owm_async here
        # activate fetch_url here
        # activate extract_fields_from_response here
        # store u_id (unique for each request)(u_id_r)
        # save u_id_r, datetime request
        # save json data (c_id,temp,humidity) (def save_to_json)(return jsonify?)
        # send POST progress and u_id_r in 'progress' to GET
        # return progress

        # TODO Receives the user defined ID,
        #  returns with the percentage of the POST progress ID (collected cities completed)
        #  until the current moment
        if request.method == 'GET':
            # Receives user id (created in html file)
            pass
            # info = request.args.get('u_id','progress')
            # return str('u_id',progress)

        pass


if __name__ == "__main__":
    app.run()
