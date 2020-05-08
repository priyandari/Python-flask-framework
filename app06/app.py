# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-05 09:12:46
 @modify date 2020-05-05 09:12:46
 @desc [description]
"""
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('home.html')

@application.route('/product')
def product():
    return render_template('product.html')

@application.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    application.run(debug=True)