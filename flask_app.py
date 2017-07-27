#!/usr/bin/env python
from flask import Flask
from subprocess import Popen

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/update')
def update_app():
    p = Popen('git pull'.split(), cwd='/opt/release/flask_app')
    return 'update initiated'

if __name__ == '__main__':
    app.run()
