from flask import Flask,render_template
from imaginary_place import app
from imaginary_place import init_bank

init_bank.create_table()

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/write')
def write():
    return render_template('write.html')
