#Index page
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)


#Application routing map
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=81)
