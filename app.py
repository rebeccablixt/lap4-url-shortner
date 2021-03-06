import random
import string
from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace("://", "ql://", 1)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


class Urls(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    long_url = db.Column(db.String())
    short_url = db.Column(db.String())

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url

    def __repr__(self):
        return f"<Url {self.short_url}>"



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_input = request.form['url_input']
        url_end = ""
    #  check if input in db already
        if Urls.query.filter_by(long_url=url_input).first():
    #  if in there, return short url            
            url_db_entry = Urls.query.filter_by(long_url=url_input).first()
            url_end = url_db_entry.short_url
    #  if not, generate short url            
        else:           
            letters = string.ascii_letters
            url_end = ''.join(random.choice(letters) for i in range(6))
            # url_end = "dsgfds"
    #  check if short url in the db      
    #  if in there, generate new short url      
            while Urls.query.filter_by(short_url=url_end).first():
                letters = string.ascii_letters
                url_end = ''.join(random.choice(letters) for i in range(6))
    # add new long and short urls to db
            url_to_insert = Urls(url_input, url_end)
            db.session.add(url_to_insert)
            db.session.commit()
        short_url_to_return = 'https://url--shorties.herokuapp.com/' + url_end
    #  return short url in render template
        visibility = "visible"
        return render_template("index.html", url_input=url_input, short_url_to_return=short_url_to_return, visibility=visibility)
    if request.method == 'GET':
        return render_template("index.html")


@app.route('/<urlend>')
def show(urlend):
    try:
        # db query
        url_result = Urls.query.filter_by(short_url=urlend).first()
        print(url_result)
        # return long url
        long_url = url_result.long_url
        print(long_url)
        # redirect to long url
        return redirect(long_url)
    except:
        raise NotFound
    # add new_url & urlend to db

@app.errorhandler(NotFound)
def handle_404(err):
    return render_template('errors/404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)