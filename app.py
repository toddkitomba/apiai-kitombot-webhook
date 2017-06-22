#!/usr/bin/env python

from __future__ import print_function

from future.standard_library import install_aliases

install_aliases()

from urllib.parse import urlencode
from urllib.request import urlopen

import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify



from intents import reporting


# Flask app should start in global layout
app = Flask(__name__)



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


def processRequest(req):
    print("action:" + req.get("result").get("action"))
    if req.get("result").get("action") == "login":
        res = doK1Login(req)
    if req.get("result").get("action") == "yahooWeatherForecast":
        res = doYahooWeatherForecast(req)
    if req.get("result").get("action") == "test":
        res = reporting.test()
    if req.get("result").get("action") == "test2":
        res = reporting.test2()

    return res

def doK1Login(req):
    baseurl = "https://staging.kitomba.com/"
    url = baseurl + "k1/auth/login"
    result = req.get("result")
    parameters = result.get("parameters")
    email = parameters.get("email")
    password = parameters.get("password")
    data = urlencode({'login': email, 'password': password})
    print("url " + url)
    print("data " + data)
    response = urlopen(url=url, data=data.encode('ascii')).read()
    response_data = json.loads(response)
    print("here")
    print("response :" + str(response_data))

    return {
        "speech": "you are logged in",
        "displayText": "you are logged in",
        "contextOut": [{"name": "token", "lifespan": 200, "parameters": {"token": response_data.get('token')}}]
    }

def doYahooWeatherForecast(req):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = makeYqlQuery(req)
    if yql_query is None:
        return {}
    yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    result = urlopen(yql_url).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res


# noinspection SqlDialectInspection
def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data):
    print("data")
    print(json.dumps(data, indent=4))
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    print(json.dumps(item, indent=4))

    speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
