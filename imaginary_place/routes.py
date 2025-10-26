from flask import Flask,render_template, redirect, url_for,request
from imaginary_place import app
from imaginary_place import init_bank
import sqlite3
import random

init_bank.create_table()

@app.route('/', methods=['GET','POST'])
def homepage():
    conn = init_bank.connect()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM places")
    
    data = cursor.fetchall()
    
    random.shuffle(data)
    
    return render_template('homepage.html', data=data)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/sending', methods=['POST','GET'])
def sending():
    conn = init_bank.connect()
    cursor = conn.cursor()
    
    author = request.form['author']
    description = request.form['description']
    history = request.form['history']
    
    cursor.execute("INSERT INTO places (author,description, text) VALUES (?,?,?)", (author, description, history))
    conn.commit()
    
    return redirect(url_for('homepage'))