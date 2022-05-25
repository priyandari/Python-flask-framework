"""
Demo Flask application to test the operation of Flask with socket.io
Aim is to create a webpage that is constantly updated with random numbers from a background python process.
30th May 2014
===================
Updated 13th April 2018
+ Upgraded code to Python 3
+ Used Python3 SocketIO implementation
+ Updated CDN Javascript and CSS sources
"""
# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request, redirect, url_for, copy_current_request_context
#from flask import Flask, render_template, request, redirect, url_for
#from random import random
from time import sleep
from threading import Thread, Event

from datetime import date, datetime
from adhan import adhan
from adhan.methods import MAKKAH, ASR_STANDARD, MUSLIM_WORLD_LEAGUE

__author__ = 'slynn'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

def adzanGenerator():
    """
    Generate azanTime every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """

    #infinite loop of magical random numbers
    while not thread_stop_event.isSet():

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
    
        dictAzan= {'fajr': '','shuruq':'','zuhr':'','asr': '','maghrib':'','isya': '','now':''}
        dictAzan['fajr'] = timeprayers['fajr'].strftime("%d/%m/%Y %H:%M")
        dictAzan['shuruq'] = timeprayers['shuruq'].strftime("%d/%m/%Y %H:%M")
        dictAzan['zuhr'] = timeprayers['zuhr'].strftime("%d/%m/%Y %H:%M")
        dictAzan['asr'] = timeprayers['asr'].strftime("%d/%m/%Y %H:%M")
        dictAzan['maghrib'] = timeprayers['maghrib'].strftime("%d/%m/%Y %H:%M")
        dictAzan['isya'] = timeprayers['isha'].strftime("%d/%m/%Y %H:%M")

        now = datetime.now()     
        #number = now.strftime("%d/%m/%Y %H:%M:%S")
        dictAzan['now'] = now.strftime("%d/%m/%Y %H:%M:%S")
        
        socketio.emit('newnumber', {'number': dictAzan}, namespace='/test')
        socketio.sleep(10)


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = socketio.start_background_task(adzanGenerator)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)