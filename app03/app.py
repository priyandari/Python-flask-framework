# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-05 07:17:32
 @modify date 2020-05-05 07:17:32
 @desc [3. Basic templates]
"""
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('mytemplate.html')
	
if __name__ == "__main__":
    application.run(debug=True)