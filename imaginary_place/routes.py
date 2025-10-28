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
    
    try: 
        cursor.execute("INSERT INTO places (author,description, text) VALUES (?,?,?)", (author, description, history))
        world_id = cursor.lastrowid
        conn.commit()
        
        return redirect(url_for('worlds', world_id=world_id))
    
    except sqlite3.Error as e:
        print(f"Erro ao inserir: {e}") 
        return "Erro ao enviar dados", 500
    finally:
        conn.close()
    
    return redirect(url_for('write'))

@app.route('/world/<int:world_id>')
def worlds(world_id):
    conn = init_bank.connect()
    cursor = conn.cursor()
    
    world = conn.execute("SELECT * FROM places WHERE id = ? ", (world_id,)).fetchone()
    
    if world is None: 
        return render_template('404.html'), 404
    return render_template('worlds_template.html', world=world)
        