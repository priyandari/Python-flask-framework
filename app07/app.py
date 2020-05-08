# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-05 10:13:51
 @modify date 2020-05-05 10:13:51
 @desc [description]
"""
from flask import Flask

application = Flask(__name__)

@application.route('/produk/<nama>')
def produk(nama):
    return '<h2>Produk %s </h2>' % nama 

if __name__=='__main__':
    application.run(debug=True)