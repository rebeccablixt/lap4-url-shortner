from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template("index.html")
