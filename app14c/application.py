# Start with a basic flask app webpage.
from flask import Flask, render_template, request, redirect, url_for, copy_current_request_context, jsonify, session, send_from_directory
# flask-moment
from flask_moment import Moment
#from flask_bower import Bower

from datetime import date, datetime, timedelta
from jinja2 import Template
# Library Adhan
from adhan import adhan
from adhan.methods import MAKKAH, ASR_STANDARD, MUSLIM_WORLD_LEAGUE


__author__ = 'priyandari'

# Generate Waktu SHolat

params = {}
params.update(MUSLIM_WORLD_LEAGUE)
params.update(ASR_STANDARD)

timePrayers = adhan(
    #day=datetime_obj.date(),
    day=date.today(),
    location=(-7.779415,110.439625),
    parameters=params,
    timezone_offset=-7.7,
)
"""
ouput :
{'fajr': datetime.datetime(2020, 5, 31, 4, 24), 'zuhr': datetime.datetime(2020, 5, 31, 11, 38), 'shuruq': datetime.datetime(2020, 5, 31, 5, 47), 'asr': datetime.datetime(2020, 5, 31, 14, 59), 'maghrib': datetime.datetime(2020, 5, 31, 17, 29), 'isha': datetime.datetime(2020, 5, 31, 18, 43)}
"""



# Flask-moment
moment = Moment()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    # initialize moment on the app within create_app()
    moment.init_app(app)
    app.debug = True
    app.secret_key = 'supersecret!'
   
    return app

# Flask Run
config ={}
app = create_app(config)   

@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html', timeAdhans=timePrayers)

if __name__ == '__main__':
    app.run()