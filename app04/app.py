# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-05 07:43:41
 @modify date 2020-05-05 07:43:41
 @desc [4. Basic model and templates]
"""
from flask import Flask, render_template
from models import MyFlaskModel

application = Flask(__name__)

@application.route('/')
def index():
    # buat objek dari class MyFlaskModel
    model = MyFlaskModel()
    
    # kirim model ke view atau templates
    return render_template('mytemplate.html', model=model)

if __name__ == '__main__':
    application.run(debug=True)