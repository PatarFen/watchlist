from flask import Flask, url_for, escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "heheda"
