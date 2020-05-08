# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-05 01:39:57
 @modify date 2020-05-05 07:12:44
 @desc [2. Aplikasi menggunakan Model]
"""
from flask import Flask
from models import MyFlaskModel

application = Flask(__name__)

@application.route('/')
def index():
    # membuat objek dari kelas MyFlaskModel
    model = MyFlaskModel()
    return '<h2>Hello Flask</h2>'
	
    # mengembalikan nilai yang diambil dari model
    return model.getText()

if __name__ == "__main__":
    application.run(debug=True)