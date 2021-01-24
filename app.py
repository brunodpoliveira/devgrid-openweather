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


# TODO Receives a user defined ID, collect weather data from Open Weather API and store:
# USER DEFINED ID, DATETIME OF REQUEST, JSON DATA W/ CITY ID,TEMP(C),HUMIDITY

@app.route('/users/<user_id>', methods=['GET', 'POST'])
def user(u_id):
    if request.method == 'GET':
        """return the information for <user_id>"""
        # receive create user id in html file
        # u_id = request.args.get(user)

    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # generate unique id for each request
        # send modded user id to def init GET request


@app.route('/api', methods=['GET', 'POST'])
def initialize():
    # html code to activate def user here or in html file
    if request.method == 'POST':
        pass
        # activate owm_async here
        # activate fetch_url here
        # activate extract_fields_from_response here
        # save u_id_mod (from def user), datetime request
        # save json data (c_id,temp,humidity) (save_to_json)
        # send progress to GET

        # TODO Receives the user defined ID,
        #  returns with the percentage of the POST progress ID (collected cities completed)
        #  until the current moment
        if request.method == 'GET':
            pass
            # postinfo = request.args.get('u_id_mod','post_progress')
            # receive modded user id here
            # POST progress here
            # display it on html file

        # return str(var_name_here.get_response(postinfo))
        # return str(bot.get_response(usertext))

        pass


if __name__ == "__main__":
    user_id = input('user id: ')
    app.run()
