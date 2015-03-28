#Index page
from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, flash
from logging import DEBUG

app = Flask(__name__)
app.logger.setLevel(DEBUG)

bookmarks = []
app.config['SECRET_KEY'] = "1\x99/\x05\x99\xde\xfb\xfd\x805#\xf4uRL\xb5\xc1\xa4\x8c\x9a'\x89l\xf0"

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "adc90",
        date = datetime.utcnow()
        ))

#Application routing map
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Title", text="More text")

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == "POST":
        url = request.form['fname']
        store_bookmark(url)
        flash("Stored bookmark: {0}".format(url))
        app.logger.debug('stored url: ' + url)
        return redirect(url_for('index'))
    return render_template('form.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return "500 error", 500

if __name__ == '__main__':
    app.run(port=81)
