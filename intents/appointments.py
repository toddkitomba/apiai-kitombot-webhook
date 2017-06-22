from __future__ import print_function
from future.standard_library import install_aliases
import requests

install_aliases()  # not sure what this does...



# k1 api example
def first_visit(base_url, token):
    url = base_url + "/k1/clients_ajax/get_client_appointments_info_for_day/Today/93895ccd5153edb2f7b09193b9225f89/all"
    headers = {'Token': token}
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
