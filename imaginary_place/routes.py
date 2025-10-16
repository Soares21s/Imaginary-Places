from flask import Flask,render_template
from imaginary_place import app

@app.route('/')
def homepage():
    return render_template('homepage.html')
