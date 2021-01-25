from flask import Flask, render_template, request
import time
import owm_async


# ------------------------------------------------------------------------


def user_id():
    u_id = ''
    return u_id


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
    # USER DEFINED ID, DATETIME OF REQUEST, JSON DATA W/ CITY ID,TEMP(C),HUMIDITY
    if request.method == 'POST':
        # u_id is created in html file
        user_id.u_id = request.args.get('msg')

        # pass u_id argument to owm_async here
        # read result.json and user_id.json and store them here
        pass

    # TODO Receives the user defined ID,
    #  returns with the percentage of the POST progress ID (collected cities completed)
    #  until the current moment
    if request.method == 'GET':
        # Receives modded_user_id (created in owm_async.extract_fields)
        # info = request.args.get('modded_u_id','progress')
        # return info
        pass


if __name__ == "__main__":
    s = time.perf_counter()
    owm_async.main()
    app.run()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
