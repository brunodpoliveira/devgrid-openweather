from flask import Flask, render_template, request
import os
# ------------------------------------------------------------------------
# TODO MAKE SURE OWM_ASYNC CAN SEE USER_ID FROM POST METHOD
user_id = 'temporary, wrong one'
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/submit', methods=['GET', 'POST'])
def main_loop():
    # TODO Receives a user defined ID, collect weather data from Open Weather API(done) and store:
    # USER DEFINED ID, DATETIME OF REQUEST(done), JSON DATA W/ CITY ID,TEMP(C),HUMIDITY
    if request.method == 'POST':
        # u_id is created in html file
        #TODO FIX BUG (user id: None)
        u_id = request.args.get('msg')
        print('user id: ', str(u_id))
        # TODO pass u_id argument to owm_async and activate it here
        os.system('python3 owm_async.py')

        # read result.json and user_id.json and store them here
        # mix_json_files()
        return str(u_id.get_response(u_id))

    #  TODO Receives the user defined ID,
    #  returns with the percentage of the POST progress ID (collected cities completed)
    #  until the current moment
    if request.method == 'GET':
        # Receives modded_user_id (created in owm_async.extract_fields)
        info = request.args.get('modded_u_id', 'progress')
        return info


if __name__ == "__main__":
    app.run()
