# -*- coding: utf-8 -*-
"""
 @author Priyandari
 @create date 2020-05-10 14:50:12
 @modify date 2020-05-10 14:50:12
 @desc [description]
"""
from unicodedata import category
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector, os 

application=Flask(__name__)

conn = cur = None
def openDb():
    global conn, cur
    conn = mysql.connector.connect(
        user="root",
        password="",
        host="127.0.0.1",
        database="stayhome"
        )
    cur = conn.cursor()
    
def closeDb():
    global conn, cur
    cur.close()
    conn.close()

@application.route('/')
def index():
    openDb()
    container = []
    cur.execute('SELECT catalogNo,title,category FROM video')
    result = cur.fetchall()
    for kode, judul, category in result:
        container.append((kode,judul,category))
    closeDb()
    return render_template('index.html', container=container)

@application.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        kode=request.form['kode']
        judul=request.form['judul']
        category=request.form['category']
        data=kode,judul,category
        openDb()
        cur.execute('INSERT INTO buku ("catalogNo", "title", "category") VALUES(?,?,?)', data)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('add_form.html')

@application.route('/edit/<kode>', methods=['GET', 'POST'])
def edit(kode):
    openDb()
    cur.execute('SELECT catalogNo,title,category FROM video WHERE catalogNo="%s"'%(kode))
    result = cur.fetchone()
    #data = cur.fetchone()
    if request.method == 'POST':
        kode=request.form['kode']
        judul=request.form['judul']
        category=request.form['category']
        cur.execute('''
            UPDATE video SET title="%s",category="%s" 
            WHERE catalogNo="%s"'''
            %(judul, category, kode))
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit_form.html', data=result)
    
@application.route('/delete/<kode>', methods=['GET', 'POST']) 
def delete(kode):
    openDb()
    cur.execute('DELETE FROM video WHERE catalogNo="%s"'%(kode,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    application.run(debug=True)