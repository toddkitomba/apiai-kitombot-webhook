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
                "type": "file",
                "payload": {
                    "url": url + ".png"
                }
            }
        }}

    }


if __name__ == '__main__':
    print(test())
