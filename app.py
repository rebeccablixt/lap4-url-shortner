import random
import string
from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace(": //", "ql: //", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        new_url = {"longUrl": request.form['url_input']}
        print(new_url)

        letters = string.ascii_letters
        urlend = ''.join(random.choice(letters) for i in range(6))
        print(urlend)
        return render_template("index.html")

    if request.method == 'GET':
        return render_template("index.html")


@app.route('/<urlend>')
def show(urlend):
    # db query
    return redirect('urlend')

    # add new_url & urlend to db
