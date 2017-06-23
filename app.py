#!/usr/bin/env python

from __future__ import print_function

from future.standard_library import install_aliases

install_aliases()

# noinspection PyCompatibility
from urllib.parse import urlencode
# noinspection PyCompatibility
from urllib.request import urlopen

import json
import os

from flask import Flask
from flask import request
from flask import make_response

from intents import appointments
from intents import login
from intents import sales
from intents import weather

# Flask app should start in global layout
app = Flask(__name__)


class AuthError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    print("Response:")
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def get_token(req):
    try:
        return req.get("result").get("parameters").get("token")

    except (RuntimeError, TypeError, NameError):
        raise AuthError("No session token")

def get_business_token(req):
    try:
        return req.get("result").get("parameters").get("business_token")

    except (RuntimeError, TypeError, NameError):
        raise AuthError("No business token")


def processRequest(req):
    print("action:" + req.get("result").get("action"))

    base_url = "https://staging.kitomba.com"

    token = get_token(req)
    business_token = get_business_token(req)

    print(token)
    print(business_token)

    res = {}  # handles non matching case

    if req.get("result").get("action") == "login":
        res = login.login(req)
    if req.get("result").get("action") == "yahooWeatherForecast":
        res = weather.doYahooWeatherForecast(req)
    if req.get("result").get("action") == "appointments.first_visit":
        print(req)
        res = appointments.first_visit(base_url, token, business_token)
    if req.get("result").get("action") == "sales.day":
        print(req)
        date = req.get("result").get("parameters").get("date")
        res = sales.today(base_url, token, business_token)

    return res


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
