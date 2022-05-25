# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-31 21:44:03
 @modify date 2020-05-31 21:44:03
 @desc [Waktu Sholat]
"""
from flask import Flask, render_template, request, redirect, url_for
import os

from datetime import date #, datetime
from adhan import adhan
from adhan.methods import MAKKAH, ASR_STANDARD, MUSLIM_WORLD_LEAGUE
import sqlite3, os

application=Flask(__name__)
"""
conn = cursor = None
def openDb():
    global conn, cursor
    conn = sqlite3.connect("dbbuku.db")
    cursor = conn.cursor()
    
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()
    .
"""

    

params = {}
params.update(MUSLIM_WORLD_LEAGUE)
params.update(ASR_STANDARD)

#datetime_str ='2020-01-01 08:15:27.24'
#datetime_obj = datetime.datetime.strptime(datetime_str,'%Y-%m-%d %H:%M:%S.%f')


adhan_times = adhan(
    #day=datetime_obj.date(),
    day=date.today(),
    location=(-7.779415,110.439625),
    parameters=params,
    timezone_offset=-7.7,
)


@application.route('/')
def index():
    """
    openDb()
    container = []
    for kode, judul, penulis in cursor.execute('SELECT kode,judul,penulis FROM buku'):
        container.append((kode,judul,penulis))
    closeDb()
    
    {'fajr': datetime.datetime(2020, 5, 31, 4, 24), 'zuhr': datetime.datetime(2020, 5, 31, 11, 38), 'shuruq': datetime.datetime(2020, 5, 31, 5, 47), 'asr': datetime.datetime(2020, 5, 31, 14, 59), 'maghrib': datetime.datetime(2020, 5, 31, 17, 29), 'isha': datetime.datetime(2020, 5, 31, 18, 43)}
    """
    return render_template('index2.html', timeprayers=adhan_times)

if __name__ == "__main__":
    application.run(debug=True)