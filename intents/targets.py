from __future__ import print_function

from future.standard_library import install_aliases
import datetime
import requests

install_aliases()  # not sure what this does...


import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('paul.sinclair', '20xGivFuRABOeYkaCyTq')
import pprint


# k1 api example
def today(base_url, token, business_token):

    # url = base_url + "/k1/targets_ajax/getKPIData?bid="+business_token+"&weekOption=lastWeek&byStaff=allStaff&designatedStaff=true&includesTax=true"
    # url = "https://staging.kitomba.com/k1/targets_ajax/getKPIData?bid=54ac0d9d53d1f4d1c5662c87fd7d7294&weekOption=lastWeek&byStaff=allStaff&designatedStaff=true&includesTax=true"
    #
    #
    # print(url)
    #
    # headers = {'Token': token}
    # response = requests.get(url, verify=False, headers=headers)
    # result = response.json()
    #
    # data = result.get("retail_sales");
    #
    # print(data)
    # #
    # trace0 = Scatter(
    #     x=[1, 2, 3, 4],
    #     y=[10, 15, 13, 17]
    # )
    # trace1 = Scatter(
    #     x=[1, 2, 3, 4],
    #     y=[16, 5, 11, 9]
    # )
    # data = Data([trace0, trace1])
    #
    # url = py.plot(data, auto_open=False, filename='basic-line')

    text = "Targets"

    return {
        "speech": text,
        "displayText": text,
        "data": {"facebook": {
            "attachment": {
                "type": "image",
                "payload": {
                     "url": "https://plot.ly/~paul.sinclair/3.png"
            }
        }}

    }}


