from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
import string
import random

app = Flask(__name__)
CORS(app)


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
