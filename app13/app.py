import os
import json
import requests

from functools import wraps
from flask import Flask, request, jsonify, session, redirect, render_template, send_from_directory
from datetime import date , datetime
import pytz
from adhan import adhan
from adhan.methods import MAKKAH, ASR_STANDARD, MUSLIM_WORLD_LEAGUE

#from flask_bower import Bower
from flask_moment import Moment

#app = Flask(__name__)
#app.debug = True

moment = Moment()
#moment.init_app(app)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    # initialize moment on the app within create_app()
    moment.init_app(app)
    app.debug = True
   
    return app

debug = True
app = create_app(debug)   

#Bower(app)
#moment = Moment(app)

#app.secret_key = "supersecretkey"

params = {}
params.update(MUSLIM_WORLD_LEAGUE)
params.update(ASR_STANDARD)

#datetime_str ='2020-01-01 08:15:27.24'
#datetime_obj = datetime.datetime.strptime(datetime_str,'%Y-%m-%d %H:%M:%S.%f')

timeprayers = adhan(
    #day=datetime_obj.date(),
    day=date.today(),
    location=(-7.779415,110.439625),
    parameters=params,
    timezone_offset=-7.7,
)

"""
{'fajr': datetime.datetime(2020, 5, 31, 4, 24), 'zuhr': datetime.datetime(2020, 5, 31, 11, 38), 'shuruq': datetime.datetime(2020, 5, 31, 5, 47), 'asr': datetime.datetime(2020, 5, 31, 14, 59), 'maghrib': datetime.datetime(2020, 5, 31, 17, 29), 'isha': datetime.datetime(2020, 5, 31, 18, 43)}
"""
"""    
dictAzan= {'fajr': '','shuruq':'','zuhr':'','asr': '','maghrib':'','isya': '','ddate':'','dtime':'','ttime':''}
dictAzan['fajr'] = timeprayers['fajr'].strftime('%H:%M')
dictAzan['shuruq'] = timeprayers['shuruq'].strftime('%H:%M')
dictAzan['zuhr'] = timeprayers['zuhr'].strftime('%H:%M')
dictAzan['asr'] = timeprayers['asr'].strftime('%H:%M')
dictAzan['maghrib'] = timeprayers['maghrib'].strftime('%H:%M')
dictAzan['isya'] = timeprayers['isha'].strftime('%H:%M')

tz_ID = pytz.timezone('Asia/Jakarta')
now = datetime.now(tz_ID) # current date and time
dictAzan['ddate'] = now.strftime('%d %B %Y')
dictAzan['dtime'] = now.strftime('%d %b %Y | %H:%M:%S')
dictAzan['ttime'] = now.strftime('%H:%M:%S')

"""

@app.route('/')
def index():
    return render_template('index.html', timeAdzans=timeprayers)

if __name__ == "__main__":
    app.run(debug=True)