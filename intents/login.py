from __future__ import print_function

from future.standard_library import install_aliases
import requests

install_aliases()

baseurl = "https://staging.kitomba.com/"
url = baseurl + "k1/auth/login"


def login(req):
    result = req.get("result")
    parameters = result.get("parameters")
    email = parameters.get("email")
    password = parameters.get("password")
    data = {'login': email, 'password': password}
    print("url " + url)
    response = requests.post(url, data, True, verify=False)

    response_data = response.json()
    print("response :" + str(response_data))

    return {
        # "speech": "you are logged in",
        # "displayText": "you are logged in",
        "contextOut": [{"name": "token", "lifespan": 200, "parameters": {"token": response_data.get('token'),"email":email,
                                                                         "business_token": response_data.get(
                                                                             'other').get('btoken')}}]
    }
