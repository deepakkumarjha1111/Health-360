
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello from Flask!'
    return render_template("home.html")
