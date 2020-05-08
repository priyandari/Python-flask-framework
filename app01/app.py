# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-05 01:28:31
 @modify date 2020-05-05 09:33:00
 @desc [1. Introduction Flask]
"""
from flask import Flask

application = Flask(__name__)

@application.route('/')
def index():
    return '<h2>Hello Flask</h2>'
	
if __name__ == "__main__":
    application.run(debug=True)