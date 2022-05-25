# Start with a basic flask app webpage.
from flask import Flask, render_template, request, redirect, url_for, copy_current_request_context, jsonify, session, send_from_directory
# flask-moment
from flask_moment import Moment
#from flask_bower import Bower

from datetime import date, datetime, timedelta

__author__ = 'priyandari'

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
    return render_template('index.html')

if __name__ == '__main__':
    app.run()