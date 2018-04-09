# views.py

from flask import render_template
import random

from app import app

@app.route('/')
def index():
    random_number = random.randint(1, 1000)
    return render_template("index.html", random_number=random_number)
    #return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")