import os, sys, time, random, base64
from pprint import pprint
from flask import (
    Flask,
    render_template,
    json,
    request,
    redirect,
    session,
    jsonify,
    flash,
)

from flask_cors import CORS, cross_origin
import logging


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

logging.getLogger("flask_cors").level = logging.DEBUG


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Origin, X-Requested-With, Content-Type, Accept, Authorization",
    )
    response.headers.add(
        "Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE"
    )
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response


@app.route("/")
def default_route():
    return "Hello World, App is working !!"

@app.route("/wait")
def wait_for_request():
    time.sleep(45)
    return "Yes, It waits for 45 sec"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8081)
