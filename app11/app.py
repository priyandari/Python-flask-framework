# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-10 14:50:12
 @modify date 2020-05-10 14:50:12
 @desc [description]
"""
from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

application=Flask(__name__)

conn = cursor = None
def openDb():
    global conn, cursor
    conn = sqlite3.connect("dbbuku.db")
    cursor = conn.cursor()
    
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@application.route('/')
def index():
    openDb()
    container = []
    for kode, judul, penulis in cursor.execute('SELECT kode,judul,penulis FROM buku'):
        container.append((kode,judul,penulis))
    closeDb()
    return render_template('index.html', container=container)

@application.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        kode=request.form['kode']
        judul=request.form['judul']
        penulis=request.form['penulis']
        data=kode,judul, penulis
        openDb()
        cursor.execute('INSERT INTO buku ("kode", "judul", "penulis") VALUES(?,?,?)', data)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('add_form.html')

@application.route('/edit/<kode>', methods=['GET', 'POST'])
def edit(kode):
    openDb()
    result = cursor.execute('SELECT kode, judul, penulis FROM buku WHERE kode=?', (kode,))
    data = cursor.fetchone()
    if request.method == 'POST':
        kode=request.form['kode']
        judul=request.form['judul']
        penulis=request.form['penulis']
        cursor.execute('''
            UPDATE buku SET judul=?, penulis=? WHERE kode=?           
            ''', (judul, penulis, kode))
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit_form.html', data=data)
    
@application.route('/delete/<kode>', methods=['GET', 'POST']) 
def delete(kode):
    openDb()
    cursor.execute('DELETE FROM buku WHERE kode=?', (kode,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    application.run(debug=True)