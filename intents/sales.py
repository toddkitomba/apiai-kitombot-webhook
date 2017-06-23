from __future__ import print_function

from future.standard_library import install_aliases
import requests

install_aliases()  # not sure what this does...

import pprint

# k1 api example
def today(base_url, token, business_token):

    url = base_url + "/k1/dashboard_ajax/getDashboardData?bid="+ business_token +"&byStaff=false&date=2017-06-23+10%3A37%3A49&GST=exclusive&stage=db_stage_1"

    print(url)

    headers = {'Token': token}
    response = requests.post(url, None, True, verify=False, headers=headers)
    result = response.json()
    pprint.pprint(result.get('data').get('sales').get('by_time').get('so_far').get('total'))




    text = "Sales so far "
    text += "$" + str(result.get('data').get('sales').get('by_time').get('so_far').get('total'))
    text += "(expected $" + str(result.get('data').get('sales').get('by_time').get('expected').get('total')) + ")"
    # text += result['models'][0]['first_name'] + "\n"
    # text += result['models'][0]['start_date'] + "\n"
    # text += result['models'][0]['appt_status']

    return {
        "speech": text,
        "displayText": text,
    }
