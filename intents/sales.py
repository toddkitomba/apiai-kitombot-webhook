from __future__ import print_function

from future.standard_library import install_aliases
import datetime
import requests

install_aliases()  # not sure what this does...

import pprint


# k1 api example
def today(base_url, token, business_token, date=None):
    if date is None:
        date = datetime.datetime.today().strftime('%Y-%m-%d')



    gif_url = "https://api.giphy.com/v1/gifs/random?api_key=7d45d6135fb64502a484194e6f7187d2&tag=money&rating=PG-13"
    gif_response = requests.get(gif_url)

    print(gif_response.json().get('data').get('url'))


    url = base_url + "/k1/dashboard_ajax/getDashboardData?bid=" + business_token + "&byStaff=false&date=" + date + "+10%3A37%3A49&GST=exclusive&stage=db_stage_1"

    print(url)

    headers = {'Token': token}
    response = requests.post(url, None, True, verify=False, headers=headers)
    result = response.json()
    pprint.pprint(result.get('data').get('sales').get('by_time').get('so_far').get('total'))

    text = "Sales so far "
    text += "$" + str(result.get('data').get('sales').get('by_time').get('so_far').get('total'))
    text += "(estimated $" + str(result.get('data').get('sales').get('by_time').get('expected').get('total')) + ")"
    # text += result['models'][0]['first_name'] + "\n"
    # text += result['models'][0]['start_date'] + "\n"
    # text += result['models'][0]['appt_status']

    return {
        "speech": text,
        "displayText": text,
        "data": {"facebook": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": gif_response.json().get('data').get('image_url')
                }
            }
        }}
    }
