from flask import Flask, render_template, request
# from flask_sql
# from flask
import pandas as pd

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

def random():
    request.

# @app.route('/read-from')

if __name__ == '__main__':
    app.run(debug=True)
