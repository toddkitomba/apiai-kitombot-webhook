from __future__ import print_function
from future.standard_library import install_aliases
import requests

install_aliases()  # not sure what this does...

import plotly.plotly as py
from plotly.graph_objs import *

url = "https://staging.kitomba.com/k1/clients_ajax/get_client_appointments_info_for_day/Today/93895ccd5153edb2f7b09193b9225f89/all"
token = "8623a3ff07832d2fe4d7079aa811745d"
headers = {'Token': token}
py.sign_in('paul.sinclair', '20xGivFuRABOeYkaCyTq')

# {'id': '654ceea0-564f-4160-841c-e4d3ee330134', 'timestamp': '2017-06-22T05:14:41.26Z', 'lang': 'en',
#  'result': {'source': 'agent', 'resolvedQuery': 'invoice', 'speech': '', 'action': 'test2', 'actionIncomplete': False,
#             'parameters': {'token': 'fb83a162598f007adc00609d6adfc5a7'}, 'contexts': [{'name': 'logged_in',
#                                                                                        'parameters': {
#                                                                                            'token.original': '',
#                                                                                            'password': 'hard24get',
#                                                                                            'email.original': 'todd@kitomba.com',
#                                                                                            'password.original': 'hard24get',
#                                                                                            'email': 'todd@kitomba.com',
#                                                                                            'token': 'fb83a162598f007adc00609d6adfc5a7'},
#                                                                                        'lifespan': 497},
#                                                                                       {'name': 'token', 'parameters': {
#                                                                                           'token.original': '',
#                                                                                           'password': 'hard24get',
#                                                                                           'email.original': 'todd@kitomba.com',
#                                                                                           'password.original': 'hard24get',
#                                                                                           'email': 'todd@kitomba.com',
#                                                                                           'token': 'fb83a162598f007adc00609d6adfc5a7'},
#                                                                                        'lifespan': 197}],
#             'metadata': {'intentId': '3bc7bf2a-ff35-4b3a-a656-e0046d7bc48f', 'webhookUsed': 'true',
#                          'webhookForSlotFillingUsed': 'false', 'intentName': 'invoice'},
#             'fulfillment': {'speech': '', 'messages': [{'type': 0, 'speech': ''}]}, 'score': 1.0},
#  'status': {'code': 200, 'errorType': 'success'}, 'sessionId': 'f2c5b215-2d62-4499-9910-bb9517e49e0c'}


# k1 api example
def test2():
    response = requests.post(url, None, True, verify=False, headers=headers)
    result = response.json()
    print(result)

    text = "First visit of today\n"
    text += result['models'][0]['first_name'] + "\n"
    text += result['models'][0]['start_date'] + "\n"
    text += result['models'][0]['appt_status']

    return {
        "speech": text,
        "displayText": text,

    }


# graph example
def test():
    trace0 = Scatter(
        x=[1, 2, 3, 4],
        y=[10, 15, 13, 17]
    )
    trace1 = Scatter(
        x=[1, 2, 3, 4],
        y=[16, 5, 11, 9]
    )
    data = Data([trace0, trace1])

    url = py.plot(data, auto_open=False, filename='basic-line')

    text = "hi"
    return {
        "speech": text,
        "displayText": text,
        "data": {"facebook": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url + ".png"
                }
            }
        }}

    }


if __name__ == '__main__':
    print(test())
