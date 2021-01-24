from flask import Flask, render_template, request
import os
import owm_async

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False


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
        # save json data (c_id,temp,humidity) (save_to_json)
        # send POST progress and u_id_r in progress to GET

        # TODO Receives the user defined ID,
        #  returns with the percentage of the POST progress ID (collected cities completed)
        #  until the current moment
        if request.method == 'GET':
            # Receives user id (created in html file)
            pass
            # info = request.args.get('progress')
            # return str(progress)

        pass


if __name__ == "__main__":
    app.run()
